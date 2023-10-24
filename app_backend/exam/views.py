from .models import Exam
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ExamSerializer
from .models import Exam, Question
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ExamSerializer, QuestionSerializer

@api_view(['POST'])
def create_exam(request):
    if request.method == 'POST':
        print(f"request_data:  {request.data}")
        serializer = ExamSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_exam(request, exam_id):
    try:
        exam = Exam.objects.get(exam_id=exam_id)
    except Exam.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ExamSerializer(exam)
    return Response(serializer.data)



@api_view(['GET'])
def start_exam(request, exam_id):
    try:
        exam = Exam.objects.get(exam_id=exam_id)
    except Exam.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Retrieve questions related to the exam
    questions = Question.objects.filter(exam=exam)

    # Serialize the questions
    serializer = QuestionSerializer(questions, many=True)

    # You can return both the exam information and the related questions
    response_data = {
        'exam': ExamSerializer(exam).data,
        'questions': serializer.data
    }

    return Response(response_data)



