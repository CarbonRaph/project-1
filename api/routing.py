from django.urls import path
from .consumers import BluetoothConsumer

websocket_urlpatterns = [
    path('ws/bluetooth/', BluetoothConsumer.as_asgi()),
]