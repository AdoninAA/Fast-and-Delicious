from django.contrib.auth.models import User
from django.db import models
from products.models import Product
from users.models import UserProfile

class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='carts',
        verbose_name='Покупатель',
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания',
    )

    @property
    def total_price(self):
        return sum(item.total_price for item in self.products.all())

    def __str__(self):
        return f"Cart {self.id} for {self.user.username}"

class CartItem(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=1)
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Корзина',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт',
    )
    quantity = models.PositiveIntegerField(
        default=1, verbose_name='Количество',
    )

    @property
    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"