from rest_framework import serializers

from .models import Article


class ArticleModelSerializer(serializers.ModelSerializer):

    category = serializers.CharField(source='category.name')
    author = serializers.CharField(source='author.username')
    created_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S %z")

    class Meta:
        model = Article
        exclude = ("id", "page_view_times")
