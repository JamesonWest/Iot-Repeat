import json
import paho.mqtt.client as mqtt
import config

def on_message(c,u,m):
    try:
        print("recv", json.loads(m.payload.decode()))
    except:
        print("recv", m.payload.decode())

client = mqtt.Client()
client.on_message = on_message
client.connect(config.BROKER_HOST, config.BROKER_PORT, 60)
client.subscribe(config.MQTT_TOPIC, qos=0)
client.loop_forever()
