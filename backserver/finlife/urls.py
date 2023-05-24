from django.urls import path
from . import views

urlpatterns = [
    path('finlife/exchange/', views.exchange_money),
    # path('finlife/save-deposit-products/', views.save_deposit_products),
    path('finlife/deposit-products/', views.deposit_products),
    path('finlife/deposit-product-options/', views.deposit_product_options),
    # path('finlife/save-saving-products/', views.save_saving_products),
    path('finlife/saving-products/', views.saving_products),
    path('finlife/saving-product-options/', views.saving_product_options),

]