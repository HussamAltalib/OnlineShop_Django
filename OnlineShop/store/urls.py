from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
       path("", views.store, name="store_page"),
       path('<category_slug>/', views.store, name='products_by_category'),
       path('<category_slug>/<product_slug>/', views.product_details, name='product_details'),
]