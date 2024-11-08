# To create a smart home application based on your functional description, we'll implement a script that uses the given sensor and actuator classes to execute the specified plans. We'll create a new Python script called `smart_home.py` that will implement the three plans: "MORNING PLAN", "LEAVE HOME PLAN", and "MOVIE PLAN". Here's how you can implement it:
# 
# ### `smart_home.py`
# 
# ```python
from home.sensor import *
from home.actuator import *
from home.home_plan import home_plan, get_all_actuators

def morning_plan(home):
    print("\nExecuting Morning Plan:")
    # Find all music players and play music
    music_players = get_all_actuators(home, "MusicPlayer")
    for player in music_players:
        player.turn_on()
        player.play_music("morning playlist")

def leave_home_plan(home):
    print("\nExecuting Leave Home Plan:")
    # Find all smart sockets and turn them off
    smart_sockets = get_all_actuators(home, "SmartSocket")
    for socket in smart_sockets:
        socket.turn_off()

def movie_plan(home):
    print("\nExecuting Movie Plan:")
    # Find all curtains and open them
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()  # Assuming turning on opens the curtain

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Execute the plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 
# - **Morning Plan:** This plan turns on all music players and starts playing a "morning playlist".
# - **Leave Home Plan:** This plan turns off all smart sockets, simulating unplugging devices from the sockets.
# - **Movie Plan:** This plan turns on all curtains, which we assume opens them.
# 
# ### Running the Application
# 
# To run this application in a Linux terminal, ensure you are in the directory containing the `home` folder and the `smart_home.py` script. Then use the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# ### Notes:
# 
# - Ensure that all necessary modules and their dependencies are properly placed and imported in your project structure.
# - This script assumes that turning on an actuator means activating its primary function (e.g., opening curtains).
# - Modify the `home_plan.py` to correctly initialize your rooms and components if any changes are necessary.
# 
# This setup should give you a good starting point for controlling your smart home according to the described plans.