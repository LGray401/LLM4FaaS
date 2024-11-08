# To create a smart home application based on your functional description and smart home layout, we can structure the code to simulate the different sensors and smart devices. The application will be a simple command-line tool that you can run in a Linux terminal. Here's a basic version of the Python script:
# 
# ```python
import random

class SmartHome:
    def __init__(self):
        self.rooms = {
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

    def get_sensor_data(self, room, sensor):
        if sensor == "Temperature":
            return f"{random.randint(18, 30)} °C"
        elif sensor == "Humidity":
            return f"{random.randint(30, 70)} %"
        elif sensor == "Light Intensity":
            return f"{random.randint(100, 1000)} lux"
        elif sensor == "Smoke":
            return random.choice(["No Smoke", "Smoke Detected"])
        else:
            return "Unknown sensor"

    def display_room_info(self, room_name):
        if room_name not in self.rooms:
            print(f"Room '{room_name}' not found.")
            return

        room = self.rooms[room_name]
        print(f"Room: {room_name}")
        print("Sensors:")
        for sensor in room["sensors"]:
            data = self.get_sensor_data(room_name, sensor)
            print(f"  {sensor}: {data}")
        print("Devices:")
        for device in room["devices"]:
            print(f"  {device}")

def main():
    home = SmartHome()
    for room in home.rooms:
        home.display_room_info(room)

if __name__ == "__main__":
    main()
# ```
# 
# ### How to Run the Application
# 
# 1. Save the above code into a file, for example `smart_home.py`.
# 
# 2. Open a terminal and navigate to the directory where you saved the file.
# 
# 3. Run the script using the following command:
#    ```bash
#    python3 smart_home.py
#    ```
# 
# This script will simulate the smart home by printing the sensor data and listing devices for each room. Note that the sensor values are generated randomly for demonstration purposes.