from rest_framework import routers
from django.urls import path, include
from .views import (
    UserViewSet,
    QuestionViewSet,
    ExamViewSet,
    ExamQuestionRelationViewSet,
    UserExamRelationViewSet,
)

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'exam-question-relations', ExamQuestionRelationViewSet)
router.register(r'user-exam-relations', UserExamRelationViewSet)



urlpatterns = [
    # Your other URL patterns
    path('api/', include(router.urls)),
]
