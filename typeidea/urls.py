"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from typeidea.custom_site import custom_site   # 自定义后台页面
from django.conf.urls import url
from blog.views import post_detail, post_list
from config.views import links

from blog.views import IndexView, CategoryView, TagView, PostDetailView, SearchView, AuthorView
from config.views import LinkListView
from comment.views import CommentView

from django.contrib.sitemaps import views as sitemap_views
from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap

urlpatterns = [

    # 增加name属性，通过name解析成URL
    # url('^$', post_list, name='index'),            #  function view
    # url('^category/(?P<category_id>\d+)/$', post_list, name='category-list'),
    # url('^tag/(?P<tag_id>\d+)/$', post_list, name='tag-list'),
    # url('^post/(?P<post_id>\d+).html$', post_detail, name='post-detail'),
    # url('^links/$', links, name='links'),

    url('^$', IndexView.as_view(), name='index'),    # class-base view
    url('^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
    url('^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    url('^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),

    url('^search/$', SearchView.as_view(), name='search'),
    url('^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author'),

    url('^links/$', LinkListView.as_view(), name='links'),
    url('^comment/$', CommentView.as_view(), name='comment'),

    # path('super_admin/', admin.site.urls),    # 管理用户后台
    # path('admin/', custom_site.urls),         # 管理业务后台
    url('^super_admin/', admin.site.urls, name='super-admin'),
    url('^admin/', custom_site.urls, name='admin'),

    url('^rss|feed/', LatestPostFeed(), name='rss'),
    url('^sitemap\.xml$', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),
]

