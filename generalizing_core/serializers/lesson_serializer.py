from generalizing_core.serializers.user_serializer import UserSerializer
from rest_framework import serializers

from generalizing_core.models.lesson import Lesson
from generalizing_core.serializers.tag_serializer import TagSerializer

class LessonSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    tags = TagSerializer(source='tags_set', many=True)

    class Meta:
        model = Lesson
        fields = (
            'uuid',
            'id',
            'name',
            'creation_date',
            'description',
            'origin',
            'domain',
            'tags',
            'user',
        )