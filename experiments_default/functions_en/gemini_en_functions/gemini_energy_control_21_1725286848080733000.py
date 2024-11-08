from home.home_plan import get_room, get_room_actuators, get_all_actuators
from home.actuator import Light, SmartTV, Curtain, CleaningRobot, MusicPlayer, Humidifier, SmartSocket
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def energy_saving_mode(home):
    """
    Turns on energy-saving mode for all smart devices:

    - Dims lights
    - Closes curtains
    - Automatically shuts off unused sockets
    - Stops humidifiers
    - Returns sweeping robots
    - Turns off music
    - Turns on TV energy-saving mode
    """

    # Dim Lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()
        light.set_brightness_level("low")

    # Close Curtains
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        # Implement close logic for curtains
        print(f"Closing curtain {curtain.id}")

    # Turn Off Unused Sockets
    sockets = get_all_actuators(home, "SmartSocket")
    for socket in sockets:
        # Implement logic to identify and turn off unused sockets
        print(f"Turning off smart socket {socket.id}")

    # Stop Humidifiers
    humidifiers = get_all_actuators(home, "Humidifier")
    for humidifier in humidifiers:
        humidifier.turn_off()
        print(f"Turning off humidifier {humidifier.id}")

    # Return Sweeping Robots
    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    for robot in cleaning_robots:
        robot.turn_off()
        print(f"Returning cleaning robot {robot.id}")

    # Turn Off Music
    music_players = get_all_actuators(home, "MusicPlayer")
    for player in music_players:
        player.turn_off()
        print(f"Turning off music player {player.id}")

    # Turn On TV Energy-Saving Mode
    tvs = get_all_actuators(home, "SmartTV")
    for tv in tvs:
        # Implement energy-saving mode logic for TV
        print(f"Turning on energy-saving mode for TV {tv.id}")


if __name__ == '__main__':
    # Example usage:
    home = home_plan()  # Assuming 'home_plan' function is defined in 'home.home_plan'
    energy_saving_mode(home)

# **Explanation:**

# 1. **Imports:** Import necessary modules from `home.home_plan` and `home.actuator`.
# 2. **`energy_saving_mode` function:**
#    - Takes `home` (the home plan) as input.
#    - Iterates through all actuators of each type to perform the actions:
#      - **Lights:** Turns on lights and sets them to low brightness.
#      - **Curtains:** Closes curtains (add logic based on your curtain implementation).
#      - **SmartSockets:** Turns off unused sockets (add logic to identify unused sockets).
#      - **Humidifiers:** Turns off humidifiers.
#      - **Cleaning Robots:** Returns cleaning robots.
#      - **Music Players:** Turns off music players.
#      - **Smart TVs:** Turns on energy-saving mode (add logic based on your TV implementation).

# 3. **`if __name__ == '__main__'` block:**
#    - This block is executed only when the script is run directly.
#    - It calls `home_plan()` (assuming you have this function defined in `home.home_plan`) to get the home plan.
#    - It then calls `energy_saving_mode` with the home plan to turn on energy-saving mode.

# **To Use This Code:**

# 1. **Replace Placeholders:**
#    - Add your specific logic for `close` in the curtain section.
#    - Add logic for `turn off unused sockets` in the smart socket section.
#    - Add logic for `energy-saving mode` in the Smart TV section.

# 2. **Import `home_plan` Function:**
#    - Ensure the `home_plan` function is correctly defined in your `home.home_plan` file and imported.

# 3. **Run the Script:**
#    - Run the `function.py` file to activate energy-saving mode.

# **Additional Notes:**

# - You might need to adjust the `get_all_actuators` function in `home.home_plan` to return the specific type of actuators (e.g., only lights, only curtains).
# - Consider adding more context-aware logic, such as using sensors (temperature, humidity, light intensity) to determine if certain actions are necessary (e.g., only close curtains if the sun is shining).
