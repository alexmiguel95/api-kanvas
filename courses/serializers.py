from rest_framework import serializers
from accounts.serializers import UserSerializer


class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    user_set = UserSerializer(many=True, read_only=True)
