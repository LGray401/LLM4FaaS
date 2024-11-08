# Based on the functional description "Please turn off unnecessary switches" and the provided source code files, I will create a `function.py` file that will include a main function to manage the actuators in the smart home system. This function will identify the unnecessary switches (e.g., lights that are on but have no corresponding sensor indicating they need to be on) and turn them off.
# 
# Here's the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_all_actuators, get_all_sensors
from home.config import LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def turn_off_unnecessary_switches(home):
    for room in home:
        # Get all lights in the room
        lights = get_all_actuators(home, "Light")
        # Get all light intensity sensors in the room
        light_sensors = get_all_sensors(home, room.name)

        for light in lights:
            # Check if the light is currently on
            if light.get_status() == "on":
                # Assume no readings if no light sensors in the room
                if not light_sensors:
                    print(f"No light sensors in {room.name}. Keeping the light {light.id} ON.")
                    continue

                # Check the readings from light intensity sensors
                total_intensity = sum(sensor.get_reading() or 0 for sensor in light_sensors)
                average_intensity = total_intensity / len(light_sensors) if light_sensors else 0
                
                # Determine if the light should be turned off
                if average_intensity < LIGHT_INTENSITY_LOW:
                    print(f"Average light intensity in {room.name} is {average_intensity} lux. Keeping the light {light.id} ON.")
                elif average_intensity > LIGHT_INTENSITY_HIGH:
                    print(f"Average light intensity in {room.name} is {average_intensity} lux. Turning off the light {light.id}.")
                    light.turn_off()
                else:
                    print(f"Average light intensity in {room.name} is {average_intensity} lux. Keeping the light {light.id} ON.")

def main():
    home = home_plan()
    turn_off_unnecessary_switches(home)

if __name__ == "__main__":
    main()