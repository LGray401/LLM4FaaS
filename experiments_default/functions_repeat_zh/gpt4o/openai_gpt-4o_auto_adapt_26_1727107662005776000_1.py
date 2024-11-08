# Based on the functional description and provided source code, I will create a `function.py` file that contains the main function to manage the temperature, humidity, and light intensity in the smart home. 
# 
# Here is the `function.py`:

# function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW

def adjust_temperature(home):
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")

    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        for heater in heaters:
            if heater.room_name == sensor.room_name:
                heater.set_target_temperature(26)  # Target temperature is 26°C
                heater.adjust_temperature(current_temp)
        for ac in acs:
            if ac.room_name == sensor.room_name:
                ac.set_target_temperature(26)  # Target temperature is 26°C
                ac.adjust_temperature(current_temp)

def adjust_humidity(home):
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        for humidifier in humidifiers:
            if humidifier.room_name == sensor.room_name:
                if current_humidity < 60:
                    humidifier.turn_on()
                    humidifier.increase_humidity()
                else:
                    humidifier.turn_off()
                    humidifier.decrease_humidity()

def adjust_light_intensity(home, activity):
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")

    brightness_map = {
        "work": "high",
        "relax": "medium",
        "rest": "off"
    }
    for sensor in light_sensors:
        sensor.turn_on()
        current_light = sensor.get_reading()
        for light in lights:
            if light.room_name == sensor.room_name:
                if activity == "rest":
                    light.turn_off()
                else:
                    light.turn_on()
                    light.set_brightness_level(brightness_map[activity])

def main():
    home = home_plan()
    adjust_temperature(home)
    adjust_humidity(home)
    # Adjust light based on activity
    adjust_light_intensity(home, "work")  # Example activity: "work", "relax", or "rest"

if __name__ == "__main__":
    main()