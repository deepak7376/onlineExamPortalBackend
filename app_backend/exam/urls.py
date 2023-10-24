from .views import create_exam, get_exam, start_exam
from django.urls import path

urlpatterns = [
    path('api/exams/create/', create_exam, name='create_exam'),
    path('api/exams/<int:exam_id>/', get_exam, name='get_exam'),
    path('api/start_exams/<int:exam_id>/', get_exam, name='start_exam'),
]