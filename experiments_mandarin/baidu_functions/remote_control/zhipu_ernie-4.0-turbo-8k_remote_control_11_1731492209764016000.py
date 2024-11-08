# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main functions for your smart home project. These functions will handle the "睡觉模式" (Sleep Mode), "起床模式" (Wake Up Mode), "关灯模式" (Lights Off Mode), and "关窗模式" (Windows Close Mode).
# 
# Here's the `function.py` file:

from home.home_plan import home_plan, get_room, get_all_actuators, get_room_actuators
from home.actuator import Light, Window

def sleep_mode(home):
    """
    Activate sleep mode in all rooms.
    Turn off all lights and close all windows.
    """
    print("\nActivating Sleep Mode...")
    for room in home:
        # Turn off lights
        lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
        for light in lights:
            light.turn_off()
        
        # Close windows
        windows = [actuator for actuator in room.actuators if isinstance(actuator, Window)]
        for window in windows:
            # Assuming window has a close method (not defined in provided code)
            # window.close()  # Uncomment and implement this method if it exists
            print(f"Closing window: {window.id}")  # Placeholder for actual window closing logic

    print("Sleep Mode Activated.")

def wake_up_mode(home):
    """
    Activate wake-up mode in all rooms.
    Turn on all lights and open all windows.
    """
    print("\nActivating Wake Up Mode...")
    for room in home:
        # Turn on lights
        lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
        for light in lights:
            light.turn_on()
            # Set to a medium brightness level as an example
            light.set_brightness_level("medium")
        
        # Open windows
        windows = [actuator for actuator in room.actuators if isinstance(actuator, Window)]
        for window in windows:
            # Assuming window has an open method (not defined in provided code)
            # window.open()  # Uncomment and implement this method if it exists
            print(f"Opening window: {window.id}")  # Placeholder for actual window opening logic

    print("Wake Up Mode Activated.")

def lights_off_mode(home):
    """
    Turn off all lights in the home.
    """
    print("\nActivating Lights Off Mode...")
    all_lights = get_all_actuators(home, "Light")
    for light in all_lights:
        light.turn_off()
    print("Lights Off Mode Activated.")

def windows_close_mode(home):
    """
    Close all windows in the home.
    """
    print("\nActivating Windows Close Mode...")
    # Since the close method for windows is assumed, we'll use a placeholder logic here
    for room in home:
        windows = [actuator for actuator in room.actuators if isinstance(actuator, Window)]
        for window in windows:
            # Assuming window has a close method (not defined in provided code)
            # window.close()  # Uncomment and implement this method if it exists
            print(f"Closing window: {window.id}")  # Placeholder for actual window closing logic

    print("Windows Close Mode Activated.")

if __name__ == "__main__":
    # Initialize the home plan
    home = home_plan()
    
    # Test the modes
    sleep_mode(home)
    # wake_up_mode(home)
    # lights_off_mode(home)
    # windows_close_mode(home)