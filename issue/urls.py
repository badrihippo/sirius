from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from issue.views import IssueDetail, IssueList
urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', IssueDetail.as_view(), name='view-issue'),
    url(r'^$', IssueList.as_view(), name='list-issues'),
)
