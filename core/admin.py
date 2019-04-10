from django.contrib import admin
from core.models import *

from import_export.admin import ImportExportModelAdmin

admin.site.site_title = "School Management System"
admin.site.site_header = "School Management System"


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'user_id', 'email', 'mobile_number', 'is_student']
    list_filter = ['is_student', 'is_executive', 'is_admin', 'is_photographer']

@admin.register(StudentInformation)
class StudentInformationAdmin(ImportExportModelAdmin):
    list_display = ['id', 'full_name', 'father_name', 'mother_name', 'studying_class', 'section']
    list_filter = ['studying_class', 'section', 'school_name']

@admin.register(SchoolInformation)
class SchoolInformationAdmin(admin.ModelAdmin):
    list_display = ['id', 'school_code', 'school_name', 'school_principal_name']
    list_filter = ['school_city', 'school_state', 'zipcode']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'message']

@admin.register(VerificationCard)
class VerificationCardAdmin(admin.ModelAdmin):
    list_display = ['user', 'student_information', 'is_verified_by_student']
    list_filter = ['is_verified_by_student']

