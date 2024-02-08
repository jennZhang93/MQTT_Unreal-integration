import sys
import paho.mqtt.client as paho
import json


def main():
    with open('config.json') as f:
        config = json.load(f)
        server_ip = config['ip']
        topic = config['topic']

    client = paho.Client()

    if client.connect(server_ip, 1883, 60) != 0:
        print("failed to connect to broker")
        sys.exit(1)

    client.publish(topic, "helloooooo worldddddd", 0)
    client.disconnect()

if __name__ == "__main__":
    main()