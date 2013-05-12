try:
    from django.conf.urls import patterns, url
except ImportError:
    # Django < 1.5
    from django.conf.urls.defaults import patterns, url

# urlpatterns = patterns('',
#     url(r'^ajax/add/(?P<object_type>\w+)/(?P<object_id>\d+)$','modelnotice.views.ajax_notice_add', name='ajax_notice_add'),
# )

urlpatterns = patterns('goto_track.views',
    url(r'^$', 'goto_url',
        name='goto_url')
)