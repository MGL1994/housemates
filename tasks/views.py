from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tag, Task
from .serializers import TagSerializer, TaskSerializer

class TaskList(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# class TagListView(APIView):

#     def get(self, _request):
#         tags = Tag.objects.all()
#         serializer = TaskSerializer(tags, many=True)
#         return Response(serializer.data)