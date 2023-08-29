import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin number
light_pin = 18

# Setup the GPIO pin for output
GPIO.setup(light_pin, GPIO.OUT)

while True:
	# Turn on the light
	GPIO.output(light_pin, GPIO.HIGH)
	print("Light on")
	# Wait for some time
	time.sleep(1)

	# Turn off the light
	GPIO.output(light_pin, GPIO.LOW)
	print("Light off")
	# Wait for some time
	time.sleep(1)

# Clean up the GPIO settings
GPIO.cleanup()
