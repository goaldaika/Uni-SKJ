from dataclasses import field, fields
from pyexpat import model
from django.forms import ModelForm

from .models import Classroom, Teacher, Student

class ClassForm(ModelForm):
    class Meta:
        model = Classroom
        fields = '__all__'
class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
class ClassInfo(ModelForm):
    class Meta:
        model = Classroom
        fields = {'teacher', 'course'}
class TeacherInfo(ModelForm):
    class Meta:
        model = Teacher
        fields = {'faculty'}
class StudentInfo(ModelForm):
    class Meta:
        model = Student
        fields = {'faculty', 'phone', 'email', 'grade', 'credit', 'classroom'}
