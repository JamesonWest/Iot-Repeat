# System Architecture
Sensors (CounterFit) → Python scripts → MQTT over TLS → CSV log → Simple rule to Relay → Optional aggregates for dashboard.

## Requirements Mapping
- IoT Device Connection: CounterFit pins 0,5,2
- Sensor Data Collection: `sensor_data.py` with timestamps and local storage
- Telemetry Transmission: `telemetry_mqtt.py` publishes JSON via MQTT with TLS and QoS 1
- Data Visualisation: CSV ingested in Power BI
- Data Processing & Actuation: rule in `actuation.py` with threshold 28°C
- Presentation & Docs: README and this report

## Challenges
Local broker limits and simple retry avoided complexity by using a public TLS broker. CounterFit used to simulate hardware.

## Demo Plan
Show sensors in CounterFit, run logger, show CSV growth, run telemetry, toggle motion and temperature, show relay state switching, then show Power BI visuals.
