from LcdHelper import LcdHelper
from SensorService import SensorService
import alexaSkill
import threading

# Here is the main loop of the program. Most of the logic is taken care of 
# externally, so it's pretty bare. 

# Create instances of objects to handle the sensors and LCD
sensorService = SensorService()
statDisplay = LcdHelper()

# Spin off flask app on a new thread targeting a lambda for the run function
threading.Thread(target = lambda: alexaSkill.app.run(debug=False)).start()

# main loop for updating information in system
while(True):
    SensorService.update() # Update sensor
    sensorData = sensorService.getSensorInfo() # grab updated sensor data (which comes in as a 4 element tuple) and save it to sensorData
    statDisplay.printSensorInfo(*sensorData) # Display updated information on LCD
    alexaSkill.updateKnownData(*sensorData) # update the sensor values for our Flask app to use
    


    