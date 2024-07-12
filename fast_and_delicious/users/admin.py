from django.contrib import admin
from .models import UserProfile
from cart.admin import CartTabAdmin  # Ensure this is correct

class UserProfileAdmin(admin.ModelAdmin):
    inlines = [CartTabAdmin]

admin.site.register(UserProfile, UserProfileAdmin)