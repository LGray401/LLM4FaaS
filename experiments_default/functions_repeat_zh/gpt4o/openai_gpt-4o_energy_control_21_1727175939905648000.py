# Sure! Based on the functional description and given code files, I will create the `function.py` file inside the `functions` folder. The `function.py` will contain the main function that implements the energy-saving mode as described.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_all_actuators

def enable_energy_saving_mode(home):
    # Adjust lights to dim setting
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()
        light.set_brightness_level("low")

    # Close all curtains
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

    # Turn off unused smart sockets
    smart_sockets = get_all_actuators(home, "SmartSocket")
    for socket in smart_sockets:
        socket.turn_off()

    # Stop humidifiers
    humidifiers = get_all_actuators(home, "Humidifier")
    for humidifier in humidifiers:
        humidifier.turn_off()

    # Return cleaning robots to their docking stations
    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    for robot in cleaning_robots:
        robot.turn_off()

    # Turn off music players
    music_players = get_all_actuators(home, "MusicPlayer")
    for music_player in music_players:
        music_player.turn_off()

    # Enable energy-saving mode on TVs
    smart_tvs = get_all_actuators(home, "SmartTV")
    for tv in smart_tvs:
        tv.turn_on()  # Assuming turning on the TV will enable energy-saving mode by default

def main():
    # Create home plan
    home = home_plan()
    
    # Enable energy-saving mode
    enable_energy_saving_mode(home)

if __name__ == "__main__":
    main()