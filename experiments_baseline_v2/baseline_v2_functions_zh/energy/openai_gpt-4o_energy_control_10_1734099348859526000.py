# To create a smart home application based on your description "关闭空调" (which translates to "turn off the air conditioner"), we need to implement a Python script that interacts with the components provided in your reference code files. Here's how we can achieve this:
# 
# 1. **Create a Python script** that initializes the home setup using the provided `home_plan.py`, and then iterates through the actuators in each room to turn off any air conditioners.
# 
# 2. **Command to run the script**: I will also provide you with a command to execute the script in a Linux terminal.
# 
# ### Implementation
# 
# Let's create a script named `smart_home.py` that will turn off all air conditioners in the home.
# 
# #### smart_home.py
# 
# ```python
from home.home_plan import home_plan, get_all_actuators

def turn_off_air_conditioners():
    home = home_plan()  # Initialize the home plan
    acs = get_all_actuators(home, "AC")  # Get all AC actuators

    for ac in acs:
        if ac.get_status() == "on":
            ac.turn_off()
            print(f"Air conditioner in {ac.room_name} is now turned off.")
        else:
            print(f"Air conditioner in {ac.room_name} is already off.")

if __name__ == "__main__":
    turn_off_air_conditioners()
# ```
# 
# ### Explanation
# 
# - **Initialization**: The script initializes the home setup by calling `home_plan()`, which returns a list of rooms with their respective sensors and actuators.
# 
# - **Retrieve AC Actuators**: The `get_all_actuators` function is used to get all AC actuators from the home setup.
# 
# - **Turn Off ACs**: The script iterates over each AC actuator and turns it off if it is currently on. It logs a message for each AC indicating its status.
# 
# ### Command to Run the Script
# 
# To run the script in a Linux terminal, navigate to the directory containing the `smart_home.py` script and execute the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# Make sure that your `PYTHONPATH` is set to include the `home` folder, or that the script is executed in a way that it can find the `home` module containing your reference files.
# 
# This script will ensure that all air conditioners in the home are turned off, as per the functional requirement "关闭空调".