# Here's the `function.py` file based on your functional description. This script contains the main function which implements the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN as described.

from home.home_plan import home_plan, get_all_actuators

def morning_plan(home):
    # Open the curtains in all rooms
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()
    print("Morning plan executed: All curtains are now open.")

def leave_home_plan(home):
    # Turn off all lights and windows
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()
    
    windows = get_all_actuators(home, "Window")
    for window in windows:
        window.turn_off()
    print("Leave home plan executed: All lights and windows are now off.")

def movie_plan(home):
    # Turn on the TV
    tvs = get_all_actuators(home, "SmartTV")
    for tv in tvs:
        tv.turn_on()
    print("Movie plan executed: The TV is now on.")

def main():
    # Create home plan
    home = home_plan()
    
    # Execute plans based on user's choice
    print("Select a plan to execute:")
    print("1. Morning Plan")
    print("2. Leave Home Plan")
    print("3. Movie Plan")
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        morning_plan(home)
    elif choice == '2':
        leave_home_plan(home)
    elif choice == '3':
        movie_plan(home)
    else:
        print("Invalid choice. Please select a valid plan.")

if __name__ == "__main__":
    main()