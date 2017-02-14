"""
This file is used to simulate actual hardware input from GPIO

Stolen from:
https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi/basic-photocell-reading
"""

import RPi.GPIO as GPIO
import time
import os
import csv

from django.conf import settings  # Needed for relative filepath saving of csv

DATA_DIR = os.path.join(settings.BASE_DIR, "data")


class PhotoCell:
	"""
	methods and stuff for the photocell.
	I actually don't know why I made this a class,
	I figured I should learn how to use classes.
	And it seemed cleaner than having a bunch of functions,
	this way I can group them all together.
	I'd only even instantiate one of these classes

	RCtime(self, RCPin)
	# This methods takes one reading of the photocell and then returns it.
	# RCPin is the input pin for data

	run(self, RCPin)
	# This reads the photocell continuously and stores the results to a csv.
	"""

	def __init__(self, RCPin, quiet=True):
		# These instance variables only apply to the instance of the class.
		self.RCPin = RCPin
		self.quiet = quiet
		GPIO.setmode(GPIO.BCM)  # Use the common GPIO board layout.

	def RCtime(self, RCPin=None):
		"""
		This methods takes one reading of the photocell and then returns it.
		"""
		RCPin = RCPin or self.RCPin
		# ^^^ Is there a cleaner way to have a default method parameter?
		reading = 0
		GPIO.setup(RCPin, GPIO.OUT)
		GPIO.output(RCPin, GPIO.LOW)
		time.sleep(0.1)

		GPIO.setup(RCPin, GPIO.IN)
		# This takes 1 millisecond per loop cycle.
		while(GPIO.input(RCPin) == GPIO.LOW):
			reading += 1
		return reading

	def run(self, RCPin=None):
		"""
		Reads the photocell continuously and stores the results to a csv
		"""
		# "rb" means read and append
		RCPin = RCPin or self.RCPin
		# ^^^ Is there a cleaner way to have a default method parameter?

		print('Running...')
		with open(os.path.join(DATA_DIR, "photoCell_data.csv"), "a") as photoCell_data:
			while True:
				writer = csv.writer(photoCell_data, delimiter=',')
				lightLevelReading = self.RCtime(RCPin)
				# print(lightLevelReading) if self.quiet else print(lightLevelReading, end="\r")
				writer.writerow([time.time(), lightLevelReading])
