# Based on the provided functional description and the source code files, I will create a `function.py` file that contains the main function to manage the indoor temperature, humidity, and light intensity according to your requirements.
# 
# Here's the `function.py` file:
# 
# ### `functions/function.py`

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW
import time

def maintain_temperature(home):
    indoor_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    heaters = get_all_actuators(home, "Heater")
    ac_units = get_all_actuators(home, "AC")

    for sensor in indoor_temperature_sensors:
        sensor.turn_on()
        current_temperature = sensor.get_reading()
        if current_temperature is not None:
            for heater in heaters:
                if heater.room_name == sensor.room_name:
                    heater.set_target_temperature(26)
                    heater.adjust_temperature(current_temperature)
            for ac in ac_units:
                if ac.room_name == sensor.room_name:
                    ac.set_target_temperature(26)
                    ac.adjust_temperature(current_temperature)

def maintain_humidity(home):
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        if current_humidity is not None:
            for humidifier in humidifiers:
                if humidifier.room_name == sensor.room_name:
                    if current_humidity < 60:
                        humidifier.turn_on()
                        humidifier.increase_humidity()
                    elif current_humidity > 60:
                        humidifier.turn_on()
                        humidifier.decrease_humidity()
                    else:
                        humidifier.turn_off()

def adjust_lighting(home, activity):
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")

    brightness_level = {
        "work": "high",
        "relax": "low",
        "rest": "off"
    }

    for sensor in light_sensors:
        sensor.turn_on()
        sensor.get_reading()
        for light in lights:
            if light.room_name == sensor.room_name:
                if activity == "rest":
                    light.turn_off()
                else:
                    light.turn_on()
                    light.set_brightness_level(brightness_level[activity])

def main():
    home = home_plan()

    while True:
        maintain_temperature(home)
        maintain_humidity(home)
        
        # Adjust lighting based on current activity
        current_activity = "work"  # This should be dynamically set based on the user's schedule or input
        adjust_lighting(home, current_activity)

        time.sleep(60)  # Wait for a minute before checking again

if __name__ == "__main__":
    main()