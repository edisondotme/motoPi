from django.shortcuts import render
from django.http import HttpResponse
import time


def index(request):
	# I guess the index here should ask what graph you want
	# to display.
	return render(request, 'display/display_home.html')


def disp_time(request):
	currTime = time.strftime("%H:%M:%S", time.gmtime())

	data = {'time': currTime}
	return render(request, 'display/time.html', data)
