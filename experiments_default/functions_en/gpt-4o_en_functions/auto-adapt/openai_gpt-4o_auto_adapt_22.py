# Sure, based on the functional description and the provided source code, I will create the `function.py` file to manage the smart home system. This file will be placed in the 'functions' folder and will contain the main function that orchestrates the behavior of the sensors and actuators according to the specified conditions.
# 
# Here is the `function.py` content:

# functions/function.py
import time
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize home plan
    home = home_plan()

    while True:
        # Check temperature
        temperature_sensors = get_all_sensors(home, "IndoorTemperature")
        all_temps = [sensor.get_reading() for sensor in temperature_sensors if sensor.get_status() == "on"]
        
        if all_temps and all(temp > TEMP_HIGH for temp in all_temps):
            acs = get_all_actuators(home, "AC")
            windows = get_all_actuators(home, "Window")
            for ac in acs:
                ac.turn_on()
            for window in windows:
                window.turn_off()

        # Check humidity
        humidity_sensors = get_all_sensors(home, "Humidity")
        for sensor in humidity_sensors:
            reading = sensor.get_reading()
            if reading is not None and reading < HUMIDITY_LOW:
                humidifiers = get_all_actuators(home, "Humidifier")
                for humidifier in humidifiers:
                    humidifier.turn_on()

        # Check light intensity
        light_sensors = get_all_sensors(home, "LightIntensive")
        for sensor in light_sensors:
            reading = sensor.get_reading()
            if reading is not None:
                if reading < LIGHT_INTENSITY_LOW:
                    lights = get_all_actuators(home, "Light")
                    for light in lights:
                        light.turn_on()
                elif reading > LIGHT_INTENSITY_HIGH:
                    curtains = get_all_actuators(home, "Curtain")
                    for curtain in curtains:
                        curtain.turn_on()
                    lights = get_all_actuators(home, "Light")
                    for light in lights:
                        light.turn_on()

        # Sleep for a while before next check
        time.sleep(1)

if __name__ == "__main__":
    main()