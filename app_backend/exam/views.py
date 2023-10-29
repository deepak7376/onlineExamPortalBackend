from rest_framework import viewsets
from .models import Role, SubscriptionStatus, UserProfile, User, Category, Question, QuestionOption, ExamType, Exam, ExamQuestionRelation, UserExamRelation, ExamAttemptStatus, ExamCategoryRelation
from .serializers import RoleSerializer, SubscriptionStatusSerializer, UserProfileSerializer, UserSerializer, CategorySerializer, QuestionSerializer, QuestionOptionSerializer, ExamTypeSerializer, ExamSerializer, ExamQuestionRelationSerializer, UserExamRelationSerializer, ExamAttemptStatusSerializer, ExamCategoryRelationSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class SubscriptionStatusViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionStatus.objects.all()
    serializer_class = SubscriptionStatusSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionOptionViewSet(viewsets.ModelViewSet):
    queryset = QuestionOption.objects.all()
    serializer_class = QuestionOptionSerializer

class ExamTypeViewSet(viewsets.ModelViewSet):
    queryset = ExamType.objects.all()
    serializer_class = ExamTypeSerializer

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class ExamQuestionRelationViewSet(viewsets.ModelViewSet):
    queryset = ExamQuestionRelation.objects.all()
    serializer_class = ExamQuestionRelationSerializer

class UserExamRelationViewSet(viewsets.ModelViewSet):
    queryset = UserExamRelation.objects.all()
    serializer_class = UserExamRelationSerializer

class ExamAttemptStatusViewSet(viewsets.ModelViewSet):
    queryset = ExamAttemptStatus.objects.all()
    serializer_class = ExamAttemptStatusSerializer

class ExamCategoryRelationViewSet(viewsets.ModelViewSet):
    queryset = ExamCategoryRelation.objects.all()
    serializer_class = ExamCategoryRelationSerializer
