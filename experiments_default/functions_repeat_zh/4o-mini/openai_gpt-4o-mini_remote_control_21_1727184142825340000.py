# Below is the `function.py` file that corresponds to your functional description of controlling various smart home devices. This file creates a main function that integrates the functionalities of the existing modules to fulfill your request:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH
from home.actuator import Light, MusicPlayer, CoffeeMachine, AC, Curtain, CleaningRobot
from home.sensor import IndoorTemperatureSensor

def main():
    # Create the home layout
    home = home_plan()

    # Define the room where the actions will take place
    living_room = next((room for room in home if room.name == "LivingRoom"), None)

    if living_room:
        # Turn on the lights and set to medium brightness
        light = next((actuator for actuator in living_room.actuators if isinstance(actuator, Light)), None)
        if light:
            light.turn_on()
            light.set_brightness_level("medium")

        # Play a relaxing song
        music_player = next((actuator for actuator in living_room.actuators if isinstance(actuator, MusicPlayer)), None)
        if music_player:
            music_player.turn_on()
            music_player.play_music("Relaxing Playlist")

        # Make a cup of coffee
        coffee_machine = next((actuator for actuator in living_room.actuators if isinstance(actuator, CoffeeMachine)), None)
        if coffee_machine:
            coffee_machine.turn_on()
            coffee_machine.make_coffee("Espresso")

        # Adjust the air conditioning
        ac = next((actuator for actuator in living_room.actuators if isinstance(actuator, AC)), None)
        if ac:
            ac.turn_on()
            ac.set_target_temperature(22)

        # Close the curtains
        curtain = next((actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)), None)
        if curtain:
            curtain.turn_on()  # Assuming turning on closes the curtains

        # Start the cleaning robot
        cleaning_robot = next((actuator for actuator in living_room.actuators if isinstance(actuator, CleaningRobot)), None)
        if cleaning_robot:
            cleaning_robot.turn_on()
            cleaning_robot.daily_routine()

    else:
        print("Living Room not found in home plan.")

if __name__ == "__main__":
    main()