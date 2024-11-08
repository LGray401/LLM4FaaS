# Based on your functional description and the provided source code, I will now provide a `function.py` file that contains the main function to control the smart home system according to the specified behavior. The behavior includes automatically closing windows and doors when the AC is on, and asking whether to open windows for cooling when the indoor temperature is higher than the outdoor temperature.
# 
# Here's the `function.py` file:

from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.sensor import Sensor
from home.actuator import Actuator, Window, Door, AC, NotificationSender
from home.config import TEMP_CHANGE_DURATION_WINDOW, TEMP_HIGH, TEMP_LOW
import time

def main():
    # Initialize the home plan
    home = home_plan()
    
    while True:
        # Get all the rooms and their components
        for room in home:
            # Check if the AC is on in the current room
            ac_list = get_all_actuators(home, "AC")
            for ac in ac_list:
                if ac.room_name == room.name and ac.status == "on":
                    # Close all windows and doors in the room when AC is on
                    windows = get_all_actuators(home, "Window")
                    doors = get_all_actuators(home, "Door")
                    for window in windows:
                        if window.room_name == room.name and window.status == "on":
                            window.turn_off()
                    for door in doors:
                        if door.room_name == room.name and door.status == "on":
                            door.turn_off()
            
            # Get indoor and outdoor temperatures
            indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
            outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
            
            for indoor_sensor in indoor_temp_sensors:
                if indoor_sensor.room_name == room.name:
                    indoor_temp = indoor_sensor.get_reading()
                    for outdoor_sensor in outdoor_temp_sensors:
                        if outdoor_sensor.get_status() == "on":  # Ensure the sensor is on to get a valid reading
                            outdoor_temp = outdoor_sensor.get_reading()
                            # Check if indoor temp is higher than outdoor temp
                            if indoor_temp > outdoor_temp:
                                # Ask the user whether to open windows for cooling
                                user_response = input(f"Indoor temperature in {room.name} is {indoor_temp}°C and outdoor is {outdoor_temp}°C. Open windows for cooling? (yes/no): ")
                                if user_response.lower() == "yes":
                                    # Open windows
                                    windows = get_all_actuators(home, "Window")
                                    for window in windows:
                                        if window.room_name == room.name:
                                            window.turn_on()
                                break  # Break after getting one valid outdoor temperature
        
        # Sleep for a while before checking again
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

if __name__ == "__main__":
    main()