# Based on your functional description and the provided source code, I will create a `function.py` file that implements the required functionality. The main function will manage the interactions between the sensors and actuators to meet your specified conditions.
# 
# Here’s the code for `function.py`:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import AC, Window

def check_ac_and_windows(home):
    for room in home:
        # Check for AC and window in the room
        ac = next((actuator for actuator in room.actuators if isinstance(actuator, AC)), None)
        window = next((actuator for actuator in room.actuators if isinstance(actuator, Window)), None)
        
        if ac and window:
            # Get indoor and outdoor temperatures
            indoor_temp_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
            outdoor_temp_sensor = next((sensor for sensor in home if isinstance(sensor, OutdoorTemperatureSensor)), None)

            if indoor_temp_sensor and outdoor_temp_sensor:
                indoor_temp = indoor_temp_sensor.get_reading()
                outdoor_temp = outdoor_temp_sensor.get_reading()

                if ac.get_status() == "on":
                    # Close the window if AC is on
                    window.turn_off()
                    print(f"Closed the window in the {room.name} because AC is ON.")

                if indoor_temp is not None and outdoor_temp is not None:
                    if indoor_temp > TEMP_HIGH and outdoor_temp < TEMP_HIGH:
                        # Open the window if indoor temperature is high and outdoor temperature is low
                        window.turn_on()
                        print(f"Opened the window in the {room.name} because indoor temperature is {indoor_temp}°C and outdoor temperature is {outdoor_temp}°C.")

def main():
    home = home_plan()
    check_ac_and_windows(home)

if __name__ == "__main__":
    main()