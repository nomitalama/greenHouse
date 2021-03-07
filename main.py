import interface
import time

WAIT_AFTER_SOIL_MOISTURE = 10
WAIT_AFTER_AIR_HUMIDITY = 10
WAIT_AFTER_SOIL_TEMP = 15
WAIT_AFTER_AIR_TEMP = 15

while True: #contininously call methods in the order of importance
    interface.actOnSoilMoisture(interface.getSoilMoisture())
    time.sleep(WAIT_AFTER_SOIL_MOISTURE)
    
    interface.actOnAirHumidity(interface.getAirHumidity())
    time.sleep(WAIT_AFTER_AIR_HUMIDITY)
    
    interface.actOnSoilTemp(interface.getSoilTemp())
    time.sleep(WAIT_AFTER_SOIL_TEMP)
    
    interface.actOnAirTemp(interface.getAirTemp())
    time.sleep(WAIT_AFTER_AIR_TEMP)
