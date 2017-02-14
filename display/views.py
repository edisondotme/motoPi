from django.shortcuts import render

import csv
from django.utils.six.moves import range
from django.http import StreamingHttpResponse

from hardware.timeClock import getCurrTime


def index(request):
	return render(request, 'display/display_home.html')


def disp_time(request):
	"""
	Use of context parameter in render function.
	https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/#render
	"""
	return render(request, 'display/time.html', getCurrTime())


def disp_csv(request):
	"""A view that streams a large CSV file."""
	# Generate a sequence of rows. The range is based on the maximum number of
	# rows that can be handled by a single sheet in most spreadsheet
	# applications.
	# https://docs.djangoproject.com/en/1.10/howto/outputting-csv/#streaming-large-csv-files

	response = StreamingHttpResponse(content_type="text/csv")

	response['Content-Disposition'] = 'attachment; filename="/data/photoCell_data.csv"'
	return response
