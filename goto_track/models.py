from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Click(models.Model):
    content_type = models.ForeignKey(ContentType,blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    referer = models.CharField(max_length=512)
    ip_addr = models.IPAddressField(blank=True, null=True)
    url = models.URLField(_(u'url'), blank=True, )

    content_object = generic.GenericForeignKey()

    class Meta:
        unique_together = (('content_type', 'object_id', 'user', 'date'))
        verbose_name = _(u'Link click')
        verbose_name_plural = _(u'Link clicks')

    def __unicode__(self):
        return _(u"%s visited link to %s on %s") % (self.user, self.content_object, self.date)
