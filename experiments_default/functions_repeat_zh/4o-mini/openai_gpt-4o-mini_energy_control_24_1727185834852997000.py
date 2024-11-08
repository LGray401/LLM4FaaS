# Based on your functional description and the provided source code, I will create a `function.py` file that implements the "节能模式" (energy-saving mode) you described. This mode includes two functionalities: 
# 
# 1. **降温1**: If the outdoor temperature is lower than the indoor temperature, the window should be opened.
# 2. **降温2**: If the indoor temperature is lower than the outdoor temperature and the sunlight is strong (as indicated by the light intensity), the curtains should be drawn.
# 
# Here's how the `function.py` file will be structured:

# functions/function.py
from home.home_plan import home_plan
from home.config import LIGHT_INTENSITY_HIGH
from home.actuator import Window, Curtain
from home.logger_config import logger

def energy_saving_mode(home):
    for room in home:
        # Get the sensors for temperature and light intensity
        indoor_temp_sensor = next((s for s in room.sensors if s.sensor_type == "IndoorTemperature"), None)
        outdoor_temp_sensor = next((s for s in room.sensors if s.sensor_type == "OutdoorTemperature"), None)
        light_intensity_sensor = next((s for s in room.sensors if s.sensor_type == "LightIntensive"), None)

        # Get the actuators for window and curtain
        window_actuator = next((a for a in room.actuators if isinstance(a, Window)), None)
        curtain_actuator = next((a for a in room.actuators if isinstance(a, Curtain)), None)

        if indoor_temp_sensor and outdoor_temp_sensor and light_intensity_sensor:
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()
            light_intensity = light_intensity_sensor.get_reading()

            # 降温1: Open window if outdoor temperature is lower than indoor temperature
            if outdoor_temp < indoor_temp:
                if window_actuator:
                    window_actuator.turn_on()
                logger.info(f"Window opened in {room.name} to cool down.")

            # 降温2: Draw curtains if indoor temperature is lower than outdoor temperature and sunlight is strong
            if indoor_temp < outdoor_temp and light_intensity > LIGHT_INTENSITY_HIGH:
                if curtain_actuator:
                    curtain_actuator.turn_on()
                logger.info(f"Curtains drawn in {room.name} to block sunlight.")

def main():
    home = home_plan()
    energy_saving_mode(home)

if __name__ == "__main__":
    main()