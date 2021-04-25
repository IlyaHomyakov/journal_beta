from django.contrib import admin

from .models import *


class InLineGroupLesson(admin.TabularInline):
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
            )
        }),
    )


admin.site.register(Group, GroupAdmin)


admin.site.register(SemesterOptions)
