from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_actuators, \
    get_all_sensors
from home.sensor import LightIntensiveSensor
from home.actuator import Light, AC, CoffeeMachine, Door, CleaningRobot, SmartTV, MusicPlayer, Curtain, Heater, \
    NotificationSender, SmartSocket
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    DAILY_ROUTINE_DURATION
import time


def morning_plan(home):
    # TODO: Alarm clock functionality (could use a separate function or a time-based trigger)

    # Find the living room
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Get the light intensive sensor
        light_sensor = get_all_sensors(home, "LightIntensive")[0]
        # Turn on the lights
        lights = get_room_actuators(living_room, "Light")
        for light in lights:
            light.turn_on()

        # Get the curtains
        curtains = get_room_actuators(living_room, "Curtain")
        for curtain in curtains:
            curtain.turn_on()

        # Get the coffee machine
        coffee_machine = get_room_actuators(living_room, "CoffeeMachine")[0]
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")

        # Adjust light brightness based on sunlight
        if light_sensor.get_reading() < LIGHT_INTENSITY_LOW:
            print(
                f"Sunlight is dim, adjusting light brightness to medium. Sensor reading: {light_sensor.get_reading()}")
            for light in lights:
                light.set_brightness_level("medium")

    # ... Add more morning plan tasks for other rooms (bedroom, bathroom)

def leave_home_plan(home):
    # Find the living room
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Turn off lights
        lights = get_room_actuators(living_room, "Light")
        for light in lights:
            light.turn_off()

        # Unplug sockets
        sockets = get_room_actuators(living_room, "SmartSocket")
        for socket in sockets:
            socket.turn_off()

        # Lock the door
        door = get_room_actuators(living_room, "Door")[0]
        door.lock()

    # ... Add more leave home plan tasks for other rooms (bedroom, bathroom)

def movie_plan(home):
    # Find the living room
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Close curtains
        curtains = get_room_actuators(living_room, "Curtain")
        for curtain in curtains:
            curtain.turn_off()

        # Dim the lights
        lights = get_room_actuators(living_room, "Light")
        for light in lights:
            light.set_brightness_level("low")

        # Turn on the TV
        tv = get_room_actuators(living_room, "SmartTV")[0]
        tv.turn_on()
        tv.play_channel("Netflix")

    # ... Add more movie plan tasks (e.g., turn on music player)

def main():
    home = home_plan()

    # Example of executing plans
    morning_plan(home)
    time.sleep(5)  # Simulate time passing
    leave_home_plan(home)
    time.sleep(5)  # Simulate time passing
    movie_plan(home)

    # ... Add more plan execution logic here
    # For example, you could create a loop that checks the time and executes plans
    # based on the current time or user commands.

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:**
#    - Imports necessary classes from `home_plan.py`, `sensor.py`, and `actuator.py`.
#    - Also imports `time` for simulating delays.

# 2. **Plan Functions:**
#    - **`morning_plan(home)`:**
#      - Finds the living room.
#      - Turns on the lights and sets brightness based on sunlight.
#      - Opens the curtains.
#      - Turns on the coffee machine and makes coffee.
#    - **`leave_home_plan(home)`:**
#      - Finds the living room.
#      - Turns off lights, unplugs sockets, and locks the door.
#    - **`movie_plan(home)`:**
#      - Finds the living room.
#      - Closes the curtains, dims the lights, and turns on the TV.

# 3. **`main()` Function:**
#    - Creates the `home` object using `home_plan()`.
#    - Executes example plans (`morning_plan`, `leave_home_plan`, `movie_plan`).
#    - `time.sleep()` simulates time passing.
#    - The `main()` function is a starting point for your plan execution logic. You can add more plan execution logic here.

# **How to Use:**

# 1. **Create your `home_plan`:** Modify the `home_plan()` function in `home_plan.py` to reflect your actual home layout and components.
# 2. **Define your plans:** Add more plan functions (e.g., `evening_plan`, `dinner_plan`) in `function.py` to implement your desired actions.
# 3. **Execute plans:** Modify the `main()` function to call your plan functions based on time, user commands, or other triggers.

# **Example Usage:**

# In main() function:
if current_time.hour == 7:
    morning_plan(home)
elif current_time.hour == 18:
    evening_plan(home)

# **Remember:**

# - Replace placeholders (e.g., "Espresso") with your actual desired values.
# - Consider using a scheduler library to automatically execute plans based on time.
# - Implement more sophisticated plan logic based on your needs (e.g., checking sensor readings, user preferences, and external events).
