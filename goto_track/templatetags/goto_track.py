"""
Template tags for Django
"""

from django import template
from django.utils.http import urlquote
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType

register = template.Library()

@register.tag(name="goto_url")
def do_goto_url(parser, token):
    bits = token.contents.split()
        # split_contents() knows not to split quoted strings.
        #tag_name, url, object_type, object_id = token.split_contents()
    if len(bits) == 1:
        raise template.TemplateSyntaxError("%r tag requires at least one arguments" % bits[0])

    url = bits[1]
    obj = bits[2] or None
            
    return GotoNode(url, obj)


class GotoNode(template.Node):
    
    def __init__(self, url, obj):
        self.url = template.Variable(url)
        self.obj = template.Variable(obj)

    def render(self, context):
        try:
            url = self.url.resolve(context)
            obj = self.obj.resolve(context)
        except template.VariableDoesNotExist:
            return ''
        url = urlquote(url)
        ctype = ContentType.objects.get_for_model(obj)
        object_type = ctype.pk
        object_id = obj.id
        action = reverse('goto_url')
        
        link = '%s?oid=%s&ot=%s&url=%s' % \
            (action, object_id, object_type, url)

        return link
