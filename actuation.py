import time, datetime, json
import paho.mqtt.client as mqtt
from counterfit_shims_grove.counterfit_connection import CounterFitConnection
from counterfit_shims_seeed_python_dht import DHT
from counterfit_shims_grove.grove_motion_sensor import GroveMotionSensor
from counterfit_shims_grove.grove_relay import GroveRelay
import config

# --- CounterFit connection ---
CounterFitConnection.init('127.0.0.1', 5000)

# --- Pin config ---
DHT_TYPE = "11"
DHT_HUMIDITY_PIN = 0
MOTION_PIN = 5
RELAY_PIN = 2

# --- Sensors & Actuator ---
dht = DHT(DHT_TYPE, DHT_HUMIDITY_PIN)
motion = GroveMotionSensor(MOTION_PIN)
relay = GroveRelay(RELAY_PIN)

client=mqtt.Client()
client.tls_set()
client.connect(config.BROKER_HOST,config.BROKER_PORT,60)
client.loop_start()

try:
    while True:
        humidity, temperature = dht.read()
        m=motion.read()
        ts=datetime.datetime.utcnow().isoformat()
        if temperature>config.TEMP_THRESHOLD and m==1:
            relay.on()
            state="on"
        else:
            relay.off()
            state="off"
        msg={"timestamp":ts,"fan":state,"temperature":temperature,"humidity":humidity,"motion":m}
        client.publish(config.MQTT_ACTUATION_TOPIC,json.dumps(msg),qos=1)
        print(state,temperature,humidity,m)
        time.sleep(3)
except KeyboardInterrupt:
    print("\nStopped.")
