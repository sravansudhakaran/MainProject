import RPi.GPIO as GPIO
import time
def clock_gen():
	try:
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(7,GPIO.OUT)
		print("[+] Clock is running !")
		while 1:
			GPIO.output(7,GPIO.HIGH)
			time.sleep(0.000001)
		
			GPIO.output(7,GPIO.LOW)
			time.sleep(0.000001)
		return

	except KeyboardInterrupt:
        	print ('Interrupted')
       		GPIO.cleanup()

clock_gen()
