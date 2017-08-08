from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view




import argparse
import base64
import time
import os
import json
import numpy as np
from pprint import pprint
import math
import operator


from threading import Thread
import time
import smtplib
import email
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import boto
import boto3
import paho.mqtt.client as mqtt
import datetime
from datetime import datetime

import boto
import boto3

import pymongo
from pymongo import MongoClient
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
import paho.mqtt.client as mqtt #import the client1
import time

AWS_ACCESS_KEY_ID = 'AKIAJWE2AL6OCUX37AWQ'
AWS_SECRET_ACCESS_KEY = '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'
broker_address="iot.eclipse.org"
client = mqtt.Client()
client.connect(broker_address)
from boto3.session import Session




def myRel(request):
    return render_to_response("secureApp/relatives.html", {})

@csrf_exempt
def signIn(request):
    username=request.POST['username']
    password=request.POST['password']
    print "Hi I am printing whatever you typed"
    print username

    con = MongoClient("mongodb://deebee07:Deebee07..@ds145312.mlab.com:45312/userauth")
    db = con.userauth
    collection=db['users']
    cursor = collection.find({})
    for document in cursor:
        if username==document['username'] and password==document['password']:
            print document['stream_url']
            stream_url=document['stream_url']
            return render_to_response("secureApp/home.html", {'stream_url':stream_url,})
        else:
            return redirect(reverse('authfail'))


    


def login(request):
    return render_to_response("secureApp/login.html", {})


def home(request):
    return render_to_response("secureApp/home.html", {})



def index(request):
    return render_to_response("secureApp/index.html", {})

def history(request):
    return render_to_response("secureApp/history.html", {})


def settings(request):
    return render_to_response("secureApp/settings.html", {})


def compare_faces(bucket, key, bucket_target, key_target, threshold=80, region="us-west-2",profile="default"):
    rekognition = boto3.client("rekognition", region)
    response = rekognition.compare_faces(
        SourceImage={
            "S3Object": {
                "Bucket": bucket,
                "Name": key
            
            }
        },
        TargetImage={
            "S3Object": {
                "Bucket": bucket_target,
                "Name": key_target
            }
        },
        SimilarityThreshold=threshold,
    )
    return response['FaceMatches']


def search_faces_by_image(bucket, key, collection_id, threshold=75, region="us-west-2",profile="default"):
    rekognition = boto3.client("rekognition", region)
    response = rekognition.search_faces_by_image(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": key,
            }
        },
        CollectionId=collection_id,
        FaceMatchThreshold=threshold,
    )
    return response['FaceMatches']




@api_view([ 'POST'])
def postImage(request):



    s3 = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    broker_address="iot.eclipse.org"
    print("creating new instance")
    client = mqtt.Client()
    client.connect(broker_address) #connect to broker
    client1 = mqtt.Client() #create new instance
    print("connecting to broker")
    client1.connect(broker_address) #connect to broker



    bucket = s3.get_bucket('deebee07-database')
    dst = s3.get_bucket('deebee07-history')
    t = datetime.now()
    formatted_time = t.strftime('%d-%m-%y-%H-%M-%S')
    file_name=formatted_time+".jpg"

    dst.copy_key(file_name, 'deebee07-database', 'test.jpg')
    try:
        check_similar=False
        meta_info_face=""
        for record in search_faces_by_image("deebee07-database", "test.jpg", "HomeFinal-Collection"):
            check_similar=True
            face = record['Face']
            meta_info_face+=str(face['ExternalImageId'])
            print record

