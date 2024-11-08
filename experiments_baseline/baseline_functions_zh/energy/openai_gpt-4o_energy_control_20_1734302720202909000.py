# To create a smart home application based on your description, we need to develop a Python program that can automatically adjust indoor temperature, humidity, and light intensity. This program will interact with the sensors and smart devices in each room as per your layout. Here's an outline of how the application might be structured and the command to run it in a Linux terminal.
# 
# ### Python Application
# 
# 1. **Define Classes for Sensors and Devices**: Create classes to represent sensors and smart devices. Each class will have methods to simulate reading values or controlling the devices.
# 
# 2. **Environment Control Logic**: Implement logic to adjust temperature, humidity, and light intensity based on sensor readings.
# 
# 3. **Main Application**: Set up the main application to initialize sensors and devices, continuously monitor the environment, and adjust devices accordingly.
# 
# Here's a basic implementation to illustrate these concepts:
# 
# ```python
# smart_home.py

import random
import time

class Sensor:
    def __init__(self, name):
        self.name = name
    
    def read_value(self):
        return random.uniform(0, 100)  # Simulate sensor reading

class SmartDevice:
    def __init__(self, name):
        self.name = name
    
    def control(self, action):
        print(f"{self.name} is now {action}")

class SmartHome:
    def __init__(self):
        # Initialize sensors
        self.living_room_sensors = {
            "temperature": Sensor("Living Room Temperature"),
            "humidity": Sensor("Living Room Humidity"),
            "light": Sensor("Living Room Light Intensity"),
        }
        
        # Initialize devices
        self.living_room_devices = {
            "heater": SmartDevice("Living Room Heater"),
            "ac": SmartDevice("Living Room AC"),
            "light": SmartDevice("Living Room Light"),
            "curtain": SmartDevice("Living Room Curtain"),
            "humidifier": SmartDevice("Living Room Humidifier"),
        }
    
    def adjust_environment(self):
        # Read sensor values
        temp = self.living_room_sensors["temperature"].read_value()
        humidity = self.living_room_sensors["humidity"].read_value()
        light = self.living_room_sensors["light"].read_value()
        
        print(f"Current Temperature: {temp:.2f}, Humidity: {humidity:.2f}, Light: {light:.2f}")
        
        # Adjust temperature
        if temp < 20:
            self.living_room_devices["heater"].control("on")
            self.living_room_devices["ac"].control("off")
        elif temp > 25:
            self.living_room_devices["ac"].control("on")
            self.living_room_devices["heater"].control("off")
        else:
            self.living_room_devices["ac"].control("off")
            self.living_room_devices["heater"].control("off")
        
        # Adjust humidity
        if humidity < 30:
            self.living_room_devices["humidifier"].control("on")
        else:
            self.living_room_devices["humidifier"].control("off")
        
        # Adjust light
        if light < 50:
            self.living_room_devices["light"].control("on")
            self.living_room_devices["curtain"].control("open")
        else:
            self.living_room_devices["light"].control("off")
            self.living_room_devices["curtain"].control("close")
    
    def run(self):
        while True:
            self.adjust_environment()
            time.sleep(5)  # Adjust every 5 seconds for demonstration purposes

if __name__ == "__main__":
    home = SmartHome()
    home.run()
# ```
# 
# ### Command to Run the Application
# 
# To run this application in a Linux terminal, you need to have Python installed. Save the above code in a file named `smart_home.py`. Then, you can execute it using the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# This basic implementation simulates sensor readings and adjusts devices in the living room. You can extend this code to cover other rooms and more sophisticated logic based on your actual requirements.