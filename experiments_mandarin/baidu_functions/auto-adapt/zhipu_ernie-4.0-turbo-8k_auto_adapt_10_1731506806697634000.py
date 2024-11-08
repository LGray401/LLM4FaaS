# Based on your functional description and the provided source code, I will now provide a `function.py` file that contains the main function to control and monitor the smart home environment. This main function will specifically focus on maintaining the temperature at 25°, humidity at a moderate level, and light intensity at a bright level.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, get_all_sensors, get_all_actuators, get_room
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW
from home.logger_config import logger


def maintain_optimal_conditions(home):
    # Get all relevant sensors and actuators
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")
    
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")
    
    # Turn on all sensors
    for sensor in temperature_sensors + humidity_sensors + light_sensors:
        if sensor.get_status() == "off":
            sensor.turn_on()
    
    # Maintain temperature at 25°
    for sensor in temperature_sensors:
        reading = sensor.get_reading()
        if reading is not None:
            if reading < TEMP_LOW:
                # Turn on heaters
                for heater in heaters:
                    if heater.room_name == sensor.room_name and heater.get_status() == "off":
                        heater.turn_on()
                        heater.set_target_temperature(TEMP_HIGH)
            elif reading > TEMP_HIGH:
                # Turn on ACs
                for ac in acs:
                    if ac.room_name == sensor.room_name and ac.get_status() == "off":
                        ac.turn_on()
                        ac.set_target_temperature(TEMP_HIGH)
            else:
                # Turn off heaters and ACs
                for device in heaters + acs:
                    if device.room_name == sensor.room_name and device.get_status() == "on":
                        device.turn_off()
    
    # Maintain humidity at moderate level
    for sensor in humidity_sensors:
        reading = sensor.get_reading()
        if reading is not None:
            if reading < HUMIDITY_LOW:
                # Turn on humidifiers
                for humidifier in humidifiers:
                    if humidifier.room_name == sensor.room_name and humidifier.get_status() == "off":
                        humidifier.turn_on()
                        humidifier.increase_humidity()
            elif reading > HUMIDITY_HIGH:
                # Turn off humidifiers (or decrease humidity if applicable)
                for humidifier in humidifiers:
                    if humidifier.room_name == sensor.room_name and humidifier.get_status() == "on":
                        humidifier.turn_off()
                        # humidifier.decrease_humidity()  # Uncomment if decrease function is needed
            else:
                # Turn off humidifiers
                for humidifier in humidifiers:
                    if humidifier.room_name == sensor.room_name and humidifier.get_status() == "on":
                        humidifier.turn_off()
    
    # Maintain light intensity at bright level
    for sensor in light_sensors:
        reading = sensor.get_reading()
        if reading is not None:
            if reading < LIGHT_INTENSITY_LOW:
                # Turn on lights
                for light in lights:
                    if light.room_name == sensor.room_name and light.get_status() == "off":
                        light.turn_on()
                        light.set_brightness_level("high")
            elif reading > LIGHT_INTENSITY_HIGH:
                # Turn off lights (or adjust to lower brightness if needed)
                for light in lights:
                    if light.room_name == sensor.room_name and light.get_status() == "on":
                        light.turn_off()
            else:
                # Ensure lights are on and at the right brightness
                for light in lights:
                    if light.room_name == sensor.room_name and light.get_status() == "off":
                        light.turn_on()
                        light.set_brightness_level("high")


def main():
    # Initialize the home plan
    home = home_plan()
    
    # Maintain optimal conditions indefinitely
    try:
        while True:
            maintain_optimal_conditions(home)
            # Sleep for a while before checking again (adjust as needed)
            # time.sleep(some_interval)
    except KeyboardInterrupt:
        print("Program stopped.")
        logger.info("Program stopped.")


if __name__ == "__main__":
    main()