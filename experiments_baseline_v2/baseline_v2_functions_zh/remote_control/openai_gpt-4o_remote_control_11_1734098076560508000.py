# To create a smart home application based on the provided functional description, we can focus on implementing the modes specified: "睡觉模式" (sleep mode), "起床模式" (wake-up mode), "关灯模式" (lights off mode), and "关窗模式" (windows off mode). Each mode will involve controlling the actuators appropriately. 
# 
# Here's an implementation outline for the `smart_home.py` script:
# 
# ```python
# smart_home.py

from home.home_plan import home_plan, get_all_actuators

def switch_sleep_mode(home):
    # Turn off lights and close windows
    lights = get_all_actuators(home, "Light")
    windows = get_all_actuators(home, "Window")
    
    for light in lights:
        light.turn_off()
    
    for window in windows:
        window.turn_off()

    print("Switched to Sleep Mode: Lights off, Windows closed.")

def switch_wakeup_mode(home):
    # Turn on lights and open curtains
    lights = get_all_actuators(home, "Light")
    curtains = get_all_actuators(home, "Curtain")
    
    for light in lights:
        light.turn_on()
    
    for curtain in curtains:
        curtain.turn_on()

    print("Switched to Wake-up Mode: Lights on, Curtains open.")

def switch_lights_off_mode(home):
    # Turn off lights
    lights = get_all_actuators(home, "Light")
    
    for light in lights:
        light.turn_off()

    print("Switched to Lights Off Mode: All lights turned off.")

def switch_windows_off_mode(home):
    # Close all windows
    windows = get_all_actuators(home, "Window")
    
    for window in windows:
        window.turn_off()

    print("Switched to Windows Off Mode: All windows closed.")

def main(mode):
    # Create the home environment
    home = home_plan()

    # Execute the mode
    if mode == "睡觉模式":
        switch_sleep_mode(home)
    elif mode == "起床模式":
        switch_wakeup_mode(home)
    elif mode == "关灯模式":
        switch_lights_off_mode(home)
    elif mode == "关窗模式":
        switch_windows_off_mode(home)
    else:
        print("Unknown mode. Please choose from: 睡觉模式, 起床模式, 关灯模式, 关窗模式.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python smart_home.py <mode>")
        sys.exit(1)

    mode = sys.argv[1]
    main(mode)
# ```
# 
# ### Instructions to Run the Application
# 
# 1. **Ensure all modules are in the correct directory structure:**
# 
#    ```
#    home/
#        sensor.py
#        actuator.py
#        home_plan.py
#        config.py
#    smart_home.py
#    ```
# 
# 2. **Navigate to the directory containing `smart_home.py` and the `home` folder.**
# 
# 3. **Run the script using a terminal command:**
# 
#    ```bash
#    python smart_home.py <mode>
#    ```
# 
#    Replace `<mode>` with one of the following options: `睡觉模式`, `起床模式`, `关灯模式`, `关窗模式`.
# 
# This script will read the mode passed as a command-line argument, instantiate the home environment using the `home_plan` function, and execute the corresponding actions for the specified mode.