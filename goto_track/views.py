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
            ct_cache_key = 'goto_track_ctype_%s' % (object_type,)
            ct = cache.get(ct_cache_key)
            if ct is None:
                ct = ContentType.objects.get(pk=object_type)
                cache.set(ct_cache_key,ct,864000)  # 10 days

            if ct is not None:
                model = ct.model_class()
             
                counter = Click()
                counter.content_type = ct

                obj_cache_key = 'goto_track_obj_count_%s_%s' % (ct.pk, object_id)
                obj_count = cache.get(obj_cache_key)
                if obj_count is None:
                    obj_count = model.objects.filter(pk=object_id).count()  # cache?
                    cache.set(obj_cache_key, obj_count, 600)
                
                if obj_count > 0:
                    counter.object_id = object_id

                counter.store(request, url)
        except:
            pass

    return redirect(redirect_url)
