from django.contrib import admin

from users.models import User


@admin.register(User)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "first_name",
        "last_name",
        "phone",
        "telegram",
        "is_active",
    )
    list_filter = (
        "is_active",
    )
    search_fields = (
        "email",
        "first_name",
        "last_name",
        "telegram",
        "phone",
    )
