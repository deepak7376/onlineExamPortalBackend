from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserExamAttempt
from .serializers import ExamResultSerializer

@api_view(['GET'])
def get_exam_results(request, exam_id):
    try:
        results = UserExamAttempt.objects.filter(exam_id=exam_id)
    except UserExamAttempt.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ExamResultSerializer(results, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_exam_result(request):
    serializer = ExamResultSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

