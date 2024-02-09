import sys
import time
import paho.mqtt.client as paho
import json
import datetime




def main():
    with open('config.json') as f:
        config = json.load(f)
        server_ip = config['ip']
        topic = config['topic']

    client = paho.Client()

    if client.connect(server_ip, 1883, 60) != 0:
        print("failed to connect to broker")
        sys.exit(1)
    else:
        print("connected to broker", flush=True)



    # Get current date and time
    time1 = datetime.datetime.now()
    
    # Send normal msg
    for i in range(0, 1000):
        message_size_kb = 10
        bigmessage = "A" * (message_size_kb * 1024)  # Create a string of 'A' characters with the desired size in bytes
        message_size_mb = 2
        bigbigmessage = "A" * (message_size_mb * 1024 * 1024)

        msg=bigbigmessage + str(i)
        client.publish(topic, msg, 0)
    
    # Send ending msg
    # msg="end"
    # client.publish(topic, msg, 0)
    
    # Send latency
    time2 = datetime.datetime.now()
    elapsed_time_ms = (time2 - time1).total_seconds() * 1000
    msg="send: " + str(elapsed_time_ms)
    client.publish(topic, msg, 0)
    
    
    time.sleep(1)
    client.disconnect()

if __name__ == "__main__":
    main()