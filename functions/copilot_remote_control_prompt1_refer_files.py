# manual added
from home.home_plan import home_plan, get_room, get_room_actuators


def control_devices(home, room_name, device_names, modes):
    room = get_room(home, room_name)
    if room is None:
        print(f"No room named {room_name} found.")
        return

    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        for i, device_name in enumerate(device_names):
            if actuator.actuator_type == device_name:
                if modes[i] is not None and hasattr(actuator, 'set_mode'):
                    actuator.set_mode(modes[i])
                break
        else:
            continue
        break
    else:
        print(f"No devices named {device_names} found in room {room_name}.")


# from home.home_plan import get_room, get_room_actuators
def control_device_always_refer_files(home, room_name, device_type, action, mode=None):
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
            elif action == "set_mode" and hasattr(actuator, 'set_mode'):
                actuator.set_mode(mode)
            else:
                print(f"Action {action} not supported for device type {device_type}.")
            return

    print(f"No device of type {device_type} found in room {room_name}.")



if __name__ == '__main__':
    home = home_plan()
    # control_device_always_refer_files(home, "LivingRoom", "Light", "turn_on")
    # control_device_always_refer_files(home, "LivingRoom", "Light", "set_brightness_level", "medium")
    #
    # control_device_always_refer_files(home, "LivingRoom", "MusicPlayer", "music_player", "medium")
    #
    # Turn on the light and heater in the living room
    control_devices(home, "LivingRoom", "MusicPlayer", "turn_on")
    #
    # # Set the brightness level of the light and heating level of the heater in the living room
    # control_devices(home, "LivingRoom", ["Light", "Heater"], ["medium", 3])
    #
    # # Turn on the music player and coffee machine in the kitchen
    # control_devices(home, "Kitchen", ["MusicPlayer", "CoffeeMachine"], ["turn_on", "turn_on"])
    #
    # # Play a specific playlist on the music player and brew coffee in the kitchen
    # control_devices(home, "Kitchen", ["MusicPlayer", "CoffeeMachine"], ["jazz_playlist", "brew"])



