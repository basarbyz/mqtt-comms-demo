# MQTT Smart Sensors Simulation

## Introduction

This project simulates a smart sensor system using MQTT protocol for real-time data communication. The system simulates temperature, humidity, and CO2 sensors, publishing their data to specific MQTT topics. It also includes a subscriber that listens to these topics to monitor the sensor data. This is a demonstration of how MQTT can be used for IoT applications, particularly for smart environments.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Documentation](#documentation)
- [Contributors](#contributors)
  
## Installation

Before running the simulation, you need to install the required Python packages. This project relies on the `paho-mqtt` client. You can install it using pip:

```bash
pip install paho-mqtt
```
## Usage

To start the smart sensors simulation, simply run the script from your command line:
```bash
python mqtt-comms-demo.py
```
## Features

- Simulates three different types of sensors: temperature, humidity, and CO2.
- Publishes sensor data to specific MQTT topics at one-minute intervals.
- A subscriber listens on the sensor data topics for real-time monitoring.
- Demonstrates MQTT client connections, publishing, and subscribing mechanisms.

## Dependencies

- Python 3.7 or newer.
- paho-mqtt package.

## Configuration

The main configurations for the MQTT connection and topics are as follows:

- Broker address: test.mosquitto.org
- Port: 1883
- Topics:
   - Temperature: sensor/temperature
   - Humidity: sensor/humidity
   - CO2: sensor/co2

These settings can be modified in the script as needed.

## Documentation

For more details on the paho-mqtt package and MQTT protocol, please refer to:

-  [paho-mqtt documentation](https://eclipse.dev/paho/files/paho.mqtt.python/html/index.html)
- [MQTT.org](https://mqtt.org/)

## Contributors
- [Ismail Basar Bayaz](https://github.com/basarbyz)


