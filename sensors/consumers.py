from channels import Group


def ws_connect(message):
	print("Someone connected.")
	path = message['path']  # i.e /sensors/light

	if path == '/sensors/light/':
		print("Adding new user to sensor group")

		# Adds user to group for broadcast
		Group("sensor").add(message.reply_channel)
		message.reply_channel.send({  # Reply to individual directly
			"text": "You're connected to sensor group :)",
		})
	else:
		print("Strange connector!")


def ws_message(message):
	# ASGI Websocket packet-received and send-packet message types
	# both have a "text" key for their textual data.
	# Group("sensor").send({'text': "Sensor reading="})
	print("Message Received!: " + message['text'] + '\n')


def ws_disconnect(message):
	print("Someone left us...")
	Group("sensor").discard(message.reply_channel)
