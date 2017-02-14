from channels.routing import route
from .consumers import ws_message, ws_connect, ws_disconnect

channel_routing = {
	# route("websocket.receive", ws_message, path=r"^/chat/"),
	"websocket.connect": ws_connect,
	"websocket.receive": ws_message,
	"websocket.disconnect": ws_disconnect,
}
