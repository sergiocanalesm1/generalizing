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
            'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance