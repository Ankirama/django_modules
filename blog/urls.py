from django.conf.urls   import url
from .                  import views, feed

urlpatterns = [
    url(r'^feed/$', feed.LatestPosts(), name='feed'),
    url(r'^$', views.BlogIndex.as_view(), name='index'),
    url(r'^tags/(?P<slug>\S+)$', views.TagIndex.as_view(), name='tagIndex'),
    url(r'^(?P<slug>\S+)$', views.BlogDetail.as_view(), name='detail'),
]
