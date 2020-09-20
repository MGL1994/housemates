from rest_framework import serializers
from .models import Owner, Tag, Task

class NestedTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'task', 'description', 'due_date')


class NestedOwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = ('id', 'name')


class OwnerSerializer(serializers.ModelSerializer):

    tasks = NestedTaskSerializer(many=True)

    class Meta:
        model = Owner
        fields = ('id', 'name', 'tasks')


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')


class TaskSerializer(serializers.ModelSerializer):

    owner = NestedOwnerSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Task
        fields = ('id', 'task', 'description', 'due_date', 'owner', 'tags')

    def validate(self, data):
        if data['task'] == data['description']:
            raise serializers.ValidationError({'description': 'More detail required'})

        return data