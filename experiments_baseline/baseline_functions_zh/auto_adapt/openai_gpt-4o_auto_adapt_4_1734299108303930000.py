# To create a smart home application based on your functional description and layout, we will write a simple Python script that simulates the interaction with sensors and smart devices. This script will monitor the environmental conditions and trigger certain actions based on predefined thresholds.
# 
# Below is an example Python script to simulate such a smart home application:
# 
# ```python
import random

# Constants for the functional description
TARGET_TEMPERATURE = 20
TARGET_HUMIDITY = 50
TARGET_LIGHT_INTENSITY = 15

# Smart Home Layout
rooms = {
    "Living Room": {
        "sensors": ["Temperature", "Humidity", "Light Intensity"],
        "devices": ["Light", "Window", "Socket", "Door", "Heater", "AC", "Curtain", "Humidifier", "Cleaning Robot", "Music Player", "TV", "Notification Sender"]
    },
    "Bedroom": {
        "sensors": ["Temperature", "Humidity", "Light Intensity"],
        "devices": ["Light", "Window", "Curtain", "AC", "Heater", "Music Player", "Door", "Socket", "Cleaning Robot", "Humidifier"]
    },
    "Bathroom": {
        "sensors": ["Temperature", "Humidity"],
        "devices": ["Light", "Window", "Heater", "Door", "Socket"]
    },
    "Kitchen": {
        "sensors": ["Humidity", "Smoke"],
        "devices": ["Light", "Window", "Heater", "Coffee Machine", "Socket", "Door"]
    },
    "Balcony": {
        "sensors": ["Temperature", "Humidity"],
        "devices": ["Door"]
    }
}

def get_sensor_data(sensor):
    # Simulate sensor data
    if sensor == "Temperature":
        return random.randint(15, 25)
    elif sensor == "Humidity":
        return random.randint(40, 60)
    elif sensor == "Light Intensity":
        return random.randint(10, 20)
    elif sensor == "Smoke":
        return random.choice([True, False])  # True indicates smoke detected
    return None

def control_devices(room, current_conditions):
    actions = []
    temperature = current_conditions.get("Temperature")
    humidity = current_conditions.get("Humidity")
    light_intensity = current_conditions.get("Light Intensity")
    smoke = current_conditions.get("Smoke")

    # Example logic for controlling devices
    if temperature is not None:
        if temperature < TARGET_TEMPERATURE:
            if "Heater" in rooms[room]["devices"]:
                actions.append("Turn on Heater")
        elif temperature > TARGET_TEMPERATURE:
            if "AC" in rooms[room]["devices"]:
                actions.append("Turn on AC")

    if humidity is not None and humidity < TARGET_HUMIDITY:
        if "Humidifier" in rooms[room]["devices"]:
            actions.append("Turn on Humidifier")

    if light_intensity is not None and light_intensity < TARGET_LIGHT_INTENSITY:
        if "Light" in rooms[room]["devices"]:
            actions.append("Turn on Light")

    if smoke is not None and smoke:
        if "Notification Sender" in rooms[room]["devices"]:
            actions.append("Send Smoke Alert")

    return actions

def main():
    for room, features in rooms.items():
        current_conditions = {}
        for sensor in features["sensors"]:
            current_conditions[sensor] = get_sensor_data(sensor)

        print(f"\n{room} Conditions: {current_conditions}")
        actions = control_devices(room, current_conditions)
        if actions:
            print(f"Actions: {', '.join(actions)}")
        else:
            print("No actions needed.")

if __name__ == "__main__":
    main()
# ```
# 
# To run this script in a Linux terminal, you can save it as `smart_home.py` and execute the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# This script simulates a basic smart home application where each room's sensors provide readings, and based on those readings, the application decides to activate certain smart devices. You can expand the logic to include more sophisticated rules and interactions as needed.