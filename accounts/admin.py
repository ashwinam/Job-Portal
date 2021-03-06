from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea
from .models import NewUser, Employee, EmployeeProfile, Employer, EmployerProfile, Institution, Company, CompanyImages, Experience, SkillSet, UserSkillSet

# Register your models here.
class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'name',)
    list_filter = ('email', 'name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'name',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
        ('Other', {'fields': ('start_date',)}),
    )
    formfield_overrides = {
        NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )

class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'name','password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
        ('Other', {'fields': ('start_date',)}),
    )

class EmployerAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'name','password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
        ('Other', {'fields': ('start_date',)}),
    )
admin.site.register(NewUser, UserAdminConfig)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Employer, EmployerAdmin)
admin.site.register(EmployeeProfile)
admin.site.register(EmployerProfile)
admin.site.register(Institution)
admin.site.register(Company)
admin.site.register(CompanyImages)
admin.site.register(Experience)
admin.site.register(SkillSet)
admin.site.register(UserSkillSet)