from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from accounts import forms
from django.contrib.auth.models import User

# Create your views here.


class Logout(generic.View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')


class RegisterView(SuccessMessageMixin, generic.CreateView):
    template_name = 'registration/register.html'
    form_class = forms.RegisterForm
    success_message = "Account created Successfully"
    success_url = reverse_lazy('login')


class ProfileView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    form_class = forms.RegisterForm
    template_name = 'registration/profile.html'
    queryset = User.objects.all()
    success_url = reverse_lazy('my_posts')
    success_message = "Profile Update Successfully"



class ImageUpdateView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'registration/profile_picture.html'

    def post(self, request, *args, **kwargs):
        img = request.FILES.get('image')
        user = get_object_or_404(User, username=request.user.username)
        user.profile.image = img
        user.save()
        return redirect('profile', request.user.id)