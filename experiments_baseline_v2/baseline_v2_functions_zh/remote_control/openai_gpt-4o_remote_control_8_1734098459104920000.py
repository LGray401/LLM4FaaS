# To implement the functional description provided, "你好机器人，请把家里的空调打开，温度调成17度，上下吹风模式，再把客厅灯打开," we will write a Python script that utilizes the provided reference files. We'll assume the reference files are in the `home` folder as mentioned.
# 
# Here's how we can break down the task:
# 
# 1. **Turn on the air conditioner (AC) and set the temperature to 17 degrees.**
# 2. **Turn on the living room light.**
# 
# We will create a script named `smart_home.py` which will interact with the classes and methods provided in the reference files to accomplish these tasks.
# 
# ### `smart_home.py`
# 
# ```python
from home.home_plan import home_plan, get_room_actuators

def main():
    # Initialize home plan
    home = home_plan()
    
    # Step 1: Turn on the air conditioner (AC) in the home and set it to 17 degrees
    acs = get_room_actuators(home, "LivingRoom")
    
    for actuator in acs:
        if isinstance(actuator, AC):
            actuator.turn_on()
            actuator.set_target_temperature(17)
            print("AC in the home is turned on and set to 17 degrees.")
            break
    else:
        print("No AC found in the home.")
    
    # Step 2: Turn on the living room light
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()
            print("Living room light is turned on.")
            break
    else:
        print("No light found in the living room.")

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# - **`home_plan()`** initializes the home with defined rooms and their components.
# - **`get_room_actuators()`** is used to fetch the actuators in a specific room, such as the living room.
# - For the air conditioner (AC), we call `turn_on()` and `set_target_temperature(17)`.
# - Similarly, we find the light actuator in the living room and turn it on.
# 
# ### Running the Script
# You can run the script from a Linux terminal using the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# Ensure that the `home` folder containing the reference files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) is in the same directory as `smart_home.py`, or update the import paths accordingly if they are located elsewhere.