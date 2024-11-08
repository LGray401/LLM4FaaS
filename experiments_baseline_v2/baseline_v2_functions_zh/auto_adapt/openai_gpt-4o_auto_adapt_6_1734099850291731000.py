# Based on the functional description and the provided source code, I'll create a simple smart home application that can be run in the Linux terminal. This application will utilize the existing code to provide temperature, humidity, and light intensity readings for the defined rooms in the home.
# 
# Here is the main application code to be placed in a file named `smart_home_app.py`:
# 
# ```python
import sys
from home.home_plan import home_plan, get_room_sensors

def display_sensor_readings(room_name):
    home = home_plan()
    sensors = get_room_sensors(home, room_name)
    if sensors is None:
        print(f"No sensors found for room: {room_name}")
        return
    
    for sensor in sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        if sensor.sensor_type == "IndoorTemperature" or sensor.sensor_type == "OutdoorTemperature":
            print(f"温度多少度: {reading}°C")
        elif sensor.sensor_type == "Humidity":
            print(f"湿度多少度: {reading}%")
        elif sensor.sensor_type == "LightIntensive":
            print(f"光照多少度等: {reading} lux")
        sensor.turn_off()

def main():
    if len(sys.argv) != 2:
        print("Usage: python smart_home_app.py <room_name>")
        sys.exit(1)

    room_name = sys.argv[1]
    display_sensor_readings(room_name)

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# - This script imports the necessary functions from the `home_plan` module to create the home configuration and retrieve room sensors.
# - `display_sensor_readings(room_name)` turns on each sensor in the specified room, gets its reading, and prints it in the format described in the functional description.
# - The script expects one command-line argument for the room name, and it will print the sensor readings for that room.
# 
# ### Command to Run the Application:
# To run this application from a Linux terminal, navigate to the directory containing `smart_home_app.py` and use the following command:
# 
# ```bash
# python smart_home_app.py <room_name>
# ```
# 
# Replace `<room_name>` with the name of the room you want to query, for example, `LivingRoom`, `Bedroom`, `Kitchen`, etc.
# 
# ### Note:
# Ensure that the `home` directory containing `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` is in the same directory or is properly referenced in your Python path so that the imports work correctly.