# Based on the provided functional description and source code, I will create a `function.py` file that contains the main function to implement the energy-saving mode as described. The two conditions for the energy-saving mode are:
# 
# 1. **Cooling 1**: If the outdoor temperature is lower than the indoor temperature, open the window.
# 2. **Cooling 2**: If the indoor temperature is lower than the outdoor temperature and the light intensity is high (indicating strong sunlight), close the curtains.
# 
# Here's the `function.py` file:

# functions/function.py

from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, LightIntensiveSensor
from home.actuator import Window, Curtain
from home.home_plan import get_room_sensors, get_room_actuators, home_plan
from home.config import TEMP_LOW, TEMP_HIGH, LIGHT_INTENSITY_HIGH

def find_sensor_by_type(sensors, sensor_type):
    for sensor in sensors:
        if sensor.sensor_type == sensor_type:
            return sensor
    return None

def find_actuator_by_type(actuators, actuator_type):
    for actuator in actuators:
        if actuator.actuator_type == actuator_type:
            return actuator
    return None

def check_and_adjust(room_name):
    # Get the room's sensors and actuators
    sensors = get_room_sensors(home_plan(), room_name)
    actuators = get_room_actuators(home_plan(), room_name)

    if not sensors or not actuators:
        print(f"No sensors or actuators found in {room_name}")
        return

    # Find the required sensors and actuators
    indoor_temp_sensor = find_sensor_by_type(sensors, "IndoorTemperature")
    outdoor_temp_sensor = find_sensor_by_type(sensors, "OutdoorTemperature")
    light_intensive_sensor = find_sensor_by_type(sensors, "LightIntensive")
    window = find_actuator_by_type(actuators, "Window")
    curtain = find_actuator_by_type(actuators, "Curtain")

    if not all([indoor_temp_sensor, outdoor_temp_sensor, light_intensive_sensor, window, curtain]):
        print(f"Missing required sensors or actuators in {room_name}")
        return

    # Turn on the sensors to get readings
    indoor_temp_sensor.turn_on()
    outdoor_temp_sensor.turn_on()
    light_intensive_sensor.turn_on()

    # Get the current readings
    indoor_temp = indoor_temp_sensor.get_reading()
    outdoor_temp = outdoor_temp_sensor.get_reading()
    light_intensity = light_intensive_sensor.get_reading()

    # Turn off the sensors after getting the readings
    indoor_temp_sensor.turn_off()
    outdoor_temp_sensor.turn_off()
    light_intensive_sensor.turn_off()

    # Check and apply the energy-saving mode
    if outdoor_temp < indoor_temp:
        # Cooling 1: Open the window if the outdoor temperature is lower
        print(f"Outdoor temperature ({outdoor_temp}°C) is lower than indoor temperature ({indoor_temp}°C). Opening the window.")
        window.turn_on()
    elif indoor_temp < outdoor_temp and light_intensity > LIGHT_INTENSITY_HIGH:
        # Cooling 2: Close the curtains if the indoor temperature is lower and light intensity is high
        print(f"Indoor temperature ({indoor_temp}°C) is lower than outdoor temperature ({outdoor_temp}°C) and light intensity is high ({light_intensity} lux). Closing the curtains.")
        curtain.turn_on()
    else:
        print("No action needed for energy-saving mode.")

def main():
    # Define the rooms to check
    rooms_to_check = ["LivingRoom", "Bedroom"]

    # Create the home plan
    home = home_plan()

    # Check and adjust each room
    for room_name in rooms_to_check:
        print(f"\nChecking and adjusting {room_name}...")
        check_and_adjust(room_name)

if __name__ == "__main__":
    main()