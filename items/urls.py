from django.urls import path, include
from .views import AllItemView, DetailItemView, SearchItemView

urlpatterns = [
    path('', AllItemView.as_view(), name='all_item'),
    path('<uuid:pk>/', DetailItemView.as_view(), name='detail_item'),
    path('search/', SearchItemView.as_view(), name='search_item'),
]
