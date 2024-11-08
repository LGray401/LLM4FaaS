# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to open the windows when the indoor temperature exceeds 26 degrees Celsius. This file will be located in the `functions` folder.
# 
# Here's the `function.py` file:

from home.home_plan import home_plan, get_all_sensors, get_room_actuators
from home.sensor import IndoorTemperatureSensor
from home.actuator import Window
import time

def main():
    # Initialize the home plan
    home = home_plan()
    
    while True:
        # Get all indoor temperature sensors
        temp_sensors = get_all_sensors(home, "IndoorTemperature")
        
        # Check each sensor's reading
        for sensor in temp_sensors:
            sensor.turn_on()  # Turn on the sensor to get the reading
            reading = sensor.get_reading()
            sensor.turn_off()  # Turn off the sensor after getting the reading
            
            # If temperature is above 26 degrees, open the windows
            if reading > 26:
                room_name = sensor.room_name
                actuators = get_room_actuators(home, room_name)
                
                for actuator in actuators:
                    if isinstance(actuator, Window):
                        actuator.turn_on()  # Open the window
                        print(f"Opened window in {room_name} due to high temperature: {reading}°C")
                        
        # Sleep for a while before checking again
        time.sleep(10)  # Check every 10 seconds (you can adjust this interval as needed)

if __name__ == "__main__":
    main()