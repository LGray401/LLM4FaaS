# Based on the provided functional description and the existing source code files, I will create the `function.py` file that implements the main function to fulfill the requirements of your smart home project.
# 
# ### `function.py`
# Here's the content of the `function.py` file:

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Light, MusicPlayer, CoffeeMachine, AC, Curtain, CleaningRobot

def main():
    # Create the home plan
    home = home_plan()

    # Define the room where the actions will take place
    living_room = get_room(home, "LivingRoom")
    kitchen = get_room(home, "Kitchen")

    if living_room:
        # Get the actuators we need
        light = next((actuator for actuator in living_room.actuators if isinstance(actuator, Light)), None)
        music_player = next((actuator for actuator in living_room.actuators if isinstance(actuator, MusicPlayer)), None)
        curtain = next((actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)), None)
        cleaning_robot = next((actuator for actuator in living_room.actuators if isinstance(actuator, CleaningRobot)), None)
        
        # Turn on the light and set brightness to medium
        if light:
            light.turn_on()
            light.set_brightness_level("medium")

        # Play a relaxing song
        if music_player:
            music_player.turn_on()
            music_player.play_music("Relaxing Playlist")

        # Move to the kitchen to operate the coffee machine and AC
        if kitchen:
            coffee_machine = next((actuator for actuator in kitchen.actuators if isinstance(actuator, CoffeeMachine)), None)
            ac = next((actuator for actuator in kitchen.actuators if isinstance(actuator, AC)), None)

            # Make a coffee
            if coffee_machine:
                coffee_machine.turn_on()
                coffee_machine.make_coffee("Espresso")

            # Set the AC to 22 degrees
            if ac:
                ac.turn_on()
                ac.set_target_temperature(22)

        # Close the curtains
        if curtain:
            curtain.turn_on()

        # Start the cleaning robot
        if cleaning_robot:
            cleaning_robot.turn_on()
            cleaning_robot.daily_routine()

if __name__ == "__main__":
    main()