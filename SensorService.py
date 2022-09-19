import time
import Settings
import TempHumiditySensor

# This is a service class that will be used to handle 
# initializing and reading data from the sensors, handling 
# the current state of the timing of readings. It is written
# as a singleton, because there should only be one instance 
# of this class existing, otherwise we could see issues with 
# the sensors.

class SensorService:

    self.currentSensorData = ((0,0), (0,0))
    self.referenceTime = 0

    def __new__(cls):
        # Creates singleton SensorService instance. If it already exists,
        # This will return the object that already exists. Beyond that, it inits sensors
        if not hasattr(cls, 'instance'):
            cls.instance = super(SensorService, cls).__new__(cls)
            
            # Create two sensors corresponding to the warm and cool sides of  the tank
            self.warmSideSensor = TempHumiditySensor(Settings.WARM_SIDE_SENSOR)
            self.coolSideSensor = TempHumiditySensor(Settings.COOL_SIDE_SENSOR)
        return cls.instance

    def update(self):
        # Update function that takes no arguments. Will be used to service 
        # this class through main. This method does some light state tracking
        # by keeping track of the time to know when to poll sensors for data 
        
        # grab the current time 
        currentTime = time.time()

        # if it has been less than 1 second since our reference time when we grabbed 
        # our last measurement, we dont need to do anything and we can return the function
        if(self.referenceTime - currentTime < Settings.POLL_TIMING):
            return 
        

        # otherwises, this bit of code will run, meaning it has been greater than or 
        # equal to our poll timing since we last polled sensors for data 

        self.referenceTime = time.time() # Take new reference time

        # Poll sensors
        self.coolSideSensor.readTemp()
        self.coolSideSensor.readHumidity()
        self.warmSideSensor.readTemp()
        self.warmSideSensor.readHumidity()

        # Update currentSensorData to reflect what we just polled from the sensors

        self.currentSensorData = ((coolSideSensor.getTemp, coolSideSensor.getHumidity), 
        (warmSideSensor.getTemp, warmSideSensor.getHumidity))

        return # return from the function


    def getSensorInfo(self):
        # Takes no arguements. Returns nested touple, first touple is data from 
        # cool side sensor, second is warm side sensor. Both of the internal touples 
        # start with temp, end with humidity of the sensor.
        return self.currentSensorData
        


'