import RPi.GPIO as GPIO
import time
def clock_ale_soc():
	GPIO.setmode(GPIO.BOARD)
	#GPIO.setmode(GPIO.BCM)
	#GPIO.setup(4,GPIO.ALT0) changed to 7
	#GPIO.setup(18,GPIO.OUT) changed to 12
	GPIO.setup(7,GPIO.ALT0)
	GPIO.setup(12,GPIO.OUT)
	GPIO.setclock(7,5000) # 500000)
	GPIO.output(7,1)
	print("[+] Clock is running !")
	while 1:
		GPIO.output(12,GPIO.HIGH)
		time.sleep(0.3)
		GPIO.output(12,GPIO.LOW)
		time.sleep(1)
	return

clock_ale_soc()
