from rest_framework import routers
from django.urls import path, include
from .views import (
    RoleViewSet,
    SubscriptionStatusViewSet,
    UserProfileViewSet,
    UserViewSet,
    CategoryViewSet,
    QuestionViewSet,
    QuestionOptionViewSet,
    ExamTypeViewSet,
    ExamViewSet,
    ExamQuestionRelationViewSet,
    UserExamRelationViewSet,
    ExamAttemptStatusViewSet,
    ExamCategoryRelationViewSet,
)

router = routers.DefaultRouter()

router.register(r'roles', RoleViewSet)
router.register(r'subscription-statuses', SubscriptionStatusViewSet)
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'question-options', QuestionOptionViewSet)
router.register(r'exam-types', ExamTypeViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'exam-question-relations', ExamQuestionRelationViewSet)
router.register(r'user-exam-relations', UserExamRelationViewSet)
router.register(r'exam-attempt-statuses', ExamAttemptStatusViewSet)
router.register(r'exam-category-relations', ExamCategoryRelationViewSet)



urlpatterns = [
    # Your other URL patterns
    path('api/', include(router.urls)),
]
