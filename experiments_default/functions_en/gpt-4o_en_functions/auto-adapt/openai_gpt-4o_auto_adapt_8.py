# Based on the functional description you provided, the `function.py` file should include a `main` function that sets the temperature, humidity, and light intensity as specified. Here is the content for the `function.py` file:

from home.home_plan import home_plan, get_all_sensors, get_all_actuators

def main():
    # Initialize home plan
    home = home_plan()

    # Set Temperature
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")

    for sensor in temperature_sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        if current_temp is not None:
            for heater in heaters:
                if heater.room_name == sensor.room_name:
                    heater.set_target_temperature(17)
                    heater.adjust_temperature(current_temp)
            for ac in acs:
                if ac.room_name == sensor.room_name:
                    ac.set_target_temperature(17)
                    ac.adjust_temperature(current_temp)

    # Set Humidity to Normal
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        if current_humidity is not None:
            for humidifier in humidifiers:
                if humidifier.room_name == sensor.room_name:
                    if current_humidity < 40:
                        humidifier.increase_humidity()
                    elif current_humidity > 60:
                        humidifier.decrease_humidity()

    # Turn off Light Intensity
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")

    for sensor in light_sensors:
        sensor.turn_on()
        current_light_intensity = sensor.get_reading()
        if current_light_intensity is not None:
            for light in lights:
                if light.room_name == sensor.room_name:
                    light.turn_off()

if __name__ == "__main__":
    main()