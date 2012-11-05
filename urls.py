from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dajaxice.core import dajaxice_autodiscover, dajaxice_config

# Dajax/Dajaxice configuration
dajaxice_autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Dajax/Dajaxice URLs
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),

    # Tech Evaluation URLs
    url(r'^$', direct_to_template, {'template': 'index.html'}, name="index"),
    url(r'^about/', include('about.urls')),
    url(r'^writeup/', direct_to_template, {'template': 'writeup.html'}, name= "writeup"),
    url(r'^500/', direct_to_template, {'template': 'error.html'}, name = "500"),
    url(r'^polls/', include('polls.urls')),
    url(r'^blog/', include('blog.urls')),

    # Test URLs
    url(r'^test/', direct_to_template, {'template': 'test.html'}, name= "test"),
    url(r'^test/dajaxice', include(testDajaxice.urls)),
)

urlpatterns += staticfiles_urlpatterns()


#Clocke... more blood sweat and tears... dead code that was simply too problematic to fix in the timeframe...
#Actually after some floorhockey ... clarity came to me

#urlpatterns = patterns('forum.views',
#	(r"", "main"),    
#	(r"^forum/(\d+)/$", "forum"),
#	(r"^thread/(\d+)/$", "thread"),
	#(r"^post/(new_thread|reply)/(\d+)/$", "post"),
	#(r"^reply/(\d+)/$", "reply"),
	#(r"^profile/(\d+)/$", "profile"),
	#(r"^new_thread/(\d+)/$", "new_thread"),
#)


#urlpatterns += patterns('',
	#url(r'calendarapp/$', 'calendarapp.views.main'),
	#(r"^(\d+)/$", "main"),
	#(r"", "main"),
	#(r"^(\d+)/$", "calendarapp.views.mainasfaf"),
	#(r"", "main"),	
#(r"^(\d+)/$", "main"),    
#(r'^calendarapp(\d+)/$", "main"),
    #(r"", "main"),
#)
