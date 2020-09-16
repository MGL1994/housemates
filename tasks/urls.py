from django.urls import path
from .views import DetailView, ListView

urlpatterns = [
    path('', ListView.as_view()),
    path('<int:pk>/', DetailView.as_view()),
]