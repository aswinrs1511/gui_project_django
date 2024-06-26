"""
URL configuration for GUI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from basics.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('about/',about,name="about"),
    path('aboutus/',aboutus,name="aboutus"),
    path('register/',register,name="register"),
    path('calc/',calc,name="calc"),
    path('index/',index,name="index"),
    path('dept/',department,name="department"),
    path('deptview/',departmentview,name="departmentview"),
    path('marks/',marks,name="marks"),
    path('departmentupdate/<id>',departmentupdate,name="departmentupdate"),
    path('student/',student,name="student"),
    path('studentview/',studentview,name="studentview"),
    path('student/delete/<int:student_id>/', delete_student, name="delete_student"),
    path('studentupdate/<id>',studentupdate,name="studentupdate"),
    path('registration/',registration,name="registration"),
    path('userlogin/',userlogin,name="userlogin"),
    path('userlogout/',userlogout,name="userlogout"),










]
