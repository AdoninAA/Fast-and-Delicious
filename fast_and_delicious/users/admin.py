from django.contrib import admin
from .models import User
from cart.admin import CartAdmin  # Импортируем ваш InlineModelAdmin

class UserAdmin(admin.ModelAdmin):  # Наследуем от ModelAdmin
    inlines = [CartAdmin]  # Используем InlineModelAdmin

admin.site.register(User, UserAdmin)  # Регистрируем модель и админ-класс