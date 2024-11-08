# To create a smart home application based on your functional description and layout, we can define the modes you mentioned and implement a command-line interface in Python that triggers actions for each mode. The modes are:
# 
# 1. **睡觉模式 (Sleep Mode)**: This mode could involve turning off unnecessary lights, closing windows and curtains, and activating the security system.
# 
# 2. **起床模式 (Wake-up Mode)**: This mode could involve turning on lights, opening curtains or windows, and perhaps playing soft music.
# 
# 3. **关灯模式 (Lights Off Mode)**: This mode will turn off all lights in the house.
# 
# 4. **关窗模式 (Windows Close Mode)**: This mode will close all windows.
# 
# Let's write a simple Python script to handle these modes. We'll use basic function definitions to simulate the actions, since we don't have actual hardware to interface with.
# 
# ```python
#!/usr/bin/env python3

def sleep_mode():
    print("Activating Sleep Mode...")
    # Turn off lights
    turn_off_device("Light", all_rooms=True)
    # Close windows and curtains
    close_device("Window", all_rooms=True)
    close_device("Curtain", all_rooms=True)
    # Activate security (simulated)
    print("Security system activated.")
    print("Sleep Mode activated.")

def wake_up_mode():
    print("Activating Wake-up Mode...")
    # Turn on lights
    turn_on_device("Light", ["Bedroom", "Living Room"])
    # Open curtains
    open_device("Curtain", ["Bedroom", "Living Room"])
    # Play soft music
    print("Playing soft music in Bedroom.")
    print("Wake-up Mode activated.")

def lights_off_mode():
    print("Activating Lights Off Mode...")
    # Turn off all lights
    turn_off_device("Light", all_rooms=True)
    print("Lights Off Mode activated.")

def windows_close_mode():
    print("Activating Windows Close Mode...")
    # Close all windows
    close_device("Window", all_rooms=True)
    print("Windows Close Mode activated.")

def turn_off_device(device, all_rooms=False, rooms=None):
    if all_rooms:
        print(f"Turning off all {device}s in all rooms.")
    else:
        print(f"Turning off {device}s in {', '.join(rooms)}.")

def turn_on_device(device, rooms):
    print(f"Turning on {device}s in {', '.join(rooms)}.")

def close_device(device, all_rooms=False, rooms=None):
    if all_rooms:
        print(f"Closing all {device}s in all rooms.")
    else:
        print(f"Closing {device}s in {', '.join(rooms)}.")

def open_device(device, rooms):
    print(f"Opening {device}s in {', '.join(rooms)}.")

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: smart_home.py <mode>")
        print("Modes: sleep, wake_up, lights_off, windows_close")
        sys.exit(1)

    mode = sys.argv[1]
    if mode == "sleep":
        sleep_mode()
    elif mode == "wake_up":
        wake_up_mode()
    elif mode == "lights_off":
        lights_off_mode()
    elif mode == "windows_close":
        windows_close_mode()
    else:
        print("Unknown mode:", mode)
        print("Available modes: sleep, wake_up, lights_off, windows_close")

if __name__ == "__main__":
    main()
# ```
# 
# ### Instructions to Run the Application
# 
# 1. Save the script to a file, for example, `smart_home.py`.
# 2. Make the script executable by running `chmod +x smart_home.py`.
# 3. You can then run the script from the terminal with one of the following commands, depending on the mode you wish to activate:
# 
#    - For Sleep Mode: `./smart_home.py sleep`
#    - For Wake-up Mode: `./smart_home.py wake_up`
#    - For Lights Off Mode: `./smart_home.py lights_off`
#    - For Windows Close Mode: `./smart_home.py windows_close`
# 
# This script is a simple simulation and can be expanded with actual code to interact with smart home devices if you have a specific API or library for your devices.