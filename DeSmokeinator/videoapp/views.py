from django.shortcuts import render

import cv2
import numpy as np
from django.http import StreamingHttpResponse
from django.views.decorators import gzip

def web_view(request):
    return render(request, 'live_stream.html')

class VideoCamera(object):
    def __init__(self):
        pass

def generate_frames(self):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        if not success:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
@gzip.gzip_page
def livestream(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(generate_frames(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except: 
        pass

def fire(request):
    fire_reported = 0
    email_status = False
    alarm_status = False
    video = cv2.VideoCapture("E:/fire1/fire1/video.mp4")
    
    while True:
        ret, frame = video.read()
        
        if not ret:
            # End of video, reset capture to loop
            video.release()
            video = cv2.VideoCapture("E:/fire1/fire1/video.mp4")
            continue
        
        frame = cv2.resize(frame, (1000, 600))
        blur = cv2.GaussianBlur(frame, (15, 15), 0)
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
        
        lower = [22, 50, 50]
        upper = [35, 255, 255]
    
        lower = np.array(lower, dtype='uint8')
        upper = np.array(upper, dtype='uint8')
        mask = cv2.inRange(hsv, lower, upper)
        output = cv2.bitwise_and(frame, hsv, mask=mask)
        number_of_total = cv2.countNonZero(mask)
        
        if int(number_of_total) > 2000:
            fire_reported = fire_reported + 1

        _, buffer = cv2.imencode('.jpg', output)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def fire1(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(fire(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except: 
        pass



def livestream_processed(request):

    def generate_frames():
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        cap = cv2.VideoCapture(0)

        while True:
            success, frame = cap.read()
            if not success:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        cap.release()

    return StreamingHttpResponse(generate_frames(), content_type="multipart/x-mixed-replace;boundary=frame")
