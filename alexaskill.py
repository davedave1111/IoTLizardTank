import logging
import os
 
from flask import Flask
from flask_ask import Ask, request, session, question, statement
import RPi.GPIO as GPIO
 
app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

STATUSTEMP = ["temperature", "temp", "how cold", "how hot", "how warm", "how cool"]
STATUSHUMIDITY = ["percent humidity", "humidity", "humid"]
STATUSGENERAL = ["general status", "update", "status", "temperature and humidity", "temp and humidity"]
 
@ask.launch
def launch():
    speech_text = 'Welcome to IoT Lizard Tank. Ask me for the Temperature/Humidity inside of the tank'
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)

@ask.intent('EnvStatusIntent', mapping = {'envstatus':'envstatus'})
def EnvStatus_Intent(envstatus,room):
    if envstatus in STATUSTEMP:
        return statement('Basking Side is 99 Degrees Fahrenheit, Cool Side is 73 Degrees Fahrenheit')
    elif envstatus in STATUSHUMIDITY:
        return statement('Basking Side is 32 percent humidity. Cool side is 36 percent humidity')
    elif envstatus in STATUSGENERAL:
        return statement('Basking Side is 99 Degrees Fahrenheit and 32 percent humidity. Cool side is 73 degrees fahrenheit and 36 percent humidity')
    else: 
        return statement('Sorry, I do not know the answer to that')


@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can ask me for the temperature of the tank, the percent humidity inside of the tank, or just a general update which gives both temperature and humidity'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)
 
 
@ask.session_ended
def session_ended():
    return "{}", 200
 
 
if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)