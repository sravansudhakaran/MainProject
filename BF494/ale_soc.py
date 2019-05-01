import RPi.GPIO as GPIO
import time
def clock_ale_soc():
	try:
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(12,GPIO.OUT)
		print("[+] ALE_SOC is running !")
		while 1:
			GPIO.output(12,GPIO.HIGH)
			time.sleep(0.3)
			GPIO.output(12,GPIO.LOW)
			time.sleep(1)
		return
	except KeyboardInterrupt:
		GPIO.cleanup()

clock_ale_soc()
