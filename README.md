# CounterFit IoT Demo

## What it is
A simple simulated IoT system using CounterFit. Two sensors (temperature/humidity and motion) publish JSON telemetry over MQTT with TLS. Data is logged locally to CSV. A rule toggles a relay as a fan when temperature is high and motion is detected.

## How to run
1. `python -m venv .venv && . .venv/bin/activate` (Windows: `.venv\Scripts\activate`)
2. `pip install -r requirements.txt`
3. Start the CounterFit app and add:
   - Temperature & Humidity sensor on pin 0
   - Motion sensor on pin 5
   - Relay on pin 2
4. Terminal A: `python sensor_data.py`
5. Terminal B: `python telemetry_mqtt.py`
6. Terminal C: `python actuation.py`
7. Optional processing: stop the logger and run `python process.py`

## MQTT
Broker: test.mosquitto.org  
Port: 8883 (TLS)  
Telemetry topic: `counterfit_iot_demo/telemetry`  
Actuation topic: `counterfit_iot_demo/actuation`

## Power BI quick path
Get Data → Text/CSV → pick `data/sensor_log.csv` → Load → build visuals for Temperature, Humidity, Motion over time. Refresh while logger runs.
