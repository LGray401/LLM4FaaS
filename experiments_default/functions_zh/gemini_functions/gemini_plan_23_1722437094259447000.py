from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import LightIntensiveSensor
from home.actuator import Curtain, MusicPlayer, Light


def morning_plan(home):
    print("--- Morning Plan ---")
    living_room = get_room(home, "LivingRoom")

    if living_room is not None:
        # Get LightIntensiveSensor in LivingRoom
        light_intensive_sensor = get_all_sensors(home, "LightIntensive")[0]

        # Check light intensity
        light_intensity = light_intensive_sensor.get_reading()

        # If light intensity is increasing, open curtains and play music
        if light_intensity >= 400:
            print("Light intensity is increasing, opening curtains and playing music...")
            # Open curtains
            curtain = get_room_actuators(living_room, "Curtain")[0]
            curtain.turn_on()

            # Play music
            music_player = get_room_actuators(living_room, "MusicPlayer")[0]
            music_player.turn_on()
            music_player.play_music("Morning Playlist")
        else:
            print("Light intensity is not increasing, skipping morning plan...")
    else:
        print(f"Could not find LivingRoom, skipping morning plan...")


def leave_home_plan(home):
    print("--- Leave Home Plan ---")
    living_room = get_room(home, "LivingRoom")

    if living_room is not None:
        # Close the door
        door = get_room_actuators(living_room, "Door")[0]
        door.lock()

        # Open the curtains
        curtain = get_room_actuators(living_room, "Curtain")[0]
        curtain.turn_on()

        # Turn off the lights
        light = get_room_actuators(living_room, "Light")[0]
        light.turn_off()

        print("Closed the door, opened the curtains, and turned off the lights.")
    else:
        print(f"Could not find LivingRoom, skipping leave home plan...")


def movie_plan(home):
    print("--- Movie Plan ---")
    living_room = get_room(home, "LivingRoom")

    if living_room is not None:
        # Close the curtains
        curtain = get_room_actuators(living_room, "Curtain")[0]
        curtain.turn_off()

        # Dim the lights
        light = get_room_actuators(living_room, "Light")[0]
        light.set_brightness_level("low")

        print("Closed the curtains and dimmed the lights.")
    else:
        print(f"Could not find LivingRoom, skipping movie plan...")


if __name__ == "__main__":
    # Create a home instance
    home = home_plan()

    # Execute the morning plan
    morning_plan(home)

    # Execute the leave home plan
    leave_home_plan(home)

    # Execute the movie plan
    movie_plan(home)

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: Contains functions to work with your home plan (rooms, sensors, actuators).
#    - `home.sensor`: Provides access to sensor classes like `LightIntensiveSensor`.
#    - `home.actuator`: Provides access to actuator classes like `Curtain`, `MusicPlayer`, and `Light`.

# 2. **Define plan functions:**
#    - `morning_plan(home)`:
#      - Gets the "LivingRoom" from the home plan.
#      - Finds the `LightIntensiveSensor` in the living room.
#      - Reads the light intensity from the sensor.
#      - If the intensity is above a threshold (400 lux), it opens the curtains and plays music.
#    - `leave_home_plan(home)`:
#      - Gets the "LivingRoom" from the home plan.
#      - Locks the door, opens the curtains, and turns off the lights in the living room.
#    - `movie_plan(home)`:
#      - Gets the "LivingRoom" from the home plan.
#      - Closes the curtains and dims the lights in the living room.

# 3. **Main execution block:**
#    - Creates a home instance using `home_plan()`.
#    - Calls each plan function to execute them: `morning_plan(home)`, `leave_home_plan(home)`, `movie_plan(home)`.

# **Key Improvements:**

# - **Clearer Function Structure:** Each plan is encapsulated in its own function, making the code more organized and reusable.
# - **Error Handling:** The code checks for the existence of rooms before trying to access their components.
# - **Dynamic Sensor/Actuator Retrieval:** Uses `get_all_sensors` and `get_room_actuators` to find specific devices based on type and room, making the code more flexible.
# - **Logical Plan Execution:** Each plan function follows the steps described in the functional description, providing a clear and understandable flow.

# **Remember to adjust the sensor threshold values and playlist names according to your preferences.** 
