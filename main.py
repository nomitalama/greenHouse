import interface

WAIT_AFTER_SOIL_MOISTURE = 10
WAIT_AFTER_AIR_HUMIDITY = 1
WAIT_AFTER_SOIL_TEMP = 1
WAIT_AFTER_AIR_TEMP = 1

while True:
    interface.actOnSoilMoisture(getSoilMoisture())
    time.sleep(WAIT_AFTER_SOIL_MOISTURE)
    
    interface.actOnAirHumidity(getAirHumidity())
    time.sleep(WAIT_AFTER_AIR_HUMIDITY)
    
    interface.actOnSoilTemp(getSoilTemp())
    time.sleep(WAIT_AFTER_SOIL_TEMP)
    
    interface.actOnAirTemp(getAirTemp())
    time.sleep(WAIT_AFTER_AIR_TEMP)
