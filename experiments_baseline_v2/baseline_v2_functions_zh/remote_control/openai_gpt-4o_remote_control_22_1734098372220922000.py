# To create a smart home application in Python that satisfies your functional description, we can utilize the provided modules (`sensor.py`, `actuator.py`, `home_plan.py`, `config.py`). Based on your description in Chinese, the application should:
# 
# 1. Turn on the lights in the living room, bedroom, and bathroom.
# 2. Turn on the air conditioners in the living room and bedroom.
# 3. Turn on the heater in the bathroom.
# 4. Turn on the TV in the living room.
# 
# Let's implement a Python script named `smart_home_app.py` that uses these functionalities:
# 
# ```python
from home.home_plan import home_plan, get_room_actuators

def execute_home_automation():
    # Initialize the home plan
    home = home_plan()
    
    # List of room names and corresponding actuators to be turned on
    actions = {
        "LivingRoom": ["Light", "AC", "SmartTV"],
        "Bedroom": ["Light", "AC"],
        "Bathroom": ["Light", "Heater"]
    }
    
    # Iterate through each room and perform the actions
    for room_name, actuator_types in actions.items():
        actuators = get_room_actuators(home, room_name)
        for actuator in actuators:
            if actuator.actuator_type in actuator_types:
                actuator.turn_on()

if __name__ == "__main__":
    execute_home_automation()
# ```
# 
# ### Explanation:
# 
# - **Initialization**: The `home_plan()` function initializes the home with the predefined rooms and devices.
# 
# - **Functionality**: We define a dictionary `actions` where the keys are room names, and the values are lists of actuator types that need to be turned on in those rooms.
# 
# - **Execution**: We loop through each room, retrieve its actuators using `get_room_actuators()`, and turn on the actuators whose types match the specified ones in the `actions` dictionary.
# 
# ### Running the Application:
# 
# To run this script in a Linux terminal, navigate to the directory containing `smart_home_app.py` and use the following command:
# 
# ```bash
# python3 smart_home_app.py
# ```
# 
# Ensure that the Python environment has access to the `home` package (which should contain `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`). Adjust the import paths if necessary based on your project structure.