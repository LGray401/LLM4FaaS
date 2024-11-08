# Based on the content of the markdown file, you are working on a smart home project and you need a `function.py` file. This file should contain the main function and be located in the 'functions' folder. The main function should control the behavior of the smart home based on the following rules:
#
# 1. Temperature: When the temperature is higher than 26°, the air conditioner will automatically turn on and adjust automatically.
# 2. Humidity: Humidity regulation is normal.
# 3. Light Intensity: Automatically open the curtains when the sun is strong at noon.
#
# The `function.py` file should interact with the four existing Python files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) in the 'home' folder.
#
# Here is a basic structure for the `function.py` file:
#
# ```python
from home.sensor import IndoorTemperatureSensor, LightIntensiveSensor
from home.actuator import AC, Curtain
from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators

def main():
    # Get the home plan
    home = home_plan()

    # Get all temperature sensors and ACs
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    acs = get_all_actuators(home, "AC")

    # Get all light intensity sensors and curtains
    light_sensors = get_all_sensors(home, "LightIntensive")
    curtains = get_all_actuators(home, "Curtain")

    # Check each room
    for room in home:
        # Check temperature
        for sensor in temp_sensors:
            if sensor.room_name == room.name:
                reading = sensor.get_reading()
                if reading is not None and reading > 26:
                    for ac in acs:
                        if ac.room_name == room.name:
                            ac.turn_on()
                            ac.set_target_temperature(26)

        # Check light intensity
        for sensor in light_sensors:
            if sensor.room_name == room.name:
                reading = sensor.get_reading()
                if reading is not None and reading > 900:
                    for curtain in curtains:
                        if curtain.room_name == room.name:
                            curtain.turn_on()

if __name__ == "__main__":
    main()
# ```
#
# This script will go through each room in the home, check the temperature and light intensity, and control the air conditioner and curtains accordingly. Please note that this is a basic implementation and may need to be adjusted based on the specific requirements of your project.