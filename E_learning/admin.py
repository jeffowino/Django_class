from django.contrib import admin
from .models import Student, Attendance, Marks, Notice

admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(Marks)
admin.site.register(Notice)
