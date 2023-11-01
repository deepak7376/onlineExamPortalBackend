from rest_framework import viewsets
from .models import User, Question,Exam, ExamQuestionRelation, UserExamRelation
from .serializers import UserSerializer, QuestionSerializer, ExamSerializer, ExamQuestionRelationSerializer, UserExamRelationSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer



class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer



class ExamQuestionRelationViewSet(viewsets.ModelViewSet):
    queryset = ExamQuestionRelation.objects.all()
    serializer_class = ExamQuestionRelationSerializer

class UserExamRelationViewSet(viewsets.ModelViewSet):
    queryset = UserExamRelation.objects.all()
    serializer_class = UserExamRelationSerializer
