from rest_framework import serializers
from .models import Role, SubscriptionStatus, UserProfile, User, Category, Question, QuestionOption, ExamType, Exam, ExamQuestionRelation, UserExamRelation, ExamAttemptStatus, ExamCategoryRelation

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class SubscriptionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionStatus
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = '__all__'

class ExamTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamType
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

class ExamAttemptStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamAttemptStatus
        fields = '__all__'

class ExamCategoryRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamCategoryRelation
        fields = '__all__'
