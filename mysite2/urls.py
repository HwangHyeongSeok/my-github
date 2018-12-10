from django.conf.urls import include, url
from django.contrib import admin
#from bookmark.views import bookmark_list, bookmark_detail 
urlpatterns = [
    url(r'^admin/',include(admin.site.urls)),

    url(r'^admin/', admin.site.urls),
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
#url(r'^bookmarks/$', bookmark_list, name='index'),
#url(r'^bookmarks/(?P<pk>\d+)/$', bookmark_detail, name='detail'), 
]

