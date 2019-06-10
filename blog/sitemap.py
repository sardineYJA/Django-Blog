from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post

''' 实现sitemap '''


class PostSitemap(Sitemap):
    changefreq = 'always'
    priority = 1.0

    # 返回正常状态的文章
    def items(self):
        return Post.objects.filter(status=Post.STATUS_NORMAL)

    # 返回文章的创建时间
    def lastmod(self, obj):
        return obj.created_time

    # 返回文章的URL
    def location(self, obj):
        return reverse('post-detail', args=[obj.pk])
