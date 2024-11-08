# Based on your request for a smart home application that can be run in a Linux terminal, I'll create a Python script that utilizes the provided source code files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) to fulfill the functional description "请关闭不必要的开关" (which translates to "Please turn off unnecessary switches").
# 
# This script will iterate through all actuators in your home and turn off any that are currently on. Let's create a script called `smart_home.py` in the `home` folder:
# 
# ### smart_home.py
# ```python
from home.home_plan import home_plan

def main():
    # Get the home plan which includes all rooms, sensors, and actuators
    home = home_plan()

    # Iterate over each room
    for room in home:
        # Check each actuator in the room
        for actuator in room.actuators:
            # If an actuator is currently on, turn it off
            if actuator.get_status() == "on":
                actuator.turn_off()

if __name__ == "__main__":
    main()
# ```
# 
# ### Instructions to Run the Script
# 
# 1. **Ensure the `home` folder contains**:
#    - `sensor.py`
#    - `actuator.py`
#    - `home_plan.py`
#    - `config.py`
#    - `smart_home.py` (the script we just created)
# 
# 2. **Navigate to the directory** containing the `home` folder in your Linux terminal.
# 
# 3. **Run the script** using Python:
#    ```bash
#    python3 home/smart_home.py
#    ```
# 
# This script will initialize your smart home environment, iterate over all actuators in each room, and turn off any that are currently on, hence addressing the functional description you provided. The output will display which actuators were turned off. Make sure you have logging properly set up if you want detailed logs.