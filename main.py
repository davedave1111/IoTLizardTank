import os
import stat
import time
import Settings
from LcdHelper import LcdHelper
from SensorService import SensorService
from alexaSkill import alexaSkill

# Here is the main loop of the program. Most of the logic is taken care of 
# externally, so it's pretty bare. 

# Create instances of objects to handle the sensors and LC
sensorService = SensorService()
statDisplay = LcdHelper()
alexaSkill = alexaSkill()

alexaSkill.app.run(debug=True)

#if 'ASK_VERIFY_REQUESTS' in os.environ:
    #verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
    #if verify == 'false':
        #alexaSkill.app.config['ASK_VERIFY_REQUESTS'] = False
    #alexaSkill.app.run(debug=True)

while(True):
    SensorService.update() # Update sensor
    statDisplay.printSensorInfo(*sensorService.getSensorInfo()) # Display updated information on LCD
    
    
    
    # print(coolSideSensor.getTemp() + " " + coolSideSensor.getHumidity() + " " +  warmSideSensor.getTemp() + " " + warmSideSensor.getHumidity())


    