# Based on the functional description and the provided code files, I will create a `function.py` file that implements the logic to control the AC and the windows based on the specified conditions. 
# 
# Here is the contents of `function.py`:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import Window, AC

def control_ac_and_windows(home):
    for room in home:
        # Check for the presence of AC and Window in the room
        acs = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
        windows = [actuator for actuator in room.actuators if isinstance(actuator, Window)]
        indoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
        outdoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, OutdoorTemperatureSensor)]

        if acs and windows and indoor_temp_sensors and outdoor_temp_sensors:
            indoor_temp = indoor_temp_sensors[0].get_reading()
            outdoor_temp = outdoor_temp_sensors[0].get_reading()

            # If the AC is on, close the window
            for ac in acs:
                if ac.get_status() == "on":
                    for window in windows:
                        window.turn_off()  # Close the window
                        print(f"Closed the window in {room.name} because AC is ON.")
            
            # If indoor temperature is above 26°C and outdoor temperature is below 26°C, open the window
            if indoor_temp is not None and outdoor_temp is not None:
                if indoor_temp > TEMP_HIGH and outdoor_temp < TEMP_HIGH:
                    for window in windows:
                        window.turn_on()  # Open the window
                        print(f"Opened the window in {room.name} because indoor temperature is {indoor_temp}°C and outdoor temperature is {outdoor_temp}°C.")

def main():
    home = home_plan()  # Create the home plan
    control_ac_and_windows(home)  # Control AC and windows based on the conditions

if __name__ == "__main__":
    main()