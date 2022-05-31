"""MyStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from polls import views
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index' ),

    path('student_list', views.student_list, name = 'student_list' ),
    path('student/<int:student_id>/', views.student, name='student'),
    path('update_student/<int:student_id>>', views.update_student,name = "update_student"),
    path('delete_student/<int:student_id>>', views.delete_student,name = "delete_student"),
    path('create_student/', views.add_student,name = "create_student"),

    path('teacher_list', views.teacher_list, name = 'teacher_list' ),
    path('teacher/<int:teacher_id>/', views.teacher, name='teacher'),
    path('update_teacher/<int:teacher_id>>', views.update_teacher,name = "update_teacher"),
    path('delete_teacher/<int:teacher_id>>', views.delete_teacher,name = "delete_teacher"),
    path('create_teacher/', views.add_teacher,name = "create_teacher"),

    path('class_list', views.class_list, name = 'class_list' ),
    path('classroom/<int:classroom_id>/', views.classroom, name='classroom'),
    path('update_class/<int:classroom_id>>', views.update_class,name = "update_class"),
    path('delete_class/<int:classroom_id>>', views.delete_class,name = "delete_class"),
    path('create_class/', views.add_class,name = "create_class"),

    path('faculty/<int:faculty_id>/', views.faculty, name='faculty'),
    path('course/<int:course_id>/', views.course, name='course'),


    path('', include("django.contrib.auth.urls")),
]
