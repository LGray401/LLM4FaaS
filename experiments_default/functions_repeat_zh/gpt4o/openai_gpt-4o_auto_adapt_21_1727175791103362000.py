# Sure, I can help you create the `function.py` file based on the provided description and source code. This file will contain the main function that reads sensor data and controls the actuators accordingly. Let's start by creating the `function.py` file.
# 
# Here is the complete code for `function.py`:

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Curtain
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, LIGHT_INTENSITY_HIGH

def monitor_and_control(home):
    while True:
        for room in home:
            sensors = get_room_sensors(home, room.name)
            actuators = get_room_actuators(home, room.name)

            for sensor in sensors:
                sensor.turn_on()
                reading = sensor.get_reading()
                sensor.turn_off()

                if isinstance(sensor, IndoorTemperatureSensor) and reading is not None:
                    acs = [actuator for actuator in actuators if isinstance(actuator, AC)]
                    for ac in acs:
                        if reading > TEMP_HIGH:
                            ac.turn_on()
                            ac.set_target_temperature(TEMP_HIGH)
                        else:
                            ac.turn_off()

                if isinstance(sensor, LightIntensiveSensor) and reading is not None:
                    curtains = [actuator for actuator in actuators if isinstance(actuator, Curtain)]
                    for curtain in curtains:
                        if reading > LIGHT_INTENSITY_HIGH:
                            curtain.turn_on()
                        else:
                            curtain.turn_off()

        time.sleep(5)  # Check every 5 seconds

def main():
    home = home_plan()
    monitor_and_control(home)

if __name__ == "__main__":
    main()