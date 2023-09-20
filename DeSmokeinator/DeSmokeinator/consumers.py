# livestream/consumers.py
import cv2
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import numpy as np

class LiveStreamConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # OpenCV video capture logic for the live stream
        cap = cv2.VideoCapture(0)  # Use the appropriate camera index
        while True:
            success, frame = cap.read()
            if not success:
                break
            frame = cv2.imencode('.jpg', frame)[1].tobytes()
            await self.send(frame)
            await asyncio.sleep(0.1)

class LiveStreamFaceDetectionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # OpenCV video capture logic for the live stream with face detection
        cap = cv2.VideoCapture(0)  # Use the appropriate camera index
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        while True:
            success, frame = cap.read()
            if not success:
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            frame = cv2.imencode('.jpg', frame)[1].tobytes()
            await self.send(frame)
            await asyncio.sleep(0.1)
