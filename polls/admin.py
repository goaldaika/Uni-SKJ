from django.contrib import admin

# Register your models here.
from .models import Student
from .models import Teacher
from .models import Faculty
from .models import Course
from .models import Classroom
from .models import Equipment

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(Classroom)
admin.site.register(Equipment)