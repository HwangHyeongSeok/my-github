from django.conf.urls import url
#from django.contrib import admin
from bookmark.views import BookmarkLV, BookmarkDV 
app_name= 'bookmarks'
urlpatterns = [
# url(r'^admin/', admin.site.urls),
    url(r'^bookmarks/$', bookmark_list, name='index'),
    url(r'^bookmarks/(?P<pk>\d+)/$', bookmark_detail, name='detail'), 
]
