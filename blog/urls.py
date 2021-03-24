from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogPageView.as_view(), name='blog'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('new/', views.BlogCreateView.as_view(), name='blog_create'),
    path('<int:pk>/edit/', views.BlogUpdateView.as_view(), name='blog_update'),
    path('<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog_delete'),
]