
from channels import Group
from django.core.management import BaseCommand
import time

# The class must be named Command, and subclass BaseCommand


class Command(BaseCommand):
	# Show this when the user types help
	help = "Simulates reading sensor and sending over Channel."

	# A command must define handle()
	def handle(self, *args, **options):
		x = 0
		while True:
			Group("sensor").send({'text': "Sensor reading=" + str(x)})
			time.sleep(2)
			x = x + 1
			self.stdout.write("Sensor reading..." + str(x))
