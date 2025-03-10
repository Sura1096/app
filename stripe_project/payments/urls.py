from django.urls import path

from .views import buy_item, buy_order, item_detail

urlpatterns = [
    path('item/<int:id>/', item_detail, name='item_detail'),
    path('buy/<int:id>/', buy_item, name='buy_item'),
    path('buy_order/<int:id>/', buy_order, name='buy_order')
]
