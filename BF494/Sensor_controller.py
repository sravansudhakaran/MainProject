import RPi.GPIO as GPIO
import time
import os

def get_values():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(True)

    GPIO.setup(12,GPIO.OUT)
    GPIO.output(12,GPIO.LOW)

    binarys = [35,29,33,31,40,38,36,32]
    bits_temp = [0,0,0,0,0,0,0,0]

    for binary in binarys:
        GPIO.setup(binary, GPIO.IN)
        print("Pin "+str(binary)+" Set")

    #Select pin Select Pin LSB
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    
    time.sleep(0.1)
    decimal_vce = 0
    decimal_vbe = 0
    decimal_temp = 0

    #GPIO.output(12,GPIO.HIGH)
    #Calculating Temp
    GPIO.output(16,GPIO.LOW)
    GPIO.output(18,GPIO.LOW)
    #Set values of input pins high or low
    GPIO.output(12,GPIO.HIGH) # Test
    for i in range(0,8):
        if(GPIO.input(binarys[i]) == True):
            bits_temp[i] = 1
        if(GPIO.input(binarys[i]) == False):
            bits_temp[i] = 0
    #Calculating decimal value of input
    for i in range(0,8):
        decimal_temp = decimal_temp + (bits_temp[i] * (2**(i)))
    raw_temp = decimal_temp
    #vce = raw_temp * 0.019607843 #######################################################
    decimal_temp = (decimal_temp /256) *500
    GPIO.output(12,GPIO.LOW) #test

    time.sleep(0.1)
    bits_vbe = [0,0,0,0,0,0,0,0]
    #Calculating Vbe
    #GPIO.output(12,GPIO.HIGH)
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(18,GPIO.LOW)
    #Set values of input pins high or low
    GPIO.output(12,GPIO.HIGH) #test
    for i in range(0,8):
        if(GPIO.input(binarys[i]) == True):
            bits_vbe[i] = 1
        if(GPIO.input(binarys[i]) == False):
            bits_vbe[i] = 0
    #Calculating decimal value of input
    for i in range(0,8):
        decimal_vbe = decimal_vbe + (bits_vbe[i] * (2**(i)))
    raw_vbe = decimal_vbe
    #temp = (raw_vbe / 256) * 500 #######################################################
    decimal_vbe = decimal_vbe * 0.019607843
    GPIO.output(12,GPIO.LOW) #test

    time.sleep(0.1)
    bits_vce = [0,0,0,0,0,0,0,0]
    #Calculating Vce
    #GPIO.output(12,GPIO.HIGH)
    GPIO.output(16,GPIO.LOW)
    GPIO.output(18,GPIO.HIGH)
    #Set values of input pins high or low
    GPIO.output(12,GPIO.HIGH) #test
    # time.sleep(0.000001)
    for i in range(0,8):
        if(GPIO.input(binarys[i]) == True):
            bits_vce[i] = 1
        if(GPIO.input(binarys[i]) == False):
            bits_vce[i] = 0
    #Calculating decimal value of input
    for i in range(0,8):
        decimal_vce = decimal_vce + (bits_vce[i] * (2**(i)))
    raw_vce = decimal_vce
    #vbe = raw_vce * 0.019607843 ##################################################
    decimal_vce = decimal_vce * 0.019607843 * 2.4 	# Scaling back to cancel out the potential divider effect on Vce
    GPIO.output(12,GPIO.LOW) #test

    GPIO.cleanup()

    print(bits_vce,bits_vbe,bits_temp)
    print(raw_vce,raw_vbe,raw_temp)
    #print(raw_vbe)
    #print(raw_vce)

    #print(vce,vbe,temp)
    return (decimal_vce,decimal_vbe,decimal_temp)

print(get_values())
