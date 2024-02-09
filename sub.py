import sys
import paho.mqtt.client as paho
import json
import datetime

firstmsg=True
time1=0.0
time2=0.0

def msgHandler(client, userdata, msg):
    global firstmsg
    global time1
    global time2
    # print(f"{msg.topic}: {msg.payload.decode()}", flush=True)
    if firstmsg==True:
        time1 = datetime.datetime.now()
        firstmsg=False
    if "end" in msg.payload.decode():
        time2 = datetime.datetime.now()
        elapsed_time_ms = (time2 - time1).total_seconds() * 1000
        print(f"{msg.topic}: {msg.payload.decode()}", flush=True)
        print(f"recv client: {elapsed_time_ms}", flush=True)

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
        print("CTRL+C to exit...", flush=True)
        client.loop_forever()
    except Exception as e:
        print("exception found...", flush=True)
        print(e, flush=True)
    finally:
        print("disconnecting...", flush=True)
        client.disconnect()


if __name__ == "__main__":
    main()