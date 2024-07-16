from django.contrib import admin
from .models import User, UserProfile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email"]
    search_fields = ["username", "first_name", "last_name", "email"]


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'date_of_birth', 'phone_number')
    search_fields = ('user__username', 'first_name', 'last_name', 'phone_number')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)