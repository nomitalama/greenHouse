import RPi.GPIO as gpio
import time
from soilMoisture import getMoisture
from bme280 import getTemp

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(5,gpio.OUT) #pin29, heat pad
gpio.setup(6,gpio.OUT) #pin31, sprinkler
gpio.setup(13,gpio.OUT) #pin33, fan out
gpio.setup(19,gpio.OUT) #pin35, fan in
gpio.setup(23,gpio.OUT) #pin 16, IM COLD LED

def changeHeatpadState(state):
    if state == 1:
        gpio.output(5,False) #Turn on.
    else:
        gpoio.output(5,True)#Turn off.
    #return state

def changeSprinklersState(state):
    if state == 1:
        gpio.output(6,False)#Turn on.
    else:
        gpio.output(6,True)#Turn off.
    #return state
    
def changeFanOutState(state):
    if state == 1:
        gpio.output(13,False)#Turn on.
    else:
        gpio.output(13,True)#Turn off.
    #return state
        
def changeFanInState(state):
    if state == 1:
        gpio.output(19,False)#Turn on.
    else:
        gpio.output(19,True)#Turn off.
    #return state