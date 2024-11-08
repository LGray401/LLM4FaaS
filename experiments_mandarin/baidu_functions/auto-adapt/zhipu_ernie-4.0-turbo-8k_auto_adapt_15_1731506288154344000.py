# Based on the functional description and the provided source code, I will create a `function.py` file that contains the main function to initialize and control the smart home system. This file will be located in the `functions` folder.
# 
# Here's the `function.py` file:

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import Sensor
from home.actuator import Actuator
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time


def initialize_smart_home():
    # Initialize the smart home by creating rooms and their components
    home = home_plan()
    print_home_plan(home)
    return home


def monitor_and_control(home):
    while True:
        for room in home:
            # Monitor sensors
            for sensor in room.sensors:
                if sensor.status == "on":
                    reading = sensor.get_reading()
                    if reading is not None:
                        # Based on the sensor type, perform appropriate actions
                        if sensor.sensor_type == "IndoorTemperature":
                            adjust_temperature(room, reading, TEMP_LOW, TEMP_HIGH)
                        elif sensor.sensor_type == "Humidity":
                            adjust_humidity(room, reading, HUMIDITY_LOW, HUMIDITY_HIGH)
                        elif sensor.sensor_type == "LightIntensive":
                            adjust_light(room, reading, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH)
            # Sleep for a while before the next iteration
            time.sleep(1)  # Adjust the sleep duration as needed


def adjust_temperature(room, current_temperature, temp_low, temp_high):
    heaters = get_all_actuators(room.actuators, "Heater")
    acs = get_all_actuators(room.actuators, "AC")
    
    for heater in heaters:
        if current_temperature < temp_low:
            heater.turn_on()
        else:
            heater.turn_off()
    
    for ac in acs:
        if current_temperature > temp_high:
            ac.turn_on()
        else:
            ac.turn_off()


def adjust_humidity(room, current_humidity, humidity_low, humidity_high):
    humidifiers = get_all_actuators(room.actuators, "Humidifier")
    
    # Assuming we have a dehumidifier as well, for simplicity, let's use the same class for both
    dehumidifiers = humidifiers  # This should be replaced with actual dehumidifier class instances if available
    
    for humidifier in humidifiers:
        if current_humidity < humidity_low:
            humidifier.increase_humidity()
        # Else if it's too high, we can use dehumidifier (if implemented separately)
        # For now, just turn off the humidifier if it's too high and it's on
        elif current_humidity > humidity_high and humidifier.status == "on":
            humidifier.turn_off()

    for dehumidifier in dehumidifiers:
        if current_humidity > humidity_high:
            dehumidifier.decrease_humidity()
        # Else if it's too low, we can turn off the dehumidifier if it's on
        elif current_humidity < humidity_low and dehumidifier.status == "on":
            dehumidifier.turn_off()


def adjust_light(room, current_intensity, intensity_low, intensity_high):
    lights = get_all_actuators(room.actuators, "Light")
    
    for light in lights:
        # Simple logic: if it's too dark, turn on the light; if it's too bright, turn it off
        # More sophisticated logic can be added to adjust brightness levels
        if current_intensity < intensity_low:
            light.turn_on()
            # Optionally set brightness level here
        elif current_intensity > intensity_high and light.status == "on":
            light.turn_off()


# Helper function to get all actuators of a specific type from a room's actuator list
def get_all_actuators(actuators, actuator_type):
    return [actuator for actuator in actuators if actuator.actuator_type == actuator_type]


if __name__ == "__main__":
    # Initialize the smart home
    home = initialize_smart_home()
    # Start monitoring and controlling the smart home
    monitor_and_control(home)