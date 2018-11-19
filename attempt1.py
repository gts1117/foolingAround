#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

buttonPin = 11
relayPin = 12
dualLED = (15, 16)

dualRed = GPIO.PWM(dualLED[0], 2000)	# Set LED freq to 2kHz
dualGreen = GPIO.PWM(dualLED[1], 2000)

# dualRed.start(0)	# Initial duty cycle = 0
# dualGreen.start(0)

def setup():
	GPIO.setmode(GPIO.BOARD)														# Numbers GPIOs by physical location on TBoard
	GPIO.setup(relayPin, GPIO.OUT)													# Sets relayPin mode as output
	GPIO.output(relayPin, GPIO.HIGH)												# Sets relay to off ( C + NC )
	GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)						# Set buttonPin mode as input, and pull up to HIGH level (3.3v)
	GPIO.add_event_detect(buttonPin, GPIO.BOTH, callback=detect, bouncetime=200)	# Detects buttonPin going to HIGH or LOW, software debounce
	GPIO.setup(dualLED, GPIO.OUT)													# Sets dualLED pins to outputs
	GPIO.output(dualLED, GPIO.LOW)													# Sets dualLED pins to LOW level (0v) to turn LED off

def charge():
	GPIO.output(dualLED[0], GPIO.HIGH)
	time.sleep(2.0)
	GPIO.output(dualLED[0], GPIO.LOW)
	time.sleep(2.0)
	GPIO.output(dualLED[0], GPIO.HIGH)
	time.sleep(1.5)
	GPIO.output(dualLED[0], GPIO.LOW)
	time.sleep(1.5)
	GPIO.output(dualLED[0], GPIO.HIGH)
	time.sleep(1.0)
	GPIO.output(dualLED[0], GPIO.LOW)
	time.sleep(1.0)
	GPIO.output(dualLED[0], GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(dualLED[0], GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(dualLED[0], GPIO.HIGH)
	time.sleep(0.25)
	GPIO.output(dualLED[0], GPIO.LOW)
	time.sleep(0.25)
	GPIO.output(dualLED[0], GPIO.HIGH)
	time.sleep(0.125)
	GPIO.output(dualLED[0], GPIO.LOW)
	time.sleep(0.125)
	GPIO.output(dualLED[0], GPIO.HIGH)
	time.sleep(0.125)
	GPIO.output(dualLED[0], GPIO.LOW)
	time.sleep(0.125)
	GPIO.output(dualLED[1], GPIO.HIGH)

def idle():
	print 'Idling...'
	GPIO.output(dualLED[0], GPIO.HIGH)


def doIt(x):
	if x == 0:
		print 'Charging...'
		charge()
		time.sleep(0.5)
		GPIO.output(relayPin, GPIO.LOW)		# Relay on ( C + NO )
	if x == 1:
		GPIO.output(relayPin, GPIO.HIGH)	# Relay off ( C + NC )
		GPIO.output(dualLED[1], GPIO.LOW)	# Turn off dualGreen
		idle()

def detect(chn):
	doIt(GPIO.input(buttonPin))


def loop():
	while True:
		pass

def destroy():
	GPIO.output(relayPin, GPIO.HIGH)	# Relay off ( C + NC )
	dualRed.stop()
	dualGreen.stop()
	GPIO.output(dualLED, GPIO.LOW)
	GPIO.cleanup()						# Release resources

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()