# Based on the functional description and the provided source code, I will create a `function.py` file for your smart home project. The `function.py` will contain a `main` function that will initiate the节能模式 based on the description.
# 
# Here's the content for the `function.py` file:

# function.py

from home.sensor import Sensor
from home.actuator import Actuator
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.logger_config import logger

def turn_off_all_lights():
    for light in get_all_actuators(home_plan(), "Light"):
        light.turn_off()

def close_all_curtains():
    for curtain in get_all_actuators(home_plan(), "Curtain"):
        curtain.turn_off()

def turn_off_all_sockets():
    for socket in get_all_actuators(home_plan(), "SmartSocket"):
        socket.turn_off()

def stop_humidifier():
    for humidifier in get_all_actuators(home_plan(), "Humidifier"):
        humidifier.turn_off()

def stop_cleaning_robot():
    for cleaning_robot in get_all_actuators(home_plan(), "CleaningRobot"):
        cleaning_robot.turn_off()

def stop_music_player():
    for music_player in get_all_actuators(home_plan(), "MusicPlayer"):
        music_player.turn_off()

def set_tv_to_energy_saving_mode():
    for tv in get_all_actuators(home_plan(), "SmartTV"):
        tv.turn_off()

def main():
    # Implement the energy-saving mode based on the description
    turn_off_all_lights()
    close_all_curtains()
    turn_off_all_sockets()
    stop_humidifier()
    stop_cleaning_robot()
    stop_music_player()
    set_tv_to_energy_saving_mode()
    logger.info("Energy-saving mode initiated successfully.")

if __name__ == "__main__":
    main()