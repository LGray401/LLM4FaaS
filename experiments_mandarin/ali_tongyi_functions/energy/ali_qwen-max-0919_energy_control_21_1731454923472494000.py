# Based on the functional description and the provided source code, I will create a `function.py` file that includes a main function to enable the "energy-saving mode" for your smart home. This mode will perform the following actions:
# - Dim the lights.
# - Close the curtains.
# - Turn off unused smart sockets.
# - Stop the humidifier.
# - Return the cleaning robot to its dock.
# - Turn off the music player.
# - Put the SmartTV in energy-saving mode.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_all_actuators
from home.actuator import Light, Curtain, SmartSocket, Humidifier, CleaningRobot, MusicPlayer, SmartTV

def set_energy_saving_mode():
    home = home_plan()
    
    # Dim the lights
    for light in get_all_actuators(home, "Light"):
        if light.status == "on":
            light.set_brightness_level("low")
    
    # Close the curtains
    for curtain in get_all_actuators(home, "Curtain"):
        if curtain.status == "on":
            curtain.turn_off()
    
    # Turn off unused smart sockets
    for socket in get_all_actuators(home, "SmartSocket"):
        if socket.status == "on":
            socket.turn_off()
    
    # Stop the humidifier
    for humidifier in get_all_actuators(home, "Humidifier"):
        if humidifier.status == "on":
            humidifier.turn_off()
    
    # Return the cleaning robot to its dock
    for robot in get_all_actuators(home, "CleaningRobot"):
        if robot.status == "on":
            robot.turn_off()
    
    # Turn off the music player
    for music_player in get_all_actuators(home, "MusicPlayer"):
        if music_player.status == "on":
            music_player.turn_off()
    
    # Put the SmartTV in energy-saving mode
    for tv in get_all_actuators(home, "SmartTV"):
        if tv.status == "on":
            tv.turn_off()

if __name__ == "__main__":
    set_energy_saving_mode()