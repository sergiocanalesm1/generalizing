from rest_framework import serializers

from generalizing_core.models.user import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'uuid',
            'id',
            'username',
            'email',
            'password',
            'creation_date'
        )