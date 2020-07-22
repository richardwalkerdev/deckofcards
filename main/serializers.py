"""This module adds a Serializer for this app"""
from rest_framework import serializers


class CardSerializer(serializers.Serializer):
    """This class adds a Serializer for this app"""
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    suit = serializers.CharField(max_length=8)
    face = serializers.CharField(max_length=8)
    value = serializers.IntegerField()
