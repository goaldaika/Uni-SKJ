from cgi import print_exception
from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.
class Teacher(models.Model):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    
    fname = models.TextField(max_length=20)
    lname = models.TextField(max_length=20)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    phone = models.IntegerField(default=None, blank=True, null=True)
    email = models.TextField(max_length=30, default=None, blank=True, null=True)
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE )
    
    def __str__(self):
        return self.lname + ' ' +  self.fname

class Student(models.Model):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]

    fname = models.TextField(max_length=20)
    lname = models.TextField(max_length=20)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE )
    phone = models.IntegerField(default=None, blank=True, null=True)
    email = models.TextField(max_length=30, default=None, blank=True, null=True)
    grade = models.IntegerField()
    credit = models.IntegerField()
    classroom = models.ForeignKey('Classroom',  default=None, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.lname + ' ' + self.fname

class Faculty(models.Model):
    name = models.TextField(max_length=30)
    def __str__(self):
        return f'{self.name}'

class Course(models.Model):
    name = models.TextField(max_length=50)
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE )
    def __str__(self):
        return f'{self.name}'

class Classroom(models.Model):
    name = models.TextField(max_length=20)
    teacher = models.ForeignKey('Teacher',  default=None, blank=True, null=True, on_delete=models.CASCADE )
    course = models.ForeignKey('Course',  default=None, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}'

class Equipment(models.Model):
    name = models.TextField(max_length=50)
    capacity = models.IntegerField()
    classroom = models.ForeignKey('Classroom',  default=None, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}'
