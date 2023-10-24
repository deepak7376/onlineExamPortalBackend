from django.db import models
from users.views import User
from exam.views import Exam

# Create your models here.
class UserExamAttempt(models.Model):
    attempt_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=[('in progress', 'In Progress'), ('completed', 'Completed')])
    user_answers = models.JSONField()