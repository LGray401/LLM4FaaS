# Based on your functional description and the provided code files, I'll create the `function.py` file located in the `functions` folder with a main function that implements the energy-saving mode. The main function will perform the following actions:
# 
# 1. Dim the lights.
# 2. Close the curtains.
# 3. Turn off unnecessary smart sockets.
# 4. Stop the humidifier.
# 5. Return the cleaning robot to its dock.
# 6. Turn off the music.
# 7. Put the TV into energy-saving mode.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_all_actuators

def energy_saving_mode():
    home = home_plan()

    # Dim the lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()
        light.set_brightness_level("low")

    # Close the curtains
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

    # Turn off unnecessary smart sockets
    smart_sockets = get_all_actuators(home, "SmartSocket")
    for socket in smart_sockets:
        socket.turn_off()

    # Stop the humidifiers
    humidifiers = get_all_actuators(home, "Humidifier")
    for humidifier in humidifiers:
        humidifier.turn_off()

    # Return the cleaning robots to dock
    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    for robot in cleaning_robots:
        robot.turn_off()

    # Turn off the music
    music_players = get_all_actuators(home, "MusicPlayer")
    for music_player in music_players:
        music_player.turn_off()

    # Put the TV into energy-saving mode
    smart_tvs = get_all_actuators(home, "SmartTV")
    for tv in smart_tvs:
        tv.turn_on()
        # Assuming energy-saving mode is equivalent to turning it on with minimal usage
        tv.turn_off()

    print("Energy-saving mode has been activated for all devices.")

if __name__ == "__main__":
    energy_saving_mode()