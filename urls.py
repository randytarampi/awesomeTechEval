from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from forum.models import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'awesomeTechEval.views.home', name='home'),
    # url(r'^awesomeTechEval/', include('awesomeTechEval.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Tech Evaluation URLs
    url(r'^$', direct_to_template, {'template': 'index.html'}, name="index"),
    url(r'^about/', include('about.urls')),#direct_to_template, {'template': 'about.html'}, name="about"),
    url(r'^writeup/', direct_to_template, {'template': 'writeup.html'}, name="writeup"),
    url(r'^500/', direct_to_template, {'template': 'error.html'}, name="500"),
    url(r'^polls/', include('polls.urls')),

)

urlpatterns = patterns('dbe.forum.views',
	(r"", "main"),    
	(r"^forum/(\d+)/$", "forum"),
	(r"^thread/(\d+)/$", "thread"),
	(r"^post/(new_thread|reply)/(\d+)/$", "post"),
	(r"^reply/(\d+)/$", "reply"),
	(r"^profile/(\d+)/$", "profile"),
	(r"^new_thread/(\d+)/$", "new_thread"),
    
)


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
