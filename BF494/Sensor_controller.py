import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def get_values():
    #Digital input pins from ADC0808
    binarys = (35,29,33,31,40,38,36,32)
    #Initialy set to zero value
    bits = [0,0,0,0,0,0,0,0]
    for binary in binarys:
        GPIO.setup(binary, GPIO.IN) #All Digital pins are input pins

    #Clock pin
    GPIO.setup(22, GPIO.OUT)
    #Select pin Select Pin LSB
    GPIO.setup(24, GPIO.OUT)
    #Select pin Select Pin MSB
    GPIO.setup(26, GPIO.OUT)
	decimal_vce = 0
	decimal_vbe = 0
	decimal_temp = 0
	
    #Calculating Vce
    GPIO.output(24,GPIO.LOW)
    GPIO.output(26,GPIO.LOW)
    #Set values of input pins high or low
    for i in range(8):
            if(GPIO.input(binarys[i]) == True):
                bits[i] = 1
            if(GPIO.input(binarys[i]) == False):
                bits[i] = 0
    #Calculating decimal value of input
     for i in range(8):
            decimal_temp = decimal_temp + (bits[i] * (2**(7-i)))
    #Calculating Vbe
    GPIO.output(24,GPIO.HIGH)
    GPIO.output(26,GPIO.LOW)
    #Set values of input pins high or low
    for i in range(8):
            if(GPIO.input(binarys[i]) == True):
                bits[i] = 1
            if(GPIO.input(binarys[i]) == False):
                bits[i] = 0
    #Calculating decimal value of input
     for i in range(8):
            decimal_vbe = decimal_vbe + (bits[i] * (2**(7-i)))
    #Calculating Temperature
    GPIO.output(24,GPIO.LOW)
    GPIO.output(26,GPIO.HIGH)
    #Set values of input pins high or low
    for i in range(8):
            if(GPIO.input(binarys[i]) == True):
                bits[i] = 1
            if(GPIO.input(binarys[i]) == False):
                bits[i] = 0
    #Calculating decimal value of input
     for i in range(8):
            decimal_vce = decimal_vce + (bits[i] * (2**(7-i)))


    return (decimal_vce,decimal_vbe,decimal_temp)        
