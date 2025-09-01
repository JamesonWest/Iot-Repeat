import os, csv, time, datetime
from counterfit_shims_grove.grove_temperature_humidity_sensor import GroveTemperatureHumiditySensor
from counterfit_shims_grove.grove_motion_sensor import GroveMotionSensor

os.makedirs("data", exist_ok=True)
path="data/sensor_log.csv"
new=not os.path.exists(path)

temp=GroveTemperatureHumiditySensor(0)
motion=GroveMotionSensor(5)

with open(path,"a",newline="") as f:
    w=csv.writer(f)
    if new:
        w.writerow(["timestamp","temperature","humidity","motion"])
    for _ in range(30):
        t,h=temp.read()
        m=motion.read()
        ts=datetime.datetime.utcnow().isoformat()
        w.writerow([ts,t,h,m])
        f.flush()
        print(ts,t,h,m)
        time.sleep(2)
