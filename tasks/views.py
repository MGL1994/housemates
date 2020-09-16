from django.shortcuts import render
from django.views import View

from .models import Task

class ListView(View):
    
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'index.html', {'tasks': tasks})


class DetailView(View):

    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        return render(request, 'show.html', {'task': task})
