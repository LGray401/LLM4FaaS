# Based on your functional description and the provided source code, here is a `function.py` file that contains the main functions to control the various aspects of your smart home. This file assumes that it is located in a `functions` folder, while the other files are in the `home` folder.
# 
# ### function.py

from home.sensor import Sensor, IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Actuator, Light, Heater, AC, Curtain, Humidifier
from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH


def regulate_light_brightness(home, room_name, target_intensity):
    """Regulate the light brightness in a specific room."""
    room = get_room(home, room_name)
    if room:
        lights = [actuator for actuator in room.actuators if actuator.actuator_type == "Light"]
        for light in lights:
            if target_intensity < LIGHT_INTENSITY_LOW:
                light.set_brightness_level("low")
            elif target_intensity < LIGHT_INTENSITY_HIGH:
                light.set_brightness_level("medium")
            else:
                light.set_brightness_level("high")
    else:
        print(f"Room {room_name} not found.")


def regulate_room_temperature(home, room_name, target_temperature):
    """Regulate the temperature in a specific room."""
    room = get_room(home, room_name)
    if room:
        heater = None
        ac = None
        for actuator in room.actuators:
            if actuator.actuator_type == "Heater":
                heater = actuator
            elif actuator.actuator_type == "AC":
                ac = actuator

        if heater and ac:
            if target_temperature < TEMP_LOW:
                print(f"Target temperature {target_temperature}°C is below the allowed range. Setting to {TEMP_LOW}°C.")
                target_temperature = TEMP_LOW
            elif target_temperature > TEMP_HIGH:
                print(f"Target temperature {target_temperature}°C is above the allowed range. Setting to {TEMP_HIGH}°C.")
                target_temperature = TEMP_HIGH

            heater.set_target_temperature(target_temperature)
            ac.set_target_temperature(target_temperature)

            # Get the current temperature sensor
            temperature_sensor = get_all_sensors(home, "IndoorTemperature")
            current_temperature = sum([sensor.get_reading() for sensor in temperature_sensor if sensor.room_name == room_name]) / len(temperature_sensor)

            heater.adjust_temperature(current_temperature)
            ac.adjust_temperature(current_temperature)
        else:
            print(f"No heater or AC found in room {room_name}.")
    else:
        print(f"Room {room_name} not found.")


def control_curtain(home, room_name, state):
    """Control the curtain in a specific room."""
    room = get_room(home, room_name)
    if room:
        curtains = [actuator for actuator in room.actuators if actuator.actuator_type == "Curtain"]
        for curtain in curtains:
            if state == "open":
                curtain.turn_on()
            elif state == "close":
                curtain.turn_off()
            else:
                print(f"Invalid state {state}. Use 'open' or 'close'.")
    else:
        print(f"Room {room_name} not found.")


def control_humidifier(home, room_name, state):
    """Control the humidifier in a specific room."""
    room = get_room(home, room_name)
    if room:
        humidifiers = [actuator for actuator in room.actuators if actuator.actuator_type == "Humidifier"]
        humidity_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"]
        
        if humidifiers and humidity_sensors:
            humidifier = humidifiers[0]  # Assuming only one humidifier per room
            humidity_sensor = humidity_sensors[0]  # Assuming only one humidity sensor per room
            
            current_humidity = humidity_sensor.get_reading()
            
            if state == "increase" and current_humidity < HUMIDITY_HIGH:
                humidifier.increase_humidity()
            elif state == "decrease" and current_humidity > HUMIDITY_LOW:
                humidifier.decrease_humidity()
            else:
                print(f"Humidity is already within the desired range ({HUMIDITY_LOW}-{HUMIDITY_HIGH}%).")
        else:
            print(f"No humidifier or humidity sensor found in room {room_name}.")
    else:
        print(f"Room {room_name} not found.")


# Main function to demonstrate the functionality
def main():
    # Initialize the home plan
    home = home_plan()

    # Example usage of the functions
    regulate_light_brightness(home, "LivingRoom", 600)
    regulate_room_temperature(home, "LivingRoom", 22)
    control_curtain(home, "LivingRoom", "open")
    control_humidifier(home, "LivingRoom", "increase")


if __name__ == "__main__":
    main()