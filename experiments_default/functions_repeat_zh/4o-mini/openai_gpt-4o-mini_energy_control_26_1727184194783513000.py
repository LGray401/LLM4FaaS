# Based on your functional description and the provided code, I've created a `function.py` file that implements the main functionality required for your smart home project. This file will check the status of the AC and the temperature readings from the sensors, and it will control the windows accordingly.
# 
# Here's the content of the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH
from home.actuator import Window
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor

def control_windows_based_on_ac_and_temperature(home):
    for room in home:
        # Check for AC in the room
        acs = get_all_actuators(home, "AC")
        if acs:
            for ac in acs:
                if ac.get_status() == "on":
                    # If AC is ON, close the window
                    windows = get_all_actuators(home, "Window")
                    for window in windows:
                        if window.room_name == room.name:
                            window.turn_off()  # Close the window
                            print(f"Closed window in {room.name} because AC is ON.")
        
        # Get temperature readings for the room
        indoor_sensors = get_all_sensors(home, "IndoorTemperature")
        outdoor_sensors = get_all_sensors(home, "OutdoorTemperature")
        
        indoor_temp = next((sensor.get_reading() for sensor in indoor_sensors if sensor.room_name == room.name), None)
        outdoor_temp = next((sensor.get_reading() for sensor in outdoor_sensors if sensor.room_name == room.name), None)

        if indoor_temp is not None and outdoor_temp is not None:
            # If indoor temperature is above 26°C and outdoor temperature is below 26°C, open the window
            if indoor_temp > 26 and outdoor_temp < 26:
                windows = get_all_actuators(home, "Window")
                for window in windows:
                    if window.room_name == room.name:
                        window.turn_on()  # Open the window
                        print(f"Opened window in {room.name} because indoor temp is {indoor_temp}°C and outdoor temp is {outdoor_temp}°C.")

def main():
    home = home_plan()
    control_windows_based_on_ac_and_temperature(home)

if __name__ == "__main__":
    main()