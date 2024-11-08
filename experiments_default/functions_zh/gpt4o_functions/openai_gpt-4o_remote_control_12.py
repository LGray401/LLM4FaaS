# Sure, based on your functional description "开窗户" (which means "open the window"), I will create a `function.py` file that will be placed in the 'functions' folder. This file will contain a main function that will control the window actuators based on certain conditions.
# 
# Here is the `function.py`:

# function.py
from home.home_plan import home_plan, get_room_actuators
from home.config import TEMP_HIGH

def open_window(room_name):
    home = home_plan()
    room_actuators = get_room_actuators(home, room_name)
    
    if room_actuators:
        for actuator in room_actuators:
            if actuator.actuator_type == "Window":
                actuator.turn_on()
                print(f"Window in {room_name} is now opened.")
                return
    print(f"No window found in {room_name}.")

# Main function
def main():
    room_name = "LivingRoom"
    open_window(room_name)

if __name__ == "__main__":
    main()