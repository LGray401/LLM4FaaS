# Sure! I have created the 'function.py' file based on the given functional description and the provided source code. Here is the content of the 'function.py' file:

from home.home_plan import home_plan, get_room_actuators

def morning_plan():
    home = home_plan()
    music_player = get_room_actuators(home, "LivingRoom")[6]  # Get the MusicPlayer in the LivingRoom
    music_player.turn_on()
    music_player.play_music("morning playlist")

def leave_home_plan():
    home = home_plan()
    smart_sockects = get_room_actuators(home, "LivingRoom")
    for socket in smart_sockects:
        socket.turn_off()

def movie_plan():
    home = home_plan()
    curtain = get_room_actuators(home, "LivingRoom")[4]  # Get the Curtain in the LivingRoom
    curtain.turn_on()

print("Function.py file was created successfully!")
