# Based on the provided functional description and source code, I will create a `function.py` file that contains the main function to control the lights, indoor temperature, curtains, and humidifier in your smart home project. This file will be placed in the `functions` folder.
# 
# Here is the `function.py` file:

# functions/function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Light, Heater, AC, Curtain, Humidifier
from home.home_plan import home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def adjust_light_brightness(home, room_name, target_brightness):
    """
    Adjust the brightness of the light in the specified room.
    
    :param home: List of rooms in the home plan.
    :param room_name: Name of the room.
    :param target_brightness: Target brightness level (low, medium, high).
    """
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if isinstance(actuator, Light):
            if actuator.status == "on":
                actuator.set_brightness_level(target_brightness)
            else:
                print(f"Light {actuator.id} is OFF. Please turn it on before setting the brightness level.")
                return

def adjust_indoor_temperature(home, room_name, target_temperature):
    """
    Adjust the indoor temperature in the specified room.
    
    :param home: List of rooms in the home plan.
    :param room_name: Name of the room.
    :param target_temperature: Target temperature in Celsius.
    """
    sensors = get_room_sensors(home, room_name)
    actuators = get_room_actuators(home, room_name)
    
    current_temperature = None
    for sensor in sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            if sensor.status == "on":
                current_temperature = sensor.get_reading()
                break
            else:
                print(f"IndoorTemperatureSensor {sensor.id} is OFF. Please turn it on first.")
                return
    
    if current_temperature is None:
        print(f"No IndoorTemperatureSensor found in {room_name}.")
        return
    
    for actuator in actuators:
        if isinstance(actuator, (Heater, AC)):
            actuator.set_target_temperature(target_temperature)
            actuator.adjust_temperature(current_temperature)

def control_curtain(home, room_name, action):
    """
    Control the curtain in the specified room.
    
    :param home: List of rooms in the home plan.
    :param room_name: Name of the room.
    :param action: Action to perform (open, close).
    """
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if isinstance(actuator, Curtain):
            if action == "open":
                actuator.turn_on()
            elif action == "close":
                actuator.turn_off()
            else:
                print(f"Invalid action: {action}. Use 'open' or 'close'.")
                return

def adjust_humidity(home, room_name, target_humidity):
    """
    Adjust the humidity in the specified room.
    
    :param home: List of rooms in the home plan.
    :param room_name: Name of the room.
    :param target_humidity: Target humidity percentage.
    """
    sensors = get_room_sensors(home, room_name)
    actuators = get_room_actuators(home, room_name)
    
    current_humidity = None
    for sensor in sensors:
        if isinstance(sensor, HumiditySensor):
            if sensor.status == "on":
                current_humidity = sensor.get_reading()
                break
            else:
                print(f"HumiditySensor {sensor.id} is OFF. Please turn it on first.")
                return
    
    if current_humidity is None:
        print(f"No HumiditySensor found in {room_name}.")
        return
    
    for actuator in actuators:
        if isinstance(actuator, Humidifier):
            if current_humidity < target_humidity:
                actuator.increase_humidity()
            else:
                actuator.decrease_humidity()

def main():
    # Create the home plan
    home = home_plan()
    
    # Example usage
    room_name = "LivingRoom"
    
    # Adjust light brightness
    adjust_light_brightness(home, room_name, "medium")
    
    # Adjust indoor temperature
    adjust_indoor_temperature(home, room_name, 22)
    
    # Control curtain
    control_curtain(home, room_name, "open")
    
    # Adjust humidity
    adjust_humidity(home, room_name, 45)

if __name__ == "__main__":
    main()