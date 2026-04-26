from django.urls import path
from django_distill import distill_path
from . import views

urlpatterns = [
    distill_path('', views.home, name='home'),
    distill_path('project/<slug:slug>/', views.project_detail, name='project_detail', distill_func=views.get_all_projects),
    distill_path('blog/<slug:slug>/', views.blog_detail, name='blog_detail', distill_func=views.get_all_posts),
]