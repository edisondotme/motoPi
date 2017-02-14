"""
This file is used to generate fake data for testing.
Consider moving it to a more appropriate directory like /tests/
"""

import random
import time


def getRandomSpeed(maxSpeed=30):
	speed = random.uniform(0, maxSpeed)
	return round(speed)


while True:
	print(getRandomSpeed(30))
	time.sleep(.5)
