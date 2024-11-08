# Based on your functional description and the provided source code files, I will create a `function.py` file that implements the specified plans for your smart home project.
# 
# The `function.py` will contain a main function that will execute the morning plan (play music), leave home plan (turn off smart socket), and movie plan (open curtains).
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room
from home.actuator import MusicPlayer, SmartSocket, Curtain

def morning_plan(home):
    # Retrieve the living room where the Music Player is located
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Find the Music Player in the living room
        music_player = next((actor for actor in living_room.actuators if isinstance(actor, MusicPlayer)), None)
        if music_player:
            music_player.turn_on()  # Turn on the Music Player
            music_player.play_music("Morning Playlist")  # Play the morning playlist
        else:
            print("Music Player not found in Living Room.")
    else:
        print("Living Room not found.")

def leave_home_plan(home):
    # Retrieve the living room where the Smart Socket is located
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Find the Smart Socket in the living room
        smart_socket = next((actor for actor in living_room.actuators if isinstance(actor, SmartSocket)), None)
        if smart_socket:
            smart_socket.turn_off()  # Turn off the Smart Socket
        else:
            print("Smart Socket not found in Living Room.")
    else:
        print("Living Room not found.")

def movie_plan(home):
    # Retrieve the living room where the Curtain is located
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Find the Curtain in the living room
        curtain = next((actor for actor in living_room.actuators if isinstance(actor, Curtain)), None)
        if curtain:
            curtain.turn_on()  # Open the curtain (assuming turn_on method opens it)
            print("Curtain opened for movie time.")
        else:
            print("Curtain not found in Living Room.")
    else:
        print("Living Room not found.")

def main():
    home = home_plan()  # Create the home plan
    print("Executing Morning Plan...")
    morning_plan(home)  # Execute morning plan
    print("Executing Leave Home Plan...")
    leave_home_plan(home)  # Execute leave home plan
    print("Executing Movie Plan...")
    movie_plan(home)  # Execute movie plan

if __name__ == "__main__":
    main()