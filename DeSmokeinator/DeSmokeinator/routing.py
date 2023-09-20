# routing.py
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from DeSmokeinator import consumers  # Replace 'livestream' with the name of your app

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/live_stream/", consumers.LiveStreamConsumer.as_asgi()),
        path("ws/live_stream_with_face_detection/", consumers.LiveStreamFaceDetectionConsumer.as_asgi()),
    ]),
})
