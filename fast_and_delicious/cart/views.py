from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, RedirectView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views.generic import View
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin


from products.models import Product
from .models import Cart, CartItem

from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cart

class CartDetailView(LoginRequiredMixin, DetailView):
    model = Cart
    template_name = 'cart/cart_detail.html'
    context_object_name = 'cart'

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.get_object()
        total_price = sum(item.product.price * item.quantity for item in cart.items.all())
        context['total_price'] = total_price
        return context


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


class CheckoutView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        items = cart.items.all()
        total_price = sum(item.product.price * item.quantity for item in items)

        email_subject = 'Ваш заказ'
        email_body = 'Вы заказали:\n\n'
        for item in items:
            email_body += f'{item.product.title} (x{item.quantity}): {item.product.price * item.quantity}\n'
        email_body += f'\nИтого к оплате: {total_price}'

        send_mail(
            email_subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=False
        )

        cart.items.all().delete()
        return redirect('cart:cart_detail')
