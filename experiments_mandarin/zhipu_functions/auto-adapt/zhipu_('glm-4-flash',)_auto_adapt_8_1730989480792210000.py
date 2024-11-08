# Based on the functional description and the source code provided, here's a `function.py` file that you can add to the `functions` folder of your smart home project. This file includes a `main` function that sets the desired temperature to 17 degrees, maintains humidity at a normal level, and ensures no light is present.

# function.py

import time

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light, Humidifier

from home_plan import home_plan

def main():
    home = home_plan()

    # Set target temperature to 17 degrees Celsius
    for room in home:
        for sensor in room.sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                for actuator in room.actuators:
                    if isinstance(actuator, Heater):
                        actuator.set_target_temperature(17)
                    elif isinstance(actuator, AC):
                        actuator.set_target_temperature(17)

    # Maintain humidity at a normal level
    for room in home:
        for sensor in room.sensors:
            if isinstance(sensor, HumiditySensor):
                # Assuming normal humidity is between 40% and 60%
                desired_humidity = 50  # Set desired humidity to 50%
                for actuator in room.actuators:
                    if isinstance(actuator, Humidifier):
                        if sensor.get_reading() < desired_humidity:
                            actuator.increase_humidity()
                        elif sensor.get_reading() > desired_humidity:
                            actuator.decrease_humidity()

    # Ensure no light is present
    for room in home:
        for sensor in room.sensors:
            if isinstance(sensor, LightIntensiveSensor):
                if sensor.get_reading() > 0:
                    for actuator in room.actuators:
                        if isinstance(actuator, Light):
                            actuator.turn_off()

    print("Home environment set to desired conditions.")

if __name__ == "__main__":
    main()