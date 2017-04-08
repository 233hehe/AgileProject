from django.contrib import admin
from .models import Student, Counselor, Appointment, Profile
# Register your models here.

admin.site.register(Student)
admin.site.register(Counselor)
admin.site.register(Appointment)
admin.site.register(Profile)