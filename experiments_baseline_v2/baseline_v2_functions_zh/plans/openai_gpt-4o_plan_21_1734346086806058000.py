# To create a smart home application in Python based on your functional description, we'll leverage the existing code in your `home` folder. We'll create a new script, `smart_home.py`, that will define the different plans: "Morning Plan", "Leave Home Plan", and "Movie Plan". This script will use classes and methods from `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` to implement the desired functionality.
# 
# Let's write the `smart_home.py` script:
# 
# ### `smart_home.py`
# ```python
from home.sensor import LightIntensiveSensor
from home.actuator import Light, Curtain, CoffeeMachine, Door, SmartSocket, SmartTV
from home.home_plan import home_plan, get_room_actuators

def morning_plan(home):
    print("\nExecuting Morning Plan...")
    # Open curtains
    for curtain in get_all_actuators(home, "Curtain"):
        curtain.turn_on()

    # Start coffee machine in the kitchen
    kitchen_actuators = get_room_actuators(home, "Kitchen")
    coffee_machine = next((a for a in kitchen_actuators if isinstance(a, CoffeeMachine)), None)
    if coffee_machine:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")

    # Check light conditions and turn on lights if necessary
    for sensor in get_all_sensors(home, "LightIntensive"):
        sensor.turn_on()
        if sensor.get_reading() < 900:
            for light in get_all_actuators(home, "Light"):
                light.turn_on()
                light.set_brightness_level("medium")

def leave_home_plan(home):
    print("\nExecuting Leave Home Plan...")
    # Lock doors
    for door in get_all_actuators(home, "Door"):
        door.lock()

    # Turn off lights
    for light in get_all_actuators(home, "Light"):
        light.turn_off()

    # Turn off all smart sockets
    for socket in get_all_actuators(home, "SmartSocket"):
        socket.turn_off()

def movie_plan(home):
    print("\nExecuting Movie Plan...")
    # Close curtains
    for curtain in get_all_actuators(home, "Curtain"):
        curtain.turn_off()

    # Dim lights
    for light in get_all_actuators(home, "Light"):
        light.turn_on()
        light.set_brightness_level("low")

    # Turn on TV and play movie
    for tv in get_all_actuators(home, "SmartTV"):
        tv.turn_on()
        tv.play_channel("Movie")

def main():
    home = home_plan()
    # Uncomment the plan you want to execute
    # morning_plan(home)
    # leave_home_plan(home)
    # movie_plan(home)

if __name__ == "__main__":
    main()
# ```
# 
# ### Command to Run the Script
# 
# To run this script in a Linux terminal, navigate to the directory containing your `home` folder and `smart_home.py`, then execute the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# ### Explanation
# 
# 1. **Morning Plan**: This plan opens the curtains, starts the coffee machine, and turns on the lights if the light intensity is below a certain threshold.
# 2. **Leave Home Plan**: This plan locks all doors, turns off all lights, and cuts power to all smart sockets.
# 3. **Movie Plan**: This plan closes the curtains, dims the lights, and turns on the TV to play a movie.
# 
# ### Notes
# 
# - Make sure the `home` folder is in the same directory as `smart_home.py`.
# - You can uncomment the relevant function call in the `main()` function to execute the desired plan.
# - You can further expand this script by adding more plans or customizing the existing ones as needed.