from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
       path("", views.intro_page, name="intro_page"),

]