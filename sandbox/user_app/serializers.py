from rest_framework import serializers
from user_app.models import SandyUser


class SandyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SandyUser
        fields = ('username', 'email', 'first_name', 'last_name')
