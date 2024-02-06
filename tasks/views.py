from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Tasks
from .serialize import TasksSerializer


# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filterset_fields = ["taskText", "taskStatus"]
    search_fields = ["taskText"]
    ordering_fields = ["in_progress", "completed"]