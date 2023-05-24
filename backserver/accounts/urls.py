from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile_view),
    path('change/', views.update_user),
    path('my_saving/<int:user_pk>/', views.update_my_saving),
    path('my_deposit/<int:user_pk>/', views.update_my_deposit),
]