from django.contrib import admin
from .models import Product, Category

class ProductInline(admin.TabularInline):
    model = Product
    extra = 0
    fields = ('title', 'description', 'slug', 'created_at', 'price', 'old_price', 'image', 'is_available', 'category')
    readonly_fields = ('created_at',)
    can_delete = True
    show_change_link = True

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'

    inlines = [ProductInline]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug', 'created_at', 'price', 'old_price', 'image', 'is_available', 'category')
    list_filter = ('category', 'is_available')
    search_fields = ('title', 'description', 'is_available')
    list_editable = ('description', 'price', 'image', 'is_available')