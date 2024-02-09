#!/bin/bash

# Check if the user has provided an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <sub or pub or server> <win or mac>"
    exit 1
fi

# Assign the first argument to the variable config_file
command=$1
sys=$2

# Check if the command is either "sub" or "pub"
if [ "$command" != "sub" ] && [ "$command" != "pub" ] && [ "$command" != "server" ]; then
    echo "Error: Command must be either 'sub' or 'pub' or 'server'."
    exit 1
fi

if [ "$sys" = "mac" ]; then

    # Start Mosquitto with the specified command
    if [ "$command" = "sub" ]; then
        echo "Starting Mosquitto subscriber..."
        python3 sub.py
    elif [ "$command" = "pub" ]; then
        echo "Starting Mosquitto publisher..."
        python3 pub.py
    elif [ "$command" = "server" ]; then
        echo "Starting Mosquitto server..."
        mosquitto -c /opt/homebrew/etc/mosquitto/mosquitto.conf -v
    fi

elif [ "$sys" = "win" ]; then

    # Start Mosquitto with the specified command
    if [ "$command" = "sub" ]; then
        echo "Starting Mosquitto subscriber..."
        python sub.py
    elif [ "$command" = "pub" ]; then
        echo "Starting Mosquitto publisher..."
        python pub.py
    elif [ "$command" = "server" ]; then
        echo "Starting Mosquitto server..."
        mosquitto -c "C:\Program Files\mosquitto\mosquitto.conf" 
    fi

fi

