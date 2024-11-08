# Based on your functional description and the provided source code, I'll create a `function.py` file that will contain the main function. This main function will follow your instructions: "turn on the air conditioner at home, adjust the temperature to 17 degrees, set the upper and lower blowing modes, and then turn on the living room light."
# 
# Here's the `function.py`:

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_actuators

def main():
    # Initialize home plan
    home = home_plan()
    
    # Find living room
    living_room = get_room(home, "LivingRoom")
    if not living_room:
        print("Living room not found!")
        return
    
    # Find AC and Light in living room
    ac = None
    living_room_light = None
    
    for actuator in living_room.actuators:
        if actuator.actuator_type == "AC":
            ac = actuator
        elif actuator.actuator_type == "Light":
            living_room_light = actuator

    if not ac:
        print("No AC found in the living room!")
        return
    
    if not living_room_light:
        print("No Light found in the living room!")
        return
    
    # Turn on AC and set temperature
    ac.turn_on()
    ac.set_target_temperature(17)
    
    # Assuming "set the upper and lower blowing modes" refers to some predefined modes
    # Since there is no functionality provided for blowing modes in the AC class,
    # we assume that turning on the AC and setting the temperature suffices.
    
    # Turn on the living room light
    living_room_light.turn_on()

if __name__ == "__main__":
    main()