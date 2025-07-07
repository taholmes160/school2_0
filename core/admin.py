from django.contrib import admin

from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'username', 'first_name', 'last_name', 'grade', 'email')
    search_fields = ('student_id', 'username', 'first_name', 'last_name', 'email')
    list_filter = ('grade',)
# Register your models here.
