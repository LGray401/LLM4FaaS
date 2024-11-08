# Based on your functional description and the provided source code files, here is the `function.py` file. This file will contain the main function to execute the plans defined in your functional description.
# 
# ### `function.py`

from home.home_plan import home_plan, get_all_actuators

def main():
    # Initialize home plan
    home = home_plan()

    # Execute MORNING PLAN: Play music
    music_players = get_all_actuators(home, 'MusicPlayer')
    if music_players:
        for music_player in music_players:
            music_player.turn_on()
            music_player.play_music('Morning Playlist')
    else:
        print("No Music Player found in the home.")

    # Execute LEAVE HOME PLAN: Unplug the socket
    smart_sockets = get_all_actuators(home, 'SmartSocket')
    if smart_sockets:
        for smart_socket in smart_sockets:
            smart_socket.turn_off()
    else:
        print("No Smart Socket found in the home.")

    # Execute MOVIE PLAN: Open the curtains
    curtains = get_all_actuators(home, 'Curtain')
    if curtains:
        for curtain in curtains:
            curtain.turn_on()
    else:
        print("No Curtain found in the home.")

if __name__ == "__main__":
    main()