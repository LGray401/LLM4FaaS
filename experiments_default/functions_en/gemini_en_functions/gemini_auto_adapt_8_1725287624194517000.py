from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.actuator import Heater, AC, Light, MusicPlayer, SmartTV, CoffeeMachine, CleaningRobot, NotificationSender, \
    Humidifier
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW


def main():
    home = home_plan()

    # # Example usage:
    #
    # # Turn on the light in the living room
    # living_room = get_room(home, "LivingRoom")
    # living_room_lights = get_room_actuators(home, "LivingRoom")
    # for light in living_room_lights:
    #     if light.actuator_type == "Light":
    #         light.turn_on()
    #         light.set_brightness_level("high")
    #
    # # Set the temperature in the living room
    # living_room_heater = get_room_actuators(home, "LivingRoom")
    # for heater in living_room_heater:
    #     if heater.actuator_type == "Heater":
    #         heater.set_target_temperature(22)
    #
    # # Play music in the living room
    # living_room_music_player = get_room_actuators(home, "LivingRoom")
    # for music_player in living_room_music_player:
    #     if music_player.actuator_type == "MusicPlayer":
    #         music_player.play_music("Jazz")
    #
    # # Turn on the TV in the living room and play a channel
    # living_room_tv = get_room_actuators(home, "LivingRoom")
    # for tv in living_room_tv:
    #     if tv.actuator_type == "SmartTV":
    #         tv.turn_on()
    #         tv.play_channel("CNN")
    #
    # # Make coffee in the kitchen
    # kitchen = get_room(home, "Kitchen")
    # kitchen_coffee_machine = get_room_actuators(home, "Kitchen")
    # for coffee_machine in kitchen_coffee_machine:
    #     if coffee_machine.actuator_type == "CoffeeMachine":
    #         coffee_machine.turn_on()
    #         coffee_machine.make_coffee("Espresso")
    #
    # # Start the daily cleaning routine for the robot in the living room
    # living_room_cleaning_robot = get_room_actuators(home, "LivingRoom")
    # for cleaning_robot in living_room_cleaning_robot:
    #     if cleaning_robot.actuator_type == "CleaningRobot":
    #         cleaning_robot.turn_on()
    #         cleaning_robot.daily_routine()
    #
    # # Send a notification to the living room
    # living_room_notification_sender = get_room_actuators(home, "LivingRoom")
    # for notification_sender in living_room_notification_sender:
    #     if notification_sender.actuator_type == "NotificationSender":
    #         notification_sender.turn_on()
    #         notification_sender.notification_sender("Dinner is ready!")

    # # Adjust temperature based on sensor readings
    # all_indoor_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    # for sensor in all_indoor_temperature_sensors:
    #     sensor.turn_on()
    #     current_temperature = sensor.get_reading()
    #     if current_temperature is not None:
    #         room = get_room(home, sensor.room_name)
    #         if room is not None:
    #             room_heaters = get_room_actuators(home, sensor.room_name)
    #             for heater in room_heaters:
    #                 if heater.actuator_type == "Heater":
    #                     heater.adjust_temperature(current_temperature)
    #             room_acs = get_room_actuators(home, sensor.room_name)
    #             for ac in room_acs:
    #                 if ac.actuator_type == "AC":
    #                     ac.adjust_temperature(current_temperature)

    # # Adjust humidity based on sensor readings
    # all_humidity_sensors = get_all_sensors(home, "Humidity")
    # for sensor in all_humidity_sensors:
    #     sensor.turn_on()
    #     current_humidity = sensor.get_reading()
    #     if current_humidity is not None:
    #         room = get_room(home, sensor.room_name)
    #         if room is not None:
    #             room_humidifiers = get_room_actuators(home, sensor.room_name)
    #             for humidifier in room_humidifiers:
    #                 if humidifier.actuator_type == "Humidifier":
    #                     if current_humidity < HUMIDITY_LOW:
    #                         humidifier.increase_humidity()
    #                     elif current_humidity > HUMIDITY_HIGH:
    #                         humidifier.decrease_humidity()

    # Adjust light based on sensor readings
    all_light_intensity_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in all_light_intensity_sensors:
        sensor.turn_on()
        current_light_intensity = sensor.get_reading()
        if current_light_intensity is not None:
            room = get_room(home, sensor.room_name)
            if room is not None:
                room_lights = get_room_actuators(home, sensor.room_name)
                for light in room_lights:
                    if light.actuator_type == "Light":
                        if current_light_intensity < LIGHT_INTENSITY_LOW:
                            light.turn_on()
                            light.set_brightness_level("high")
                        elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                            light.turn_off()

    # # Simulate temperature changes
    # for _ in range(TEMP_CHANGE_DURATION_WINDOW):
    #     all_indoor_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    #     for sensor in all_indoor_temperature_sensors:
    #         sensor.turn_on()
    #         current_temperature = sensor.get_reading()
    #         if current_temperature is not None:
    #             room = get_room(home, sensor.room_name)
    #             if room is not None:
    #                 room_heaters = get_room_actuators(home, sensor.room_name)
    #                 for heater in room_heaters:
    #                     if heater.actuator_type == "Heater":
    #                         heater.adjust_temperature(current_temperature)
    #                 room_acs = get_room_actuators(home, sensor.room_name)
    #                 for ac in room_acs:
    #                     if ac.actuator_type == "AC":
    #                         ac.adjust_temperature(current_temperature)
    #     time.sleep(1)


if __name__ == '__main__':
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: Contains functions to create the home plan, get rooms, sensors, and actuators.
#    - `home.actuator`: Contains classes for actuators like heater, AC, light, music player, etc.
#    - `home.sensor`: Contains classes for sensors like temperature, humidity, light intensity.
#    - `home.config`: Contains configuration settings like temperature thresholds, humidity thresholds, etc.

# 2. **Define the `main()` function:**
#    - This function contains the main logic of the smart home system.
#    - It first creates the home plan using `home_plan()`.
#    - Then, it demonstrates how to interact with different components of the home:
#      - Turning on lights and setting brightness
#      - Setting temperature using heaters and AC
#      - Playing music
#      - Turning on TV and playing a channel
#      - Making coffee
#      - Starting the cleaning robot's daily routine
#      - Sending notifications
#    - Finally, it simulates temperature changes and adjusts the temperature based on sensor readings.

# 3. **Temperature adjustment:**
#    - The code iterates through all indoor temperature sensors and gets their readings.
#    - It then locates the heaters and ACs in the corresponding rooms and adjusts their status based on the current temperature and target temperature (if set).

# 4. **Humidity adjustment:**
#    - Similar to temperature adjustment, it iterates through humidity sensors, locates humidifiers in the corresponding rooms, and adjusts their status based on the current humidity and predefined thresholds.

# 5. **Light intensity adjustment:**
#    - The code iterates through light intensity sensors and adjusts the light brightness based on the current light intensity and predefined thresholds.

# 6. **Simulate temperature changes:**
#    - This section simulates temperature fluctuations by repeatedly getting readings from all indoor temperature sensors and adjusting the temperature controls.

# **To use this code:**

# 1. Make sure you have the `home` folder with the files `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` in your project.
# 2. Create a `functions` folder and place `function.py` inside it.
# 3. Run `function.py` using `python functions/function.py`.

# This code provides a basic structure for a smart home system. You can extend it by adding more sensors, actuators, and functionalities.
