from msilib.schema import Class
from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Teacher, Student, Faculty, Course, Classroom, Equipment
from .forms import ClassForm, ClassInfo, StudentForm, StudentInfo, TeacherForm, TeacherInfo

# Create your views here.
def index(request):
    #classes = Classroom.objects.all()

    return render(request, 'polls/index.html')
#############################
def class_list(request):
    classes = Classroom.objects.all()

    return render(request, 'polls/class_list.html', {'classes': classes})

def student_list(request):
    students = Student.objects.all()

    return render(request, 'polls/student_list.html', {'students': students})

def teacher_list(request):
    teachers = Teacher.objects.all()

    return render(request, 'polls/teacher_list.html', {'teachers': teachers})
###############################
def classroom(request, classroom_id):
    classroom = get_object_or_404(Classroom, pk=classroom_id)    
    #teacher = classroom.teacher_set.first()
    teachers = Teacher.objects.filter(classroom=classroom)
    #print(teachers)
    students = Student.objects.filter(classroom=classroom)
    courses = Course.objects.filter(classroom=classroom)
    equipment = Equipment.objects.filter(classroom=classroom)
    return render(request, 'polls/classroom.html', {'classroom':classroom, 'teachers':teachers, 'students':students, 'courses':courses, 'equipments':equipment})

def add_class(request):
    form = ClassForm()
    if request.method == 'POST':
        form  = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    context = {'form' : form    }
    return render(request, 'form/addclass.html',context)

def update_class(request, classroom_id):
    classroom = Classroom.objects.get(pk = classroom_id)
    form = ClassInfo(instance = classroom)

    if request.method == 'POST':
        form  = ClassInfo(request.POST, instance = classroom)
        if form.is_valid():
            form.save()
            return redirect('class_list')

    context = {'form':form}
    return render(request, 'form/addclass.html',context)

def delete_class(request, classroom_id):
    classroom = Classroom.objects.get(pk = classroom_id)
    if request.method == 'POST':
        classroom.delete()
        return redirect('class_list')
    context = {'class':classroom}
    return render(request, 'form/delete_class.html', context)
#################################
def teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    faculties = Faculty.objects.filter(teacher=teacher)
    courses = teacher.faculty.course_set.all()
    
    classrooms = Classroom.objects.filter(teacher=teacher)
    #students = Student.objects.filter(teacher=teacher)
    students = []
    for cls in classrooms:
        students.extend(Student.objects.filter(classroom=cls))

    return render(request, 'polls/teacher.html', {'teacher': teacher,'faculties': faculties, 'courses':courses,'classrooms':classrooms, 'students':students})

def add_teacher(request):
    form = TeacherForm()
    if request.method == 'POST':
        form  = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    context = {'form' : form    }
    return render(request, 'form/addteacher.html',context)

def update_teacher(request, teacher_id):
    teacher = Teacher.objects.get(pk = teacher_id)
    form = TeacherInfo(instance = teacher)

    if request.method == 'POST':
        form  = TeacherInfo(request.POST, instance = teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    context = {'form':form}
    return render(request, 'form/addteacher.html',context)

def delete_teacher(request, teacher_id):
    teacher = Teacher.objects.get(pk = teacher_id)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    context = {'teacher':teacher}
    return render(request, 'form/delete_teacher.html', context)
#################################
def student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    faculty = Faculty.objects.filter(student=student)
    courses = student.faculty.course_set.all()
    classroom = Classroom.objects.filter(student=student)
    return render(request, 'polls/student.html', {'student': student,'faculty': faculty, 'courses':courses,'classrooms':classroom})

def update_student(request, student_id):
    student = Student.objects.get(pk = student_id)
    form = StudentInfo(instance = student)

    if request.method == 'POST':
        form  = StudentInfo(request.POST, instance = student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    context = {'form':form}
    return render(request, 'form/addstudent.html',context)

def delete_student(request, student_id):
    student = Student.objects.get(pk = student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    context = {'student':student}
    return render(request, 'form/delete_student.html', context)

def add_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form  = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    context = {'form' : form    }
    return render(request, 'form/addstudent.html',context)
##################################
def course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    classrooms = Classroom.objects.filter(course=course)
    faculty = Faculty.objects.filter(course=course)
    teachers = []#courses.faculty.course_set.all()
    for cls in classrooms:
        teachers.append(cls.teacher)
    students = []
    for cls in classrooms:
        students.extend(Student.objects.filter(classroom=cls))
    return render(request, 'polls/course.html', {'course': course,'faculties': faculty, 'teachers':teachers,'students':students})

def faculty(request, faculty_id):
    faculties = get_object_or_404(Faculty, pk=faculty_id)
    courses = Course.objects.filter(faculty=faculties)
    teachers = Teacher.objects.filter(faculty=faculties)
    students = Student.objects.filter(faculty=faculties)
    return render(request, 'polls/faculty.html', {'faculty': faculties,'courses': courses, 'teachers':teachers, 'students':students})

