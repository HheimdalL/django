from django.shortcuts import render
from .models import Item, Cart
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.shortcuts import redirect
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

def add_to_cart(request):
    user = request.user
    item_id = request.GET.get('item_id')
    item = Item.objects.get(id=item_id)
    Cart(customuser=user, item=item).save()
    return redirect('/cart')

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(customuser=user)
    return render(request, 'cart.html', locals())