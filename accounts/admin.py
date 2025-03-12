from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

CustomerUser = get_user_model()

# Register your models here.
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = (
        'email',
        'username',
        'is_superuser'
    )


admin.site.register(CustomUser, CustomUserAdmin)