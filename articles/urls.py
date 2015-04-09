from django.conf.urls import patterns, include, url
from articles.views import ArticleDetail, ArticleList
urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', ArticleDetail.as_view(), name='article-by-pk'),
    url(r'^(?P<slug>[-\w]+)/$', ArticleDetail.as_view(), name='read-article'),
    url(r'^$', ArticleList.as_view(), name='list-articles'),
)
