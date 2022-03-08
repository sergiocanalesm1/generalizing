from rest_framework import serializers

from generalizing_core.models.expertise import Expertise

class ExpertiseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expertise
        fields = '__all__'