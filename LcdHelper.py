from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
# This class just gives wraps the existing LCD class and provides a 
# method to display our formated sensor data 
class LcdHelper:
    lcd = LCD() # creates LCD 

    def safe_exit(signum, frame):
        exit(1)

    def printSensorInfo(self, coolSideTemp, coolSideHumidity, warmSideTemp, warmSideHumidity):
        # takes the nested tuple format we use to store and pass around sensor data. Returns nothing. Prints
        # data to LCD screen
        tempColumnString = "  " + coolSideTemp + " F ||  " + warmSideTemp + " F "
        humidityColumnString = "  " + coolSideHumidity + "%  ||  " + warmSideHumidity + "% "
        self.lcd.text("Cool Side||Warm Side", 1)
        self.lcd.text("---------||---------", 2)
        self.lcd.text(tempColumnString, 3)
        self.lcd.text(humidityColumnString, 4)


    #signal(SIGTERM, safe_exit)
    #signal(SIGHUP, safe_exit)


