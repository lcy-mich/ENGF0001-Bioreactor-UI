from settings import Stat, MQTT_HOST, MQTT_KEEPALIVE, MQTT_PORT, MQTT_TOPIC

import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion

from json import loads

from PySide6.QtCore import QThread, Signal
from threading import Lock

class DataParser:
    sim_statToName = {
            Stat.Acidity : "pH",
            Stat.Temperature : "temperature_C",
            Stat.Stirring : "rpm"
        }
    
    def __init__(self, is_simulated, data):
        self.raw_data = data
        self.is_simulated = is_simulated
    
    def get_setpoints(self):
        raw_setpoints = self.raw_data["setpoints"]
        ph = raw_setpoints["pH"]
        rpm = raw_setpoints["rpm"]
        temp = raw_setpoints["temperature_C"]

        return {Stat.Acidity : ph, Stat.Temperature : temp, Stat.Stirring : rpm}
    
    def get_stat_mean(self, stat):
        if not self.is_simulated: return

        stat_name = self.sim_statToName[stat]
        return self.raw_data[stat_name]["mean"]
    
    def get_start_time(self):
        return self.raw_data["window"]["start"]
    
    def get_end_time(self):
        return self.raw_data["window"]["end"]

class MQTTDataFeed:
    signal = Signal(object)

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
        self.signal.emit(loads(msg.payload))
    
    def __del__(self):
        self.client.disconnect()