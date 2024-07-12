from django.contrib import admin
from .models import Cart, CartItem

class CartTabAdmin(admin.TabularInline):
    model = CartItem  # Should refer to CartItem, not Cart
    fields = ["product", "quantity", "total_price"]
    readonly_fields = ["total_price"]
    extra = 1

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'total_price',)
    search_fields = ('product__title', 'cart__user__username',)
    list_filter = ('product', 'cart__user',)
    raw_id_fields = ('product', 'cart',)

    def total_price(self, obj):
        return obj.total_price

    total_price.short_description = 'Общая цена'

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'cart_products', 'total_price',)
    list_filter = ('created_at',)
    search_fields = ('user__username', 'user__email', 'created_at',)
    readonly_fields = ('total_price',)

    def cart_products(self, obj):
        return [item for item in obj.products.all()]

    def total_price(self, obj):
        return obj.total_price

    cart_products.short_description = 'Список товаров'
    total_price.short_description = 'Общая цена'

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)