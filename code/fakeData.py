import random
import time


def getRandomSpeed(maxSpeed=30):
	speed = random.uniform(0, maxSpeed)
	return round(speed)


while True:
	print(getRandomSpeed(30))
	time.sleep(.5)
