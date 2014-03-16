from django.contrib.sitemaps import Sitemap
from jeffreyvwong.models import Snippet

class SnippetSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Snippet.objects.all()

    def lastmod(self, obj):
        return obj.updated_date