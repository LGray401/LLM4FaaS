# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to open the windows when the indoor temperature is above 26 degrees Celsius. This function will be placed in the `functions` folder.
# 
# Here is the `function.py` file:

# functions/function.py

from home.sensor import IndoorTemperatureSensor
from home.actuator import Window
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH

def main():
    # Initialize the home plan
    home = home_plan()

    # Iterate through each room in the home
    for room in home:
        # Get all the indoor temperature sensors in the current room
        sensors = get_room_sensors(home, room.name)
        indoor_temp_sensors = [sensor for sensor in sensors if isinstance(sensor, IndoorTemperatureSensor)]

        # Get all the windows in the current room
        actuators = get_room_actuators(home, room.name)
        windows = [actuator for actuator in actuators if isinstance(actuator, Window)]

        # Check the temperature and control the windows
        for sensor in indoor_temp_sensors:
            if sensor.status == "on":
                current_temp = sensor.get_reading()
                if current_temp and current_temp > 26:  # Open the window if the temperature is above 26 degrees
                    for window in windows:
                        window.turn_on()
                        print(f"Window {window.id} in {room.name} is opened due to high temperature: {current_temp}°C")
                else:
                    for window in windows:
                        window.turn_off()
                        print(f"Window {window.id} in {room.name} is closed due to normal temperature: {current_temp}°C")
            else:
                print(f"Indoor temperature sensor {sensor.id} in {room.name} is OFF. Cannot get reading.")

if __name__ == "__main__":
    main()