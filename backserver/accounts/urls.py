from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile_view),
    path('change/', views.update_user),
    path('my_saving/<int:user_pk>/', views.update_my_saving),
    path('my_deposit/<int:user_pk>/', views.update_my_deposit),

    path('search/saving/<int:user_pk>/age/', views.viewSavingProductAge),
    path('search/saving/<int:user_pk>/earn/', views.viewSavingProductEarn),

    path('search/deposit/<int:user_pk>/age/', views.viewDepositProductAge),
    path('search/deposit/<int:user_pk>/earn/', views.viewDepositProductEarn),
]