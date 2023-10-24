from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'username', 'email', 'password', 'role', 'registration_date', 'last_login', 'subscription_status')
        extra_kwargs = {
            'password': {'write_only': True},  # The 'password' field should not be displayed in responses.
            'last_login': {'read_only': True},  # The 'last_login' field is read-only.
            'registration_date': {'read_only': True},  # The 'registration_date' field is read-only.
        }

    def create(self, validated_data):
        # Create and return a new User instance, given the validated data.
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        # Update and return an existing User instance with the validated data.
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.role = validated_data.get('role', instance.role)
        instance.subscription_status = validated_data.get('subscription_status', instance.subscription_status)
        
        # Update the password if provided (requires additional password hashing logic).
        password = validated_data.get('password')
        if password:
            instance.set_password(password)

        instance.save()
        return instance

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'role', 'subscription_status')
        extra_kwargs = {
            'password': {'write_only': True},
            'role': {'default': 'student'},  # Set a default role
            'subscription_status': {'default': 'active'},  # Set a default subscription status
        }