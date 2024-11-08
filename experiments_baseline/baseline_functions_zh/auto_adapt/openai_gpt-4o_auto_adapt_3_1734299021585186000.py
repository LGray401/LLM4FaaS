# To create a smart home application based on your functional description and layout, we can write a Python script that simulates the operation of sensors and smart devices within each room. The application will display the current status of sensors and allow basic interaction with smart devices.
# 
# Here's a basic implementation of the smart home application:
# 
# ```python
#!/usr/bin/env python3

class Room:
    def __init__(self, name, sensors, devices):
        self.name = name
        self.sensors = sensors
        self.devices = devices

    def display_status(self):
        print(f"--- {self.name} ---")
        print("Sensors:")
        for sensor, value in self.sensors.items():
            print(f"  {sensor}: {value}")
        print("Devices:")
        for device in self.devices:
            print(f"  {device}")

def main():
    # Define sensor readings based on functional description
    sensor_readings = {
        "Temperature": "温度26度",
        "Humidity": "湿度50",
        "Light Intensity": "光适中",
        "Smoke": "No smoke detected"
    }

    # Define rooms with their sensors and devices
    rooms = [
        Room("Living Room", 
             {"Temperature": sensor_readings["Temperature"], "Humidity": sensor_readings["Humidity"], "Light Intensity": sensor_readings["Light Intensity"]},
             ["Light", "Light", "Window", "Window", "Socket", "Socket", "Door", "Heater", "AC", "Curtain", "Humidifier", "Cleaning Robot", "Music Player", "TV", "Notification Sender"]),
        Room("Bedroom", 
             {"Temperature": sensor_readings["Temperature"], "Humidity": sensor_readings["Humidity"], "Light Intensity": sensor_readings["Light Intensity"]},
             ["Light", "Light", "Window", "Curtain", "AC", "Heater", "Music Player", "Door", "Socket", "Socket", "Cleaning Robot", "Humidifier"]),
        Room("Bathroom", 
             {"Temperature": sensor_readings["Temperature"], "Humidity": sensor_readings["Humidity"]},
             ["Light", "Window", "Heater", "Door", "Socket", "Socket"]),
        Room("Kitchen", 
             {"Humidity": sensor_readings["Humidity"], "Smoke": sensor_readings["Smoke"]},
             ["Light", "Window", "Heater", "Coffee Machine", "Socket", "Socket", "Socket", "Door"]),
        Room("Balcony", 
             {"Temperature": sensor_readings["Temperature"], "Humidity": sensor_readings["Humidity"]},
             ["Door"])
    ]

    # Display the status of each room
    for room in rooms:
        room.display_status()
        print()

if __name__ == "__main__":
    main()
# ```
# 
# ### Instructions to Run the Application
# 
# 1. Save the script to a file named `smart_home.py`.
# 2. Make the script executable: `chmod +x smart_home.py`
# 3. Run the script using the command: `./smart_home.py`
# 
# This basic implementation will display the current sensor readings and list the smart devices in each room. You can extend this script with additional functionality, such as simulating interactions with the devices, logging changes, or even integrating with real smart home APIs if desired.