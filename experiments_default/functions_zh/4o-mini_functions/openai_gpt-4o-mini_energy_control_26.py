# Based on the functional description you provided, we need to create a `function.py` file that implements the following logic:
# 
# 1. When the AC in the bedroom or living room is turned on, the corresponding window should be closed.
# 2. If the indoor temperature exceeds 26 degrees Celsius and the outdoor temperature is below 26 degrees Celsius, the window should be opened.
# 
# Here's how we can implement this in the `function.py` file:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import AC, Window

def control_windows(home):
    for room in home:
        # Get the AC and window in the current room
        ac = next((actuator for actuator in room.actuators if isinstance(actuator, AC)), None)
        window = next((actuator for actuator in room.actuators if isinstance(actuator, Window)), None)

        if ac:
            # Check if AC is on
            if ac.get_status() == "on":
                if window:
                    window.turn_off()  # Close the window if AC is on
                    print(f"Closed {window.id} because {ac.id} is on.")

            # Get the indoor temperature sensor
            indoor_temp_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
            outdoor_temp_sensor = next((sensor for sensor in home for sensor in sensor.sensors if isinstance(sensor, OutdoorTemperatureSensor)), None)

            if indoor_temp_sensor and outdoor_temp_sensor:
                indoor_temp = indoor_temp_sensor.get_reading()
                outdoor_temp = outdoor_temp_sensor.get_reading()

                if indoor_temp is not None and outdoor_temp is not None:
                    # Check the conditions for opening the window
                    if indoor_temp > TEMP_HIGH and outdoor_temp < TEMP_HIGH:
                        if window:
                            window.turn_on()  # Open the window
                            print(f"Opened {window.id} because indoor temperature is {indoor_temp}°C and outdoor temperature is {outdoor_temp}°C.")

def main():
    home = home_plan()  # Create the home plan
    control_windows(home)  # Control windows based on AC and temperature conditions

if __name__ == "__main__":
    main()