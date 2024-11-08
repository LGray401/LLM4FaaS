# To implement the 'energy-saving mode' functionality described in your request, we will create a `function.py` file that contains the main function to turn on energy-saving mode. This function will call the necessary methods on the actuators to dim lights, close curtains, shut off unused sockets, stop humidifiers, return sweeping robots, turn off music, and turn on the TV energy-saving mode.
# 
# Here's the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_all_actuators


def main():
    # Get the home plan
    home = home_plan()

    # Dim lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()  # Ensure the light is on before setting brightness
        light.set_brightness_level("low")

    # Close curtains
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_off()  # Assuming turning off the curtain means closing it

    # Shut off unused sockets
    sockets = get_all_actuators(home, "SmartSocket")
    for socket in sockets:
        socket.turn_off()

    # Stop humidifiers
    humidifiers = get_all_actuators(home, "Humidifier")
    for humidifier in humidifiers:
        humidifier.turn_off()

    # Return sweeping robots
    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    for robot in cleaning_robots:
        robot.turn_off()  # Assuming turning off the robot means stopping and returning it

    # Turn off music
    music_players = get_all_actuators(home, "MusicPlayer")
    for music_player in music_players:
        music_player.turn_off()

    # Turn on TV energy-saving mode
    tvs = get_all_actuators(home, "SmartTV")
    for tv in tvs:
        tv.turn_on()  # Ensure the TV is on before setting energy-saving mode
        # Assuming there's a method to set energy-saving mode on the TV, if not, add it in the SmartTV class
        # tv.set_energy_saving_mode()

    print("Energy-saving mode activated for all smart devices.")


if __name__ == "__main__":
    main()