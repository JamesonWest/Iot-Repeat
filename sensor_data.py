import os, csv, time, datetime
from counterfit_connection import CounterFitConnection
from counterfit_shims_seeed_python_dht import DHT

CounterFitConnection.init('127.0.0.1', 5000)

DHT_TYPE="11"
DHT_HUMIDITY_PIN=0
dht=DHT(DHT_TYPE, DHT_HUMIDITY_PIN)

os.makedirs("data", exist_ok=True)
path="data/sensor_log.csv"
new=not os.path.exists(path)

with open(path,"a",newline="") as f:
    w=csv.writer(f)
    if new:
        w.writerow(["timestamp","temperature","humidity"])
    while True:
        humidity, temperature=dht.read()
        ts=datetime.datetime.utcnow().isoformat()
        w.writerow([ts,temperature,humidity])
        f.flush()
        print(ts,temperature,humidity)
        time.sleep(2)
