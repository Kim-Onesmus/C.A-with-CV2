from cgitb import html
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import auth
from.models import student
import datetime
import cv2
# import requests
# Create your views here.

from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')
    # students = student.objects.all()
    # if request.method == 'POST':
    #     admission = request.POST['admission']
    #     upload = request.POST ['upload']
        
    #     if client.objects.filter(admission=admission).exists:
    #         messages.info(request, 'Admmission number already exists')
    #         return redirect('')
    #     elif student.objects.filter(upload=upload).exists:
    #         messages.info(request, 'The upload already exists')
    #         return redirect('')
    #     else:
    #         p = student(admission=admission, upload=upload)
    #         p.save()
    #         return redirect ('thanks')
    # else:

def upload(request):
    # data=requests.get("app/templates/SMILE/smile.py")
    # print(data.text)
    # data=data.text
    # data = 
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('app/templates/SMILE/haarcascade_frontalface_default.xml')
    smile_cascade = cv2.CascadeClassifier('app/templates/SMILE/haarcascade_smile.xml')

    while True:
        _, frame = cap.read()
        original_frame = frame.copy()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray, 1.3, 5)
        for x, y, w, h in face:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            face_roi = frame[y:y+h, x:x+w]
            gray_roi = gray[y:y+h, x:x+w]
            smile = smile_cascade.detectMultiScale(gray_roi, 1.3, 25)
            for x1, y1, w1, h1 in smile:
                cv2.rectangle(face_roi, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 2)
                time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                file_name = f'selfie-{time_stamp}.png'
                cv2.imwrite(file_name, original_frame)
        cv2.imshow('KIM TECHNOLOGIES', frame)
        if cv2.waitKey(1) == ord('q'):
            break
        # print(data.text)
        # data=data.text
    return render(request, 'home.html')

def th(request):
    return redirect(request, 'th.html')
def smile(request):
    return redirect(request, 'smile.py')

