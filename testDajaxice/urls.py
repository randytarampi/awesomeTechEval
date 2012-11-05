from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('testDajaxice.views',
    url(r'^$', 'contact_form', name = "testDajaxice_index"),
)
