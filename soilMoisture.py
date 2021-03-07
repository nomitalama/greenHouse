from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw

i2c_bus = busio.I2C(SCL,SDA)
ss = Seesaw(i2c_bus, addr=0x36)

#read data
def getMoisture():
    touch = ss.moisture_read()
    return touch
   
def getTemp():
    temp = ss.get_temp()
    soilTemp_F = temp*9.0 / 5.0 + 32
    return soilTemp_F