import logging
from flask import Flask
from flask_ask import Ask, request, session, question, statement

# This module handles the device-hosted backend of the alexa skill. It maps different intents and 
# utterances that we can expect to recieve to specific responses. 

# I'd like to give credit where credit is due, as I used the following tutorial to help with
# building this portion of the code. Unfortunately, there is no author listed, but I'd like to still 
# give credit as this tutorial was very useful and they have many more on their website:
#
# 
#  https://tutorials-raspberrypi.com/develop-your-own-raspberry-pi-alexa-skill-and-control-pi-remotely/


# The different utterances associated with each of the values in the ENVSTATUS slot. 
# These are the utterances that will be used to trigger specific responses from the 
# device. 
STATUSTEMP = ["temperature", "temp", "how cold", "how hot", "how warm", "how cool"]
STATUSHUMIDITY = ["percent humidity", "humidity", "humid"]
STATUSGENERAL = ["general status", "update", "status", "temperature and humidity", "temp and humidity"]

# Global variables that will be used to track the tempurature & humidity as it updates from the sensors 
coolSideTemp = '1' 
coolSideHumidity = '1'
warmSideTemp = '1'
warmSideHumidity = '1'

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

def updateKnownData(coolSide_Temp, coolSide_Humidity, warmSide_Temp, warmSide_Humidity):
    global coolSideTemp
    global coolSideHumidity
    global warmSideTemp 
    global warmSideHumidity

    coolSideTemp = coolSide_Temp
    coolSideHumidity = coolSide_Humidity
    warmSideTemp = warmSide_Temp
    warmSideHumidity = warmSide_Humidity
    return

@ask.launch
def launch():
    # this is used to launch the skill, and gives a simple explaination of what this skill does
    speech_text = 'Welcome to IoT Lizard Tank. Ask me for the Temperature/Humidity inside of the tank'
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)


@ask.intent('EnvStatusIntent', mapping = {'envstatus':'envstatus'})
def EnvStatus_Intent(self,envstatus,room):
    # This method is called whenever we recieve an utterance that falls into our EnvStatusIntent.
    # There are three ways that a user can interact with this skill:
    # First, they may request only the temperature, which gives temperature on both sides of the tank.
    if envstatus in STATUSTEMP:
        return statement('Basking Side is ' + warmSideTemp + ' Degrees Fahrenheit. Cool side is ' + coolSideTemp + ' Degrees Fahrenheit')
            #'Basking Side is ' + self.warmSideTemp + ' Degrees Fahrenheit, Cool Side is ' + self.coolSideTemp + ' Degrees Fahrenheit')

    # Next, they may request only the humidity inside the tank
    elif envstatus in STATUSHUMIDITY:
        return statement('Basking Side is ' + warmSideHumidity + ' percent humidity. Cool side is ' + coolSideHumidity + ' percent humidity')

    # Finally, they may request a general update, which provides both the temperature and humidity on each side of the tank
    elif envstatus in STATUSGENERAL:
        return statement('Basking Side is ' + warmSideTemp + ' Degrees Fahrenheit and ' + warmSideHumidity + ' percent humidity. Cool side is ' 
        + coolSideTemp + ' degrees fahrenheit and ' + coolSideHumidity + ' percent humidity')
        # print("hello")

    # If the utterance doesn't match any of those requests, we simply let the user know that we don't know the answer to the question they asked
    else: 
        return statement('Sorry, I do not know the answer to that')


@ask.intent('AMAZON.HelpIntent')
def help():
    # basic amazon help intent that allows a user to ask for help in using the skill.
    speech_text = 'You can ask me for the temperature of the tank, the percent humidity inside of the tank, or just a general update which gives both temperature and humidity'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)
 
 
@ask.session_ended
def session_ended():
    return "{}", 200

    