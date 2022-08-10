from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD

lcd = LCD()

def safe_exit(signum, frame):
    exit(1)

signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

try:
    lcd.text("Cool Side||Warm Side", 1)
    lcd.text("---------||---------", 2)
    lcd.text("  77.6 F ||  98.2 F ", 3)
    lcd.text(" 40% HUM || 32% HUM ", 4)
    pause()

except KeyboardInterrupt:
    pass

finally:
    lcd.clear()

