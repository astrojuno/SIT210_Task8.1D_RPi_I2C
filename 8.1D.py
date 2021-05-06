# SIT210 8.1D
import smbus
import time

# Variables to customise the program
# time in seconds between readings
TIME_BETWEEN_READINGS = 3 
# Values for brightness levels. Defaults taken from https://www.ohsa.com.au/services/lighting-survey/
TOO_BRIGHT = 400
BRIGHT = 350
MEDIUM = 150
DARK = 100
TOO_DARK = 40

# Setup the I2C address
SENSOR = 0x23
CONTINUOS_HIG_RES_MODE = 0x13
bus = smbus.SMBus(1)

# gets and returns the light reading from the sensor
def getLightReading():
    reading = bus.read_i2c_block_data(SENSOR, CONTINUOS_HIG_RES_MODE)
    # the lux is in position 1
    return (reading[1])

# takes an int lux level and returns what range it is in as a string
def getBrightnessRanking(lux):
    if lux > TOO_BRIGHT:
        return "too bright"
    if lux > BRIGHT:
        return "bright"
    if lux > MEDIUM:
        return "medium"
    if lux > DARK: 
        return "dark"
    
    return "too dark"

# prints the light level repeatedly
def main():
    while True: 
        lightLevel = getLightReading()
        print("Light level is " + getBrightnessRanking(lightLevel))
        #print("Light Level: " + format(lightLevel[1], '.2f'))
        time.sleep(TIME_BETWEEN_READINGS)

# needed to redirect to main() on some ide's
if __name__ == "__main__":
    main()
