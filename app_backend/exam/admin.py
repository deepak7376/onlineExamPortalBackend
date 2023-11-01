from django.contrib import admin
from .models import User, Question, Exam, ExamQuestionRelation, UserExamRelation

# Define custom admin classes for each model

class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]

class QuestionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Question._meta.fields]

class ExamAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Exam._meta.fields]

class ExamQuestionRelationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ExamQuestionRelation._meta.fields]

class UserExamRelationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserExamRelation._meta.fields]

# Register the models with the custom admin classes
admin.site.register(User, UserAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(ExamQuestionRelation, ExamQuestionRelationAdmin)
admin.site.register(UserExamRelation, UserExamRelationAdmin)
