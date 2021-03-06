from django.contrib import admin
from .models import student,subject,attendanceclass,time,attendance
# Register your models here.
admin.site.register(student)
admin.site.register(subject)
admin.site.register(time)
admin.site.register(attendance)
@admin.register(attendanceclass)
class attendaceAdmin(admin.ModelAdmin):
    list_display = ('date','status')