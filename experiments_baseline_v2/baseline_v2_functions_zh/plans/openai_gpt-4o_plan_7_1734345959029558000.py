# To implement the smart home application based on your functional description, we'll create a new Python script that orchestrates the different components and functionalities described. Here's how we'll proceed:
# 
# 1. We'll create a main script (`smart_home.py`) that uses the existing classes and methods from the reference files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`).
# 
# 2. The script will execute the three plans: `MORNING PLAN`, `LEAVE HOME PLAN`, and `MOVIE PLAN`.
# 
# 3. Each plan will use the appropriate actuators and sensors as described in your functional description.
# 
# Here's the implementation of `smart_home.py`:
# 
# ```python
from datetime import datetime, time
from home_plan import home_plan, get_room_actuators, get_all_actuators
from actuator import MusicPlayer, CoffeeMachine, Door, Light, Curtain, SmartSocket, SmartTV

def morning_plan(home):
    print("Executing MORNING PLAN...")
    # 7:00 Wake up
    current_time = datetime.now().time()
    if current_time.hour == 7 and current_time.minute == 0:
        # Assuming an alarm mechanism is present
        print("Alarm: Wake up!")

    # 7:05 Play music
    if current_time.hour == 7 and current_time.minute == 5:
        bedroom_actuators = get_room_actuators(home, "Bedroom")
        for actuator in bedroom_actuators:
            if isinstance(actuator, MusicPlayer):
                actuator.turn_on()
                actuator.play_music("周杰伦歌单")

    # 7:20 Make coffee
    if current_time.hour == 7 and current_time.minute == 20:
        kitchen_actuators = get_room_actuators(home, "Kitchen")
        for actuator in kitchen_actuators:
            if isinstance(actuator, CoffeeMachine):
                actuator.turn_on()
                actuator.make_coffee("Espresso")

def leave_home_plan(home):
    print("Executing LEAVE HOME PLAN...")
    current_time = datetime.now().time()
    leave_time = time(7, 30)
    
    # After 7:30, lock doors and turn off lights and sockets
    if current_time >= leave_time:
        all_doors = get_all_actuators(home, "Door")
        for door in all_doors:
            door.lock()

        all_lights = get_all_actuators(home, "Light")
        for light in all_lights:
            light.turn_off()

        all_sockets = get_all_actuators(home, "SmartSocket")
        for socket in all_sockets:
            socket.turn_off()

def movie_plan(home):
    print("Executing MOVIE PLAN...")
    # Trigger when a movie is started
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    for actuator in living_room_actuators:
        if isinstance(actuator, SmartTV):
            actuator.turn_on()
            actuator.play_channel("Movie Channel")
            
            # Close curtains and dim lights
            for curtain in living_room_actuators:
                if isinstance(curtain, Curtain):
                    curtain.turn_on()
            for light in living_room_actuators:
                if isinstance(light, Light):
                    light.turn_on()
                    light.set_brightness_level("low")

def main():
    home = home_plan()
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()
# ```
# 
# ### How to Run
# 
# 1. Save the script as `smart_home.py` in the same directory as the `home` folder containing the reference files.
# 2. Ensure all the reference files (`sensor.py`, `actuator.py`, `home_plan.py`, `config.py`) are in the `home` folder.
# 3. Open a terminal in the directory where `smart_home.py` is located.
# 4. Run the script with the command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# This script demonstrates the three plans based on the current time and actions within a simulated environment. Adjust the logic and functionality as needed to fit your specific use case and environment setup.