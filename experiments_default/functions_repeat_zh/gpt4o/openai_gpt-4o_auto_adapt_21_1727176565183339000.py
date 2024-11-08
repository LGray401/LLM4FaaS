# Based on the functional description and the provided source code files, I'll create a `function.py` file that will control the smart home environment. This file will monitor the sensors and trigger the actuators based on the conditions specified.
# 
# The `functions` folder should contain the `function.py` file, which will have the main function that integrates all the functionalities.
# 
# Here's the `function.py` file:

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Curtain
from home.home_plan import home_plan, get_room_sensors, get_room_actuators

TEMP_THRESHOLD = 26  # Celsius
LIGHT_INTENSITY_THRESHOLD = 900  # Lux

def monitor_and_control(home):
    while True:
        for room in home:
            sensors = get_room_sensors(home, room.name)
            actuators = get_room_actuators(home, room.name)

            for sensor in sensors:
                sensor.turn_on()
                reading = sensor.get_reading()

                if isinstance(sensor, IndoorTemperatureSensor) and reading is not None:
                    if reading > TEMP_THRESHOLD:
                        ac_list = [actuator for actuator in actuators if isinstance(actuator, AC)]
                        for ac in ac_list:
                            ac.set_target_temperature(TEMP_THRESHOLD)
                            ac.adjust_temperature(reading)
                
                if isinstance(sensor, LightIntensiveSensor) and reading is not None:
                    if reading > LIGHT_INTENSITY_THRESHOLD:
                        curtain_list = [actuator for actuator in actuators if isinstance(actuator, Curtain)]
                        for curtain in curtain_list:
                            curtain.turn_on()

                # Humidity control logic can be added here if needed

            # Turn off all sensors after reading to save power
            for sensor in sensors:
                sensor.turn_off()

        # Sleep for a while before taking the next reading
        time.sleep(5)

def main():
    home = home_plan()
    monitor_and_control(home)

if __name__ == "__main__":
    main()