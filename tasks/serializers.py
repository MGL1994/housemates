from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'task', 'description', 'due_date')

    def validate(self, data):
        if data['task'] == data['description']:
            raise serializers.ValidationError({'description': 'More detail required'})

        return data