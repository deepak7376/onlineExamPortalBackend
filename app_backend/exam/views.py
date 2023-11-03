from rest_framework import viewsets
from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Question,Exam, ExamQuestionRelation, UserExamRelation
from .serializers import UserSerializer, QuestionSerializer, ExamSerializer, ExamQuestionRelationSerializer, UserExamRelationSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        exam_id = self.request.query_params.get('exam_id', None)
        if exam_id is not None:
            # Get the questions related to the specified exam
            related_question_ids = ExamQuestionRelation.objects.filter(exam=exam_id).values_list('question', flat=True)
            queryset = queryset.filter(id__in=related_question_ids)
            return queryset

        return queryset


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category_name = self.request.query_params.get('category_name', None)

        
        if category_name is not None:
            queryset = queryset.filter(category_name=category_name)
        
        return queryset

    @action(detail=False, methods=['GET'])
    def by_category(self, request, category_name):
        exams = Exam.objects.filter(category_name=category_name)
        print(exams)
        serializer = self.get_serializer(exams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ExamQuestionRelationViewSet(viewsets.ModelViewSet):
    queryset = ExamQuestionRelation.objects.all()
    serializer_class = ExamQuestionRelationSerializer

    @action(detail=False, methods=['GET'])
    def questions_for_exam(self, request):
        exam_id = request.query_params.get('exam_id', None)
        if exam_id is not None:
            questions = ExamQuestionRelation.objects.filter(exam=exam_id).values_list('question', flat=True)
            # Assuming 'question' is the field that links questions to the relation.
            return Response(questions, status=status.HTTP_200_OK)
        return Response("Exam ID not provided", status=status.HTTP_400_BAD_REQUEST)

class UserExamRelationViewSet(viewsets.ModelViewSet):
    queryset = UserExamRelation.objects.all()
    serializer_class = UserExamRelationSerializer