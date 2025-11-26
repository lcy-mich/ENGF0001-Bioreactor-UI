import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, reason_code):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("bioreactor/sensor/data")


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


if __name__ == "__main__":
    mqttc = mqtt.Client()
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    mqttc.connect("broker.hivemq.com", 1883, 60)
    mqttc.loop_forever()