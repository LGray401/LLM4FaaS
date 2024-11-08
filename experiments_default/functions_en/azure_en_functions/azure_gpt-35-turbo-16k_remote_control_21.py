# Sure! I will create the 'function.py' file for your smart home project based on the given functional description and the provided code files. Here is the 'function.py' file:

from home.home_plan import home_plan, get_room_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, LightIntensiveSensor
from home.actuator import Light, MusicPlayer, AC, Curtain, CoffeeMachine, CleaningRobot

def main():
    # Create home plan
    home = home_plan()

    # Get required sensors and actuators
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_all_actuators(home, "Light") + get_all_actuators(home, "MusicPlayer")

    bedroom_sensors = get_room_sensors(home, "Bedroom")
    bedroom_actuators = get_all_actuators(home, "Light") + get_all_actuators(home, "MusicPlayer") + get_all_actuators(home, "AC")

    kitchen_sensors = get_room_sensors(home, "Kitchen")
    kitchen_actuators = get_all_actuators(home, "Light") + get_all_actuators(home, "CoffeeMachine")

    bathroom_sensors = get_room_sensors(home, "Bathroom")
    bathroom_actuators = get_all_actuators(home, "Light")

    balcony_sensors = get_room_sensors(home, "Balcony")
    balcony_actuators = get_all_actuators(home, "Light") + get_all_actuators(home, "Curtain")

    # Turn on the light in the living room
    for sensor in living_room_sensors:
        if isinstance(sensor, LightIntensiveSensor):
            sensor.turn_on()
            break

    # Adjust the light intensity in the living room
    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            actuator.set_brightness_level("medium")
            break

    # Play a stress-relieving song in the living room
    for actuator in living_room_actuators:
        if isinstance(actuator, MusicPlayer):
            actuator.play_music("stress-relief")
            break

    # Turn on the AC in the living room and set the temperature to 22°C
    for actuator in living_room_actuators:
        if isinstance(actuator, AC):
            actuator.turn_on()
            actuator.set_target_temperature(22)
            break

    # Close the curtains in the living room
    for actuator in living_room_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
            break

    # Let the cleaning robot start working in the living room
    for actuator in living_room_actuators:
        if isinstance(actuator, CleaningRobot):
            actuator.turn_on()
            actuator.daily_routine()
            break

    # Print the status of the coffee machine in the kitchen
    for sensor in kitchen_sensors:
        if isinstance(sensor, CoffeeMachine):
            sensor.get_status()
            break

if __name__ == "__main__":
    main()