from django.urls import path
from .views import BlogListViews

app_name='blog'

urlpatterns = [
    path('', BlogListViews.as_view(), name="home")
]