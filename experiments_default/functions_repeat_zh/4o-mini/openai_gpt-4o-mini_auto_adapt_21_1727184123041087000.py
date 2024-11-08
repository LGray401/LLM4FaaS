# Based on your functional description and the provided source code, I will create a `function.py` file that implements the desired functionalities for your smart home project. The main function will monitor the conditions and control the actuators accordingly.
# 
# Here is the `function.py` file that meets your requirements:

# functions/function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, LIGHT_INTENSITY_HIGH
from home.actuator import AC, Curtain
from home.logger_config import logger
import time

def main():
    # Initialize home plan and get sensors and actuators
    home = home_plan()

    # Main loop to monitor sensors and control actuators
    while True:
        # Monitor each room
        for room in home:
            # Get temperature and humidity sensors
            temp_sensors = get_all_sensors(home, "IndoorTemperature")
            humidity_sensors = get_all_sensors(home, "Humidity")
            light_intensity_sensors = get_all_sensors(home, "LightIntensive")
            ac_units = get_all_actuators(home, "AC")
            curtains = get_all_actuators(home, "Curtain")

            # Check temperature and control AC
            for temp_sensor in temp_sensors:
                current_temp = temp_sensor.get_reading()
                if current_temp is not None:
                    if current_temp > TEMP_HIGH:
                        for ac in ac_units:
                            ac.set_target_temperature(25)  # Set desired temperature for AC
                            ac.adjust_temperature(current_temp)

            # Check humidity and maintain it (Assuming normal humidity condition is between 30% and 50%)
            for humidity_sensor in humidity_sensors:
                current_humidity = humidity_sensor.get_reading()
                if current_humidity is not None:
                    # In a real scenario, you might want to adjust a humidifier or dehumidifier here.
                    if current_humidity < 30:
                        logger.info(f"Humidity low in {room.name}. Consider using a humidifier.")
                    elif current_humidity > 50:
                        logger.info(f"Humidity high in {room.name}. Consider using a dehumidifier.")

            # Check light intensity and control curtains
            for light_sensor in light_intensity_sensors:
                current_light = light_sensor.get_reading()
                if current_light is not None:
                    if current_light > LIGHT_INTENSITY_HIGH:
                        for curtain in curtains:
                            curtain.turn_on()  # Open curtains to reduce light intensity
                    else:
                        for curtain in curtains:
                            curtain.turn_off()  # Close curtains when light is within limits

        # Sleep for a while before the next reading
        time.sleep(10)  # Adjust the sleep duration as needed


if __name__ == "__main__":
    main()