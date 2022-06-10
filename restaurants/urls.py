from django.urls import path
from restaurants import views

urlpatterns = [
    path('',views.HomeListView.as_view(),name='home'),
]