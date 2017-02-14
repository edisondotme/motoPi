import time


def getCurrTime():
	"""
	Gets the current time and returns in dictionary format so that django
	can load it as a context.

	https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/#render
	"""
	currTime = time.strftime("%I:%M:%S", time.gmtime())

	data = {'time': currTime}

	return data
