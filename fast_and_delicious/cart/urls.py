from django.urls import path
from .views import CartDetailView, AddToCartView, RemoveFromCartView, IncreaseCartItemQuantityView, DecreaseCartItemQuantityView, CheckoutView

app_name = 'cart'

urlpatterns = [
    path('', CartDetailView.as_view(), name='cart_detail'),
    path('add/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove/<int:item_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('increase/<int:item_id>/', IncreaseCartItemQuantityView.as_view(), name='increase_cart_item_quantity'),
    path('decrease/<int:item_id>/', DecreaseCartItemQuantityView.as_view(), name='decrease_cart_item_quantity'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]
