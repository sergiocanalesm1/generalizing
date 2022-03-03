from rest_framework import serializers

from generalizing_core.models.tag import Tag

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('tag')