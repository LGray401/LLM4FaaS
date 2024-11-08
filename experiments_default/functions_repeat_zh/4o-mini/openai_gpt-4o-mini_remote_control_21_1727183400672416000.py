# Based on your functional description and the provided source code, I'll create a `function.py` file that implements the main functionality of your smart home project. This file will orchestrate the actions specified in your request: turning on the light with a medium brightness, playing a relaxing song, brewing coffee, setting the air conditioning to 22°C, closing the curtains, and starting the cleaning robot.
# 
# Here's the content for `functions/function.py`:

from home.home_plan import home_plan, get_room, get_room_actuators, get_room_sensors
from home.logger_config import logger
from home.config import TEMP_LOW, TEMP_HIGH

def main():
    # Initialize home and retrieve the rooms
    home = home_plan()
    
    # Define the room names
    living_room_name = "LivingRoom"
    bedroom_name = "Bedroom"

    # Get the Living Room
    living_room = get_room(home, living_room_name)

    if living_room:
        # Turn on the light and set it to medium brightness
        light_actors = get_room_actuators(home, living_room_name)
        for actor in light_actors:
            if isinstance(actor, Light):
                actor.turn_on()
                actor.set_brightness_level("medium")
        
        # Play a relaxing song
        music_player = next((actor for actor in light_actors if isinstance(actor, MusicPlayer)), None)
        if music_player:
            music_player.turn_on()
            music_player.play_music("Relaxing Playlist")

        # Brew coffee
        coffee_machine = next((actor for actor in light_actors if isinstance(actor, CoffeeMachine)), None)
        if coffee_machine:
            coffee_machine.turn_on()
            coffee_machine.make_coffee("Espresso")

        # Set the AC to 22°C
        ac = next((actor for actor in light_actors if isinstance(actor, AC)), None)
        if ac:
            ac.turn_on()
            ac.set_target_temperature(22)

        # Close the curtains
        curtain_actors = get_room_actuators(home, living_room_name)
        for actor in curtain_actors:
            if isinstance(actor, Curtain):
                actor.turn_on()  # Assuming turn_on closes the curtain

        # Start the cleaning robot
        cleaning_robot = next((actor for actor in light_actors if isinstance(actor, CleaningRobot)), None)
        if cleaning_robot:
            cleaning_robot.turn_on()
            cleaning_robot.daily_routine()

    else:
        logger.error("Living room not found.")

if __name__ == "__main__":
    main()