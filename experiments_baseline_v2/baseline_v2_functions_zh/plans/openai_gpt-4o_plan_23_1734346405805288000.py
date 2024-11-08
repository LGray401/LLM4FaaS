# To create a smart home application based on your functional description and the provided source code files, we will implement a Python script that simulates the Morning Plan, Leave Home Plan, and Movie Plan. We will utilize the classes and methods from the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files to achieve the desired functionality.
# 
# Here is the implementation of the smart home application:
# 
# ### smart_home.py
# 
# ```python
from home.home_plan import home_plan, get_all_sensors, get_all_actuators

def morning_plan(home):
    print("\nExecuting Morning Plan:")
    # Turn on light intensity sensors
    light_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in light_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        if reading and reading > 900:
            # Open curtains
            curtains = get_all_actuators(home, "Curtain")
            for curtain in curtains:
                curtain.turn_on()
            # Play music
            music_players = get_all_actuators(home, "MusicPlayer")
            for player in music_players:
                player.turn_on()
                player.play_music("morning playlist")

def leave_home_plan(home):
    print("\nExecuting Leave Home Plan:")
    # Lock doors
    doors = get_all_actuators(home, "Door")
    for door in doors:
        door.lock()
    # Open curtains
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()
    # Turn off lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

def movie_plan(home):
    print("\nExecuting Movie Plan:")
    # Close curtains
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_off()
    # Dim lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()
        light.set_brightness_level("low")

def main():
    home = home_plan()

    # Execute plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()
# ```
# 
# ### Command to Run the Application
# 
# To execute the smart home application, save the above code in a file named `smart_home.py` and run the following command in a Linux terminal:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# ### Explanation
# 
# - **Morning Plan**: The script turns on light intensity sensors and checks their readings. If readings are above 900, it opens curtains and plays music using the music players.
# 
# - **Leave Home Plan**: It locks all doors, opens curtains, and turns off all lights.
# 
# - **Movie Plan**: It closes all curtains and dims the lights to a low brightness level.
# 
# This implementation leverages the existing home automation framework and components defined in the provided source code files.