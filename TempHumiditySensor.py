import adafruit_dht
import board

# This class more or less is acting like a wrapper around the base 
# adafruit_dht.DHT22 class. It allows us to create instances of 
# the orginal adafruit library and poll sensors, with a little 
# bit of exception handling and unit conversions thrown in.


class TempHumiditySensor:

    # We have to init these values to something before we take a reading, 
    # otherwise this can cause problems when the LCD attempts to display 
    # null. The reading happens soon after this is instantiated, so it 
    # won't be displayed long enough for the user to see 
    currentTemp = 0.1
    currentHumidity = 0.1

    def __init__(self, pin):
        #For Creating a new instance of our class. Takes a board pin object which is used to
        #instatiate the dht11 object
        self.DHTSensor = adafruit_dht.DHT22(pin)

    def readTemp(self):
        # Takes no arguments and returns nothing. Polls sensor
        # for temperature. If the read fails for whatever reason 
        # (which tends to happen every now and then), we simply 
        # don't update the temp. 
        try:
            self.currentTemp = self.DHTSensor.temperature
        except RuntimeError as e:
            self.currentTemp = self.currentTemp
        
    def readHumidity(self):
        # Takes no arguments and returns nothing. Polls sensor
        # for humidity. If the read fails for whatever reason 
        # (which tends to happen every now and then), we simply 
        # don't update the temp.
        try:
            self.currentHumidity = self.DHTSensor.humidity
        except RuntimeError as e:
            self.currentHumidity = self.currentHumidity
    
    def getTemp(self):
        # Takes no Arguments. Returns Temp in F
        return str(round(((self.currentTemp*9)/5)+32, 1))

    def getHumidity(self):
        # takes no arguements. Returns percent of humidity
        return str(self.currentHumidity)
