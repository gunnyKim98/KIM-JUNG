
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer, NewsListSerializer, \
    NewsCommentSerializer, NewsArticleSerializer, AnnouncementListSerializer, AnnouncementArticleSerializer

from .models import Articles, Comments, NewsBoardArticles, NewsBoardComments, AnnouncementBoard


# 커뮤니티 게시판
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def article_list(request):
    print(request.user)
    print(request.data)
    if request.method == 'GET':
        articles = get_list_or_404(Articles)
        serializer = ArticleListSerializer(articles, many=True)
        print(articles)
        print(serializer)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Articles, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = get_list_or_404(Comments)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comments, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Articles, pk=article_pk)
    print(1)
    print(article)
    print(request.data)
    serializer = CommentSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 뉴스 게시판
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def news_article_list(request):
    print(request.user)
    print(request.data)
    if request.method == 'GET':
        articles = get_list_or_404(NewsBoardArticles)
        serializer = NewsListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NewsArticleSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def news_article_detail(request, article_pk):
    article = get_object_or_404(NewsBoardArticles, pk=article_pk)

    if request.method == 'GET':
        serializer = NewsArticleSerializer(article)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = NewsArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def news_comment_list(request):
    if request.method == 'GET':
        comments = get_list_or_404(NewsBoardComments)
        serializer = NewsCommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def news_comment_detail(request, comment_pk):
    comment = get_object_or_404(NewsBoardComments, pk=comment_pk)

    if request.method == 'GET':
        serializer = NewsCommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = NewsCommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def news_comment_create(request, article_pk):
    article = get_object_or_404(NewsBoardArticles, pk=article_pk)
    print(article)
    serializer = NewsCommentSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid(raise_exception=True):
        serializer.save(articles=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 공지 게시판
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def announce_article_list(request):
    print(1)
    if request.method == 'GET':
        articles = get_list_or_404(AnnouncementBoard)
        serializer = AnnouncementListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AnnouncementArticleSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def announce_article_detail(request, article_pk):
    article = get_object_or_404(AnnouncementBoard, pk=article_pk)

    if request.method == 'GET':
        serializer = AnnouncementArticleSerializer(article)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = AnnouncementArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)