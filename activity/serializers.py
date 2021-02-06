from rest_framework import serializers
from accounts.serializers import UserSerializer


class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    repo = serializers.CharField()
    grade = serializers.FloatField()
    user_id = UserSerializer(read_only=True)
