import RPi.GPIO as GPIO
import time
import os

def get_values():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(True)
    #print("1")0
    
    binarys = [35,29,33,31,40,38,36,32]
    #Initialy set to zero value
    bits = [0,0,0,0,0,0,0,0]
    for binary in binarys:
        GPIO.setup(binary, GPIO.IN)
        print("Pin Set")
    print("2")
    
    #Select pins
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    value = 0
    #print("3")
    
    #Channel Select
    GPIO.output(16,GPIO.LOW)
    GPIO.output(18,GPIO.LOW)

    #Set values of input pins high or low
    for i in range(0,8):
        if(GPIO.input(binarys[i]) == True):
            bits[i] = 1
        if(GPIO.input(binarys[i]) == False):
            bits[i] = 0
    #print("4")

    #Calculating decimal value of input
    for i in range(0,8):
        value = value + (bits[i] * (2**(i)))
    #print("5")
    
    print(value)
    print(bits)

    value = (value /1024)*500
    GPIO.cleanup()
    return (value)

print(get_values())
