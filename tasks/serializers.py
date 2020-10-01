from rest_framework import serializers
from .models import Tag, Task


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')


class TaskSerializer(serializers.ModelSerializer):

    tags = TagSerializer(many=True)

    class Meta:
        model = Task
        fields = ('id', 'task', 'description', 'due_date', 'tags')

    def validate(self, data):
        if data['task'] == data['description']:
            raise serializers.ValidationError({'description': 'More detail required'})
        return data