# Based on the provided functional description and source code, I'll create a `function.py` file that implements the modes (睡觉模式, 起床模式, 关灯模式, 关窗模式). This file will reside in the `functions` folder and include the main function to handle these modes.
# 
# Here's the `function.py`:

# functions/function.py
from home.home_plan import home_plan, get_all_actuators
from home.actuator import Light, Curtain, Window, CoffeeMachine, MusicPlayer, NotificationSender

def main():
    home = home_plan()

    def sleep_mode():
        print("Activating Sleep Mode...")
        # Turn off all lights
        lights = get_all_actuators(home, "Light")
        for light in lights:
            light.turn_off()
        
        # Close all curtains
        curtains = get_all_actuators(home, "Curtain")
        for curtain in curtains:
            curtain.turn_off()

        # Close all windows
        windows = get_all_actuators(home, "Window")
        for window in windows:
            window.turn_off()

        # Send notification
        notifications = get_all_actuators(home, "NotificationSender")
        for notification in notifications:
            notification.turn_on()
            notification.notification_sender("Sleep Mode Activated")

    def wake_up_mode():
        print("Activating Wake Up Mode...")
        # Turn on lights in bedroom and bathroom
        lights = get_all_actuators(home, "Light")
        for light in lights:
            if light.room_name in ["Bedroom", "Bathroom"]:
                light.turn_on()

        # Open curtains in bedroom
        curtains = get_all_actuators(home, "Curtain")
        for curtain in curtains:
            if curtain.room_name == "Bedroom":
                curtain.turn_on()

        # Make coffee in kitchen
        coffee_machines = get_all_actuators(home, "CoffeeMachine")
        for coffee_machine in coffee_machines:
            coffee_machine.turn_on()
            coffee_machine.make_coffee("Espresso")

        # Play music in bedroom
        music_players = get_all_actuators(home, "MusicPlayer")
        for music_player in music_players:
            if music_player.room_name == "Bedroom":
                music_player.turn_on()
                music_player.play_music("Morning Playlist")

        # Send notification
        notifications = get_all_actuators(home, "NotificationSender")
        for notification in notifications:
            notification.turn_on()
            notification.notification_sender("Wake Up Mode Activated")

    def turn_off_lights_mode():
        print("Activating Turn Off Lights Mode...")
        # Turn off all lights
        lights = get_all_actuators(home, "Light")
        for light in lights:
            light.turn_off()

    def close_windows_mode():
        print("Activating Close Windows Mode...")
        # Close all windows
        windows = get_all_actuators(home, "Window")
        for window in windows:
            window.turn_off()

    # Example usage
    mode = input("Enter mode (Sleep, WakeUp, TurnOffLights, CloseWindows): ").strip().lower()

    if mode == "sleep":
        sleep_mode()
    elif mode == "wakeup":
        wake_up_mode()
    elif mode == "turnofflights":
        turn_off_lights_mode()
    elif mode == "closewindows":
        close_windows_mode()
    else:
        print("Invalid mode")

if __name__ == "__main__":
    main()