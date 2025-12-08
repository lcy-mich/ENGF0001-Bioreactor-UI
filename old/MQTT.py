import paho.mqtt.client as mqtt
import logging
from paho.mqtt.enums import CallbackAPIVersion
import time
from json import dumps


def on_connect(client, userdata, flags, reason_code):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("bioreactor_group_3/telemetry/summary")


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

def publish(client):
    msg = {"Subsystem" : "stirring", "Value" : 891}
    result = client.publish("bioreactor/sensor/data", dumps(msg))
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Sent")
    else:
        print(f"Failed")

if __name__ == "__main__":
    mqttc = mqtt.Client(CallbackAPIVersion.VERSION2, "the ")
    print("log")
    mqttc.enable_logger()
    print("connect")
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    print('start user')
    mqttc.username_pw_set(username="group3", password="Group3abc")
    print('strart connect')
    mqttc.connect("26063fe98ec0480d93ee20fbab5cf154.s1.eu.hivemq.cloud", 8883, 60)
    print("finished all")
    mqttc.loop_forever()
    # publish(mqttc)