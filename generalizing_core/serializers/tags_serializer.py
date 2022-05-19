from rest_framework import serializers

from generalizing_core.models.tag import Tag

class TagsReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'