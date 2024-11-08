# To create a smart home application based on your functional description and the provided source code, we will implement a script that initializes the home plan and turns off all lights and water sources. Based on the available code, it seems that the water sources are not directly represented, but we will assume that any additional code managing water sources can be implemented in a similar fashion to the existing code for lights.
# 
# Here is the implementation of the main application script:
# 
# ```python
# main.py
from home.home_plan import home_plan, get_all_actuators

def main():
    # Initialize the home plan
    my_home = home_plan()

    # Turn off all lights
    lights = get_all_actuators(my_home, 'Light')
    for light in lights:
        light.turn_off()

    # Turn off all water sources
    # Assuming we have a similar actuator for water sources, e.g., 'WaterSource'
    water_sources = get_all_actuators(my_home, 'WaterSource')
    for water_source in water_sources:
        water_source.turn_off()

if __name__ == "__main__":
    main()
# ```
# 
# ### Running the Application
# 
# To run this application in a Linux terminal, ensure the following:
# 
# 1. Your Python environment is set up correctly.
# 2. The directory structure is as follows:
#    ```
#    └── home/
#        ├── sensor.py
#        ├── actuator.py
#        ├── home_plan.py
#        ├── config.py
#    └── main.py
#    ```
# 
# 3. From the terminal, navigate to the directory containing `main.py` and run:
# 
# ```bash
# python3 main.py
# ```
# 
# ### Assumptions and Notes
# 
# - **Water Sources**: If water sources are not implemented, you need to create a class similar to `Light` under `actuator.py` for water sources (e.g., `WaterSource`) and modify the function call `get_all_actuators(my_home, 'WaterSource')`.
# - **Logger Configuration**: Ensure that the `logger_config` module is available. The code references a `logger` which is not provided in the snippets above.
# - **Dependencies**: Ensure all dependencies and Python modules are installed and available in your Python environment.
# 
# This script accomplishes the task described: turning off all lights and water sources in a simulated smart home environment.