from django.db import models

class User(models.Model):
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
    question_text = models.TextField()
    option_text = models.TextField(default=list)
    correct_answer = models.TextField(default=list)
    

class Exam(models.Model):
    EXAM_TYPE_CHOICES = [
        ('subjectwise', 'Subject Wise'),
        ('mock', 'Mock'),
        ('premium', 'Premium'),
    ]
    CATEGORY_NAMES = [
        ('SSC', 'SSC'),
        ('GATE', 'GATE'),
        ('CAT', 'CAT'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    exam_type = models.CharField(max_length=255, choices=EXAM_TYPE_CHOICES)
    category_name = models.CharField(max_length=255, choices=CATEGORY_NAMES)
    duration = models.PositiveIntegerField()
    pass_mark = models.PositiveIntegerField()
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




