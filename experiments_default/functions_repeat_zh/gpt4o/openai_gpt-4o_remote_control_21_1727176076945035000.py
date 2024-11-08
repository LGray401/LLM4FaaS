# Based on the functional description and the given source code files, we need to create a `function.py` file in the `functions` folder. This file will include the main function that performs the actions described in the functional description. Here's the `functions/function.py` file:

from home.home_plan import home_plan, get_room_actuators

def main():
    home = home_plan()

    # Find actuators in the LivingRoom
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    # Find specific actuators
    light = next((a for a in living_room_actuators if a.actuator_type == "Light"), None)
    music_player = next((a for a in living_room_actuators if a.actuator_type == "MusicPlayer"), None)
    coffee_machine = next((a for a in living_room_actuators if a.actuator_type == "CoffeeMachine"), None)
    ac = next((a for a in living_room_actuators if a.actuator_type == "AC"), None)
    curtain = next((a for a in living_room_actuators if a.actuator_type == "Curtain"), None)
    cleaning_robot = next((a for a in living_room_actuators if a.actuator_type == "CleaningRobot"), None)

    # Perform actions
    if light:
        light.turn_on()
        light.set_brightness_level("medium")
    
    if music_player:
        music_player.turn_on()
        music_player.play_music("Relaxing Playlist")
    
    if coffee_machine:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")
    
    if ac:
        ac.turn_on()
        ac.set_target_temperature(22)
    
    if curtain:
        curtain.turn_off()  # Assuming turning it off means closing the curtain
    
    if cleaning_robot:
        cleaning_robot.turn_on()
        cleaning_robot.daily_routine()

if __name__ == "__main__":
    main()