# Based on your functional description and the provided source code, here is the `function.py` file that contains the main functions to execute the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN:

from home.home_plan import home_plan, get_room, get_all_actuators
from home.actuator import MusicPlayer, SmartSocket, Curtain

def morning_plan(home):
    # Play music in the LivingRoom
    room = get_room(home, "LivingRoom")
    if room:
        music_players = [actuator for actuator in room.actuators if isinstance(actuator, MusicPlayer)]
        if music_players:
            music_players[0].turn_on()
            music_players[0].play_music("morning playlist")
        else:
            print("No MusicPlayer found in LivingRoom.")
    else:
        print("LivingRoom not found.")

def leave_home_plan(home):
    # Turn off all SmartSockets in the home
    smart_sockets = get_all_actuators(home, "SmartSocket")
    for socket in smart_sockets:
        socket.turn_off()

def movie_plan(home):
    # Open curtains in the LivingRoom
    room = get_room(home, "LivingRoom")
    if room:
        curtains = [actuator for actuator in room.actuators if isinstance(actuator, Curtain)]
        if curtains:
            curtains[0].turn_on()  # Assuming turn_on() opens the curtains
        else:
            print("No Curtain found in LivingRoom.")
    else:
        print("LivingRoom not found.")

if __name__ == "__main__":
    # Initialize the home plan
    home = home_plan()
    
    # Execute the plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)