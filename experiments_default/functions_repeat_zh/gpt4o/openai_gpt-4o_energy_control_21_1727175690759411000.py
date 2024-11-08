# Based on the provided functional description and the source code files, I'll create a `functions/function.py` file that contains the main function to activate energy-saving mode as described. Here is the `function.py` file:

from home.home_plan import home_plan, get_all_actuators

def activate_energy_saving_mode(home):
    # Set all lights to dim mode
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()
        light.set_brightness_level("low")

    # Close all curtains
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()  # Assuming the curtain actuator needs to be turned on to operate
        curtain.turn_off()  # Assuming turning off means closing the curtains

    # Turn off unused smart sockets
    sockets = get_all_actuators(home, "SmartSocket")
    for socket in sockets:
        socket.turn_off()

    # Stop humidifiers
    humidifiers = get_all_actuators(home, "Humidifier")
    for humidifier in humidifiers:
        humidifier.turn_off()

    # Return cleaning robot to its dock
    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    for robot in cleaning_robots:
        robot.turn_off()  # Assuming turning off means sending it back to the dock

    # Turn off music
    music_players = get_all_actuators(home, "MusicPlayer")
    for player in music_players:
        player.turn_off()

    # Set TV to energy-saving mode
    smart_tvs = get_all_actuators(home, "SmartTV")
    for tv in smart_tvs:
        tv.turn_on()  # Assuming turning on is necessary to set energy-saving mode
        # Implementation to set energy-saving mode can be added here

def main():
    home = home_plan()
    activate_energy_saving_mode(home)

if __name__ == "__main__":
    main()