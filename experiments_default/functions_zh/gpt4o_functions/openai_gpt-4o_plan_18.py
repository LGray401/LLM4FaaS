# Below is the implementation of the `function.py` file that contains the `main` function to handle the smart home project based on the provided functional description:

# functions/function.py

from home.home_plan import home_plan, get_all_actuators

def main():
    # Initialize the home plan
    home = home_plan()

    # MORNING PLAN: Play music
    morning_plan(home)

    # LEAVE HOME PLAN: Turn off smart sockets
    leave_home_plan(home)

    # MOVIE PLAN: Open curtains
    movie_plan(home)


def morning_plan(home):
    print("\nExecuting MORNING PLAN: Playing music...")
    music_players = get_all_actuators(home, "MusicPlayer")
    for player in music_players:
        player.turn_on()
        player.play_music("Morning Playlist")


def leave_home_plan(home):
    print("\nExecuting LEAVE HOME PLAN: Turning off smart sockets...")
    smart_sockets = get_all_actuators(home, "SmartSocket")
    for socket in smart_sockets:
        socket.turn_off()


def movie_plan(home):
    print("\nExecuting MOVIE PLAN: Opening curtains...")
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

if __name__ == "__main__":
    main()