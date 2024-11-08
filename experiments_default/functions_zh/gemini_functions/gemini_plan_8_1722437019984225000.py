from home.home_plan import home_plan, get_room, get_room_actuators, get_all_actuators
from home.sensor import IndoorTemperatureSensor
from home.actuator import Light, MusicPlayer, Heater, AC, CleaningRobot, SmartTV, CoffeeMachine, Door
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW

# function.py

def morning_plan(home):
    print("Morning plan started!")

    # Turn on lights in LivingRoom
    living_room = get_room(home, "LivingRoom")
    living_room_lights = get_room_actuators(home, "LivingRoom", "Light")
    for light in living_room_lights:
        light.turn_on()
        # optionally, set brightness
        light.set_brightness_level("medium")

    # Turn on music in LivingRoom
    living_room_music_player = get_room_actuators(home, "LivingRoom", "MusicPlayer")[0]
    living_room_music_player.turn_on()
    living_room_music_player.play_music("Morning playlist")

    # Adjust temperature in LivingRoom
    living_room_heater = get_room_actuators(home, "LivingRoom", "Heater")[0]
    living_room_ac = get_room_actuators(home, "LivingRoom", "AC")[0]

    # Option 1: Adjust based on current temperature
    # living_room_temp_sensor = get_room_sensors(home, "LivingRoom", "IndoorTemperature")[0]
    # current_temperature = living_room_temp_sensor.get_reading()
    # if current_temperature < TEMP_LOW:
    #     living_room_heater.turn_on()
    #     living_room_heater.set_target_temperature(TEMP_HIGH)
    # elif current_temperature > TEMP_HIGH:
    #     living_room_ac.turn_on()
    #     living_room_ac.set_target_temperature(TEMP_LOW)

    # Option 2: Set a desired temperature
    living_room_heater.turn_on()
    living_room_heater.set_target_temperature(22) # Example desired temperature

    # Start daily cleaning routine
    all_cleaning_robots = get_all_actuators(home, "CleaningRobot")
    for cleaning_robot in all_cleaning_robots:
        cleaning_robot.turn_on()
        cleaning_robot.daily_routine()

    # Make coffee
    kitchen = get_room(home, "Kitchen")
    kitchen_coffee_machine = get_room_actuators(home, "Kitchen", "CoffeeMachine")[0]
    kitchen_coffee_machine.turn_on()
    kitchen_coffee_machine.make_coffee("Espresso")

    print("Morning plan completed!")


def leave_home_plan(home):
    print("Leave home plan started!")

    # Turn off all lights
    all_lights = get_all_actuators(home, "Light")
    for light in all_lights:
        light.turn_off()

    # Turn off all music players
    all_music_players = get_all_actuators(home, "MusicPlayer")
    for music_player in all_music_players:
        music_player.turn_off()

    # Turn off all heaters and ACs
    all_heaters = get_all_actuators(home, "Heater")
    for heater in all_heaters:
        heater.turn_off()
    all_acs = get_all_actuators(home, "AC")
    for ac in all_acs:
        ac.turn_off()

    # Lock all doors
    all_doors = get_all_actuators(home, "Door")
    for door in all_doors:
        door.lock()

    # Optionally, turn off other appliances as needed

    print("Leave home plan completed!")


def movie_plan(home):
    print("Movie plan started!")

    # Turn on TV in LivingRoom
    living_room = get_room(home, "LivingRoom")
    living_room_tv = get_room_actuators(home, "LivingRoom", "SmartTV")[0]
    living_room_tv.turn_on()
    living_room_tv.play_channel("Netflix")

    # Turn off lights in LivingRoom
    living_room_lights = get_room_actuators(home, "LivingRoom", "Light")
    for light in living_room_lights:
        light.turn_off()

    # Optionally, adjust curtains, AC/heater for movie watching

    print("Movie plan completed!")


if __name__ == '__main__':
    home = home_plan()

    # Example usage
    # morning_plan(home)
    # leave_home_plan(home)
    movie_plan(home)

# **Explanation:**

# * **Imports:** Imports necessary modules from your `home` package (e.g., `home_plan`, `sensor`, `actuator`, `config`).
# * **Functions:** 
#     * `morning_plan(home)`: Defines actions for the morning plan, including:
#         * Turning on lights and music in the living room
#         * Adjusting temperature (heater/AC) in the living room
#         * Starting daily cleaning routines for all cleaning robots
#         * Making coffee in the kitchen
#     * `leave_home_plan(home)`: Defines actions for leaving home, including:
#         * Turning off all lights, music players, heaters/ACs
#         * Locking all doors
#     * `movie_plan(home)`: Defines actions for movie time, including:
#         * Turning on the TV in the living room and selecting Netflix
#         * Turning off lights in the living room
# * **Main Block:** 
#     * Creates a `home` object using `home_plan()`.
#     * Provides example calls to the `morning_plan`, `leave_home_plan`, and `movie_plan` functions.

# **To use this:**

# 1. Save this code as `function.py` in your `functions` folder.
# 2. Replace example actions and conditions with your desired logic for each plan.
# 3. You can call these functions from other parts of your project, passing the `home` object as an argument.

# **Example:**

from functions.function import morning_plan, leave_home_plan, movie_plan
from home.home_plan import home_plan

home = home_plan()
morning_plan(home) 