from home.home_plan import home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW
from home.logger_config import logger

def main():
    home = home_plan()
    # Example 1: Automatically close windows when AC is turned on
    ac = get_all_actuators(home, "AC")[0]
    windows = get_all_actuators(home, "Window")
    # for window in windows:
    #     print(window.id)
    if ac.get_status() == "on":
        for window in windows:
            window.turn_off()
            print(f"Window {window.id} closed automatically.")
            logger.info(format(f"Window {window.id} closed automatically."))
    
    # Example 2: Ask user if they want to open the window when indoor temperature is high and outdoor temperature is low
    indoor_temps = get_all_sensors(home, "IndoorTemperature")
    outdoor_temps = get_all_sensors(home, "OutdoorTemperature")
    for indoor_temp in indoor_temps:
        for outdoor_temp in outdoor_temps:
            indoor_temp.turn_on()
            outdoor_temp.turn_on()
            indoor_reading = indoor_temp.get_reading()
            outdoor_reading = outdoor_temp.get_reading()
            # print(f"indoor reading is {indoor_reading}, outdoor reading is {outdoor_reading}")
            if indoor_reading is not None and outdoor_reading is not None:
                if indoor_reading > TEMP_HIGH and outdoor_reading < TEMP_LOW:
                    user_input = input(
                        f"The indoor temperature is {indoor_reading}°C, and the outdoor temperature is {outdoor_reading}°C. "
                        f"Would you like to open a window to cool down? (yes/no) ")
                    if user_input.lower() == "yes":
                        windows = get_all_actuators(home, "Window")
                        for window in windows:
                            window.turn_on()
                            print(f"Window {window.id} opened.")
                            logger.info(format(f"Window {window.id} opened."))
                    else:
                        print(f"No action taken.")
                        logger.info(format(f"No action taken."))
    
    # Example 3: Monitor and adjust the brightness of the light based on the light intensity
    lights = get_all_actuators(home, "Light")
    light_intensities = get_all_sensors(home, "LightIntensive")
    for light in lights:
        for light_intensity in light_intensities:
            light_intensity.turn_on()
            light_intensity_reading = light_intensity.get_reading()
            if light_intensity_reading is not None:
                if light_intensity_reading < LIGHT_INTENSITY_LOW:
                    light.turn_on()
                    light.set_brightness_level("high")
                    print(f"Light {light.id} turned on and brightness set to HIGH.")
                    logger.info(format(f"Light {light.id} turned on and brightness set to HIGH."))
                elif light_intensity_reading > LIGHT_INTENSITY_HIGH:
                    light.turn_off()
                    print(f"Light {light.id} turned off.")
                    logger.info(format(f"Light {light.id} turned off."))
                else:
                    light.turn_on()
                    light.set_brightness_level("medium")
                    print(f"Light {light.id} turned on and brightness set to MEDIUM.")
                    logger.info(format(f"Light {light.id} turned on and brightness set to MEDIUM."))
    
    # Example 4: Monitor and adjust the temperature of the AC or Heater based on the indoor temperature
    acs = get_all_actuators(home, "AC")
    heaters = get_all_actuators(home, "Heater")
    for ac in acs:
        for heater in heaters:
            indoor_temps = get_all_sensors(home, "IndoorTemperature")
            for indoor_temp in indoor_temps:
                indoor_temp.turn_on()
                indoor_reading = indoor_temp.get_reading()
                if indoor_reading is not None:
                    if indoor_reading < TEMP_LOW:
                        # turn on the heater
                        heater.turn_on()
                        heater.set_target_temperature(TEMP_HIGH)
                        print(f"Heater {heater.id} turned on and set to {TEMP_HIGH}°C.")
                        logger.info(format(f"Heater {heater.id} turned on and set to {TEMP_HIGH}°C."))
                        # turn off the AC
                        ac.turn_off()
                        print(f"AC {ac.id} turned off.")
                        logger.info(format(f"AC {ac.id} turned off."))
                    elif indoor_reading > TEMP_HIGH:
                        # turn on the AC
                        ac.turn_on()
                        ac.set_target_temperature(TEMP_LOW)
                        print(f"AC {ac.id} turned on and set to {TEMP_LOW}°C.")
                        logger.info(format(f"AC {ac.id} turned on and set to {TEMP_LOW}°C."))
                        # turn off the heater
                        heater.turn_off()
                        print(f"Heater {heater.id} turned off.")
                        logger.info(format(f"Heater {heater.id} turned off."))
                    else:
                        # turn off both AC and heater
                        ac.turn_off()
                        print(f"AC {ac.id} turned off.")
                        logger.info(format(f"AC {ac.id} turned off."))
                        heater.turn_off()
                        print(f"Heater {heater.id} turned off.")
                        logger.info(format(f"Heater {heater.id} turned off."))
    
    # Example 5: Monitor and adjust the humidity of the humidifier based on the indoor humidity
    humidifiers = get_all_actuators(home, "Humidifier")
    for humidifier in humidifiers:
        indoor_humidities = get_all_sensors(home, "Humidity")
        for indoor_humidity in indoor_humidities:
            indoor_humidity.turn_on()
            indoor_reading = indoor_humidity.get_reading()
            if indoor_reading is not None:
                if indoor_reading < HUMIDITY_LOW:
                    humidifier.increase_humidity()
                    print(f"Humidifier {humidifier.id} increasing humidity.")
                    logger.info(format(f"Humidifier {humidifier.id} increasing humidity."))
                elif indoor_reading > HUMIDITY_HIGH:
                    humidifier.decrease_humidity()
                    print(f"Humidifier {humidifier.id} decreasing humidity.")
                    logger.info(format(f"Humidifier {humidifier.id} decreasing humidity."))
                else:
                    print(f"Humidifier {humidifier.id} maintaining humidity.")
                    logger.info(format(f"Humidifier {humidifier.id} maintaining humidity."))

if __name__ == "__main__":
    main()