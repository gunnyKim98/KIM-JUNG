# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views


urlpatterns = [
    path('community/', views.article_list),
    path('community/<int:article_pk>/', views.article_detail),
    path('community/comments/', views.comment_list),
    path('community/comments/<int:comment_pk>/', views.comment_detail),
    path('community/<int:article_pk>/comments/', views.comment_create),

    path('news/', views.news_article_list),
    path('news/<int:article_pk>/', views.news_article_detail),
    path('news/comments/', views.news_comment_list),
    path('news/comments/<int:comment_pk>/', views.news_comment_detail),
    path('news/<int:article_pk>/comments/', views.news_comment_create),

    path('announce/', views.announce_article_list),
    path('announce/<int:article_pk>/', views.announce_article_detail),
]
