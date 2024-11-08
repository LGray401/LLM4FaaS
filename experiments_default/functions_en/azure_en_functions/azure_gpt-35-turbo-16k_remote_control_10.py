# Sure! I have created the 'function.py' file for your smart home project. Here is the code:

from home.home_plan import home_plan, get_room_actuators

def open_windows():
    home = home_plan()
    actuators = get_room_actuators(home, "LivingRoom")
    
    for actuator in actuators:
        if actuator.actuator_type == "Window":
            actuator.turn_on()
            print(f"Opened window {actuator.id}")

if __name__ == "__main__":
    open_windows()