# Sure, here is the 'function.py' file for your smart home project:

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators, \
    get_all_sensors, get_all_actuators
from home.sensor import LightIntensiveSensor, IndoorTemperatureSensor, HumiditySensor, OutdoorTemperatureSensor
from home.actuator import Light, Curtain, MusicPlayer, CoffeeMachine, Door, Window, CleaningRobot, SmartTV

def main():
    # Create the home plan
    home = home_plan()

    # Print the home plan
    print_home_plan(home)

    # Get the living room
    living_room = get_room(home, "LivingRoom")

    # Get the living room sensors
    living_room_sensors = get_room_sensors(home, "LivingRoom")

    # Get the living room actuators
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Get all temperature sensors
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")

    # Get all light actuators
    light_actuators = get_all_actuators(home, "Light")

if __name__ == "__main__":
    main()