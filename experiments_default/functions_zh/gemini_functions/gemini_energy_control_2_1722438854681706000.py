from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, LightIntensiveSensor
from home.actuator import Window, Light, AC
from home.config import TEMP_LOW, TEMP_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    home = home_plan()

    # Rule 1: Air Conditioner On, Windows Close
    living_room = get_room(home, "LivingRoom")
    if living_room:
        ac = get_room_actuators(home, "LivingRoom")[0]
        if ac.get_status() == "on":
            windows = get_room_actuators(home, "LivingRoom")[1:3]
            for window in windows:
                window.turn_off()

    # Rule 2: Temperature below 20, AC Off
    all_indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in all_indoor_temp_sensors:
        if sensor.get_reading() < TEMP_LOW:
            room = get_room(home, sensor.room_name)
            if room:
                ac = get_room_actuators(home, sensor.room_name)[0]
                if ac.get_status() == "on":
                    ac.turn_off()

    # Rule 3: Light Intensive, Light Off or Dimmed
    all_light_intensive_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in all_light_intensive_sensors:
        if sensor.get_reading() > LIGHT_INTENSITY_HIGH:
            room = get_room(home, sensor.room_name)
            if room:
                lights = get_room_actuators(home, sensor.room_name)
                for light in lights:
                    if light.get_status() == "on":
                        light.set_brightness_level("low")
                        # Alternatively, turn off the light:
                        # light.turn_off() 

    # Rule 4: Leaving home, Turn off music player and TV
    # ... (Implementation depends on how you detect leaving home, 
    #      e.g., using presence sensors, door sensors, etc.)
    #      For example:
    #      if presence_sensor.get_status() == "off":
    #          music_player = get_room_actuators(home, "LivingRoom")[4] 
    #          music_player.turn_off()
    #          tv = get_room_actuators(home, "LivingRoom")[9] 
    #          tv.turn_off()

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - Import the relevant functions from `home.home_plan` for accessing rooms, sensors, and actuators.
#    - Import sensor and actuator classes from `home.sensor` and `home.actuator`.
#    - Import thresholds from `home.config`.

# 2. **`main` function:**
#    - **Get the home plan:** Calls `home_plan()` to create the structure of your home.
#    - **Rule 1: AC on, windows close:**
#      - Finds the living room using `get_room`.
#      - Gets the AC actuator and checks its status.
#      - If the AC is on, finds all windows in the living room and turns them off.
#    - **Rule 2: Temperature below 20, AC off:**
#      - Gets all indoor temperature sensors using `get_all_sensors`.
#      - Iterates through the sensors.
#      - If a sensor reading is below the threshold `TEMP_LOW`:
#        - Gets the room associated with the sensor.
#        - Finds the AC in that room and turns it off if it's on.
#    - **Rule 3: Light intensive, light off or dimmed:**
#      - Gets all light intensity sensors using `get_all_sensors`.
#      - Iterates through the sensors.
#      - If a sensor reading is above the threshold `LIGHT_INTENSITY_HIGH`:
#        - Gets the room associated with the sensor.
#        - Finds all lights in that room.
#        - For each light that's on, sets the brightness to low (or you can turn it off completely).
#    - **Rule 4: Leaving home, turn off music player and TV:**
#      - This part is commented out because it depends on how you detect leaving home. You'll need to implement logic using presence sensors, door sensors, or other appropriate methods.

# **How to integrate this function:**

# 1. **Add to your project:** Place this `function.py` file in your `functions` folder.
# 2. **Call `main()`:** In your main script (e.g., `main.py`), add a line to call `functions.function.main()`. This will trigger the execution of your rules.

# **Remember to:**

# - Modify the thresholds in `config.py` to match your preferences.
# - Implement the logic for detecting leaving home (Rule 4).
# - Adjust the actuator types and actions based on the actual actuators in your smart home system.

# With these changes, your `function.py` file will now automate the described smart home behaviors. 
