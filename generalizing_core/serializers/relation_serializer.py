from rest_framework import serializers

from generalizing_core.models.relation import Relation

class RelationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Relation
        fields = '__all__'