# Based on your functional description and provided source code, I'll create a `function.py` file to enable the energy-saving mode as described. This file will be located in the `functions` folder and will contain the main function to execute the required operations.
# 
# Here's your `function.py`:

# functions/function.py

from home.home_plan import home_plan, get_all_actuators

def energy_saving_mode():
    home = home_plan()

    # Get all the actuators based on their types
    lights = get_all_actuators(home, "Light")
    curtains = get_all_actuators(home, "Curtain")
    smart_sockets = get_all_actuators(home, "SmartSocket")
    humidifiers = get_all_actuators(home, "Humidifier")
    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    music_players = get_all_actuators(home, "MusicPlayer")
    smart_tvs = get_all_actuators(home, "SmartTV")

    # Set all lights to dim (low brightness)
    for light in lights:
        light.turn_on()
        light.set_brightness_level("low")

    # Close all curtains
    for curtain in curtains:
        curtain.turn_on()
        curtain.turn_off()

    # Turn off unused smart sockets
    for socket in smart_sockets:
        socket.turn_off()

    # Turn off all humidifiers
    for humidifier in humidifiers:
        humidifier.turn_off()

    # Return all cleaning robots to their docks
    for robot in cleaning_robots:
        robot.turn_off()

    # Turn off all music players
    for music_player in music_players:
        music_player.turn_off()

    # Set all TVs to energy-saving mode
    for tv in smart_tvs:
        tv.turn_on()
        tv.turn_off()

    print("Energy saving mode activated.")

if __name__ == "__main__":
    energy_saving_mode()