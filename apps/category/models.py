from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class ArticleCategory(models.Model):
    """each article category"""
    class Meta:
        db_table = "categories"

    name = models.CharField(max_length=64, blank=False, unique=True)
    created_time = models.DateTimeField(null=True, auto_now_add=True)

    def count_number(self):
        return self.article_set.count()

    count_number.short_description = 'article number'

    def __str__(self):
        return '%s' % self.name
