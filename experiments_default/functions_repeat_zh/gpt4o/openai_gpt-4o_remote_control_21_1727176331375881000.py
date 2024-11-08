# Sure, I can help you create the `function.py` file based on the provided functional description and the source code of the other files in your project. Here is the `function.py` file that you can place in the `functions` folder:

from home.home_plan import home_plan, get_room_actuators

def main():
    home = home_plan()

    # Get actuators for the Living Room
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Dictionary to quickly access actuators by type
    actuator_dict = {actuator.actuator_type: actuator for actuator in living_room_actuators}

    # Step 1: Turn on the Light and set to medium brightness
    if 'Light' in actuator_dict:
        light = actuator_dict['Light']
        light.turn_on()
        light.set_brightness_level('medium')

    # Step 2: Play a stress-relieving song on the Music Player
    if 'MusicPlayer' in actuator_dict:
        music_player = actuator_dict['MusicPlayer']
        music_player.turn_on()
        music_player.play_music('relaxing_playlist')

    # Step 3: Make a cup of coffee using the Coffee Machine
    if 'CoffeeMachine' in actuator_dict:
        coffee_machine = actuator_dict['CoffeeMachine']
        coffee_machine.turn_on()
        coffee_machine.make_coffee('espresso')

    # Step 4: Turn on the AC and set temperature to 22 degrees
    if 'AC' in actuator_dict:
        ac = actuator_dict['AC']
        ac.turn_on()
        ac.set_target_temperature(22)

    # Step 5: Close the Curtains
    if 'Curtain' in actuator_dict:
        curtain = actuator_dict['Curtain']
        curtain.turn_on()

    # Step 6: Start the Cleaning Robot
    if 'CleaningRobot' in actuator_dict:
        cleaning_robot = actuator_dict['CleaningRobot']
        cleaning_robot.turn_on()
        cleaning_robot.daily_routine()

if __name__ == "__main__":
    main()