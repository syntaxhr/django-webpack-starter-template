from django.conf.urls import url

from posts.views import PostDetail, PostListCategory, PostList
from posts.settings import POST_DETAIL_URL, POSTS_CATEGORY_DETAIL_URL, POSTS_LIST_URL

urlpatterns = [
    url(
        r'^detail/(?P<post_id>[\w-]+)/(?P<post_slug>[\w-]+)/$',
        PostDetail.as_view(),
        name=POST_DETAIL_URL
    ),
    url(
        r'^(?P<category_id>[\w-]+)/(?P<category_slug>[\w-]+)/$',
        PostListCategory.as_view(),
        name=POSTS_CATEGORY_DETAIL_URL
    ),
    url(
        r'^$',
        PostList.as_view(),
        name=POSTS_LIST_URL
    ),
]

