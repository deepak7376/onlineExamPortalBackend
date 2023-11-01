from rest_framework import serializers
from .models import  User, Question,  Exam, ExamQuestionRelation, UserExamRelation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class ExamQuestionRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamQuestionRelation
        fields = '__all__'

class UserExamRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExamRelation
        fields = '__all__'

