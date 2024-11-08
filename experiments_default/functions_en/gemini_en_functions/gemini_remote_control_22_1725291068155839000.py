from home.home_plan import home_plan, get_room, get_room_actuators, get_all_actuators
from home.logger_config import logger

def main():
    home = home_plan()

    # Turn on lights in living room, bedroom, and bathroom
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")
    bathroom = get_room(home, "Bathroom")

    living_room_lights = get_room_actuators(living_room, "Light")
    for light in living_room_lights:
        light.turn_on()

    bedroom_lights = get_room_actuators(bedroom, "Light")
    for light in bedroom_lights:
        light.turn_on()

    bathroom_lights = get_room_actuators(bathroom, "Light")
    for light in bathroom_lights:
        light.turn_on()

    # Turn on air conditioners in living room and bedroom
    living_room_acs = get_room_actuators(living_room, "AC")
    for ac in living_room_acs:
        ac.turn_on()

    bedroom_acs = get_room_actuators(bedroom, "AC")
    for ac in bedroom_acs:
        ac.turn_on()

    # Turn on heater in the bathroom
    bathroom_heaters = get_room_actuators(bathroom, "Heater")
    for heater in bathroom_heaters:
        heater.turn_on()

    # Turn on TV in the living room
    living_room_tvs = get_all_actuators(home, "SmartTV")
    for tv in living_room_tvs:
        tv.turn_on()

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: For accessing the home plan, rooms, and actuators.
#    - `home.logger_config`: For logging information.

# 2. **Define `main` function:**
#    - This function contains the logic to execute the desired actions.

# 3. **Get home plan:**
#    - `home = home_plan()`: Retrieves the home plan from the `home_plan` module.

# 4. **Turn on lights:**
#    - Get the `LivingRoom`, `Bedroom`, and `Bathroom` rooms using `get_room`.
#    - Get all `Light` actuators in each room using `get_room_actuators`.
#    - Iterate through the lights and turn them on using `light.turn_on()`.

# 5. **Turn on air conditioners:**
#    - Get the `AC` actuators in the `LivingRoom` and `Bedroom` using `get_room_actuators`.
#    - Turn on each `AC`.

# 6. **Turn on heater:**
#    - Get the `Heater` actuators in the `Bathroom` using `get_room_actuators`.
#    - Turn on each `Heater`.

# 7. **Turn on TV:**
#    - Get all `SmartTV` actuators in the entire home using `get_all_actuators`.
#    - Turn on each `SmartTV`.

# 8. **Run the `main` function:**
#    - `if __name__ == "__main__":` ensures the `main` function is executed only when the script is run directly, not when imported as a module.
