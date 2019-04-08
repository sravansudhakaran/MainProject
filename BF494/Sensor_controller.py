import RPi.GPIO as IO

def get_values():
	#initial_setup	
	IO.setwarnings(True)
	IO.setmode (IO.BCM)
	vce = 12.0
	vbe = 1.0
	ambient_temp = 30.0
	
	#8 Digital pins with incoming ADC output
	IO.setup(4,IO.IN)
	IO.setup(17,IO.IN)
	IO.setup(27,IO.IN)
	IO.setup(22,IO.IN)
	IO.setup(5,IO.IN)
	IO.setup(6,IO.IN)
	IO.setup(13,IO.IN)
	IO.setup(19,IO.IN)
	
	#get vce and vbe and temp from ADC0808
	
	return (vce,vbe,ambient_temp)
