from django.contrib import admin

from habit_tracker.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "action",
        "user",
        "place",
        "time",
        "periodical",
        "pleasant_action",
        "reward",
        "is_public",
        "pleasant_sign",
    )

    list_filter = (
        "user",
        "action",
        "periodical",
        "is_public",
        "pleasant_sign",
    )
    search_fields = (
        "user",
        "action",
        "is_public",
        "pleasant_sign",
    )
