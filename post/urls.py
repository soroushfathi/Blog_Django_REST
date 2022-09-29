from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view(), name='detail'),
    path('list/', views.PostList.as_view(), name='list'),
]
