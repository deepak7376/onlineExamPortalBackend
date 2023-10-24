from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    
    # Set default values for the registration_date, last_login, and role fields.
    registration_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)
    role = models.CharField(
        max_length=10,
        choices=[('admin', 'Admin'), ('teacher', 'Teacher'), ('student', 'Student')],
        default='student'  # You can set the default role to 'student' or any other value.
    )
    
    subscription_status = models.CharField(
        max_length=10,
        choices=[('active', 'Active'), ('expired', 'Expired'), ('canceled', 'Canceled')],
        default='active'  # Set the default subscription_status to 'active' or another value.
    )
