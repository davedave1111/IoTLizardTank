import time
import Settings
from TempHumiditySensor import TempHumiditySensor

# This is a service class that will be used to handle 
# initializing and reading data from the sensors, handling 
# the current state of the timing of readings. It is written
# as a singleton, because there should only be one instance 
# of this class existing, otherwise we could see issues with 
# the sensors.

class SensorService:

    def __new__(cls):
        # Creates singleton SensorService instance. If it already exists,
        # This will return the object that already exists. Beyond that, it inits sensors
        if not hasattr(cls, 'instance'):
            cls.instance = super(SensorService, cls).__new__(cls)
            
            # Create two sensors corresponding to the warm and cool sides of  the tank
            cls.warmSideSensor = TempHumiditySensor(Settings.WARM_SIDE_SENSOR)
            cls.coolSideSensor = TempHumiditySensor(Settings.COOL_SIDE_SENSOR)
            cls.currentSensorData = ("0", "0", "0", "0")
            cls.referenceTime = 0
        return cls.instance

    @classmethod
    def update(cls):
        # Update function that takes no arguments. Will be used to service 
        # this class through main. This method does some light state tracking
        # by keeping track of the time to know when to poll sensors for data 
        
        # grab the current time 
        currentTime = time.time()

        # if it has been less than 1 second since our reference time when we grabbed 
        # our last measurement, we dont need to do anything and we can return the function
        if(currentTime-cls.referenceTime < Settings.POLL_TIMING):
            return 
        

        # otherwises, this bit of code will run, meaning it has been greater than or 
        # equal to our poll timing since we last polled sensors for data 

        cls.referenceTime = time.time() # Take new reference time

        # Poll sensors
        cls.coolSideSensor.readTemp()
        cls.coolSideSensor.readHumidity()
        cls.warmSideSensor.readTemp()
        cls.warmSideSensor.readHumidity()

        # Update currentSensorData to reflect what we just polled from the sensors

        cls.currentSensorData = (cls.coolSideSensor.getTemp(), cls.coolSideSensor.getHumidity(), cls.warmSideSensor.getTemp(), cls.warmSideSensor.getHumidity())

        return # return from the function

    @classmethod
    def getSensorInfo(cls):
        # Takes no arguements. Returns sensor data in 4 string tuple, in the order:
        # (COOL_SIDE_TEMP, COOL_SIDE_HUMIDITY, WARM_SIDE_TEMP, WARM_SIDE_HUMIDITY).
        return cls.currentSensorData
        


