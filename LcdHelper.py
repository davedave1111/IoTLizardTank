from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD

class LcdHelper:
    lcd = LCD()

    def safe_exit(signum, frame):
        exit(1)

    def printSensorInfo(self, coolSideTemp, coolSideHumidity, warmSideTemp, warmSideHumidity):
        tempColumnString = "  " + coolSideTemp + " F ||  " + warmSideTemp + " F "
        humidityColumnString = " " + coolSideHumidity + "% HUM || " + warmSideHumidity + "% HUM "
        self.lcd.text("Cool Side||Warm Side", 1)
        self.lcd.text("---------||---------", 2)
        self.lcd.text(tempColumnString, 3)
        self.lcd.text(humidityColumnString, 4)


    #signal(SIGTERM, safe_exit)
    #signal(SIGHUP, safe_exit)


