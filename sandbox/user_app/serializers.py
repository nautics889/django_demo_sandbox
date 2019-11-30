import django.contrib.auth.password_validation as validators
from django.core import exceptions
from rest_framework import serializers

from user_app.models import SandyUser


class SandyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SandyUser
        fields = ('username', 'email', 'status', 'password')

    email = serializers.EmailField(required=True, min_length=5)
    password = serializers.CharField(
        write_only=True,
        required=True,
    )

    def validate(self, data):
        password = data.get('password', None)

        try:
            validators.validate_password(password)
        except exceptions.ValidationError:
            raise
        else:
            return super(SandyUserSerializer, self).validate(data)

    def create(self, validated_data):
        validated_data['is_active'] = False
        return SandyUser.objects.create_user(**validated_data)
