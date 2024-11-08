# Based on your functional description and the provided source code, I will create the `function.py` file for your smart home project. This file will contain a `main` function that implements the energy-saving mode by controlling the various smart devices as specified.
# 
# Here's the implementation of the `function.py` file:

# function.py

from home.home_plan import home_plan
from home.sensor import HumiditySensor, LightIntensiveSensor
from home.actuator import Light, Curtain, SmartSocket, Humidifier, CleaningRobot, MusicPlayer, SmartTV

def activate_energy_saving_mode(home):
    for room in home:
        # Dim lights
        lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
        for light in lights:
            light.set_brightness_level("low")
            light.turn_on()
        
        # Close curtains
        curtains = [actuator for actuator in room.actuators if isinstance(actuator, Curtain)]
        for curtain in curtains:
            curtain.turn_on()  # Assuming turning on means closing
        
        # Shut off unused sockets
        sockets = [actuator for actuator in room.actuators if isinstance(actuator, SmartSocket)]
        for socket in sockets:
            socket.turn_off()
        
        # Stop humidifiers
        humidifiers = [actuator for actuator in room.actuators if isinstance(actuator, Humidifier)]
        for humidifier in humidifiers:
            humidifier.turn_off()
        
        # Return sweeping robots
        cleaning_robots = [actuator for actuator in room.actuators if isinstance(actuator, CleaningRobot)]
        for robot in cleaning_robots:
            robot.turn_off()  # Assuming we stop the robot
        
        # Turn off music
        music_players = [actuator for actuator in room.actuators if isinstance(actuator, MusicPlayer)]
        for player in music_players:
            player.turn_off()
        
        # Turn on TV energy-saving mode
        tvs = [actuator for actuator in room.actuators if isinstance(actuator, SmartTV)]
        for tv in tvs:
            tv.turn_on()  # Assuming turning on means setting to energy-saving mode

def main():
    home = home_plan()  # Load the home plan
    activate_energy_saving_mode(home)  # Activate energy-saving mode

if __name__ == "__main__":
    main()