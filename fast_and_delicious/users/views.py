from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .models import UserProfile
from .forms import UserRegistrationForm, UserProfileForm

class UserRegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        # Создаем пользователя
        response = super().form_valid(form)
        user = form.save()

        # Создаем профиль пользователя
        UserProfile.objects.create(user=user)

        # Логиним пользователя сразу после регистрации
        login(self.request, user)

        return response

class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserProfileView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('products:index')

    def get_object(self, queryset=None):
        # Получаем или создаем профиль текущего пользователя
        user_profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        return user_profile

    def get_initial(self):
        initial = super().get_initial()
        user_profile = self.get_object()
        initial['first_name'] = user_profile.user.first_name
        initial['last_name'] = user_profile.user.last_name
        initial['email'] = user_profile.user.email
        return initial

    def form_valid(self, form):
        user_profile = form.save(commit=False)
        user_profile.user.first_name = form.cleaned_data['first_name']
        user_profile.user.last_name = form.cleaned_data['last_name']
        user_profile.user.email = form.cleaned_data['email']

        user_profile.user.save()
        user_profile.save()
        return super().form_valid(form)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')