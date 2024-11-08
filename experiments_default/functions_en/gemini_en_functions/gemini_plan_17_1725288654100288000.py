from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_actuators, \
    get_all_sensors
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, \
    LIGHT_INTENSITY_LOW
from home.logger_config import logger


def morning_plan(home):
    # Get the coffee machine in the kitchen
    coffee_machine = get_all_actuators(home, "CoffeeMachine")[0]
    # Turn on the coffee machine and make a coffee
    coffee_machine.turn_on()
    coffee_machine.make_coffee("Espresso")
    # Optional: you can add more actions for the morning plan, like turning on lights, etc.
    return "Morning plan executed!"


def leave_home_plan(home):
    # Get the lights in the living room
    living_room_lights = get_room_actuators(home, "LivingRoom")
    # Turn off all the lights in the living room
    for light in living_room_lights:
        if light.actuator_type == "Light":
            light.turn_off()
    # Optional: you can add more actions for the leave home plan, like locking doors, etc.
    return "Leave home plan executed!"


def movie_plan(home):
    # Get the bed curtains in the bedroom
    bedroom_curtains = get_room_actuators(home, "Bedroom")
    # Close the curtains in the bedroom
    for curtain in bedroom_curtains:
        if curtain.actuator_type == "Curtain":
            curtain.turn_off()
    # Optional: you can add more actions for the movie plan, like turning on the TV, dimming the lights, etc.
    return "Movie plan executed!"


def run_auto_adjust(home):
    logger.info("Start to run the auto adjust function!")
    # Get all the temperature sensors
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    for temp_sensor in temp_sensors:
        temp_sensor.turn_on()  # Turn on the sensor to get reading
        current_temperature = temp_sensor.get_reading()
        room = get_room(home, temp_sensor.room_name)
        # Get all the heaters in the room
        room_heaters = get_room_actuators(room, room.name)
        for heater in room_heaters:
            if heater.actuator_type == "Heater":
                # Adjust the heater based on the current temperature
                heater.adjust_temperature(current_temperature)

        # Get all the ACs in the room
        room_acs = get_room_actuators(room, room.name)
        for ac in room_acs:
            if ac.actuator_type == "AC":
                # Adjust the AC based on the current temperature
                ac.adjust_temperature(current_temperature)

    # Get all the humidity sensors
    humidity_sensors = get_all_sensors(home, "Humidity")
    for humidity_sensor in humidity_sensors:
        humidity_sensor.turn_on()  # Turn on the sensor to get reading
        current_humidity = humidity_sensor.get_reading()
        room = get_room(home, humidity_sensor.room_name)
        # Get all the humidifiers in the room
        room_humidifiers = get_room_actuators(room, room.name)
        for humidifier in room_humidifiers:
            if humidifier.actuator_type == "Humidifier":
                # Adjust the humidifier based on the current humidity
                if current_humidity < HUMIDITY_LOW:
                    humidifier.increase_humidity()
                elif current_humidity > HUMIDITY_HIGH:
                    humidifier.decrease_humidity()

    # Get all the LightIntensive sensors
    light_intensive_sensors = get_all_sensors(home, "LightIntensive")
    for light_intensive_sensor in light_intensive_sensors:
        light_intensive_sensor.turn_on()  # Turn on the sensor to get reading
        current_light_intensive = light_intensive_sensor.get_reading()
        room = get_room(home, light_intensive_sensor.room_name)
        # Get all the lights in the room
        room_lights = get_room_actuators(room, room.name)
        for light in room_lights:
            if light.actuator_type == "Light":
                # Adjust the light based on the current light intensity
                if current_light_intensive < LIGHT_INTENSITY_LOW:
                    light.turn_on()
                    light.set_brightness_level("high")
                elif current_light_intensive > LIGHT_INTENSITY_HIGH:
                    light.turn_off()

    logger.info("Finish the auto adjust function!")


def main():
    # Create the home plan
    home = home_plan()
    # Run the plans
    # morning_plan(home)
    # leave_home_plan(home)
    movie_plan(home)
    # Run the auto adjust function
    # run_auto_adjust(home)

    # You can add more logic here to handle user interactions, schedule plans, etc.

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:** Imports relevant classes and functions from other files.
# 2. **`morning_plan(home)`:** Turns on the coffee machine and makes coffee. You can add more actions for this plan.
# 3. **`leave_home_plan(home)`:** Turns off the lights in the living room. You can add more actions for this plan.
# 4. **`movie_plan(home)`:** Closes the curtains in the bedroom. You can add more actions for this plan.
# 5. **`run_auto_adjust(home)`:** This function handles automatic adjustments based on sensor readings:
#     - It retrieves temperature sensors and adjusts heaters/ACs based on the current temperature.
#     - It retrieves humidity sensors and adjusts humidifiers based on the current humidity.
#     - It retrieves light intensity sensors and adjusts lights based on the current light intensity.
# 6. **`main()`:**
#     - Creates the home plan using `home_plan()`.
#     - Calls the plans or auto adjust function as needed.
#     - You can extend this function to handle user interactions, scheduling, etc.

# **To use this file:**

# 1. Place `function.py` in the `functions` folder.
# 2. Run `python functions/function.py`.
# 3. You can modify the plan functions or add new plans as needed.
# 4. You can customize the auto adjust logic further based on your specific smart home requirements.

# **Remember:** This is a basic framework. You'll need to expand it based on your specific home plan and features. For example:
# - You might need to add more logic for user interaction (e.g., voice commands).
# - You might want to incorporate scheduling to automatically run plans at certain times.
# - You might need to add more actuators or sensors to your home plan.

# Feel free to ask further questions as you develop your smart home project.
