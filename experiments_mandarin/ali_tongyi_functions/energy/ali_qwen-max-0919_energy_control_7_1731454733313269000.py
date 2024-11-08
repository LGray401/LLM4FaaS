# Based on the functional description and the provided source code, I will create a `function.py` file that contains the main function to implement the specified behavior. The main function will:
# 
# 1. Check if the AC is turned on.
# 2. If the AC is on, it will close all windows and doors in the room.
# 3. If the indoor temperature is higher than the outdoor temperature, it will ask the user if they want to open the windows to cool down the room.
# 
# Here's the `function.py` file:

# functions/function.py

import random
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import Window, Door, AC, NotificationSender
from home.home_plan import home_plan, get_room_actuators, get_all_sensors
from home.config import TEMP_LOW, TEMP_HIGH, TEMP_CHANGE_DURATION_WINDOW

def main():
    # Initialize the home plan
    home = home_plan()

    # Get all rooms with an AC
    for room in home:
        acs = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
        if acs:
            ac = acs[0]  # Assume there's only one AC per room
            if ac.status == "on":
                print(f"AC is on in {room.name}. Closing all windows and doors.")
                
                # Close all windows and doors in the room
                for actuator in room.actuators:
                    if isinstance(actuator, (Window, Door)):
                        actuator.turn_off()
                
                # Get the indoor and outdoor temperature sensors
                indoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
                outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
                
                if indoor_temp_sensors and outdoor_temp_sensors:
                    indoor_temp_sensor = indoor_temp_sensors[0]
                    outdoor_temp_sensor = outdoor_temp_sensors[0]
                    
                    # Turn on the sensors to get the readings
                    indoor_temp_sensor.turn_on()
                    outdoor_temp_sensor.turn_on()
                    
                    indoor_temp = indoor_temp_sensor.get_reading()
                    outdoor_temp = outdoor_temp_sensor.get_reading()
                    
                    # Turn off the sensors after getting the readings
                    indoor_temp_sensor.turn_off()
                    outdoor_temp_sensor.turn_off()
                    
                    if indoor_temp > outdoor_temp:
                        # Ask the user if they want to open the windows
                        response = input(f"Indoor temperature ({indoor_temp}°C) is higher than outdoor temperature ({outdoor_temp}°C). Do you want to open the windows? (y/n): ")
                        if response.lower() == 'y':
                            # Open all windows in the room
                            for actuator in room.actuators:
                                if isinstance(actuator, Window):
                                    actuator.turn_on()
                            print("Windows opened to cool down the room.")
                        else:
                            print("Windows remain closed.")
                    else:
                        print("Indoor temperature is not higher than outdoor temperature. No action needed.")
                else:
                    print(f"No temperature sensors found in {room.name}.")
        else:
            print(f"No AC found in {room.name}.")

if __name__ == "__main__":
    main()