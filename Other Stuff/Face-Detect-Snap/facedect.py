


import numpy as np
import cv2
import boto
import boto.s3
import sys
import time
import requests
from boto.s3.key import Key

AWS_ACCESS_KEY_ID = 'AKIAJWE2AL6OCUX37AWQ'
AWS_SECRET_ACCESS_KEY = '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'
url = 'http://172.20.10.4:8000/api/getpersoninfo/'

face_cascade = cv2.CascadeClassifier('/Users/pparikh/Desktop/295/haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('/Users/pparikh/Desktop/295/haarcascade_eye.xml')
cap = cv2.VideoCapture(0)

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()


bucket_name = 'deebee07-database'
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        print('detected');
        ret,frame = cap.read()
        cv2.imwrite('test.jpg',frame)
        

        bucket = conn.get_bucket(bucket_name)
        print('bucket connection initiated');

        testfile = "test.jpg"
        print ('Uploading %s to Amazon S3 bucket %s' % \
            (testfile, bucket_name))

        k = Key(bucket)
        k.key = 'test.jpg'
        k.set_contents_from_filename(testfile,
            cb=percent_cb, num_cb=10)
        r = requests.post(url, data="abcd")
        print(r.json())

        time.sleep(10)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()