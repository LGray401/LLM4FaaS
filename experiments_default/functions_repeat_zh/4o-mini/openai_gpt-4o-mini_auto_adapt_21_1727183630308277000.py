# Based on your functional description and the provided source code, here is how the `function.py` file could look. This file will contain a `main` function that will check the readings from the sensors and control the actuators accordingly.

# function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH, LIGHT_INTENSITY_HIGH
from home.actuator import AC, Curtain
from home.sensor import IndoorTemperatureSensor, LightIntensiveSensor

def main():
    # Initialize the home plan with rooms and their components
    home = home_plan()

    # Iterate through the rooms to check temperature and light intensity
    for room in home:
        # Check for temperature sensors and control the AC if needed
        temperature_sensor = next((s for s in room.sensors if isinstance(s, IndoorTemperatureSensor)), None)
        if temperature_sensor:
            current_temp = temperature_sensor.get_reading()
            if current_temp is not None and current_temp > TEMP_HIGH:
                ac = next((a for a in room.actuators if isinstance(a, AC)), None)
                if ac:
                    ac.turn_on()
                    ac.set_target_temperature(24)  # Set to a comfortable temperature
                    print(f"AC in {room.name} is turned ON due to high temperature: {current_temp}°C")

        # Check for light intensity sensors and control the curtains if needed
        light_sensor = next((s for s in room.sensors if isinstance(s, LightIntensiveSensor)), None)
        if light_sensor:
            current_light = light_sensor.get_reading()
            if current_light is not None and current_light > LIGHT_INTENSITY_HIGH:
                curtain = next((a for a in room.actuators if isinstance(a, Curtain)), None)
                if curtain:
                    curtain.turn_on()  # Open the curtains
                    print(f"Curtains in {room.name} are opened due to high light intensity: {current_light} lux")

if __name__ == "__main__":
    main()