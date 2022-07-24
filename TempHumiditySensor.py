import adafruit_dht
import board

class TempHumiditySensor:
    currentTemp = 0
    currentHumidity = 0

    def __init__(self, pin):
        #For Creating a new instance of our class. Takes a board pin object which is used to
        #instatiate the dht11 object
        self.DHTSensor = adafruit_dht.DHT11(pin)

    def readTemp(self):
        try:
            currentTemp = self.DHTSensor.temperature
        except RuntimeError as e:
            currentTemp = currentTemp
        
    def readHumidity(self):
        try:
            currentHumidity = self.DHTSensor.humidity
        except RuntimeError as e:
            currentHumidity = currentHumidity
