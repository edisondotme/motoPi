from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r"^time", views.disp_time, name='time'),
	url(r"^csv", views.disp_csv, name='csv'),
]
