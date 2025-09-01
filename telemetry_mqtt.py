import os, csv, time, datetime, json
import paho.mqtt.client as mqtt
from counterfit_connection import CounterFitConnection
from counterfit_shims_seeed_python_dht import DHT
import config

CounterFitConnection.init('127.0.0.1', 5000)

DHT_TYPE="11"
DHT_HUMIDITY_PIN=0
dht=DHT(DHT_TYPE, DHT_HUMIDITY_PIN)

os.makedirs("data",exist_ok=True)
log_path="data/sensor_log.csv"
new=not os.path.exists(log_path)

client=mqtt.Client()
client.connect(config.BROKER_HOST, config.BROKER_PORT, 60)
client.loop_start()

with open(log_path,"a",newline="") as f:
    w=csv.writer(f)
    if new:
        w.writerow(["timestamp","temperature","humidity"])
    try:
        while True:
            humidity, temperature = dht.read()
            ts = datetime.datetime.utcnow().isoformat()
            payload = {"timestamp": ts, "temperature": temperature, "humidity": humidity}
            client.publish(config.MQTT_TOPIC, json.dumps(payload), qos=0)
            w.writerow([ts, temperature, humidity])
            f.flush()
            print("sent", payload)
            time.sleep(config.SAMPLE_INTERVAL)
    except KeyboardInterrupt:
        print("\nStopped.")
