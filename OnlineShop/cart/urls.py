from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
       path("", views.cart, name="cart"),
       path('add_cart/<product_id>/', views.add_cart, name='add_cart'),

]