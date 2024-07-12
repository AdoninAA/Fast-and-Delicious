from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='custom_user_set', 
        related_query_name='custom_user', 
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name='custom_user_set',  
        related_query_name='custom_user',  
    )
    

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Add additional fields here
    # Example:
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    



    def __str__(self):
        return self.username