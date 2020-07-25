from django.contrib import admin
from login.models import *
# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list_display=('studentRollno','studentName','studentEmail','password','Due')

admin.site.register(student,studentAdmin)
