from rest_framework import serializers

from generalizing_core.models.challenge import Challenge

class ChallengeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Challenge
        fields = '__all__'