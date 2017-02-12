from django.shortcuts import render
from django.http import HttpResponse

from code.timeClock import getCurrTime


def index(request):
	# I guess the index here should ask what graph you want
	# to display.
	return render(request, 'display/display_home.html')


def disp_time(request):
	return render(request, 'display/time.html', getCurrTime())
