# Based on the given functional description and the provided source code, I'll create a `function.py` file that will contain a main function to manage the temperature, humidity, and light intensity according to your requirements.
# 
# Here's the `function.py` file:

# function.py

from home_plan import home_plan, get_all_sensors, get_all_actuators
from time import sleep
from config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    home = home_plan()

    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humid_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")

    for sensor in indoor_temp_sensors:
        sensor.turn_on()

    for sensor in humid_sensors:
        sensor.turn_on()

    for sensor in light_sensors:
        sensor.turn_on()

    for heater in heaters:
        heater.turn_on()
        heater.set_target_temperature(26)

    for ac in acs:
        ac.turn_on()
        ac.set_target_temperature(26)

    for humidifier in humidifiers:
        humidifier.turn_on()

    for light in lights:
        light.turn_on()

    try:
        while True:
            # Control Temperature
            for sensor in indoor_temp_sensors:
                current_temp = sensor.get_reading()
                if current_temp is not None:
                    for heater in heaters:
                        heater.adjust_temperature(current_temp)
                    for ac in acs:
                        ac.adjust_temperature(current_temp)

            # Control Humidity
            for sensor in humid_sensors:
                current_humidity = sensor.get_reading()
                if current_humidity is not None:
                    for humidifier in humidifiers:
                        if current_humidity < 60:
                            humidifier.increase_humidity()
                        elif current_humidity > 60:
                            humidifier.decrease_humidity()

            # Control Light Intensity
            for light in lights:
                # Assuming an external function to get the current activity
                current_activity = get_current_activity()  # This function needs to be defined to get current activity
                if current_activity == "work":
                    light.set_brightness_level("high")
                elif current_activity == "relax":
                    light.set_brightness_level("low")
                elif current_activity == "rest":
                    light.turn_off()

            sleep(1)

    except KeyboardInterrupt:
        print("Shutting down the system...")
        for sensor in indoor_temp_sensors + humid_sensors + light_sensors:
            sensor.turn_off()
        for actuator in heaters + acs + humidifiers + lights:
            actuator.turn_off()

def get_current_activity():
    # Dummy implementation; this should be replaced with real activity tracking logic
    return "work"  # Placeholder: could be "work", "relax", or "rest"

if __name__ == "__main__":
    main()