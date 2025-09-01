# IoT CounterFit Demo Project

## Overview
This project demonstrates a simple IoT pipeline using the CounterFit simulator.  
It uses a **DHT11 sensor** (for temperature and humidity) simulated in CounterFit, logs readings locally, sends telemetry over MQTT, and prepares data for visualization in Power BI.

## Features
- Logs sensor data (temperature + humidity) to CSV
- Sends telemetry via MQTT to a broker
- Aggregates data into 1-minute averages for analysis
- Visualizes data in Power BI

## Requirements
Install dependencies in a Python virtual environment:

```powershell
pip install -r requirements.txt
