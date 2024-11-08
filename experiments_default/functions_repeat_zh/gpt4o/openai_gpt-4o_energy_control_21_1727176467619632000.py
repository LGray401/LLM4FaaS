# Sure, based on your functional description, I will create the `function.py` file located in the `functions` folder. This file will contain a main function that will enable the energy-saving mode by adjusting the state of various smart devices.
# 
# Here's how the `function.py` file will look:

import sys
sys.path.append('..')  # Adjust the system path to include the parent directory

from home.home_plan import home_plan, get_all_actuators

def enable_energy_saving_mode(home):
    # Turn off unnecessary devices
    lights = get_all_actuators(home, "Light")
    curtains = get_all_actuators(home, "Curtain")
    smart_sockets = get_all_actuators(home, "SmartSocket")
    humidifiers = get_all_actuators(home, "Humidifier")
    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    music_players = get_all_actuators(home, "MusicPlayer")
    smart_tvs = get_all_actuators(home, "SmartTV")

    for light in lights:
        light.turn_on()
        light.set_brightness_level("low")

    for curtain in curtains:
        curtain.turn_off()

    for smart_socket in smart_sockets:
        smart_socket.turn_off()

    for humidifier in humidifiers:
        humidifier.turn_off()

    for cleaning_robot in cleaning_robots:
        cleaning_robot.turn_off()

    for music_player in music_players:
        music_player.turn_off()

    for smart_tv in smart_tvs:
        smart_tv.turn_on()
        print(f"{smart_tv.id} is now in energy-saving mode.")
        
    print("Energy-saving mode enabled.")

def main():
    home = home_plan()
    enable_energy_saving_mode(home)

if __name__ == "__main__":
    main()