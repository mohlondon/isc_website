from django.shortcuts import render
from .models import Event
from .serializers import EventsSerializer
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView)
from django.http import JsonResponse


class EventsListAPI(ListView):
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = EventsSerializer(queryset, many=True).data
        return JsonResponse(
            data, status=200, safe=False)

    def get_queryset(self):
        return Event.objects.filter(status=1)
