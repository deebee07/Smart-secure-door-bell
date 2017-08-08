from pymongo import MongoClient
from operator import itemgetter

import logging, requests, json, thread
from flask import Flask, render_template

from flask_ask import Ask, statement, question, session

con = MongoClient('mongodb://smelly:smell@ds119370.mlab.com:19370/smell_security')
db = con.smell_security



app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

person = ""
smellmap = {}
smellmap[0] = "OFF"
smellmap[1] = "GREEN"
smellmap[2] = "AQUA"
smellmap[3] = "MAGENTA"
smellmap[4] = "WHITE"
smellmap[5] = "EMERALD"
smellmap[6] = "FREE_GREEN"
smellmap[7] = "SPRING"
smellmap[8] = "DODGER"
smellmap[9] = "BLUE2"
smellmap[10] = "BLUE"
smellmap[11] = "PURPLE"
smellmap[12] = "ELECTRIC"
smellmap[13] = "SUN"
smellmap[14] = "ICE"


@ask.launch
def new_session():
    print "Changing scent"
    text = "Whose favourite scent do you want to update? Friends, Family or Owner ?"
    return question(text)

@ask.intent("ResponseIntent")
def changeScent(Person):
    print '888888888888888888888888888888'
    print Person
    text = "Changing favourite fragrance of {}. What smell do you want to set. Frebeze has plenty of variety. You can choose from GREEN, BLUE, EMERALD, WHITE, AQUA, MAGENTA, PURPLE, SPRING, SUN, DODGER, ELECTRIC AND ICE. Personally I like Aqua".format(Person)

    global person
    if (Person == "family"):
        Person = "friend"

    person = Person

    return question(text)

@ask.intent("ColorIntent")
def setColor(Color):
    print '11111111111111111'
    print Color
    doc = db.UserFav.find_one({"person": person})
    myColor = Color
    print myColor.upper()
    title = 0
    if (person == "friend" or person == "family"):
        title = 2
    else:
        title = 1
    text = "Updating the favourite scent. 3. 2. 1. Scent is now set to {}".format(Color)
    index = smellmap.keys()[smellmap.values().index(myColor.upper())]

    db.UserFav.update({"person":doc['person']},{'$set':{"smellID": smellmap.keys()[smellmap.values().index(myColor.upper())]}},upsert = False)
    thread.start_new_thread(febreze, (title, index))
    return statement(text)

def febreze(title,index):
    #   print "888888888888888888888888888888888888888888888888888888888888888"
    print type(title)
    url = "https://na-hackathon-api.arrayent.io:443/v3/devices/50331668"
    headers = {
        'authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOiI3OGQ1MmY0MC0wMTUzLTExZTctYWU0Ni01ZmMyNDA0MmE4NTMiLCJlbnZpcm9ubWVudF9pZCI6Ijk0OGUyY2YwLWZkNTItMTFlNi1hZTQ2LTVmYzI0MDQyYTg1MyIsInVzZXJfaWQiOiI5MDAwMTA0Iiwic2NvcGVzIjoie30iLCJncmFudF90eXBlIjoiYXV0aG9yaXphdGlvbl9jb2RlIiwiaWF0IjoxNDg4Njg0NjI2LCJleHAiOjE0ODk4OTQyMjZ9.dcBtnmO2Pa9Na8hRuxvsjTWEnNVBm630cZhtf1OLYEVE1r7s24IWoL4zyQqZpwpmTz_gX8zqZUYk9Yzv6cIizA",
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "28e38285-01ad-15eb-d74f-03ed7d4336ae"
    }


    print type(title)
    payload = "[{\"DeviceAction\": \"alarm_enable=0\" },{\"DeviceAction\": \"led_mode=1\" }, {\"DeviceAction\": \"led_color=0,"+str(index)+",2,4,4\" },{\"DeviceAction\": \"home_state=1\"}]"

    response2 = requests.request("PUT", url, data=payload, headers=headers)
    print(response2.text)


@ask.session_ended
def session_ended():
    return "", 200



if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=5090)
