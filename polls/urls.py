from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from polls.models import Poll

urlpatterns = patterns('polls.views',
    url(r'^$',
        ListView.as_view(
            queryset=Poll.objects.order_by('-pub_date')[:5],
            context_object_name='latest_poll_list',
            template_name='pollsIndex.html'),
            name='poll_index'),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll,
            template_name='pollsDetail.html'),
            name='poll_detail'),
    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Poll,
            template_name='pollsResults.html'),
        name='poll_results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote', name='poll_vote'),
    url(r'^create/', 'create', name='poll_create'),
)
