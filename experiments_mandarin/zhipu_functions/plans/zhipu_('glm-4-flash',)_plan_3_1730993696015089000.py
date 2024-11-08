# Based on the provided functional description and the source code from the four Python files (sensor.py, actuator.py, home_plan.py, and config.py), I will now provide a `function.py` file located in the `functions` folder. The `function.py` will contain a `main` function that will trigger the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN based on the descriptions given.
# 
# Here is the content for `function.py`:

# function.py
from home.home_plan import home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Light, Curtain, CoffeeMachine, AC, Heater

def main():
    home = home_plan()

    # MORNING PLAN
    # Assuming there is a CoffeeMachine and a Heater in the LivingRoom
    living_room = get_room_sensors(home, "LivingRoom")
    coffee_machine = None
    heater = None
    for actuator in living_room:
        if isinstance(actuator, CoffeeMachine):
            coffee_machine = actuator
        elif isinstance(actuator, Heater):
            heater = actuator

    if coffee_machine and heater:
        coffee_machine.make_coffee("espresso")
        heater.set_target_temperature(22)  # Set desired temperature to 22°C

    # LEAVE HOME PLAN
    # Turn off all the lights
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()

    # MOVIE PLAN
    # Assuming there is a Curtain in the LivingRoom
    living_room = get_room_sensors(home, "LivingRoom")
    curtain = None
    for actuator in living_room:
        if isinstance(actuator, Curtain):
            curtain = actuator
            break

    if curtain:
        curtain.turn_on()  # Close the curtain

# Helper function to get room sensors
def get_room_sensors(home, room_name):
    for room in home:
        if room.name == room_name:
            return room.sensors
    return []

# Helper function to get room actuators
def get_room_actuators(home, room_name):
    for room in home:
        if room.name == room_name:
            return room.actuators
    return []

if __name__ == "__main__":
    main()