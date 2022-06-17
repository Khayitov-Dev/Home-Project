from django.urls import path
from django.contrib.auth import views
from accounts.views import Logout, RegisterView, ProfileView,ImageUpdateView

urlpatterns = [
    path('login/', views.LoginView.as_view(),name='login'),
    path('logout/', Logout.as_view(),name='logout'),
    path('register/', RegisterView.as_view(),name='register'),
    path('password-reset/', views.PasswordResetView.as_view(),name='password_reset'),
    path('password-reset-done/', views.PasswordResetView.as_view(),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password-reset-complete/', views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('profile/<int:pk>/', ProfileView.as_view(),name='profile'),
    path('profile-picture/', ImageUpdateView.as_view(),name='update_image'),
]