from rest_framework import serializers
from accounts.models import User


class ActivitiesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    repo = serializers.CharField()
    grade = serializers.IntegerField(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
