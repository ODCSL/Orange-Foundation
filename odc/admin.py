from django.contrib import admin
from .models import Student, Startup, Course

# Register your models here.

admin.site.register(Student)
admin.site.register(Startup)
admin.site.register(Course)
