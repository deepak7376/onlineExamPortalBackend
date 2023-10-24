from .views import get_exam_results, create_exam_result
from django.urls import path

urlpatterns = [
    path('api/results/<int:exam_id>/', create_exam_result, name='create_exam_result'),
    path('api/results/', get_exam_results, name='get_exam_results'),
]