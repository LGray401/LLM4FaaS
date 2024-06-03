from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, SmartSocket, Door, CleaningRobot, SmartTV
from home.home_plan import get_room, get_room_actuators, home_plan


def control_device(home, room_name, device_name, mode=None):
    room = get_room(home, room_name)
    if room is None:
        print(f"No room named {room_name} found.")
        return

    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if actuator.actuator_type == device_name:
            if mode is not None and hasattr(actuator, 'set_mode'):
                actuator.set_mode(mode)
            return

    print(f"No device named {device_name} found in room {room_name}.")

if __name__ == '__main__':
    home = home_plan()

    # Turn on the light in the living room
    control_device(home, "LivingRoom", "Light", "turn_on")

    # Set the brightness level of the light in the living room to medium
    control_device(home, "LivingRoom", "Light", "medium")

    # Turn on the heater in the bedroom
    control_device(home, "Bedroom", "Heater", "on")

    # Set the heating level of the heater in the bedroom to 3
    control_device(home, "Bedroom", "Heater", 3)

    # Turn on the music player in the kitchen
    control_device(home, "Kitchen", "MusicPlayer", "on")

    # Play a specific playlist on the music player in the kitchen
    control_device(home, "Kitchen", "MusicPlayer", "jazz_playlist")

    # Turn on the coffee machine in the kitchen
    control_device(home, "Kitchen", "CoffeeMachine", "on")
