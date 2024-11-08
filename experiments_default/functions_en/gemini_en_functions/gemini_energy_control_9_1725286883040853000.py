from home.home_plan import home_plan, get_all_actuators, get_all_sensors

def main():
    home = home_plan()

    # Turn off all lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

    # Turn off all water (assuming water is controlled by smart sockets)
    smart_sockets = get_all_actuators(home, "SmartSocket")
    for socket in smart_sockets:
        socket.turn_off()

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary functions:** 
#    - `home_plan` from `home.home_plan` to create the home plan and access rooms.
#    - `get_all_actuators` and `get_all_sensors` from `home.home_plan` to retrieve specific actuators and sensors.

# 2. **`main` function:**
#    - Calls `home_plan()` to create the home structure.
#    - Retrieves all lights using `get_all_actuators(home, "Light")`.
#    - Iterates through the list of lights and turns each one off using `light.turn_off()`.
#    - Retrieves all smart sockets using `get_all_actuators(home, "SmartSocket")`.
#    - Iterates through the list of smart sockets and turns each one off using `socket.turn_off()`. 
#      (This assumes that water is controlled by smart sockets).

# 3. **`if __name__ == "__main__":` block:** 
#    - Ensures that the `main` function is executed only when the script is run directly, not when imported as a module.

# **How to Use:**

# 1. Save this code as `function.py` in the `functions` folder of your project.
# 2. Make sure your `home`, `sensor`, `actuator`, and `config` modules are correctly set up.
# 3. Run `function.py` from the terminal.

# **Note:**

# This code assumes that:

# - You have defined a `SmartSocket` actuator type in your `actuator.py` file.
# - The `SmartSocket` actuator controls water-related appliances (e.g., a water heater).

# You can adjust the code to work with different actuator types or modify the logic to handle specific water appliances if needed. 
