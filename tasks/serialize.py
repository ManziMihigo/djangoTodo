from .models import Tasks
from rest_framework import serializers


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['taskText', 'taskStatus']


