import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import SensarData

class BluetoothConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        accel_x = data.get('AccelX')
        accel_y = data.get('AccelY')
        accel_z = data.get('AccelZ')

        if accel_x is not None and accel_y is not None and accel_z is not None:
            SensarData.objects.create(accel_x=accel_x, accel_y=accel_y, accel_z=accel_z)

        await self.send(text_data=json.dumps({
            'status': 'success'
        }))