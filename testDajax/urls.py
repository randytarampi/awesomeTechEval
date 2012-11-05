from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('testDajax.views',
    url(r'^$', 'index', name = "testDajax_index"),
)
