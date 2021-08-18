
from django.contrib import admin
from django.urls import path ,include
from thread import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', views.student_details),
]