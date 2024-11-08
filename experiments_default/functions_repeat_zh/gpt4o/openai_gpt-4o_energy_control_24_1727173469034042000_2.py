# Based on the functional description and the provided source code, we need to implement a function in `function.py` that activates energy-saving modes. The two modes described are:
# 
# 1. If the outdoor temperature is lower than the indoor temperature, open the windows.
# 2. If the indoor temperature is higher than the outdoor temperature and the light intensity is strong, close the curtains.
# 
# Here is the implementation of the `function.py` file:

from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, LightIntensiveSensor
from home.actuator import Window, Curtain
from home.home_plan import home_plan, get_all_sensors, get_all_actuators, print_home_plan
from home.config import TEMP_CHANGE_DURATION_WINDOW

def main():
    # Initialize the home plan
    home = home_plan()

    # Print the home plan
    print_home_plan(home)

    # Get all sensors and actuators
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    light_sensors = get_all_sensors(home, "LightIntensive")

    windows = get_all_actuators(home, "Window")
    curtains = get_all_actuators(home, "Curtain")

    # Turn on all necessary sensors and actuators
    for sensor in indoor_temp_sensors + outdoor_temp_sensors + light_sensors:
        sensor.turn_on()

    for actuator in windows + curtains:
        actuator.turn_on()

    # Energy-saving mode logic
    for indoor_sensor in indoor_temp_sensors:
        indoor_temp = indoor_sensor.get_reading()

        for outdoor_sensor in outdoor_temp_sensors:
            outdoor_temp = outdoor_sensor.get_reading()

            if outdoor_temp is not None and indoor_temp is not None:
                # Energy-saving mode 1: Open windows if outdoor temperature is lower than indoor temperature
                if outdoor_temp < indoor_temp:
                    for window in windows:
                        window.turn_on()  # Assuming turning on the window means opening it

                # Energy-saving mode 2: Close curtains if indoor temperature is higher than outdoor temperature and light intensity is strong
                elif indoor_temp > outdoor_temp:
                    for light_sensor in light_sensors:
                        light_intensity = light_sensor.get_reading()

                        if light_intensity is not None and light_intensity > 900:
                            for curtain in curtains:
                                curtain.turn_on()  # Assuming turning on the curtain means closing it

if __name__ == "__main__":
    main()