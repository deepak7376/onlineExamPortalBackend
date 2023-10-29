from django.db import models

class Role(models.Model):
    role_name = models.CharField(max_length=255)

    def __str__(self):
        return self.role_name

class SubscriptionStatus(models.Model):
    status_name = models.CharField(max_length=255)

    def __str__(self):
        return self.status_name

class UserProfile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=255)
    preferences = models.TextField()

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    registration_date = models.DateTimeField()
    last_login = models.DateTimeField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    subscription_status = models.ForeignKey(SubscriptionStatus, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_type = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.category_name

class Question(models.Model):
    question_text = models.TextField()
    question_tag = models.CharField(max_length=255, blank=True)
    question_type = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    difficulty_level = models.CharField(max_length=255)

class QuestionOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=255)
    correct_answer = models.BooleanField()

class ExamType(models.Model):
    type_name = models.CharField(max_length=255)

    def __str__(self):
        return self.type_name

class Exam(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    exam_type = models.ForeignKey(ExamType, on_delete=models.CASCADE)
    pass_mark = models.PositiveIntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField()
    code = models.CharField(max_length=255)
    scheduled_start_time = models.DateTimeField()
    scheduled_end_time = models.DateTimeField()

class ExamQuestionRelation(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class UserExamRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status_id = models.ForeignKey('ExamAttemptStatus', on_delete=models.CASCADE)
    score = models.PositiveIntegerField()

class ExamAttemptStatus(models.Model):
    status_name = models.CharField(max_length=255)

    def __str__(self):
        return self.status_name

class ExamCategoryRelation(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
