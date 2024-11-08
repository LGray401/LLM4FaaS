# Based on your functional description and the provided source code, I will now provide a `function.py` file that contains the main function to interact with your smart home system. This main function will demonstrate how to initialize the home plan, turn on sensors, get readings, and adjust actuators based on the sensor readings.
# 
# Here's the `function.py` file:

from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.sensor import Sensor
from home.actuator import Actuator, Heater, AC, Light
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize the home plan
    home = home_plan()

    # Example: Get and print info for a specific room
    living_room = get_room(home, "LivingRoom")
    if living_room:
        living_room.print_info()

    # Turn on all sensors in the LivingRoom
    if living_room:
        for sensor in living_room.sensors:
            sensor.turn_on()
    
    # Get and print readings from all sensors in the LivingRoom
    if living_room:
        for sensor in living_room.sensors:
            reading = sensor.get_reading()
            if reading is not None:
                print(f"{sensor.id} reading: {reading}")

    # Adjust actuators based on sensor readings (example: temperature and light)
    if living_room:
        # Adjust heaters and ACs based on temperature
        for actuator in living_room.actuators:
            if isinstance(actuator, Heater):
                # Find the average indoor temperature
                indoor_temps = [sensor.get_reading() for sensor in living_room.sensors if isinstance(sensor, Sensor) and "IndoorTemperature" in sensor.id]
                if indoor_temps:
                    avg_indoor_temp = sum(indoor_temps) / len(indoor_temps)
                    actuator.set_target_temperature(TEMP_HIGH if avg_indoor_temp < TEMP_LOW else TEMP_LOW)
                    actuator.adjust_temperature(avg_indoor_temp)
                    
            elif isinstance(actuator, AC):
                # Find the average indoor temperature
                indoor_temps = [sensor.get_reading() for sensor in living_room.sensors if isinstance(sensor, Sensor) and "IndoorTemperature" in sensor.id]
                if indoor_temps:
                    avg_indoor_temp = sum(indoor_temps) / len(indoor_temps)
                    actuator.set_target_temperature(TEMP_LOW if avg_indoor_temp > TEMP_HIGH else TEMP_HIGH)
                    actuator.adjust_temperature(avg_indoor_temp)

            # Adjust lights based on light intensity
            elif isinstance(actuator, Light):
                light_intensities = [sensor.get_reading() for sensor in living_room.sensors if isinstance(sensor, Sensor) and "LightIntensive" in sensor.id]
                if light_intensities:
                    avg_light_intensity = sum(light_intensities) / len(light_intensities)
                    if avg_light_intensity < LIGHT_INTENSITY_LOW:
                        actuator.turn_on()
                        actuator.set_brightness_level("high")
                    elif avg_light_intensity > LIGHT_INTENSITY_HIGH:
                        actuator.turn_off()
                    else:
                        actuator.set_brightness_level("medium")

# Example of running the main function
if __name__ == "__main__":
    main()