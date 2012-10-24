from django.conf.urls.defaults import *
from blog.models import *

urlpatterns = patterns('blog.views',
   (r"^(\d+)/$", "post"),
   (r"^add_comment/(\d+)/$", "add_comment"),
   (r"^delete_comment/(\d+)/$", "delete_comment"),
   (r"^delete_comment/(\d+)/(\d+)/$", "delete_comment"),
   (r"^month/(\d+)/(\d+)/$", "month"),
   (r"", "main"),
)
