import sys
import paho.mqtt.client as paho
import json

def msgHandler(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")


def main():
    with open('config.json') as f:
        config = json.load(f)
        server_ip = config['ip']
        topic = config['topic']

    client = paho.Client()
    client.on_message = msgHandler

    if client.connect(server_ip, 1883, 60) != 0:
        print("failed to connect to broker")
        sys.exit(1)

    client.subscribe(topic)

    try:
        print("CTRL+C to exit...")
        client.loop_forever()
    except Exception:
        print("exception found...")
    finally:
        print("disconnecting...")
        client.disconnect()


if __name__ == "__main__":
    main()