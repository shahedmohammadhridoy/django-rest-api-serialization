from django.urls import path
from . import views

urlpatterns = [
    path('Api/', views.StudentView, name='stu-api')
]
