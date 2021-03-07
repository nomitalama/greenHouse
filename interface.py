import bme280
import soilMoisture
import relayBoard

#get all the sensor data
def getSoilMoisture():
    return soilMoisture.getMoisture()
def getSoilTemp():
    return soilMoisture.getTemp()

def getAirHumidity():
    return bme280.getHumidity()
def getAirTemp():
    return bme280.getTemp()


def actOnAirHumidity(airHumidity):
    if airHumidity < 30 or airHumidity > 80:
        if airHumidity < 30:#IF DRY
            relayBoard.changeSprinklersState(1)#Turn sprinkers ON
            while(airHumidity <= 40): #keep sprinklers on unitl 
                time.sleep(0.1)
                airHumidity = getAirHumidity()
            relayBoard.changeSprinklersState(0)#Turn sprinklers OFF
        else: #IF WET
            relayBoard.changeFanOutState(1)#Turn on fanOut
            while(airHumidity >= 75): #keep fan on until airHumidity decreases to 75
                time.sleep(0.1)
                airHumidity = getAirHumidity()
            relayBoard.changeFanOutState(0)#Turn off fanOut
                
def actOnAirTemp(airTemp):
    if airTemp < 55 or airTemp > 85:
        if airTemp < 55: #IF cold
            #Blink IMCOLD led five times.
            for i in range (0,5):
                gpio.output(23, True)
                time.sleep(1)
                gpio.output(23, False)
                time.sleep(1)
        else: #IF HOT            
            relayBoard.changeFanInState(1)#Turn fanIn on
            relayBoard.changeFanOutState(1)#Turn fanOut on
            while(airTemp >= 75):#keep fan on until airTemp decreases to 75
                time.sleep(0.1)
                airTemp = getAirTemp()
            relayBoard.changeFanInState(0)#Turn fanIn off
            relayBoard.changeFanOutState(0)#Turn fanOut off
                               
def actOnSoilMoisture(soilMoisture): #GET real data
      if soilMoisture < 450 or soilMoisture > 650:
        if soilMoisture < 450:#IF DRY
            relayBoard.changeSprinklersState(1)#Turn sprinkers ON
            while(soilMoisture <= 550): #keep sprinklers on unitl 
                time.sleep(0.1)
                soilMoisture = getSoilMoisture()
            relayBoard.changeSprinklersState(0)#Turn sprinklers OFF
        else: #IF WET
            relayBoard.changeFanOutState(1)#Turn on fanOut
            while(soilMoisture >= 550): #keep fan on until airHumidity decreases <= 70
                time.sleep(0.1)
                soilMoisture = getSoilMoisture()
            relayBoard.changeFanOutState(0)#Turn off fanOut

def actOnSoilTemp(soilTemp):
    if soilTemp < 60 or soilTemp > 80:
        if soilTemp < 60: #IF COLD
            relayBoard.changeHeatpadState(1)#Turn on head pad.
            while(soilTemp <= 65): #keep heat pad on until soilTemp reaches <= 65
                time.sleep(0.1)
                soilTemp = getSoilTemp()
            relayBoard.changeHeatpadState(0)#Turn off head pad.      
        else: #IF HOT
            relayBoard.changeFanInState(1)#Turn fanIn on 
            relayBoard.changeFanOutState(1)#Turn fanOut on
            while(soilTemp >= 75): #keep fans on until soilTemp decreases to 75
                time.sleep(0.1)
                soilTemp = getSoilTemp()
            relayBoard.changeFanInState(0)#Turn fanIn off 
            relayBoard.changeFanOutState(0)#Turn fanOut off           
