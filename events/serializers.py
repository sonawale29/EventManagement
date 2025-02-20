from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, Event, Ticket


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user registration"""
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'role']


class EventSerializer(serializers.ModelSerializer):
    """Serializer for event creation and listing"""
    class Meta:
        model = Event
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    """Serializer for ticket purchases"""
    class Meta:
        model = Ticket
        fields = '__all__'
