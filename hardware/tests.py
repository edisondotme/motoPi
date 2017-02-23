from django.test import TestCase

from hardware.photoCell import PhotoCell


class LightSensorTest(TestCase):
	"""
	Tests multiple methods for light sensor.
	"""
	def setUp(self):
		example = PhotoCell(18)  # try/except if pin is not connected

	def test_sensor_reading_returns_number(self):
		sensorReadout = example(RCtime())
		self.assertTrue(type(sensorReadout) == int)

	def test_csv_logging(self):
		pass
