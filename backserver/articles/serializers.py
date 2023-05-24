from rest_framework import serializers
from .models import Articles, Comments, NewsBoardArticles, NewsBoardComments, AnnouncementBoard
from django.contrib.auth import get_user_model

User = get_user_model()

# 커뮤니티 게시판 serialzier
class ArticleListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Articles
        fields = ('id', 'category', 'title', 'username', 'created_at','content')
        read_only_fields = ('user', )


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Comments
        fields = '__all__'
        read_only_fields = ('article', 'user',)


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Articles
        fields = '__all__'
        read_only_fields = ('user', )


# 뉴스 게시판 serializer
class NewsListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = NewsBoardArticles
        fields = ('id', 'username', 'title', 'created_at','content')
        read_only_fields = ('user',)


class NewsCommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = NewsBoardComments
        fields = '__all__'
        read_only_fields = ('articles', 'user',)


class NewsArticleSerializer(serializers.ModelSerializer):
    comment_set = NewsCommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = NewsBoardArticles
        fields = '__all__'
        read_only_fields = ('user', 'username')


# 공지 게시판 serializer
class AnnouncementListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = AnnouncementBoard
        fields = ('id', 'title', 'username', 'created_at','content')
        read_only_fields = ('user',)


class AnnouncementArticleSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = AnnouncementBoard
        fields = '__all__'
        read_only_fields = ('user', 'username',)
