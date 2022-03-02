from dataclasses import field
from rest_framework import serializers

from generalizing_core.models.user import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username','email','password','creation_date')