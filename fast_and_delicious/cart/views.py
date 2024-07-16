from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin

from products.models import Product
from .models import Cart, CartItem

class CartDetailView(LoginRequiredMixin, DetailView):
    model = Cart
    template_name = 'cart/cart_detail.html'
    context_object_name = 'cart'

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart

class AddToCartView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        return reverse_lazy('cart:cart_detail')

class RemoveFromCartView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        item_id = self.kwargs.get('item_id')
        cart = Cart.objects.get(user=self.request.user)
        cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)

        cart_item.delete()
        return reverse_lazy('cart:cart_detail')

class IncreaseCartItemQuantityView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        item_id = self.kwargs.get('item_id')
        cart = Cart.objects.get(user=self.request.user)
        cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)

        cart_item.quantity += 1
        cart_item.save()
        return reverse_lazy('cart:cart_detail')


class DecreaseCartItemQuantityView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        item_id = self.kwargs.get('item_id')
        cart = Cart.objects.get(user=self.request.user)
        cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()  # Remove the item if quantity is 0

        return reverse_lazy('cart:cart_detail')
