from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from issue.views import SquiggleByID, SquiggleHome, SquiggleByDate, SquigglesByYear
urlpatterns = patterns('',
    url(r'^(?P<year>\d{4})/$',
        SquigglesByYear.as_view(),
        name='squiggles-by-year'),
    url(r'^$', SquiggleHome.as_view(), name='list-squiggles'),
    url(r'^(?P<pk>\d+)/$', SquiggleByID.as_view(), name='squiggle-by-id'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})-(?P<day>\d{1,2})/$',
        SquiggleByDate.as_view(),
        name='squiggle-by-date'),
)
