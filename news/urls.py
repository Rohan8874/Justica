from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path('news', views.news_view, name='news'),
#     path('news/<int:pk>/', views.news_detail, name='news_detail'),
#     path('news_detail/<int:pk>/', views.news_detail, name='news_detail'),
#     path('news_single/<str:pk>', views.news_ldy, name='news_ldy'),
#     path("news_single", views.news_single, name="news_single"),
#     path('news/<str:pk>', views.news_dy, name='news_dy'),
#     path('post/<int:pk>/like/', views.like_post, name='like_post'),
#     path('create/', views.create_post, name='create_post'),  
]