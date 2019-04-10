import RPi.GPIO as GPIO
import time
import os

def get_values():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    #Digital input pins from ADC0808
    binarys = (35,29,33,31,40,38,36,32)
    #Initialy set to zero value
    bits = [0,0,0,0,0,0,0,0]
    for binary in binarys:
        GPIO.setup(binary, GPIO.IN) #All Digital pins are input pins

    #Select pin Select Pin LSB
    GPIO.setup(16, GPIO.OUT)
    #Select pin Select Pin MSB
    GPIO.setup(18, GPIO.OUT)
    decimal_vce = 0
    decimal_vbe = 0
    decimal_temp = 0
	
    #Calculating Vce
    GPIO.output(16,GPIO.LOW)
    GPIO.output(18,GPIO.LOW)
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
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(18,GPIO.LOW)
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
    GPIO.output(16,GPIO.LOW)
    GPIO.output(18,GPIO.HIGH)
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

print(get_values())
