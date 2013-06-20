from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'social_distance.views.home', name='home'),
    # url(r'^social_distance/', include('social_distance.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^social_distance/new_distance/$', 'social_distance.views.new_distance'),
    (r'^auth_callback$', 'social_distance.views.auth_callback'),
    (r'^auth_callback/$', 'social_distance.views.auth_callback'),
    (r'^social_distance/social_users/$', 'social_distance.views.social_users'),
    (r'^social_distance/find_distance/$', 'social_distance.views.find_distance'),

    (r'^social_distance/$', 'social_distance.views.index'),
    (r'^social_distance/(?P<poll_id>\d+)/$', 'social_distance.views.detail'),
    (r'^social_distance/(?P<poll_id>\d+)/results/$', 'social_distance.views.results'),
    (r'^social_distance/(?P<poll_id>\d+)/vote/$', 'social_distance.views.vote'),

    url(r'^admin/', include(admin.site.urls)),
)
