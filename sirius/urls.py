from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from sirius import views
from django.contrib.flatpages.views import flatpage

from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    # url(r'^sirius/', include('sirius.foo.urls')),
    url(r'^issue/', include('issue.urls')),
    url(r'^article/', include('articles.urls')),
    url(r'^squiggle/', include('issue.urls_squiggle')),
    url(r'^person/', include('people.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
#Flatpages

urlpatterns += patterns('',
    (r'^dispatch.wsgi/(?P<url>.*/)$', flatpage),
    (r'^(?P<url>.*/)$', flatpage),
)
