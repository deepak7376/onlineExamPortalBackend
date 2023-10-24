from django.contrib import admin
from .models import Exam, Question, Category, QuestionExamRelationship


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('exam_id', 'title', 'duration', 'created_by', 'creation_date', 'code')
    list_filter = ('created_by', 'creation_date')
    search_fields = ('title', 'code')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'question_text', 'question_type', 'category_list')
    list_filter = ('question_type', 'category')
    search_fields = ('question_text',)

    def category_list(self, obj):
        # questions = Question.objects.filter(category=obj.category)  # Access questions related to the same category
        # question_list = ", ".join([str(question.question_text) for question in questions])
        return obj.category.category_name

    category_list.short_description = 'Categories'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name')
    search_fields = ('category_name',)

@admin.register(QuestionExamRelationship)
class QuestionExamRelationshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'exam')
