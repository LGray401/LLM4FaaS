from home.home_plan import get_room, get_room_actuators, home_plan


def control_device(home, room_name, device_type, action):
    room = get_room(home, room_name)
    if room is None:
        print(f"No room named {room_name} found.")
        return

    actuators = get_room_actuators(home, room_name)
    if actuators is None:
        print(f"No actuators found in room {room_name}.")
        return

    for actuator in actuators:
        if actuator.actuator_type == device_type:
            if action == "turn_on":
                actuator.turn_on()
            elif action == "turn_off":
                actuator.turn_off()
            elif action == "set_brightness" and device_type == "Light":
                actuator.set_brightness_level("medium")  # Set brightness level to medium as an example
            else:
                print(f"Action {action} not supported for device type {device_type}.")
            return

    print(f"No device of type {device_type} found in room {room_name}.")



if __name__ == '__main__':
    home = home_plan()

    # Turn on the light in the living room
    control_device(home, "LivingRoom", "Light", "turn_on")

    # Turn off the light in the living room
    control_device(home, "LivingRoom", "Light", "set_brightness")

    # Turn on the heater in the bedroom
    control_device(home, "Bedroom", "Heater", "turn_on")

    # Turn off the heater in the bedroom
    control_device(home, "Bedroom", "Heater", "turn_off")

    # Turn on the music player in the kitchen
    control_device(home, "Kitchen", "MusicPlayer", "turn_on")

    # Turn off the music player in the kitchen
    control_device(home, "Kitchen", "MusicPlayer", "turn_off")


    # Turn off the music player in the Living  Room
    control_device(home, "LivingRoom", "MusicPlayer", "turn_off")
    # Turn on the music player in the Living Room
    control_device(home, "LivingRoom", "MusicPlayer", "turn_on")
