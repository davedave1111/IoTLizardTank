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
    time.sleep(1)

    