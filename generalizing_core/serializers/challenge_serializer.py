from rest_framework import serializers

from generalizing_core.serializers.lesson_serializer import LessonReadSerializer
from generalizing_core.models.challenge import Challenge

class ChallengeReadSerializer(serializers.ModelSerializer):

    lesson_1 = LessonReadSerializer(read_only=True)
    lesson_2 = LessonReadSerializer(read_only=True)

    class Meta:
        model = Challenge
        fields = '__all__'

class ChallengeWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Challenge
        fields = '__all__'