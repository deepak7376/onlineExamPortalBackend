from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('teacher', 'Teacher'), ('student', 'Student')])
    registration_date = models.DateTimeField()
    last_login = models.DateTimeField(null=True, blank=True)
    subscription_status = models.CharField(max_length=10, choices=[('active', 'Active'), ('expired', 'Expired'), ('canceled', 'Canceled')])