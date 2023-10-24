from django.contrib import admin
from .models import UserExamAttempt

# Register your models here.
@admin.register(UserExamAttempt)
class UserExamAttemptAdmin(admin.ModelAdmin):
    list_display = ('attempt_id', 'user', 'exam', 'start_time', 'status')
    list_filter = ('status',)
    search_fields = ('user__username', 'exam__title')