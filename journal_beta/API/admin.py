from django.contrib import admin

from .models import *


class InLineGroupLesson(admin.StackedInline):
    model = GroupLesson
    extra = 0


class GroupAdmin(admin.ModelAdmin):
    inlines = [InLineGroupLesson]
    list_display = ('group_number', 'faculty_choice', 'course_choice')
    fieldsets = (
        (None, {
            'fields': (
                'group_number',
                'faculty_choice',
                'course_choice',
                'semester_start_date',
                'semester_end_date',
                'group_week_type_choice',
                'session_start_date',
                'session_end_date',
                'educational_practice_start_date',
                'educational_practice_end_date',
                'holidays_start_date',
                'holidays_end_date',
            )
        }),
    )


admin.site.register(Group, GroupAdmin)
