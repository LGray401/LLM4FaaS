# Based on your functional description and the provided source code, I will create a `function.py` file that implements the desired smart home automation plans: the Morning Plan, Leave Home Plan, and Movie Plan. The main function will coordinate the execution of these plans by using the classes defined in your existing source code.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan
from home.actuator import MusicPlayer, Curtain, SmartSocket

def morning_plan(home):
    """Play music in the living room."""
    living_room = get_room(home, "LivingRoom")
    if living_room:
        music_player = next((actuator for actuator in living_room.actuators if isinstance(actuator, MusicPlayer)), None)
        if music_player:
            music_player.turn_on()
            music_player.play_music("Morning Playlist")

def leave_home_plan(home):
    """Unplug all smart sockets in the house."""
    all_sockets = get_all_actuators(home, "SmartSocket")
    for socket in all_sockets:
        socket.turn_off()

def movie_plan(home):
    """Open the curtains in the living room."""
    living_room = get_room(home, "LivingRoom")
    if living_room:
        curtain = next((actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)), None)
        if curtain:
            curtain.turn_on()  # Assuming turning on will open the curtains

def get_room(home, room_name):
    for room in home:
        if room.name == room_name:
            return room
    return None

def get_all_actuators(home, actuator_type):
    all_actuators = []
    for room in home:
        for actuator in room.actuators:
            if actuator.actuator_type == actuator_type:
                all_actuators.append(actuator)
    return all_actuators

def main():
    """Main function to execute smart home plans."""
    home = home_plan()
    
    # Execute plans
    print("Starting Morning Plan...")
    morning_plan(home)
    
    print("\nStarting Leave Home Plan...")
    leave_home_plan(home)
    
    print("\nStarting Movie Plan...")
    movie_plan(home)

if __name__ == "__main__":
    main()