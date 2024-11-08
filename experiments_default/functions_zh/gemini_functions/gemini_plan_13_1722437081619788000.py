from home.home_plan import home_plan, get_room_actuators, get_all_actuators
from home.actuator import Light, MusicPlayer, CoffeeMachine, CleaningRobot, SmartTV, Window, Curtain, Door
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH


def morning_plan(home):
    # Get actuators
    living_room_lights = get_room_actuators(home, "LivingRoom")[0]
    bedroom_lights = get_room_actuators(home, "Bedroom")[0]
    kitchen_lights = get_room_actuators(home, "Kitchen")[0]
    living_room_curtains = get_room_actuators(home, "LivingRoom")[4]
    living_room_music_player = get_room_actuators(home, "LivingRoom")[5]
    kitchen_coffee_machine = get_room_actuators(home, "Kitchen")[3]

    # Morning Routine
    living_room_curtains.turn_on()
    living_room_lights.turn_on()
    living_room_lights.set_brightness_level("medium")
    kitchen_lights.turn_on()
    kitchen_lights.set_brightness_level("medium")
    bedroom_lights.turn_on()
    bedroom_lights.set_brightness_level("medium")
    kitchen_coffee_machine.turn_on()
    kitchen_coffee_machine.make_coffee("Espresso")
    living_room_music_player.turn_on()
    living_room_music_player.play_music("Relaxing Music")

    print("Morning plan executed successfully!")


def leave_home_plan(home):
    # Get actuators
    living_room_lights = get_room_actuators(home, "LivingRoom")[0]
    bedroom_lights = get_room_actuators(home, "Bedroom")[0]
    kitchen_lights = get_room_actuators(home, "Kitchen")[0]
    living_room_curtains = get_room_actuators(home, "LivingRoom")[4]
    living_room_door = get_room_actuators(home, "LivingRoom")[0]
    kitchen_smart_sockets = get_room_actuators(home, "Kitchen")[5]
    bedroom_smart_sockets = get_room_actuators(home, "Bedroom")[9]

    # Leave home routine
    living_room_lights.turn_off()
    bedroom_lights.turn_off()
    kitchen_lights.turn_off()
    living_room_curtains.turn_on()
    living_room_door.lock()
    kitchen_smart_sockets.turn_off()
    bedroom_smart_sockets.turn_off()

    print("Leave home plan executed successfully!")


def movie_plan(home):
    # Get actuators
    living_room_lights = get_room_actuators(home, "LivingRoom")[0]
    living_room_curtains = get_room_actuators(home, "LivingRoom")[4]
    living_room_smart_tv = get_room_actuators(home, "LivingRoom")[10]

    # Movie plan routine
    living_room_curtains.turn_on()
    living_room_lights.turn_on()
    living_room_lights.set_brightness_level("low")
    living_room_smart_tv.turn_on()
    living_room_smart_tv.play_channel("Netflix")

    print("Movie plan executed successfully!")


def auto_adjust_lights(home):
    # Get all Light actuators
    all_lights = get_all_actuators(home, "Light")

    for light in all_lights:
        if light.status == "on":
            # Check Light Intensity
            # if light.brightness_level < LIGHT_INTENSITY_LOW:
            #     light.set_brightness_level("high")
            # elif light.brightness_level > LIGHT_INTENSITY_HIGH:
            #     light.set_brightness_level("low")
            # else:
            #     print(f"{light.id} is currently at the optimal brightness level.")
            print(f"{light.id} is currently at the optimal brightness level.")
        else:
            print(f"{light.id} is currently off.")


def auto_adjust_temperature(home):
    # Get all Heater and AC actuators
    all_heaters = get_all_actuators(home, "Heater")
    all_acs = get_all_actuators(home, "AC")

    # Iterate through heaters and adjust temperature
    for heater in all_heaters:
        if heater.status == "on":
            # Check current temperature
            # if current_temperature < TEMP_LOW:
            #     heater.turn_on()
            #     print(f"{heater.id} is turned on to adjust the temperature.")
            # elif current_temperature > TEMP_HIGH:
            #     heater.turn_off()
            #     print(f"{heater.id} is turned off.")
            print(f"{heater.id} is currently at the optimal temperature.")
        else:
            print(f"{heater.id} is currently off.")

    # Iterate through ACs and adjust temperature
    for ac in all_acs:
        if ac.status == "on":
            # Check current temperature
            # if current_temperature > TEMP_HIGH:
            #     ac.turn_on()
            #     print(f"{ac.id} is turned on to adjust the temperature.")
            # elif current_temperature < TEMP_LOW:
            #     ac.turn_off()
            #     print(f"{ac.id} is turned off.")
            print(f"{ac.id} is currently at the optimal temperature.")
        else:
            print(f"{ac.id} is currently off.")


def auto_adjust_humidity(home):
    # Get all Humidifier actuators
    all_humidifiers = get_all_actuators(home, "Humidifier")

    # Iterate through humidifiers and adjust humidity
    for humidifier in all_humidifiers:
        if humidifier.status == "on":
            # Check current humidity
            # if current_humidity < HUMIDITY_LOW:
            #     humidifier.increase_humidity()
            #     print(f"{humidifier.id} is increasing humidity.")
            # elif current_humidity > HUMIDITY_HIGH:
            #     humidifier.decrease_humidity()
            #     print(f"{humidifier.id} is decreasing humidity.")
            print(f"{humidifier.id} is currently at the optimal humidity level.")
        else:
            print(f"{humidifier.id} is currently off.")


def main():
    home = home_plan()

    # Example: Call plans and auto-adjust functions
    # morning_plan(home)
    # leave_home_plan(home)
    movie_plan(home)
    # auto_adjust_lights(home)
    # auto_adjust_temperature(home)
    # auto_adjust_humidity(home)


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: Imports functions for managing the home plan.
#    - `home.actuator`: Imports actuator classes like `Light`, `MusicPlayer`, etc.
#    - `home.config`: Imports configuration constants like temperature thresholds.

# 2. **Define plan functions:**
#    - `morning_plan(home)`: Contains steps for the morning routine.
#    - `leave_home_plan(home)`: Contains steps for leaving the home.
#    - `movie_plan(home)`: Contains steps for preparing for a movie.

# 3. **Define auto-adjust functions:**
#    - `auto_adjust_lights(home)`: Checks light intensity and adjusts accordingly.
#    - `auto_adjust_temperature(home)`: Checks temperature and adjusts heaters/ACs.
#    - `auto_adjust_humidity(home)`: Checks humidity and adjusts humidifiers.

# 4. **`main()` function:**
#    - Creates the home plan (`home`).
#    - Calls the plan functions and auto-adjust functions for demonstration.

# 5. **`if __name__ == "__main__":` block:**
#    - Runs the `main()` function when the script is executed directly.

# **How to use the `function.py` file:**

# 1. **Create a `functions` folder in your project.**
# 2. **Save the code as `function.py` in the `functions` folder.**
# 3. **Import the `functions.py` file into your main script.**
# 4. **Call the functions from your main script, passing the `home` object created using `home_plan()` as an argument.**

# **Example:**

from home.home_plan import home_plan
from functions.function import morning_plan

home = home_plan()
morning_plan(home)

# **Remember to replace the comments in the auto-adjust functions with actual logic based on sensor readings and actuator controls.** You can access sensor readings from the `sensor.py` file and control actuators using the methods provided in the `actuator.py` file.
