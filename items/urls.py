from django.urls import path, include
from .views import AllItemView, DetailItemView, SearchItemView
from . import views

urlpatterns = [
    path('', AllItemView.as_view(), name='all_item'),
    path('<uuid:pk>/', DetailItemView.as_view(), name='detail_item'),
    path('search/', SearchItemView.as_view(), name='search_item'),
    #1
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
]
