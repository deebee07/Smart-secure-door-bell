import logging, requests, json, thread

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)




@ask.launch
def new_session():
    response = requests.post("http://192.168.1.156:8000/api/getpersoninfo/")
    message = " {}".format(json.loads(response.text)['Detail'])


    #message = "Changing Scents"
    title = " {}".format(json.loads(response.text)['Key'])
    #title = 1
    print "7777777777777777777777777777777777777777777777777777777777777"
    print title
    return statement(message)

    #return statement(message)
    


@ask.session_ended
def session_ended():
    return "", 200



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8082)

