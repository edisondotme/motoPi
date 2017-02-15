from django.shortcuts import render


def index(request):
	return render(request, 'sensors/sensors_home.html')


def light(request):
	return render(request, 'sensors/light.html',
		{
			'sensor': '99',
		})
