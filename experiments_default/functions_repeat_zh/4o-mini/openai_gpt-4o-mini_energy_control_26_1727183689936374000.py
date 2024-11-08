# Based on the provided functional description and the existing code, here is the `function.py` file that implements the required behavior for your smart home project. This file includes the main function that checks the status of the AC and the temperature readings, and controls the windows accordingly.

# functions/function.py

from home.home_plan import home_plan
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import AC, Window
from home.config import TEMP_HIGH

def control_windows(home):
    for room in home:
        # Check for AC and Windows
        acs = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
        windows = [actuator for actuator in room.actuators if isinstance(actuator, Window)]

        # If AC is running, close the windows
        for ac in acs:
            if ac.status == "on":
                for window in windows:
                    window.turn_off()  # Closing the windows
                    print(f"Closed the windows in {room.name} because AC is on.")
        
        # Get indoor and outdoor temperatures
        indoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
        outdoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, OutdoorTemperatureSensor)]

        indoor_temp = None
        outdoor_temp = None

        # Get the readings
        for sensor in indoor_temp_sensors:
            indoor_temp = sensor.get_reading()
        
        for sensor in outdoor_temp_sensors:
            outdoor_temp = sensor.get_reading()

        # If indoor temperature is above threshold and outdoor temperature is lower, open the windows
        if indoor_temp is not None and outdoor_temp is not None:
            if indoor_temp > TEMP_HIGH and outdoor_temp < TEMP_HIGH:
                for window in windows:
                    window.turn_on()  # Opening the windows
                    print(f"Opened the windows in {room.name} because indoor temperature is high and outdoor temperature is low.")

def main():
    home = home_plan()
    control_windows(home)

if __name__ == "__main__":
    main()