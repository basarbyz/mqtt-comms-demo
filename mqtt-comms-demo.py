import random
import time
import threading
import sys
from paho.mqtt import client as mqtt_client

# Constants
BROKER_ADDRESS = "test.mosquitto.org"
PORT = 1883
TOPIC_TEMPERATURE = "sensor/temperature"
TOPIC_HUMIDITY = "sensor/humidity"
TOPIC_CO2 = "sensor/co2"
CLIENT_ID = "mqtt_smart_sensors_demo"
SENSOR_IDS = {"temperature": "temp_sensor_01", "humidity": "humid_sensor_01", "co2": "co2_sensor_01"}

# MQTT Client Connection
def connect_mqtt(client_id):
    def on_connect(client, userdata, flags, reasonCode, properties=None):
        if flags.session_present:
            print(f"Session already present for {client_id}")
        if reasonCode == 0:
            print(f"Connected to {BROKER_ADDRESS} with client ID: {client_id}")
        if reasonCode > 0:
            print(f"Connection failed with code {reasonCode}")
    
    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION2, client_id) 
    client.on_connect = on_connect

    try:
        client.connect(BROKER_ADDRESS, PORT)
    except OSError as e:
        print(f"Failed to connect to MQTT broker at {BROKER_ADDRESS}:{PORT}")
        print("Exception: ", e)
        sys.exit(1)
    return client

# Smart Sensors Simulation
def publish_sensor_data(client, sensor_type):
    msg_count = 0
    while msg_count < 120:  # Simulating for 120 minutes (2 hours)
        time.sleep(60) # Simulating with 1 minute intervals
        if sensor_type == "temperature":
            temperature = random.uniform(20, 25)
            message = f"{SENSOR_IDS['temperature']},{temperature}"
            client.publish(TOPIC_TEMPERATURE, message)
        elif sensor_type == "humidity":
            humidity = random.uniform(30, 60)
            message = f"{SENSOR_IDS['humidity']},{humidity}"
            client.publish(TOPIC_HUMIDITY, message)
        elif sensor_type == "co2":
            co2 = random.uniform(400, 800)
            message = f"{SENSOR_IDS['co2']},{co2}"
            client.publish(TOPIC_CO2, message)
        msg_count += 1
        print(f"Published {message} to {sensor_type} topic")

# Monitoring Service
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(TOPIC_TEMPERATURE)
    client.subscribe(TOPIC_HUMIDITY)
    client.subscribe(TOPIC_CO2)
    client.on_message = on_message

# Main function to start the demo
def start_demo():
    # Connect to the MQTT broker as a publisher and a subscriber
    client_publisher = connect_mqtt(f"{CLIENT_ID}_publisher")
    client_subscriber = connect_mqtt(f"{CLIENT_ID}_subscriber")
    
    # Start the network loop in a new thread for asynchronous processing
    client_publisher.loop_start()
    client_subscriber.loop_start()
    
    # Subscribe to the topics
    subscribe(client_subscriber)
    
    # Create new threads for each sensor data publishing task
    temperature_thread = threading.Thread(target=publish_sensor_data, args=(client_publisher, "temperature"))
    humidity_thread = threading.Thread(target=publish_sensor_data, args=(client_publisher, "humidity"))
    co2_thread = threading.Thread(target=publish_sensor_data, args=(client_publisher, "co2"))

    # Start the threads
    temperature_thread.start()
    humidity_thread.start()
    co2_thread.start()

    # Wait for all threads to finish
    temperature_thread.join()
    humidity_thread.join()
    co2_thread.join()

    # Stop the network loop
    client_publisher.loop_stop()
    client_subscriber.loop_stop()

start_demo()
