import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion

from json import loads

class MQTTDataFeed:

    def __init__(self, host, port, keep_alive, topic, message_callback, connect_callback=None):
        self.client = mqtt.Client(CallbackAPIVersion.VERSION2)
        self.topic = topic

        self.message_callback = message_callback
        self.connect_callback = connect_callback

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.client.connect(host, port, keep_alive)
        self.client.loop_start()
    
    def on_connect(self, client, userdata, flags, reason_code, properties):
        print(f"Connection succeeded with result code : {reason_code}")
        if self.connect_callback:
            self.connect_callback()
        self.client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        self.message_callback(loads(msg.payload))
    
    def __del__(self):
        self.client.disconnect()