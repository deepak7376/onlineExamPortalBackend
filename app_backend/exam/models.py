from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('student', 'Student'),
    ]
    SUBSCRIPTION_STATUS_CHOICES = [
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('canceled', 'Canceled'),
    ]

    status_name = models.CharField(max_length=255, choices=SUBSCRIPTION_STATUS_CHOICES)
    role_name = models.CharField(max_length=255, choices=ROLE_CHOICES)
    username = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    registration_date = models.DateTimeField()
    last_login = models.DateTimeField()

    def __str__(self):
        return self.username


class Question(models.Model):
    QUESTION_TYPES = [
        ('multiple_choice', 'Multiple Choice'),
        ('true_false', 'True/False'),
        # Add other question types as needed
    ]
    DIFFICULTY_LEVEL = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    question_text = models.TextField()
    question_tag = models.CharField(max_length=255, blank=True)
    question_type = models.CharField(max_length=255, choices=QUESTION_TYPES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    difficulty_level = models.CharField(max_length=255, choices=DIFFICULTY_LEVEL)
    option_text = models.JSONField(default=list)
    correct_answer = models.JSONField(default=list)

    
class Exam(models.Model):
    EXAM_TYPE_CHOICES = [
        ('subjectwise', 'Subject Wise'),
        ('mock', 'Mock'),
        ('premium', 'Premium'),
    ]
    CATEGORY_TYPES = [
        ('Science', 'Science'),
        ('Mathematics', 'Mathematics'),
        ('OnlineExam', 'OnlineExam'),
    ]
    CATEGORY_NAMES = [
        ('SSC', 'SSC'),
        ('GATE', 'GATE'),
        ('CAT', 'CAT'),
    ]

    category_name = models.CharField(max_length=255, choices=CATEGORY_NAMES)
    category_type = models.CharField(max_length=255, choices=CATEGORY_TYPES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    exam_type = models.CharField(max_length=255, choices=EXAM_TYPE_CHOICES)
    duration = models.PositiveIntegerField()
    pass_mark = models.PositiveIntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField()
    code = models.CharField(max_length=255)


class ExamQuestionRelation(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class UserExamRelation(models.Model):
    STATUS_CHOICES = [
        ('inprogress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status_name = models.CharField(max_length=255, choices=STATUS_CHOICES)
    score = models.PositiveIntegerField()




