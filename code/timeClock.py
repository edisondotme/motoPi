import time


def getCurrTime():
	currTime = time.strftime("%I:%M:%S", time.gmtime())

	data = {'time': currTime}

	return data
