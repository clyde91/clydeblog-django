from django.contrib.sitemaps import Sitemap
from arch_blog.models import ArchBlog
from code_blog.models import CodeBlog
from django.contrib.sitemaps import GenericSitemap


archblog_dict = {
    'queryset': ArchBlog.objects.all(),
    'date_field': 'created_time',
}

codeblog_dict = {
    'queryset': CodeBlog.objects.all(),
    'date_field': 'created_time',
}


sitemap_dict = {
    'arch_blog': GenericSitemap(archblog_dict, priority=0.6),
    'code_blog': GenericSitemap(codeblog_dict, priority=0.6),
}