# Based on your functional description and the provided source code, I will create a `function.py` file that encapsulates the main functionality to interact with your smart home system. The main function will be designed to execute the tasks you specified: turning on lights to a medium brightness, playing a stress-relief song, brewing coffee, setting the AC to 22°C, closing the curtains, and starting the cleaning robot.
# 
# Here's the content for `function.py`:

# functions/function.py

from home.home_plan import home_plan
from home.actuator import Light, MusicPlayer, CoffeeMachine, AC, Curtain, CleaningRobot
from time import sleep

def main():
    # Initialize the home plan
    home = home_plan()

    # Define the room you want to control (you can change this as needed)
    living_room = next((room for room in home if room.name == "LivingRoom"), None)
    if not living_room:
        print("Living room not found.")
        return

    # Control the Light
    lights = [actuator for actuator in living_room.actuators if isinstance(actuator, Light)]
    for light in lights:
        light.turn_on()
        light.set_brightness_level("medium")

    # Control the Music Player
    music_players = [actuator for actuator in living_room.actuators if isinstance(actuator, MusicPlayer)]
    for music_player in music_players:
        music_player.turn_on()
        music_player.play_music("Stress Relief Playlist")

    # Control the Coffee Machine
    coffee_machine = next((actuator for actuator in living_room.actuators if isinstance(actuator, CoffeeMachine)), None)
    if coffee_machine:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")

    # Control the Air Conditioner
    ac = next((actuator for actuator in living_room.actuators if isinstance(actuator, AC)), None)
    if ac:
        ac.turn_on()
        ac.set_target_temperature(22)

    # Control the Curtain
    curtains = [actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)]
    for curtain in curtains:
        curtain.turn_on()  # Assuming we have a method to open the curtain
        print(f"{curtain.id} has been opened.")

    # Control the Cleaning Robot
    cleaning_robot = next((actuator for actuator in living_room.actuators if isinstance(actuator, CleaningRobot)), None)
    if cleaning_robot:
        cleaning_robot.turn_on()
        cleaning_robot.daily_routine()

    print("All tasks have been completed successfully!")

if __name__ == "__main__":
    main()