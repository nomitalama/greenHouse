import math
import board
import busio
import adafruit_bme280
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

bme280.sea_level_pressure = 1013.4 #manually set

def getTemp():
    measuredTemperature = bme280.temperature
    measuredTemperature_F = measuredTemperature*9.0 / 5.0 + 32
    return measuredTemperature_F
    #print("\nTemperature: %0.1f C" % measuredTemperature)

def getHumidity():
    measuredHumidity = bme280.humidity
    return measuredHumidity
    #print("\nHumidity: %0.1f %%" % measuredHumidity)

def getPressure():
    measuredPressure = bme280.pressure
    return measuredPressure
    #print("Pressure: %0.1f hPa" % measuredPressure)

def getAltitude():
    altitude = bme280.altitude
    return altitude
    #print("Altitude = %0.2f meters" % altitude)

def getDewPoint(measuredTemperature, measuredHumidity):
    #variables for Magnus formula to calculate dew point
    b = 17.62
    c = 243.12
    gamma = ((b * measuredTemperature)/(c+measuredTemperature))+math.log(measuredHumidity/100.0) #TODO: mreasuredTemperature is a NoneType??
    dewPoint = (c * gamma)/(b-gamma)
    return dewPoint
    #print("\nDew Point: %0.2f" % dewPoint)

