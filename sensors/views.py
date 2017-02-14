from django.shortcuts import render


def index(request):
	return render(request, 'sensors/sensors_home.html')
