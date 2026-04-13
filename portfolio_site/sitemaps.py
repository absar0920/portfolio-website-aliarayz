from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['index', 'all_projects', 'all_videos']

    def location(self, item):
        return reverse(item)