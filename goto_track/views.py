from models import Click
from django.core.cache import cache
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect

#from django.conf import settings
#from default_settings import RATINGS_VOTES_PER_IP

def goto_url(request):
    url = request.GET.get('url',None)
    object_id = request.GET.get('oid',None)
    object_type = request.GET.get('ot',None)

    if url is None:
        redirect_url = '/'
    else:
        redirect_url = url
        try:
            ct_cache_key = 'content_type%s' % (object_type,)
            ct = cache.get(ct_cache_key)
            if ct is None:
                ct = ContentType.objects.get(pk=object_type)
                cache.set(ct_cache_key,ct,60*60*24)

            if ct is not None:
                model = ct.model_class()
             
                counter = Click()
                counter.content_type = ct

                obj_count = model.objects.filter(pk=object_id).count()  # cache?
                
                if obj_count > 0:
                    counter.object_id = object_id

                ip_addr = request.META.get('REMOTE_ADDR','')

                user = None
                if request.user.is_authenticated():
                    user = request.user
                print 'USER', user
                counter.user = user
                
                counter.referer = request.META.get('HTTP_REFERER','')
                counter.ip_addr = ip_addr

                counter.save()
        except:
            pass

    return redirect(redirect_url)
