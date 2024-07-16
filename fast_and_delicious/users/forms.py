from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, UserProfile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    email = forms.EmailField(label='Email', required=True)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].initial = self.instance.user.email if self.instance.user else ''
