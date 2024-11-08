from home.home_plan import home_plan, get_room_actuators, get_room_sensors, get_all_actuators, get_all_sensors
from home.actuator import MusicPlayer, Light, Window, Curtain, CleaningRobot, SmartTV, SmartSocket
from home.sensor import LightIntensiveSensor
from home.config import LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    """
    This function implements the main logic of the smart home system.
    It defines the plans for different scenarios and executes them using the available sensors and actuators.
    """
    home = home_plan()
    
    # MORNING PLAN
    print("\n---MORNING PLAN---")
    music_player = get_all_actuators(home, "MusicPlayer")[0]
    music_player.turn_on()
    music_player.play_music("Morning Playlist")

    # LEAVE HOME PLAN
    print("\n---LEAVE HOME PLAN---")
    smart_sockets = get_all_actuators(home, "SmartSocket")
    for socket in smart_sockets:
        socket.turn_off()
    
    # MOVIE PLAN
    print("\n---MOVIE PLAN---")
    living_room = get_room_actuators(home, "LivingRoom")
    curtain = [actor for actor in living_room if actor.actuator_type == "Curtain"][0]
    curtain.turn_on()

    # Example of using light intensity sensor
    print("\n---LIGHT INTENSITY SENSOR EXAMPLE---")
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    light_sensor = [sensor for sensor in living_room_sensors if sensor.sensor_type == "LightIntensive"][0]
    light_sensor.turn_on()
    light_intensity = light_sensor.get_reading()
    print(f"Light intensity: {light_intensity}")
    if light_intensity < LIGHT_INTENSITY_LOW:
        print("It's dark. Turning on the lights.")
        lights = [actor for actor in living_room if actor.actuator_type == "Light"]
        for light in lights:
            light.turn_on()
    elif light_intensity > LIGHT_INTENSITY_HIGH:
        print("It's bright. Turning off the lights.")
        lights = [actor for actor in living_room if actor.actuator_type == "Light"]
        for light in lights:
            light.turn_off()
    else:
        print("Light intensity is good.")

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: For managing the home layout and accessing sensors/actuators.
#    - `home.actuator`: To interact with various actuators (MusicPlayer, Light, etc.).
#    - `home.sensor`: To access and read sensor data (LightIntensiveSensor).
#    - `home.config`: To get configuration parameters like light intensity thresholds.

# 2. **Define the `main()` function:**
#    - This function contains the main logic for the smart home system.
#    - It retrieves the home plan and sets up the scenarios.
#    - **Morning Plan:** Turns on the music player and plays a morning playlist.
#    - **Leave Home Plan:** Turns off all smart sockets.
#    - **Movie Plan:** Opens the curtains in the living room.
#    - **Light Intensity Sensor Example:**
#      - Turns on a LightIntensiveSensor in the living room.
#      - Reads the light intensity.
#      - Based on the intensity, turns on/off lights in the living room.

# 3. **Execute the `main()` function:**
#    - If the script is run directly (not imported), the `main()` function is called.

# **To run this code:**

# 1. Make sure you have the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files in the `home` directory.
# 2. Save the code above as `function.py` in the `functions` directory.
# 3. Run the `function.py` file. You should see the output of each scenario's actions.

# **Remember to adjust the playlists, specific actuators, and configurations in the `config.py` file based on your actual smart home setup.**
