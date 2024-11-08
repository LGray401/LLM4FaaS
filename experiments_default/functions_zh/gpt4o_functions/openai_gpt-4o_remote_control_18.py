# Sure, based on your provided functional description "开灯" (which means "turn on the light" in Chinese) and the source codes of the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files, I will create a `function.py` file that contains the main function to turn on the lights in the smart home.
# 
# Here is the content of the `function.py` file:

# function.py
from home.home_plan import home_plan, get_all_actuators

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Get all the lights in the home
    all_lights = get_all_actuators(home, "Light")
    
    # Turn on all the lights
    for light in all_lights:
        light.turn_on()

if __name__ == "__main__":
    main()