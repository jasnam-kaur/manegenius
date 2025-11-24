from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# This class tells Django how to display your custom fields in the Admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # These are the fields to display in the list view (columns)
    list_display = ['email', 'username', 'enrollment_number', 'college', 'is_staff']
    
    # These are the fields to display when editing a specific user
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('enrollment_number', 'course_and_shift', 'college')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('enrollment_number', 'course_and_shift', 'college')}),
    )

# Register the model
admin.site.register(CustomUser, CustomUserAdmin)