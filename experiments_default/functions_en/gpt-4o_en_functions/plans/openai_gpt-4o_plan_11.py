# Here is the `function.py` file based on the provided functional description and source code. The `function.py` file contains the main function to implement the required smart home plans.

import os
import sys

# Add the 'home' folder to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'home')))

from home_plan import home_plan, get_all_actuators
from sensor import OutdoorTemperatureSensor
from actuator import Light, Curtain, SmartTV

def main():
    home = home_plan()

    # MORNING PLAN: Please turn on the light in the rain
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    for sensor in outdoor_temp_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        if reading and reading < 10:  # Assuming rain is detected when temperature is below 10 degrees
            lights = get_all_actuators(home, "Light")
            for light in lights:
                light.turn_on()

    # LEAVE HOME PLAN: Please open the curtains when it rains
    for sensor in outdoor_temp_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        if reading and reading < 10:  # Assuming rain is detected when temperature is below 10 degrees
            curtains = get_all_actuators(home, "Curtain")
            for curtain in curtains:
                curtain.turn_on()

    # MOVIE PLAN: Xiaoyu, please turn on the TV
    tvs = get_all_actuators(home, "SmartTV")
    for tv in tvs:
        tv.turn_on()

if __name__ == "__main__":
    main()