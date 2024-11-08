from home.home_plan import get_room_actuators, get_room_sensors, get_all_actuators, get_all_sensors
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def energy_saving_mode(home):
    """
    Implements the energy saving mode.
    """
    # Cooling 1: Outdoor temperature is lower than indoor temperature, open the window.
    outdoor_sensors = get_all_sensors(home, "OutdoorTemperature")
    indoor_sensors = get_all_sensors(home, "IndoorTemperature")

    for outdoor_sensor in outdoor_sensors:
        for indoor_sensor in indoor_sensors:
            outdoor_temp = outdoor_sensor.get_reading()
            indoor_temp = indoor_sensor.get_reading()
            if outdoor_temp is not None and indoor_temp is not None:
                if outdoor_temp < indoor_temp:
                    windows = get_all_actuators(home, "Window")
                    for window in windows:
                        window.turn_on()
                        logger.info(f"{window.id} is open for cooling.")
                        print(f"{window.id} is open for cooling.")

    # Cooling 2: Indoor temperature is lower than outdoor temperature, sunlight is strong, draw the curtain.
    light_sensors = get_all_sensors(home, "LightIntensive")

    for indoor_sensor in indoor_sensors:
        for outdoor_sensor in outdoor_sensors:
            for light_sensor in light_sensors:
                outdoor_temp = outdoor_sensor.get_reading()
                indoor_temp = indoor_sensor.get_reading()
                light_intensity = light_sensor.get_reading()
                if outdoor_temp is not None and indoor_temp is not None and light_intensity is not None:
                    if indoor_temp < outdoor_temp and light_intensity > LIGHT_INTENSITY_HIGH:
                        curtains = get_all_actuators(home, "Curtain")
                        for curtain in curtains:
                            curtain.turn_on()
                            logger.info(f"{curtain.id} is drawn for cooling.")
                            print(f"{curtain.id} is drawn for cooling.")

if __name__ == "__main__":
    # Example usage
    from home.home_plan import home_plan
    home = home_plan()
    energy_saving_mode(home)
