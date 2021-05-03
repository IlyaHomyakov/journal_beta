from django.contrib import admin

from .models import *


class InLineGroupLesson(admin.StackedInline):
    model = GroupLesson
    extra = 0


class GroupAdmin(admin.ModelAdmin):
    inlines = [InLineGroupLesson]
    list_display = ('groupNumber', 'facultyChoice', 'courseChoice')
    fieldsets = (
        (None, {
            'fields': (
                'groupNumber',
                'facultyChoice',
                'courseChoice',
                'semesterStartDate',
                'semesterEndDate',
                'groupWeekTypeChoice',
                'sessionStartDate',
                'sessionEndDate',
                'educationalPracticeStartDate',
                'educationalPracticeEndDate',
                'holidaysStartDate',
                'holidaysEndDate',
            )
        }),
    )


admin.site.register(Group, GroupAdmin)
