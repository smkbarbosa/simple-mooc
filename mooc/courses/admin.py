from django.contrib import admin

from .models import Course


class CourseAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'start_course', 'created_at']
    search_fields = ['name', 'slug']

admin.site.register(Course, CourseAdmin)
