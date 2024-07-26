import serial
import asyncio
import websockets
import json

# Adjust the serial port name and baud rate according to your setup
ser = serial.Serial('COM3', 9600)  # For Windows
# ser = serial.Serial('/dev/tty.HC-05-DevB', 9600)  # For macOS

async def send_data():
    uri = "ws://127.0.0.1:8000/ws/bluetooth/"
    async with websockets.connect(uri) as websocket:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                if "AccelX" in line:
                    data = {kv.split(":")[0]: float(kv.split(":")[1]) for kv in line.split(",")}
                    await websocket.send(json.dumps(data))
                    response = await websocket.recv()
                    print(response)

asyncio.get_event_loop().run_until_complete(send_data())