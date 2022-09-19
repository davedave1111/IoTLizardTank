import stat
import time
import Settings

from LcdHelper import LcdHelper
from TempHumiditySensor import TempHumiditySensor
# Here is the main loop of the program. Most of the logic is taken care of 
# externally, so it's pretty bare. 

# Create instances of objects to handle the sensors and LC
sensorService = SensorService()
statDisplay = LcdHelper()

while(True):
    SensorService.update() # Update sensor
    statDisplay.printSensorInfo(SensorService.getSensorInfo()) # Display updated information on LCD
    
    
    # print(coolSideSensor.getTemp() + " " + coolSideSensor.getHumidity() + " " +  warmSideSensor.getTemp() + " " + warmSideSensor.getHumidity())


    