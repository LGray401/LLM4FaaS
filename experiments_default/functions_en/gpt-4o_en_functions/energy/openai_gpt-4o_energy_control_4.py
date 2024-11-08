# Based on your functional description and provided source code, I'll create a `function.py` file that contains a main function to open the windows to cool down the house if the indoor temperature is higher than a predefined threshold (`TEMP_HIGH`).
# 
# Here's the `function.py`:

# function.py
from home.sensor import IndoorTemperatureSensor
from home.actuator import Window
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, TEMP_CHANGE_DURATION_WINDOW
import time

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Iterate through each room
    for room in home:
        # Get the indoor temperature sensors in the room
        sensors = get_room_sensors(home, room.name)
        
        # Find the indoor temperature sensor
        indoor_temp_sensor = None
        for sensor in sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                indoor_temp_sensor = sensor
                break
        
        if indoor_temp_sensor:
            # Turn on the sensor to get the reading
            indoor_temp_sensor.turn_on()
            current_temp = indoor_temp_sensor.get_reading()
            
            if current_temp is not None and current_temp > TEMP_HIGH:
                # If the temperature is higher than TEMP_HIGH, open the windows in the room
                actuators = get_room_actuators(home, room.name)
                for actuator in actuators:
                    if isinstance(actuator, Window):
                        actuator.turn_on()
                        print(f"Opening {actuator.id} to cool down the room.")
                        time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Simulate time for window to open
                        actuator.turn_off()
                        
                print(f"Cooling down {room.name} by opening windows.")
            else:
                print(f"Temperature in {room.name} is within the comfortable range.")
            
            indoor_temp_sensor.turn_off()
        else:
            print(f"No indoor temperature sensor found in {room.name}.")

if __name__ == "__main__":
    main()