from django.db import models
from users.models import User

class Exam(models.Model):
    exam_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.PositiveIntegerField()
    pass_marks = models.PositiveIntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField()
    code = models.CharField(max_length=10, unique=True, default='YOUR_DEFAULT_CODE_VALUE')

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    exams = models.ManyToManyField(Exam, through='QuestionExamRelationship')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    question_text = models.TextField()
    question_type = models.CharField(max_length=15, choices=[('multiple-choice', 'Multiple Choice'), ('true-false', 'True/False'), ('short-answer', 'Short Answer')])
    options = models.JSONField(null=True, blank=True)  # Store options as JSON
    correct_answer = models.TextField(null=True, blank=True)  # For multiple-choice questions

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)


class QuestionExamRelationship(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)