from rest_framework import serializers

from base.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user_id', 'title', 'description', 'complete', 'created_at']