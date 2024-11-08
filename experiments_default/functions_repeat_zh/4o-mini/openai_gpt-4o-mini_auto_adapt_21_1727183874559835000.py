# Based on your functional description and the provided source code, the `function.py` file will include a main function that monitors the readings from the sensors and controls the actuators accordingly. Here is how the `function.py` file can be structured:

# function.py
import time
from home.home_plan import home_plan
from home.config import TEMP_HIGH, LIGHT_INTENSITY_HIGH
from home.sensor import IndoorTemperatureSensor, LightIntensiveSensor
from home.actuator import AC, Curtain

def main():
    # Initialize home and components
    home = home_plan()

    # Example room names
    living_room = home[0]  # Assuming LivingRoom is the first room in the list

    # Get the relevant sensors and actuators
    temp_sensor = next((sensor for sensor in living_room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
    light_sensor = next((sensor for sensor in living_room.sensors if isinstance(sensor, LightIntensiveSensor)), None)
    ac = next((actuator for actuator in living_room.actuators if isinstance(actuator, AC)), None)
    curtain = next((actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)), None)

    if temp_sensor and ac:
        temp_sensor.turn_on()  # Turn on the temperature sensor to start getting readings
        while True:
            current_temp = temp_sensor.get_reading()
            if current_temp is not None:
                if current_temp > TEMP_HIGH:
                    ac.set_target_temperature(26)  # Set AC target temperature
                    ac.adjust_temperature(current_temp)  # Autzomatically adjust AC based on temperature
                time.sleep(5)  # Wait before the next reading

    if light_sensor and curtain:
        light_sensor.turn_on()  # Turn on the light sensor to start getting readings
        while True:
            current_light = light_sensor.get_reading()
            if current_light is not None:
                if current_light > LIGHT_INTENSITY_HIGH:
                    curtain.turn_on()  # Open curtain if light intensity is high
                else:
                    curtain.turn_off()  # Close curtain if light intensity is normal
                time.sleep(5)  # Wait before the next reading

if __name__ == "__main__":
    main()