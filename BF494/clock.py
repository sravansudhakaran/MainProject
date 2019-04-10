import RPi.GPIO as GPIO
import time
def clock_ale_soc():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(4,GPIO.ALT0)
	GPIO.setup(12,GPIO.OUT)
	GPIO.setclock(4,500000)
	GPIO.output(4,1)
	while 1:
		GPIO.output(12,GPIO.HIGH)
		time.sleep(0.3)
		GPIO.output(12,GPIO.LOW)
		time.sleep(1)
	return

clock_ale_soc()
