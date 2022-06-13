from django.urls import path
from restaurants import views

urlpatterns = [
    path('',views.HomeListView.as_view(),name='home'),
    path('<slug:slug>/', views.HomeDetailView.as_view(), name='detail'),
]