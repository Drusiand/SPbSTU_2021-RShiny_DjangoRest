from rest_framework import serializers
from .models import GameUnit


class GameUnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GameUnit
        fields = ("name", "difficulty", "content", "answer")
