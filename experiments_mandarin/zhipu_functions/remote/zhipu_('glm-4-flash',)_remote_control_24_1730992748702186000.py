# Based on your functional description of "turning off the light in the bedroom," and the provided source code, here is a Python function that you can include in your `function.py` file in the `functions` folder. This function will utilize the code from `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` to achieve the goal:

# functions/function.py

from home import home_plan
from home.sensor import LightIntensiveSensor
from home.actuator import Light
from home.logger_config import logger

def turn_off_bedroom_light():
    home = home_plan()
    bedroom = get_room(home, "Bedroom")
    if bedroom:
        light_sensors = [sensor for sensor in bedroom.sensors if isinstance(sensor, LightIntensiveSensor)]
        if light_sensors:
            for light_sensor in light_sensors:
                light_sensor.turn_off()
                logger.info(f"Bedroom light turned off: {light_sensor.id}")
        else:
            logger.warning("No light sensors found in the bedroom.")
    else:
        logger.error("Bedroom not found in the home plan.")

if __name__ == "__main__":
    turn_off_bedroom_light()