# Based on the provided functional description and the existing code files, I will create a `function.py` file that implements the desired functionality. The main function will check the status of the air conditioners in the bedroom and living room, manage the state of the windows based on temperature readings, and ensure that interactions between sensors and actuators occur as specified.
# 
# Here's the code for `function.py`:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import AC, Window

def manage_windows_and_ac(home):
    # Iterate through each room to manage AC and windows
    for room in home:
        acs_in_room = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
        windows_in_room = [actuator for actuator in room.actuators if isinstance(actuator, Window)]
        indoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
        outdoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, OutdoorTemperatureSensor)]

        # Check AC status
        for ac in acs_in_room:
            if ac.get_status() == 'on':
                # Close windows if AC is on
                for window in windows_in_room:
                    window.turn_off()
        
        # Manage window based on temperature readings
        if indoor_temp_sensors and outdoor_temp_sensors:
            indoor_temp = indoor_temp_sensors[0].get_reading()
            outdoor_temp = outdoor_temp_sensors[0].get_reading()

            # Check if the indoor temperature is higher than 26 degrees Celsius
            if indoor_temp and indoor_temp > TEMP_HIGH:
                # Open windows if outdoor temperature is lower than 26 degrees Celsius
                if outdoor_temp and outdoor_temp < TEMP_HIGH:
                    for window in windows_in_room:
                        window.turn_on()

def main():
    # Initialize home plan
    home = home_plan()

    # Manage AC and window states
    manage_windows_and_ac(home)

if __name__ == "__main__":
    main()