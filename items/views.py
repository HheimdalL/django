from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DetailView
from django.db.models import Q

class AllItemView(ListView):
    model = Item
    template_name = 'all_item.html'
    
class DetailItemView(DetailView):
    model = Item
    template_name = 'detail_item.html'
    
class SearchItemView(ListView):
    model = Item
    template_name = 'search_item.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Item.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
