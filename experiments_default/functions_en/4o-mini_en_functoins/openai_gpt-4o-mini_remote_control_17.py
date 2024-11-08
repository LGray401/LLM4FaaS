# Based on your functional description of turning off the living room lights, I will create a `function.py` file that includes a main function to accomplish this task. This function will make use of the classes defined in your existing `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files.
# 
# Here's how the `function.py` will look:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators

def turn_off_living_room_lights():
    # Get the home plan
    home = home_plan()

    # Get the actuators in the living room
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Turn off all lights in the living room
    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            actuator.turn_off()

def main():
    print("Turning off the living room lights...")
    turn_off_living_room_lights()

if __name__ == "__main__":
    main()