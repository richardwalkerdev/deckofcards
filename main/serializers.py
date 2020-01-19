from rest_framework import serializers

class CardSerializer(serializers.Serializer):
    suit = serializers.CharField(max_length=8)
    face = serializers.CharField(max_length=8)
    value = serializers.IntegerField()