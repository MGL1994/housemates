from django.urls import path
from .views import OwnerList, OwnerDetail, TaskList, TaskDetail

urlpatterns = [
    path('', TaskList.as_view()),
    path('<int:pk>/', TaskDetail.as_view()),
    path('owners/', OwnerList.as_view()),
    path('owners/<int:pk>/', OwnerDetail.as_view()),
]