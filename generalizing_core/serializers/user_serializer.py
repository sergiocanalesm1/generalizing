from rest_framework import serializers

from generalizing_core.models.user import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uuid',
            'email',
            'birth_date',
            'gender',
            'workspace',
            'city_population',
            'average_weekly_sleep_hrs',
            'creation_date',
        ]