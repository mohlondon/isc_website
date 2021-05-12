from django.urls import path
from .views import EventsListAPI

app_name = 'Events'

urlpatterns = [
    path('api/list/', EventsListAPI.as_view(), name="Events_list_api"),
]
