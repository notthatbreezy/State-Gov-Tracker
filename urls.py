from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.defaults import *

#Uncomment these when you're ready to integrate stuff from Chris's project
#in chris's these were all from StateGovTracker_Django.views import *
#from state_gov_tracker_app.views import home
from state_gov_tracker_app.views import search_form
#from state_gov_tracker_app.views import search_results
from state_gov_tracker_app.views import WhichRep
# from state_gov_tracker_app.views import RecordVote
from state_gov_tracker_app.views import profile, pa_tweets, about_myrep
from blog.views import Blog, Article
from secretballot.views import vote
from django.contrib import admin
from state_gov_tracker_app.api import PreferencesResource, PR_Resource
from tastypie.api import Api


v1_api = Api(api_name='v1')
v1_api.register(PreferencesResource())
v1_api.register(PR_Resource())

admin.autodiscover()

urlpatterns = patterns('',
    ('^$', search_form),
    ('^results$', WhichRep),
    ('^profile/(PAL\d+)/?', profile),
    ('^pa-tweets$', pa_tweets),
    ('^about$', about_myrep),
    url(r'blog$', Blog),
    url(r'blog/post_num/(.*)$', Article),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
    url(r'^vote/$', vote), 
)

'''

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^current_time/', 'state_gov_tracker_app.views.current_datetime'),
    url(r'^twitter_test/', 'state_gov_tracker_app.views.twitter_view'),
    url(r'^$', 'state_gov_tracker_app.views.home', name='home'),
    # url(r'^state_gov_tracker/', include('state_gov_tracker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
'''