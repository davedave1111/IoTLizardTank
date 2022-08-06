import time
import Settings

from TempHumiditySensor import TempHumiditySensor

warmSideSensor = TempHumiditySensor(Settings.WARM_SIDE_SENSOR)

while(True):
    warmSideSensor.readTemp()
    warmSideSensor.readHumidity()

    print(warmSideSensor.currentTemp)
    print(warmSideSensor.currentHumidity)
    print("Done")
    print("")
    #print("Temp: {:.1f} *C \t Humidity: {}%".format(warmSideSensor.currentTemp, warmSideSensor.currentHumidity))
    #print(warmSideSensor.currentTemp + "    " + warmSideSensor.currentHumidity)
    time.sleep(1)
    