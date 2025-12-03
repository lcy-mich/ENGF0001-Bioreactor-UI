from settings import Stat, MQTT_PUBLISH_TOPIC

import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion

from json import loads, dumps

from PySide6.QtCore import QThread, Signal, QObject, Slot
from threading import Lock

class DataParser:
    
    def __init__(self, is_simulated, data):
        self.raw_data = data
        self.is_simulated = is_simulated
    
    def get_setpoints(self):
        raw_setpoints = self.raw_data["setpoints"]
        ph = raw_setpoints["pH"]
        rpm = raw_setpoints["rpm"]
        temp = raw_setpoints["temperature_C"]

        return {Stat.Acidity : ph, Stat.Temperature : temp, Stat.Stirring : rpm}
    
    def get_stat(self, stat):
        if self.is_simulated:
            stat_name = {
                Stat.Acidity : "pH",
                Stat.Temperature : "temperature_C",
                Stat.Stirring : "rpm"
            }[stat]
            
            return self.raw_data[stat_name]["mean"]
        for stat_data in self.raw_data[0]:
            if stat_data["Subsystem"] == stat.value:
                return stat_data["Value"]
    
    def get_start_time(self):
        return self.raw_data["window"]["start"]
    
    def get_end_time(self):
        return self.raw_data["window"]["end"]

class MQTTDataFeed(QThread):
    signal = Signal(object)

    def __init__(self, host, port, keep_alive, topic, parent=None):
        super(self.__class__, self).__init__(parent)
        self.client = mqtt.Client(CallbackAPIVersion.VERSION2)
        self.topic = topic

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.host = host
        self.port = port
        self.keep_alive = keep_alive
        

    def run(self):
        self.client.connect(self.host, self.port, self.keep_alive)
        self.client.loop_forever()
    
    def publish_change(self, stat, value):
        msg = {"Subsystem" : stat.value, "Value" : value}
        print(dumps(msg))
        result = self.client.publish(MQTT_PUBLISH_TOPIC, dumps(msg))
        
        status = result[0]
        if status == 0:
            print(f"Sent")
        else:
            print(f"Failed")
    
    def on_connect(self, client, userdata, flags, reason_code, properties):
        print(f"Connection succeeded with result code : {reason_code}")
        self.client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        self.signal.emit(loads(msg.payload))
    
    def __del__(self):
        self.client.disconnect()