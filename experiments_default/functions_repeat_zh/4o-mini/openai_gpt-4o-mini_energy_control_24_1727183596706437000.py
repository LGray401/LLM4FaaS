# Based on your functional description and provided source code, I've created the `function.py` file that includes the main function to implement the "节能模式" (energy-saving mode) behavior. In this mode, the system will check the temperature readings and control the window and curtains based on the specified conditions.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH
from home.logger_config import logger
from home.actuator import Window, Curtain

def energy_saving_mode(home):
    for room in home:
        indoor_temp_sensor = next((sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"), None)
        outdoor_temp_sensor = next((sensor for sensor in room.sensors if sensor.sensor_type == "OutdoorTemperature"), None)
        window = next((actuator for actuator in room.actuators if isinstance(actuator, Window)), None)
        curtain = next((actuator for actuator in room.actuators if isinstance(actuator, Curtain)), None)
        
        if indoor_temp_sensor and outdoor_temp_sensor and window and curtain:
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()

            # Check for cooling conditions
            if indoor_temp is not None and outdoor_temp is not None:
                if outdoor_temp < indoor_temp:  # Condition for opening the window
                    window.turn_on()
                else:
                    window.turn_off()

                if indoor_temp < outdoor_temp and indoor_temp < TEMP_LOW:  # Condition for pulling curtains
                    curtain.turn_on()
                else:
                    curtain.turn_off()


def main():
    home = home_plan()  # Initialize the home plan
    energy_saving_mode(home)  # Activate energy saving mode


if __name__ == "__main__":
    main()