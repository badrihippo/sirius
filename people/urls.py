from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from people.views import PersonDetail, PersonList
urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', PersonDetail.as_view(), name='view-person'),
    url(r'^$', PersonList.as_view(), name='list-people'),
)
