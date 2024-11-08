# To fulfill the functional description "打开窗户" (which means "Open the window" in English), we will create a `function.py` file in the `functions` folder. This file will contain a `main` function that will open the windows in all rooms.
# 
# Here's the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_all_actuators
from home.actuator import Window

def main():
    # Create the home plan
    home = home_plan()
    
    # Get all windows in the home
    all_windows = get_all_actuators(home, "Window")
    
    # Open all windows
    for window in all_windows:
        window.turn_on()
        
    print("All windows are now opened.")

if __name__ == "__main__":
    main()