#Face inside the Collection
        if check_similar:
            print "Similar Face found..."
            print os.path.splitext(meta_info_face.split('_')[1])[0]

            if str(os.path.splitext(meta_info_face.split('_')[1])[0]) == "owner":
                out_str="Hi {} my lord, I know you are tired, I have turned on . .".format(meta_info_face.split('_')[0])
                client.loop_start()
                print("Publishing message to topic","house/bulbs/bulb1")
                client.publish("vhouse/bulbs/bulb1","ON")
                client.loop_stop()
                
                client1.loop_start() #start the loop
                print("Publishing message to topic","rjp295b")
                client1.publish("rjp295b",out_str)
                client1.loop_stop() #start the loop
                return Response({'Detail': out_str,"Key":"1"})
                # Handle Criminal and Family here
            else:
                if str(os.path.splitext(meta_info_face.split('_')[1])[0]) == "criminal":
                    client.loop_start()
                    print("Publishing message to topic","house/bulbs/bulb1")
                    client.publish("vhouse/bulbs/bulb1","CRIMINAL")
                    client.loop_stop()
                    out_str="Criminal {} is at your door, inform police department. Red Alert Red Alert Red Alert".format(meta_info_face.split('_')[0])
                    client1.loop_start() #start the loop
                    print("Publishing message to topic","rjp295b")
                    client1.publish("rjp295b",out_str)
                    client1.loop_stop() #start the loop
                    return Response({'Detail': out_str,"Key":"3"})
                else:
                    out_str="{}, your {} is at the door. I have opened the door for him and have turned on the lights in his room".format(meta_info_face.split('_')[0],os.path.splitext(meta_info_face.split('_')[1])[0])
                    client.loop_start()
                    print("Publishing message to topic","house/bulbs/bulb1")
                    client.publish("vhouse/bulbs/bulb1","OFF")
                    client.loop_stop()
                    client1.loop_start() #start the loop
                    print("Publishing message to topic","rjp295b")
                    client1.publish("rjp295b",out_str)
                    client1.loop_stop() #start the loop
                    return Response({"Detail": out_str,"Key":"2"})

        else:
            out_str= "It is a stranger at the door; The door is still closed. "
            client1.loop_start() #start the loop
            print("Publishing message to topic","rjp295b")
            client1.publish("rjp295b",out_str)
            client1.loop_stop() #start the loop
            return Response({'Detail': "You have a stranger at the door.","Key":"0"})



        # matches = compare_faces("owner-database-bucket", "image.jpg","imagestotest", "test.jpg" )
        # print len(matches)
        # return Response({'Detail': "I found a face on the door !"})


    except:
        out_str="I checked no one is at the door !"
        return Response({'Detail': "I checked no one is at the door !","Key":"0"})


@api_view([ 'POST'])
def postOwner(request):
    reqObj = json.loads(request.body)
    print reqObj
    owner=reqObj['Owner']
    print owner
    print  "HIIIIIIIIII"
    con = MongoClient("mongodb://deebee07:Deebee07..@ds145312.mlab.com:45312/userauth")
    db = con.userauth
    post = db.users.find_one({'username': "deebee07"})
    if owner ==1:
        post['owner_p'] = 1
        db.users.save(post)
    else:
        post['owner_p'] = 0
        db.users.save(post)
    return Response({})



client.loop_stop() #start the loop

@api_view([ 'POST'])
def switchInfo(request):
    reqObj = json.loads(request.body)
    print reqObj
    owner=reqObj['Owner']
    if owner ==1:
        client.loop_start()
        client.publish("vhouse/bulbs/bulb1","ON")
        client.loop_stop() #start the loop
    elif owner==0:
        client.loop_start() #start the loop
        client.publish("vhouse/bulbs/bulb1","OFF")
        client.loop_stop() #start the loop
    else:
        client.loop_start() #start the loop
        client.publish("vhouse/bulbs/bulb1","CRIMINAL")
        client.loop_stop() #start the loop
    return Response({})


@api_view([ 'POST'])
def addDatabase(request):
    reqObj = json.loads(request.body)
    print reqObj
    owner=reqObj['Owner']
    from boto3.session import Session
    session = Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
   
    final_rel=owner+"_acq.jpg"
    print final_rel
    _s3 = session.resource("s3")
    _s3.Object('deebee07-database',final_rel).copy_from(CopySource='deebee07-database/test.jpg')
    _s3.Object('deebee07-database','test.jpg').delete()
    return Response({})


def json_list(list):
    lst = []
    for pn in list:
        d = {}
        d['link']=pn
        lst.append(d)
    return json.dumps(lst)


from django.http import JsonResponse

@api_view([ 'POST'])
def getHistory(request):
    from boto3.session import Session
    session = Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    s3 = session.resource("s3")
    my_bucket = s3.Bucket('deebee07-history')
    unsorted = []
    for file in my_bucket.objects.filter():
        unsorted.append(file)
    orderedList = sorted(unsorted, key=lambda k: k.last_modified)
    keysYouWant = orderedList[0:100]
    new_keys=keysYouWant[::-1]
    finalList=[]
    count=0
    print new_keys[0].key
    for x in range(0, 4):
        tempStr="https://s3-us-west-2.amazonaws.com/deebee07-history/"+new_keys[x].key
        finalList.append(tempStr)
    print 
    print json_list(finalList)
    return JsonResponse(finalList, safe=False)




