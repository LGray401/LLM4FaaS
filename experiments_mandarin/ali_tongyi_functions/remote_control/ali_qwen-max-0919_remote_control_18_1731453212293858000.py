# Based on your functional description and the provided source code, I will create a `function.py` file that contains a main function to turn on the lights in a specified room. The `function.py` will be placed in the `functions` folder, and it will use the classes and methods defined in your `sensor.py`, `actuator.py`, and `home_plan.py` files.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators

def turn_on_lights(room_name):
    """
    Turn on all the lights in the specified room.
    
    :param room_name: The name of the room where the lights should be turned on.
    """
    # Get the home plan
    home = home_plan()
    
    # Get all the actuators in the specified room
    actuators = get_room_actuators(home, room_name)
    
    if actuators is None:
        print(f"No actuators found in {room_name}.")
        return
    
    # Filter out the light actuators
    lights = [actuator for actuator in actuators if actuator.actuator_type == "Light"]
    
    if not lights:
        print(f"No lights found in {room_name}.")
        return
    
    # Turn on each light
    for light in lights:
        light.turn_on()
        print(f"Turned on {light.id} in {room_name}.")

if __name__ == "__main__":
    # Example usage: Turn on lights in the LivingRoom
    turn_on_lights("LivingRoom")