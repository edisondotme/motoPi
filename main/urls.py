from django.conf.urls import url, include
from . import views

urlpatterns = [
	# views.index indicates the function index in the file views.py
	url(r'^', views.index, name='index'),
]
