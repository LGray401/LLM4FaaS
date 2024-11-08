# Here is the 'function.py' file for your smart home project:

from home.home_plan import home_plan, print_home_plan, get_room_sensors, get_room_actuators

def main():
    # Create the home plan
    home = home_plan()

    # Print the home plan
    print_home_plan(home)

    # Get the sensors and actuators in a specific room
    room_name = "LivingRoom"
    sensors = get_room_sensors(home, room_name)
    actuators = get_room_actuators(home, room_name)

    # Perform actions based on the functional description
    # MORNING PLAN: Play music
    play_music(sensors, actuators)

    # LEAVE HOME PLAN: Unplug the socket
    unplug_socket(sensors, actuators)

    # MOVIE PLAN: Open the curtains
    open_curtains(sensors, actuators)


def play_music(sensors, actuators):
    # Check if the required sensors and actuators are available
    if sensors is None or actuators is None:
        print("Cannot perform the action. Required sensors or actuators are missing.")
        return

    # Check if the music player is available
    music_player = None
    for actuator in actuators:
        if isinstance(actuator, MusicPlayer):
            music_player = actuator
            break

    if music_player is None:
        print("Cannot play music. Music player is missing.")
        return

    # Play music
    music_player.turn_on()
    music_player.play_music("morning playlist")


def unplug_socket(sensors, actuators):
    # Check if the required sensors and actuators are available
    if sensors is None or actuators is None:
        print("Cannot perform the action. Required sensors or actuators are missing.")
        return

    # Check if the smart socket is available
    smart_socket = None
    for actuator in actuators:
        if isinstance(actuator, SmartSocket):
            smart_socket = actuator
            break

    if smart_socket is None:
        print("Cannot unplug the socket. Smart socket is missing.")
        return

    # Unplug the socket
    smart_socket.turn_off()
    print("Socket is unplugged.")


def open_curtains(sensors, actuators):
    # Check if the required sensors and actuators are available
    if sensors is None or actuators is None:
        print("Cannot perform the action. Required sensors or actuators are missing.")
        return

    # Check if the curtains are available
    curtains = None
    for actuator in actuators:
        if isinstance(actuator, Curtain):
            curtains = actuator
            break

    if curtains is None:
        print("Cannot open the curtains. Curtains are missing.")
        return

    # Open the curtains
    curtains.turn_on()
    print("Curtains are open.")


if __name__ == "__main__":
    main()