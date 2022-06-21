from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import  generic
from restaurants import models
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import HomeCreateForm



# Create your views here.



class HomeListView(generic.ListView):
    queryset = models.HomePlaceSale.objects.all()
    paginate_by = 6
    template_name = 'restaurants/list.html'



    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')
        author = self.request.GET.get('author')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(details__icontains=q)
            ).distinct()
        if cat:
            queryset = queryset.filter(categories__icontains=cat)

        if author:
            queryset = queryset.filter(user__username=author)
        return queryset

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        post_id = request.POST.get('unlike')
        post_id2 = request.POST.get('like')
        if post_id is not None:
            post = get_object_or_404(models.HomePlaceSale, id=post_id)
            post.likes.remove(request.user)
        if post_id2 is not None:
            post_id2 = request.POST.get('like')
            post = get_object_or_404(models.HomePlaceSale, id=post_id2)
            post.likes.add(request.user)
        return redirect('home')

    

class HomeDetailView(generic.DetailView):
    queryset = models.HomePlaceSale.objects.all().order_by('-created_at')

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        comment = request.POST.get('comment')
        c_slug = request.POST.get('slug')
        if comment:
            if c_slug:
                post = get_object_or_404(models.HomePlaceSale, slug=c_slug)
                comment = models.Comment.objects.create(
                    user=request.user, post=post, text=comment)
                comment.save()
                return redirect('detail', c_slug)
        return redirect('detail', c_slug)



class HomeCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'restaurants/form.html'
    form_class = HomeCreateForm
    success_url = reverse_lazy('my_posts')
    success_message = 'Post Created Successfully!'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)



class HomeUpdateView(LoginRequiredMixin,SuccessMessageMixin, generic.UpdateView):
    form_class = HomeCreateForm
    template_name = 'restaurants/form.html'
    success_url = reverse_lazy('my_posts')
    success_message = 'Post Update Successfully!'


    def get_queryset(self):
        return models.HomePlaceSale.objects.filter(user=self.request.user)



class HomeDeleteView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    success_url = reverse_lazy('my_posts')
    success_message = 'Post Deleted Successfully!'


    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request,*args, **kwargs)



    def get_queryset(self):
        return models.HomePlaceSale.objects.filter(user=self.request.user)



class MyPostView(LoginRequiredMixin, generic.ListView):
    template_name = 'restaurants/my_posts.html'


    def get_queryset(self):
        return models.HomePlaceSale.objects.filter(user=self.request.user)