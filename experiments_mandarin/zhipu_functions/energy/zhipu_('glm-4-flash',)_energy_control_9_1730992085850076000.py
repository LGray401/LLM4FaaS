# Based on the functional description you provided, the goal is to turn off all lights and close all water sources. To achieve this, we will create a `function.py` file with a main function that iterates through all the actuators in the home plan and performs the required actions.
# 
# Here's the content of `function.py`:

# function.py
from home_plan import home

def turn_off_all_lights():
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()

def turn_off_all_water_sources():
    for room in home:
        for actuator in room.actuators:
            # Assuming we have a WaterSource actuator, if not, you can add the necessary actuator here.
            if isinstance(actuator, WaterSource):
                actuator.turn_off()

def main():
    # Turn off all lights
    turn_off_all_lights()
    print("All lights are now turned off.")

    # Turn off all water sources
    turn_off_all_water_sources()
    print("All water sources are now closed.")

if __name__ == "__main__":
    main()