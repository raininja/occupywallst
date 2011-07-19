r"""

    occupywallst.urls
    ~~~~~~~~~~~~~~~~~

    HTTP request routing.

"""

from django.conf import settings
from django.conf.urls.defaults import patterns, url, include

from occupywallst import admin, api, utils, feeds


adminsite = admin.AdminSite(name='occupyadmin')

urlpatterns = patterns('',
    url(r'^$', 'occupywallst.views.index'),
    url(r'^rss/news/$', feeds.RSSNewsFeed()),
    url(r'^rss/comments/$', feeds.RSSCommentFeed()),
    url(r'^article/(?P<slug>[-_\d\w]+)/', 'occupywallst.views.article'),
    url(r'^attendees/$', 'occupywallst.views.attendees'),
    url(r'^rides/$', 'occupywallst.views.rides'),
    url(r'^housing/$', 'occupywallst.views.housing'),
    url(r'^about/$', 'occupywallst.views.about'),
    url(r'^login/$', 'occupywallst.views.login'),
    url(r'^logout/$', 'occupywallst.views.logout'),
    url(r'^signup/$', 'occupywallst.views.signup'),
    url(r'^users/(?P<username>[-_\d\w]+)/$', 'occupywallst.views.user_page'),
    url(r'^api/attendees/$', utils.api_view(api.attendees)),
    url(r'^api/attendee/info/$', utils.api_view(api.attendee_info)),
    url(r'^api/comment/new/$', utils.api_view(api.comment_new)),
    url(r'^api/comment/edit/$', utils.api_view(api.comment_edit)),
    url(r'^api/comment/remove/$', utils.api_view(api.comment_remove)),
    url(r'^api/comment/delete/$', utils.api_view(api.comment_delete)),
    url(r'^api/comment/vote/$', utils.api_view(api.comment_vote)),
    url(r'^api/message/send/$', utils.api_view(api.message_send)),
    url(r'^api/message/delete/$', utils.api_view(api.message_delete)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^admin/', include(adminsite.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
