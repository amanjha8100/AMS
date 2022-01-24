from django.contrib import admin
from .models import student,subject,attendanceclass,time,attendance,User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, user_type
# Register your models here.
admin.site.register(student)
admin.site.register(subject)
admin.site.register(time)
admin.site.register(attendance)
@admin.register(attendanceclass)
class attendaceAdmin(admin.ModelAdmin):
    list_display = ('date','status')

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'name', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)
