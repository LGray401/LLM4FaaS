# Sure, I can help you with that. Here is the 'function.py' file based on your functional description and the provided source code:

from home.sensor import IndoorTemperatureSensor, HumiditySensor
from home.actuator import AC, Heater
from home.home_plan import home_plan, print_home_plan, get_room_sensors, get_room_actuators

def main():
    # Create home plan
    home = home_plan()

    # Print home plan
    print_home_plan(home)

    # Get room sensors and actuators
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Turn on AC in living room
    for actuator in living_room_actuators:
        if isinstance(actuator, AC):
            actuator.set_target_temperature(26)
            actuator.adjust_temperature(living_room_sensors[0].get_reading())

    # Turn on Heater in living room
    for actuator in living_room_actuators:
        if isinstance(actuator, Heater):
            actuator.set_target_temperature(100)
            actuator.adjust_temperature(living_room_sensors[0].get_reading())

if __name__ == "__main__":
    main()