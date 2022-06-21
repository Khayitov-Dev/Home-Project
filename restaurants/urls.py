from django.urls import path
from restaurants import views

urlpatterns = [
    path('',views.HomeListView.as_view(),name='home'),
    path('create/', views.HomeCreateView.as_view(), name='create'),
    path('<slug:slug>/', views.HomeDetailView.as_view(), name='detail'),
    path('<slug:slug>/delete/', views.HomeDeleteView.as_view(), name='delete'),
    path('<slug:slug>/update/', views.HomeUpdateView.as_view(), name='update'),
    path('dashboard/my_posts/', views.MyPostView.as_view(), name='my_posts'),
]