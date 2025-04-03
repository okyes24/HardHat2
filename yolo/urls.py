from django.urls import path
from django.conf import settings

from yolo.views import yolo_helmet

urlpatterns = [

    path('yolo_helmet/', yolo_helmet, name='yolo_helmet'),
]