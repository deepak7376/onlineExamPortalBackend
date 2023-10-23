from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'role', 'registration_date', 'subscription_status')
    list_filter = ('role', 'subscription_status')
    search_fields = ('username', 'email')




