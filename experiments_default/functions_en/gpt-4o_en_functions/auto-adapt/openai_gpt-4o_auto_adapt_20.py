# Sure, based on the functional description and the provided source files, here is the `function.py` file that implements the main functionality to control the smart home system:

# functions/function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def main():
    # Initialize home plan
    home = home_plan()

    # Get all sensors and actuators
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")
    
    ac_actuators = get_all_actuators(home, "AC")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")

    # Main loop to check sensor readings and control actuators
    while True:
        # Temperature control
        for sensor in temp_sensors:
            sensor.turn_on()
            temp = sensor.get_reading()
            if temp is not None and temp > TEMP_HIGH:
                for ac in ac_actuators:
                    if ac.room_name == sensor.room_name:
                        ac.set_target_temperature(TEMP_HIGH)
                        ac.adjust_temperature(temp)

        # Humidity control
        for sensor in humidity_sensors:
            sensor.turn_on()
            humidity = sensor.get_reading()
            if humidity is not None:
                for humidifier in humidifiers:
                    if humidifier.room_name == sensor.room_name:
                        if humidity < HUMIDITY_LOW:
                            humidifier.turn_on()
                            humidifier.increase_humidity()
                        elif humidity > HUMIDITY_HIGH:
                            humidifier.turn_on()
                            humidifier.decrease_humidity()
                        else:
                            humidifier.turn_off()

        # Light intensity control
        for sensor in light_sensors:
            sensor.turn_on()
            light_intensity = sensor.get_reading()
            if light_intensity is not None:
                for light in lights:
                    if light.room_name == sensor.room_name:
                        if light_intensity < LIGHT_INTENSITY_LOW:
                            light.turn_on()
                            light.set_brightness_level("high")
                        elif light_intensity > LIGHT_INTENSITY_HIGH:
                            light.turn_on()
                            light.set_brightness_level("low")
                        else:
                            light.turn_off()

        # Sleep for a while before the next reading
        time.sleep(2)

if __name__ == "__main__":
    main()