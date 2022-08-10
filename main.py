import stat
import time
import Settings

from LcdHelper import LcdHelper
from TempHumiditySensor import TempHumiditySensor


warmSideSensor = TempHumiditySensor(Settings.WARM_SIDE_SENSOR)
coolSideSensor = TempHumiditySensor(Settings.COOL_SIDE_SENSOR)
statDisplay = LcdHelper()

while(True):
    warmSideSensor.readTemp()
    warmSideSensor.readHumidity()

    coolSideSensor.readTemp()
    coolSideSensor.readHumidity()
    statDisplay.printSensorInfo(coolSideSensor.getTemp(), coolSideSensor.getHumidity(), warmSideSensor.getTemp(), warmSideSensor.getHumidity())

    print(coolSideSensor.getTemp() + " " + coolSideSensor.getHumidity() + " " +  warmSideSensor.getTemp() + " " + warmSideSensor.getHumidity())
    #print("Temp: {:.1f} *C \t Humidity: {}%".format(warmSideSensor.currentTemp, warmSideSensor.currentHumidity))
    #print(warmSideSensor.currentTemp + "    " + warmSideSensor.currentHumidity)
    time.sleep(1)
    