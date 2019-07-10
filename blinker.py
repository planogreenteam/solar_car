import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leftSigPin = 4
rightSigPin = 5
hazSigPin = 6

leftOutPin = 25
rightOutPin = 24

GPIO.setup(leftSigPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(rightSigPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(hazSigPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(leftOutPin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(rightOutPin, GPIO.OUT, initial=GPIO.LOW)

leftBool = GPIO.input(leftSigPin)
rightBool = GPIO.input(rightSigPin)
hazBool = GPIO.input(hazSigPin)

leftGlitch = True
rightGlitch = True
hazGlitch = True


def updatePins():
	global leftBool
	global rightBool
	global hazBool
	global leftGlitch
	global rightGlitch
	global hazGlitch

	leftBool = GPIO.input(leftSigPin)
	rightBool = GPIO.input(rightSigPin)
	hazBool = GPIO.input(hazSigPin)
	print leftBool
	if leftBool == GPIO.LOW:
		leftGlitch = False
	if rightBool == GPIO.LOW:
		rightGlitch = False
	if hazBool == GPIO.LOW:
		hazGlitch = False
	time.sleep(.01)

try:
	while True:
		global leftGlitch
		global rightGlitch
		global hazGlitch

		leftGlitch = True
		rightGlitch = True
		hazGlitch = True

		for x in range(10):
			updatePins()

		print leftGlitch

		if (leftGlitch or rightGlitch or hazGlitch):
			if (leftGlitch or hazGlitch):
				GPIO.output(leftOutPin, 1)
			if (rightGlitch or hazGlitch):
				GPIO.output(rightOutPin, 1)

			time.sleep(.25)

			GPIO.output(leftOutPin, 0)
			GPIO.output(rightOutPin, 0)

			time.sleep(.15)

except KeyboardInterrupt:
	GPIO.cleanup()
GPIO.cleanup()
