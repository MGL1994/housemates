from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Tag, Task

class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', )


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')


class TaskSerializer(serializers.ModelSerializer):

    tags = TagSerializer(many=True, read_only=True)
    owner = OwnerSerializer()

    class Meta:
        model = Task
        fields = ('id', 'task', 'description', 'due_date', 'tags', 'owner')

    def validate(self, data):
        if data['task'] == data['description']:
            raise serializers.ValidationError({'description': 'More detail required'})
        return data