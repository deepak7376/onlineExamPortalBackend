# serializers.py

from rest_framework import serializers
from .models import UserExamAttempt

class ExamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExamAttempt
        fields = '__all__'
