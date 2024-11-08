from home.home_plan import home_plan, get_room_actuators, get_room_sensors, get_all_sensors, get_all_actuators, \
    get_room
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Light, Curtain, MusicPlayer, CoffeeMachine, SmartTV, SmartSocket
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH


def morning_plan(home):
    print("\n---Morning Plan---")
    living_room = get_room(home, "LivingRoom")
    if living_room:
        curtains = get_room_actuators(home, "LivingRoom")[5]
        curtains.turn_on()
        music_player = get_room_actuators(home, "LivingRoom")[6]
        music_player.turn_on()
        music_player.play_music("Morning Music")
        coffee_machine = get_room_actuators(home, "Kitchen")[4]
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")
        print("Morning Plan Completed")


def leave_home_plan(home):
    print("\n---Leave Home Plan---")
    # Turn off lights and close doors and windows
    for room_name in ["LivingRoom", "Bedroom", "Kitchen", "Bathroom", "Balcony"]:
        room = get_room(home, room_name)
        if room:
            lights = get_room_actuators(home, room_name)[0]
            for light in lights:
                light.turn_off()
            door = get_room_actuators(home, room_name)[0]
            door.lock()
            windows = get_room_actuators(home, room_name)[2:4]
            for window in windows:
                window.turn_off()
    # Disconnect sockets except for fridge
    sockets = get_all_actuators(home, "SmartSocket")
    for socket in sockets:
        if socket.room_name != "Kitchen":
            socket.turn_off()
    print("Leave Home Plan Completed")


def movie_plan(home):
    print("\n---Movie Plan---")
    living_room = get_room(home, "LivingRoom")
    if living_room:
        curtains = get_room_actuators(home, "LivingRoom")[5]
        curtains.turn_off()
        lights = get_room_actuators(home, "LivingRoom")[0]
        for light in lights:
            light.set_brightness_level("low")
        tv = get_room_actuators(home, "LivingRoom")[10]
        tv.turn_on()
        tv.play_channel("Netflix")
    print("Movie Plan Completed")


def main():
    home = home_plan()
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home_plan`: Functions to interact with the home plan structure, like getting rooms, sensors, and actuators.
#    - `sensor`: Classes for different sensor types (IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor).
#    - `actuator`: Classes for different actuator types (Light, Curtain, MusicPlayer, CoffeeMachine, SmartTV, SmartSocket).
#    - `config`: Constants for temperature thresholds, humidity thresholds, and light intensity thresholds.

# 2. **Define plans:**
#    - **`morning_plan(home)`:**
#       - Gets the `LivingRoom` from the `home`.
#       - Turns on the curtains, music player, and coffee machine in the `LivingRoom`.
#    - **`leave_home_plan(home)`:**
#       - Iterates through each room and turns off the lights, closes the windows and locks the door.
#       - Disconnects all smart sockets except the one in the kitchen (presumably for the refrigerator).
#    - **`movie_plan(home)`:**
#       - Closes the curtains, dims the lights, and turns on the TV in the `LivingRoom`.

# 3. **`main()` function:**
#    - Creates the `home` plan using `home_plan()`.
#    - Calls each plan function in sequence: `morning_plan`, `leave_home_plan`, `movie_plan`.

# 4. **`if __name__ == "__main__":` block:**
#    - Executes the `main()` function only when the script is run directly, not when imported as a module.

# **Improvements:**

# - **More realistic plan details:** You can add more actions to each plan, like turning on/off specific appliances, setting target temperatures, or playing different music playlists.
# - **User interaction:** You can add prompts to ask the user for input, such as choosing a specific coffee type or setting the desired brightness level.
# - **Error handling:** You can add error checks and handle cases where a requested room, sensor, or actuator is not found.
# - **Real-time simulation:** Instead of just printing actions, you could integrate with a smart home simulator to actually control virtual devices based on the plan.
# - **Scheduling:** You can use a scheduler library (like `schedule`) to automatically execute the plans at specific times.

# This code provides a basic framework for implementing your smart home plan functions. You can further customize it based on your specific requirements and project goals. 
