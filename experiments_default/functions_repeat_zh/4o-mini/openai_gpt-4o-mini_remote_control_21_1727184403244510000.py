# Based on your functional description and the provided source code, I will create a `function.py` file that implements the required actions for your smart home system. This file will include a main function that orchestrates the interactions between various sensors and actuators to fulfill your requests.
# 
# Here’s the content for `function.py`:

# function.py

from home.home_plan import home_plan, get_room, get_room_actuators, get_room_sensors
from home.actuator import Light, MusicPlayer, CoffeeMachine, AC, Curtain, CleaningRobot
from home.sensor import IndoorTemperatureSensor, LightIntensiveSensor

def main():
    # Create the home plan
    home = home_plan()

    # Get the living room
    living_room = get_room(home, "LivingRoom")

    if living_room:
        # Turn on the light and set brightness to medium
        lights = get_room_actuators(home, "Light")
        for light in lights:
            light.turn_on()
            light.set_brightness_level("medium")

        # Play relaxing music
        music_players = get_room_actuators(home, "MusicPlayer")
        for music_player in music_players:
            music_player.turn_on()
            music_player.play_music("Relaxing Playlist")

        # Make coffee
        coffee_machines = get_room_actuators(home, "CoffeeMachine")
        for coffee_machine in coffee_machines:
            coffee_machine.turn_on()
            coffee_machine.make_coffee("Espresso")

        # Control the AC to set temperature to 22°C
        ac_units = get_room_actuators(home, "AC")
        for ac in ac_units:
            ac.turn_on()
            ac.set_target_temperature(22)

        # Close the curtains
        curtains = get_room_actuators(home, "Curtain")
        for curtain in curtains:
            curtain.turn_on()  # Assuming this opens or closes the curtain appropriately

        # Start the cleaning robot
        cleaning_robots = get_room_actuators(home, "CleaningRobot")
        for robot in cleaning_robots:
            robot.turn_on()
            robot.daily_routine()

if __name__ == "__main__":
    main()