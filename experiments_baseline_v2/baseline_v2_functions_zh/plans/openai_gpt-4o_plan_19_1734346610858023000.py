# To create a smart home application based on your functional description and the provided reference code files, we need to implement the plans for different activities (MORNING PLAN, LEAVE HOME PLAN, MOVIE PLAN) using the existing sensor and actuator classes. Let's start by writing the smart home application in a new file named `smart_home.py`.
# 
# ### `smart_home.py`
# 
# ```python
from home.home_plan import home_plan, get_room_actuators

def morning_plan(home):
    print("Executing Morning Plan: Opening curtains and making coffee.")
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    kitchen_actuators = get_room_actuators(home, "Kitchen")

    # Open curtains in the bedroom
    for actuator in bedroom_actuators:
        if actuator.actuator_type == "Curtain":
            actuator.turn_on()
    
    # Make coffee in the kitchen
    for actuator in kitchen_actuators:
        if actuator.actuator_type == "CoffeeMachine":
            actuator.turn_on()
            actuator.make_coffee("espresso")

def leave_home_plan(home):
    print("Executing Leave Home Plan: Lock doors and turn off all power.")
    for room in home:
        for actuator in room.actuators:
            if actuator.actuator_type == "Door":
                actuator.lock()
            elif actuator.actuator_type in ["Light", "AC", "Heater", "MusicPlayer", "SmartTV", "SmartSocket"]:
                actuator.turn_off()

def movie_plan(home):
    print("Executing Movie Plan: Prepare the living room for movie watching.")
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    for actuator in living_room_actuators:
        if actuator.actuator_type == "Light":
            actuator.turn_on()
            actuator.set_brightness_level("low")
        elif actuator.actuator_type == "SmartTV":
            actuator.turn_on()
            actuator.play_channel("Netflix")
        elif actuator.actuator_type == "Curtain":
            actuator.turn_off()

def main():
    home = home_plan()
    
    # Execute plans (you can uncomment the plan you want to execute)
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()
# ```
# 
# ### Running the Application
# 
# To run this application in a Linux terminal, save the above code in a file named `smart_home.py` in the same directory where your `home` folder is located. Then execute the following command in your terminal:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# ### Explanation
# 
# - **Morning Plan**: The system will open the curtains in the bedroom and make coffee in the kitchen.
# - **Leave Home Plan**: The system will lock all doors and turn off all power-consuming devices like lights, AC, heaters, music players, smart TVs, and smart sockets.
# - **Movie Plan**: The system will prepare the living room by dimming the lights, turning on the smart TV to play a channel, and closing the curtains for a movie-like ambiance.
# 
# Each plan uses the sensors and actuators from the `home_plan.py` setup, demonstrating how you can interact with the components in different scenarios. Adjustments can be made to the plans as needed.