from home.home_plan import home_plan, get_room, get_room_actuators, get_all_actuators
from home.sensor import IndoorTemperatureSensor
from home.actuator import Light, AC, CoffeeMachine, CleaningRobot, MusicPlayer
from home.config import TEMP_HIGH, TEMP_LOW


def main():
    # Create a home plan
    home = home_plan()

    # Example usage: Turn on the light in the LivingRoom and adjust its brightness to medium
    living_room = get_room(home, "LivingRoom")
    if living_room:
        lights = get_room_actuators(home, "LivingRoom", "Light")
        if lights:
            for light in lights:
                light.turn_on()
                light.set_brightness_level("medium")

    # Example usage: Adjust the AC in the LivingRoom to 22°C
    living_room = get_room(home, "LivingRoom")
    if living_room:
        acs = get_room_actuators(home, "LivingRoom", "AC")
        if acs:
            for ac in acs:
                ac.set_target_temperature(22)

    # Example usage: Play a song that can relieve stress
    music_players = get_all_actuators(home, "MusicPlayer")
    if music_players:
        for music_player in music_players:
            music_player.turn_on()
            music_player.play_music("relaxing music")

    # Example usage: Make a cup of coffee
    kitchen = get_room(home, "Kitchen")
    if kitchen:
        coffee_machines = get_room_actuators(home, "Kitchen", "CoffeeMachine")
        if coffee_machines:
            for coffee_machine in coffee_machines:
                coffee_machine.turn_on()
                coffee_machine.make_coffee("Espresso")

    # Example usage: Start the robot vacuum cleaner
    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    if cleaning_robots:
        for cleaning_robot in cleaning_robots:
            cleaning_robot.turn_on()
            cleaning_robot.daily_routine()

    # Example usage: Turn on the air conditioner to 22°C and close the curtains
    living_room = get_room(home, "LivingRoom")
    if living_room:
        acs = get_room_actuators(home, "LivingRoom", "AC")
        if acs:
            for ac in acs:
                ac.turn_on()
                ac.set_target_temperature(22)

        curtains = get_room_actuators(home, "LivingRoom", "Curtain")
        if curtains:
            for curtain in curtains:
                curtain.turn_on()
                # Assuming a close method for curtains

    # Example usage: Adjust temperature in all rooms
    home = home_plan()
    for room in home:
        temperature_sensors = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
        if temperature_sensors:
            current_temperature = temperature_sensors[0].get_reading()
            if current_temperature < TEMP_LOW:
                heaters = get_room_actuators(home, room.name, "Heater")
                if heaters:
                    for heater in heaters:
                        heater.turn_on()
                        heater.set_target_temperature(TEMP_HIGH)
            elif current_temperature > TEMP_HIGH:
                acs = get_room_actuators(home, room.name, "AC")
                if acs:
                    for ac in acs:
                        ac.turn_on()
                        ac.set_target_temperature(TEMP_LOW)


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: For working with the home plan, rooms, and devices.
#    - `home.sensor`: To access sensor objects (e.g., `IndoorTemperatureSensor`).
#    - `home.actuator`: To access actuator objects (e.g., `Light`, `AC`, `CoffeeMachine`).
#    - `home.config`: To load configuration settings.

# 2. **`main` function:**
#    - **Create a home plan:** `home = home_plan()`
#    - **Handle user commands:**
#      - **Turn on light and set brightness:**
#        - Get the `LivingRoom` from the `home` plan.
#        - Get all `Light` actuators in the `LivingRoom`.
#        - Turn on each light and set its brightness level to "medium".
#      - **Adjust AC temperature:**
#        - Get the `LivingRoom`.
#        - Get all `AC` actuators in the `LivingRoom`.
#        - Set the target temperature of each AC to 22°C.
#      - **Play relaxing music:**
#        - Get all `MusicPlayer` actuators in the home.
#        - Turn on each music player and play the "relaxing music" playlist.
#      - **Make a cup of coffee:**
#        - Get the `Kitchen`.
#        - Get all `CoffeeMachine` actuators in the `Kitchen`.
#        - Turn on each coffee machine and make an "Espresso".
#      - **Start robot vacuum cleaner:**
#        - Get all `CleaningRobot` actuators in the home.
#        - Turn on each cleaning robot and start its daily cleaning routine.
#      - **Turn on AC and close curtains:**
#        - Get the `LivingRoom`.
#        - Get all `AC` actuators and turn them on.
#        - Set the target temperature of each AC to 22°C.
#        - Get all `Curtain` actuators and turn them on (assuming a `close` method).
#      - **Temperature adjustment in all rooms:**
#        - Iterate through each room in the `home` plan.
#        - Find the `IndoorTemperatureSensor` in the room.
#        - Get the current temperature reading.
#        - If the temperature is below `TEMP_LOW`, turn on heaters and set the target temperature to `TEMP_HIGH`.
#        - If the temperature is above `TEMP_HIGH`, turn on ACs and set the target temperature to `TEMP_LOW`.

# 3. **`if __name__ == "__main__":` block:**
#    - Calls the `main` function when the script is run directly.

# **Note:**

# - This code demonstrates the basic functionality and how to interact with devices in the home. 
# - You'll need to expand it with additional logic and features to handle more complex user commands and scenarios. 
# - The comments explain how each part of the code works.
# - The `home.config` module provides constants for temperature thresholds and other settings, which can be modified based on your needs. 
