from django.contrib import admin
from .models import Role, SubscriptionStatus, UserProfile, User, Category, Question, QuestionOption, ExamType, Exam, ExamQuestionRelation, UserExamRelation, ExamAttemptStatus, ExamCategoryRelation

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['role_name']

@admin.register(SubscriptionStatus)
class SubscriptionStatusAdmin(admin.ModelAdmin):
    list_display = ['status_name']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'contact_details']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'registration_date', 'last_login', 'role', 'subscription_status']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'category_type']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'question_tag', 'question_type', 'created_by', 'difficulty_level']

@admin.register(QuestionOption)
class QuestionOptionAdmin(admin.ModelAdmin):
    list_display = ['question', 'option_text', 'correct_answer']

@admin.register(ExamType)
class ExamTypeAdmin(admin.ModelAdmin):
    list_display = ['type_name']

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'duration', 'exam_type', 'pass_mark', 'created_by', 'creation_date', 'code', 'scheduled_start_time', 'scheduled_end_time']

@admin.register(ExamQuestionRelation)
class ExamQuestionRelationAdmin(admin.ModelAdmin):
    list_display = ['exam', 'question']

@admin.register(UserExamRelation)
class UserExamRelationAdmin(admin.ModelAdmin):
    list_display = ['user', 'exam', 'start_time', 'end_time', 'status_id', 'score']

@admin.register(ExamAttemptStatus)
class ExamAttemptStatusAdmin(admin.ModelAdmin):
    list_display = ['status_name']

@admin.register(ExamCategoryRelation)
class ExamCategoryRelationAdmin(admin.ModelAdmin):
    list_display = ['exam', 'category']
