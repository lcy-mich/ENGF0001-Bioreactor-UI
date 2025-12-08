import paho.mqtt.client as mqtt
import time
from json import dumps, loads
from random import randint

tempsetpoint = 35
stirsetpoint = 800
phsetpoint = 7.0

lastjump = 0


def on_connect(client, userdata, flags, reason_code):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("bioreactor/control")


def on_message(client, userdata, msg):
    global phsetpoint, tempsetpoint, stirsetpoint

    print(msg.topic + " " + str(msg.payload))
    payload = loads(msg.payload)
    match payload["Subsystem"]:
        case "ph":
            phsetpoint = payload["Value"]/2
        case "temp":
            tempsetpoint = payload["Value"]/2
        case "stirring":
            stirsetpoint = payload["Value"]/2
    time.sleep(randint(1,5))
    match payload["Subsystem"]:
        case "ph":
            phsetpoint = payload["Value"]
        case "temp":
            tempsetpoint = payload["Value"]
        case "stirring":
            stirsetpoint = payload["Value"]
    
def suddennoise(low, high):
    global lastjump
    if randint(1,1000) > 995 - (time.time() - lastjump):
        lastjump = time.time()
        print("JUMPED")
        return randint(low, high)
    else:
        return 0

def publish(client):
    msg = {"temp" : tempsetpoint + (randint(-25, 25)/10) + suddennoise(-5,5), "stirring": stirsetpoint + randint(-50,50) + suddennoise(-100,100), "ph" : phsetpoint+ (randint(-50,50)/100) + suddennoise(-1,1)}
    result = client.publish("bioreactor/sensor/data", dumps(msg))
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Sent: {dumps(msg)}")
    else:
        print(f"Failed")

if __name__ == "__main__":
    mqttc = mqtt.Client()
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    mqttc.connect("broker.hivemq.com", 1883, 60)
    mqttc.loop_start()
    try:
        while True:
            publish(mqttc)
            time.sleep(1)
    finally:
        print("exiting")
        mqttc.loop_stop()