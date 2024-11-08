# Certainly! Below is the `function.py` file based on the functional description you provided. This script will be located in the 'functions' folder and will contain the main function to handle temperature, humidity, and light intensity according to the requirements.

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Curtain
from home.home_plan import home_plan

def main():
    home = home_plan()

    while True:
        for room in home:
            for sensor in room.sensors:
                sensor.turn_on()
                reading = sensor.get_reading()

                if isinstance(sensor, IndoorTemperatureSensor):
                    ac = next((actuator for actuator in room.actuators if isinstance(actuator, AC)), None)
                    if ac:
                        if reading > 26:
                            ac.set_target_temperature(24)
                            ac.adjust_temperature(reading)
                        else:
                            ac.turn_off()

                elif isinstance(sensor, LightIntensiveSensor):
                    curtain = next((actuator for actuator in room.actuators if isinstance(actuator, Curtain)), None)
                    current_hour = time.localtime().tm_hour
                    if curtain and current_hour == 12 and reading > 900:
                        curtain.turn_on()
                    else:
                        curtain.turn_off()

                # Humidity regulation is normal (no specific control action defined)
                elif isinstance(sensor, HumiditySensor):
                    pass

                sensor.turn_off()

        time.sleep(60)  # Wait for 1 minute before the next cycle


if __name__ == "__main__":
    main()