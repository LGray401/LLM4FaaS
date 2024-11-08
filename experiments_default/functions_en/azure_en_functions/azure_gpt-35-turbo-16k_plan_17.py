# Sure! I have created the 'function.py' file based on the given functional description and provided source code. Here is the 'function.py' file:

from home.home_plan import home_plan, print_home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, SmartSocket, Door, CleaningRobot, SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def morning_plan():
    home = home_plan()

    # Get the coffee machine in the kitchen
    kitchen_actuators = get_room_actuators(home, "Kitchen")
    coffee_machine = None
    for actuator in kitchen_actuators:
        if isinstance(actuator, CoffeeMachine):
            coffee_machine = actuator
            break

    if coffee_machine is None:
        print("Coffee machine not found in the kitchen!")
        return

    # Turn on the coffee machine
    coffee_machine.turn_on()
    print("Coffee machine is turned on.")

def leave_home_plan():
    home = home_plan()

    # Get the lamp in the living room
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    lamp = None
    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            lamp = actuator
            break

    if lamp is None:
        print("Lamp not found in the living room!")
        return

    # Turn off the lamp
    lamp.turn_off()
    print("Lamp is turned off.")

def movie_plan():
    home = home_plan()

    # Get the bed curtains in the bedroom
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    bed_curtains = None
    for actuator in bedroom_actuators:
        if isinstance(actuator, Curtain):
            bed_curtains = actuator
            break

    if bed_curtains is None:
        print("Bed curtains not found in the bedroom!")
        return

    # Close the bed curtains
    bed_curtains.turn_on()
    print("Bed curtains are closed.")

if __name__ == "__main__":
    morning_plan()
    leave_home_plan()
    movie_plan()