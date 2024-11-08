# Based on your functional description and the provided source code, I will create a `function.py` file that implements the required behavior: when the AC in the bedroom or living room is turned on, the corresponding window should close, and when the indoor temperature exceeds 26 degrees Celsius while the outdoor temperature is below 26 degrees Celsius, the window should open.
# 
# Here is the implementation of `function.py`:

# function.py
from home.home_plan import home_plan
from home.config import TEMP_HIGH
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import AC, Window
from home.logger_config import logger

def check_ac_and_window(home):
    for room in home:
        acs = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
        windows = [actuator for actuator in room.actuators if isinstance(actuator, Window)]

        # Close the window if AC is on
        for ac in acs:
            if ac.get_status() == "on":
                for window in windows:
                    window.turn_off()  # Close the window
                    logger.info(f"Closed the {window.id} because {ac.id} is ON.")

        # Get readings from temperature sensors
        indoor_temp_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        outdoor_temp_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, OutdoorTemperatureSensor)), None)

        if indoor_temp_sensor and outdoor_temp_sensor:
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()

            # Open the window if conditions are met
            if indoor_temp is not None and outdoor_temp is not None:
                if indoor_temp > TEMP_HIGH and outdoor_temp < TEMP_HIGH:
                    for window in windows:
                        window.turn_on()  # Open the window
                        logger.info(f"Opened the {window.id} because indoor temperature is {indoor_temp}°C and outdoor temperature is {outdoor_temp}°C.")

def main():
    home = home_plan()
    check_ac_and_window(home)

if __name__ == "__main__":
    main()