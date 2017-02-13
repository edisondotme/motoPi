# This file is used to simulate actual hardware input from GPIO

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)


def RCtime(RCPin):
	reading = 0
	GPIO.setup(RCPin, GPIO.OUT)
	GPIO.output(RCPin, GPIO.LOW)
	time.sleep(0.1)

	GPIO.setup(RCPin, GPIO.IN)
	# this takes 1 millisecond per loop cycle
	while(GPIO.input(RCPin) == GPIO.LOW):
		# print(GPIO.input(RCPin))
		reading += 1
	return reading


while True:
	print(RCtime(18))

