from django.urls import path, re_path
from . views import articles, article_details

urlpatterns = [
    path('articles', articles, name='articles'),
    # path('article/<int:pk>/<slug:slug>', article_details, name='article_details')
    re_path(r'^articles/(?P<pk>[0-9]+)/(?P<slug>[-\w\[\]\u0600-\u06FF\u0660-\u0669\u06F0-\u06F9]+)$', article_details, name='article_details'),     # use persion slug
]
