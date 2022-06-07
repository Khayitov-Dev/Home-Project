from django.shortcuts import render
from django.views import  generic
from restaurants import models
from django.db.models import Q

# Create your views here.




class HomeListView(generic.ListView):
    queryset = models.HomePlaceSale.objects.all()
    paginate_by = 5
    template_name = 'restaurants/list.html'
    context_object_name = 'homes'



    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')
        author = self.request.GET.get('author')


        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(details__icontains=q)
            ).distinict()
        if cat:
            queryset = queryset.filter(categories__icontains=cat)

        if author:
            queryset = queryset.filter(user__username=author)
        return  queryset
    

