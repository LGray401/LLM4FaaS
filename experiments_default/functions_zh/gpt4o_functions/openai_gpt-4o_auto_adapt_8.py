# Certainly! Given the functional description and the provided source code, I'll create the `function.py` file that will adjust the temperature to 17 degrees, ensure normal humidity levels, and turn off the light intensity.
# 
# Here is the `function.py`:
# 
# ### function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Light
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH

def main():
    home = home_plan()

    # Adjust Temperature to 17 degrees
    target_temp = 17
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    heaters = get_all_actuators(home, "Heater")
    ac_units = get_all_actuators(home, "AC")

    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()

        for heater in heaters:
            if heater.room_name == sensor.room_name:
                heater.set_target_temperature(target_temp)
                heater.adjust_temperature(current_temp)

        for ac in ac_units:
            if ac.room_name == sensor.room_name:
                ac.set_target_temperature(target_temp)
                ac.adjust_temperature(current_temp)

    # Ensure normal humidity
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()

        for humidifier in humidifiers:
            if humidifier.room_name == sensor.room_name:
                if current_humidity < HUMIDITY_LOW:
                    humidifier.turn_on()
                    humidifier.increase_humidity()
                elif current_humidity > HUMIDITY_HIGH:
                    humidifier.turn_on()
                    humidifier.decrease_humidity()
                else:
                    humidifier.turn_off()

    # Turn off light intensity
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")

    for sensor in light_intensity_sensors:
        sensor.turn_on()
        current_light_intensity = sensor.get_reading()

        for light in lights:
            if light.room_name == sensor.room_name:
                light.turn_off()

if __name__ == "__main__":
    main()