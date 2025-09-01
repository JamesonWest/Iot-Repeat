
---
# IoT Project Report

## Introduction
This project demonstrates an IoT workflow using the CounterFit simulator. The system simulates environmental sensing with a DHT11 sensor, processes and logs the data locally, sends telemetry via MQTT, and prepares the results for visualization in Power BI.

## System Architecture
1. **Sensor Layer (CounterFit)**
   - DHT11 sensor simulated in CounterFit
   - Provides temperature and humidity readings

2. **Data Logging**
   - Python script (`sensor_data.py`) collects data every 2 seconds
   - Stores readings in `data/sensor_log.csv`

3. **Telemetry**
   - Python script (`telemetry_mqtt.py`) sends readings to an MQTT broker
   - Payload includes timestamp, temperature, and humidity

4. **Data Processing**
   - `process.py` aggregates raw data into 1-minute averages
   - Output saved in `data/aggregates.csv`

5. **Visualization**
   - Power BI imports CSV files
   - Line charts display temperature and humidity trends over time

## Tools and Libraries
- **CounterFit** – IoT simulator
- **counterfit-shims-seeed-python-dht** – DHT11 sensor shim
- **paho-mqtt** – Telemetry transmission
- **pandas** – Data processing
- **Power BI** – Visualization

## Results
- Continuous logging of sensor data
- Successful transmission of MQTT telemetry
- Aggregated CSV file prepared for analysis
- Power BI dashboard showing real-time trends

## Conclusion
This project successfully demonstrates an IoT pipeline at a simulated level:
- **Sensing**: DHT11 data collected in CounterFit
- **Transmission**: Telemetry sent over MQTT
- **Processing**: Aggregated dataset prepared
- **Visualization**: Power BI charting of results

Although simplified, this workflow covers the main IoT building blocks and is suitable as a foundation for future expansion with additional sensors and actuators.



## Useful commands:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

.venv\Scripts\Activate

cd Iot-repeat

pip install -r requirements.txt

counterfit

python sensor_data.py

python telemetry_mqtt.py

python actuation.py

