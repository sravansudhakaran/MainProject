import RPi.GPIO as GPIO
import time
import os

def get_values():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(True)
    #print("1")
    
    binarys = [35,33,31,29,40,38,36,32]

    for i in range(8):
        print(GPIO.setup(binarys[i],GPIO.IN))
    return

    for i in range(8):
        print(GPIO.input(binarys[i]))
    return

get_values()
