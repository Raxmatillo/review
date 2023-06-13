from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Role


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ("email", "first_name", "last_name", "status")
    list_filter = ("status",)
    fieldsets = (
        (None, {"fields": ("email",)}),
        ("Permissions", {"fields": ("first_name", "last_name",
         "status", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "first_name", "last_name", "email", "password1", "password2", 'status', "groups", "user_permissions",\
                "job_title", "role", "organization", "phone_number", "address"
            )}
         ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(Role)