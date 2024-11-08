# Based on your functional description and the source code provided, I will create a `function.py` file that serves as the main entry point for your smart home project. The file will include functionality for controlling the brightness of lights, adjusting indoor temperature, controlling curtain operation, and managing the humidifier. 
# 
# Here's how `function.py` will be structured:
# 
# 1. **Initialize Home**: This will involve creating the home with rooms and their respective sensors and actuators.
# 2. **Control Functions**: Functions to control light brightness, adjust temperature, open/close curtains, and control the humidifier will be implemented.
# 3. **Main Function**: This will serve as the entry point for executing the above functionalities.
# 
# Here's the code for `function.py`:

# functions/function.py
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH
from home.logger_config import logger

def control_light(room, brightness_level):
    light_actuators = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
    if light_actuators:
        for light in light_actuators:
            light.turn_on()
            light.set_brightness_level(brightness_level)
    else:
        print(f"No light actuator found in {room.name}")

def adjust_temperature(room, current_temperature):
    heater = next((actuator for actuator in room.actuators if isinstance(actuator, Heater)), None)
    ac = next((actuator for actuator in room.actuators if isinstance(actuator, AC)), None)

    if heater:
        heater.set_target_temperature(TEMP_HIGH)
        heater.adjust_temperature(current_temperature)
    
    if ac:
        ac.set_target_temperature(TEMP_LOW)
        ac.adjust_temperature(current_temperature)

def control_curtain(room, action):
    curtain_actuators = [actuator for actuator in room.actuators if isinstance(actuator, Curtain)]
    if curtain_actuators:
        for curtain in curtain_actuators:
            if action == "open":
                curtain.turn_on()
                print(f"{curtain.id} is now opened.")
            elif action == "close":
                curtain.turn_off()
                print(f"{curtain.id} is now closed.")
    else:
        print(f"No curtain actuator found in {room.name}")

def control_humidifier(room, action):
    humidifier_actuator = next((actuator for actuator in room.actuators if isinstance(actuator, Humidifier)), None)
    if humidifier_actuator:
        if action == "increase":
            humidifier_actuator.increase_humidity()
        elif action == "decrease":
            humidifier_actuator.decrease_humidity()
    else:
        print(f"No humidifier found in {room.name}")

def main():
    home = home_plan()

    # Example Control Commands
    room_name = "LivingRoom"
    room = next((room for room in home if room.name == room_name), None)

    if room:
        # Control light brightness
        control_light(room, "medium")

        # Adjust temperature
        current_temp = 22  # Example current temperature
        adjust_temperature(room, current_temp)

        # Control curtains
        control_curtain(room, "open")  # or "close"

        # Control humidifier
        control_humidifier(room, "increase")  # or "decrease"
    else:
        print(f"Room {room_name} not found.")

if __name__ == "__main__":
    main()