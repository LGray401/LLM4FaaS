# Here is the 'function.py' file placed in the 'functions' folder that implements the main function to control the air conditioner based on the temperature, humidity, and light intensity readings as per your functional description:

# functions/function.py

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH

def main():
    home = home_plan()

    # Get all relevant sensors and actuators
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")
    ac_units = get_all_actuators(home, "AC")

    while True:
        for temp_sensor in temperature_sensors:
            temp_sensor.turn_on()
            temp_reading = temp_sensor.get_reading()
            if temp_reading is not None and temp_reading > 26:
                for ac in ac_units:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(temp_reading)

        for humidity_sensor in humidity_sensors:
            humidity_sensor.turn_on()
            humidity_reading = humidity_sensor.get_reading()
            if humidity_reading is not None:
                for temp_sensor in temperature_sensors:
                    temp_reading = temp_sensor.get_reading()
                    if temp_reading is not None and temp_reading > 10:
                        for ac in ac_units:
                            ac.set_target_temperature(TEMP_HIGH)
                            ac.adjust_temperature(temp_reading)

        for light_sensor in light_sensors:
            light_sensor.turn_on()
            light_reading = light_sensor.get_reading()
            if light_reading is not None and light_reading > 20:
                for ac in ac_units:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(temp_reading)

        # Wait for a certain duration before the next check
        time.sleep(10)

if __name__ == "__main__":
    main()