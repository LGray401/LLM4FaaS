from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, \
    LIGHT_INTENSITY_HIGH, TEMP_CHANGE_DURATION_WINDOW
from home.logger_config import logger
from typing import List

# Function for home automation tasks
def main():
    """Main function for home automation."""

    home = home_plan()
    # Example: get all sensors
    # print("Get all Light Intensive sensors")
    # sensors = get_all_sensors(home, "LightIntensive")
    # for sensor in sensors:
    #     print(sensor.id)

    # Example: get all actuators
    # print("Get all lights")
    # actuators = get_all_actuators(home, "Light")
    # for actuator in actuators:
    #     print(actuator.id)

    # Example: turn on a light in the LivingRoom
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     lights = get_room_actuators(home, "LivingRoom")
    #     if lights:
    #         for light in lights:
    #             if light.actuator_type == "Light":
    #                 light.turn_on()

    # Example: set the temperature of the Living Room
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     heaters = get_room_actuators(home, "LivingRoom")
    #     if heaters:
    #         for heater in heaters:
    #             if heater.actuator_type == "Heater":
    #                 heater.set_target_temperature(22)  # Set the target temperature to 22°C

    # Example: adjust the temperature of the Living Room
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     temperature_sensors = get_room_sensors(home, "LivingRoom")
    #     if temperature_sensors:
    #         for sensor in temperature_sensors:
    #             if sensor.sensor_type == "IndoorTemperature":
    #                 current_temperature = sensor.get_reading()
    #                 if current_temperature is not None:
    #                     heaters = get_room_actuators(home, "LivingRoom")
    #                     if heaters:
    #                         for heater in heaters:
    #                             if heater.actuator_type == "Heater":
    #                                 heater.adjust_temperature(current_temperature)

    # Example: control the coffee machine in the kitchen
    # kitchen = get_room(home, "Kitchen")
    # if kitchen:
    #     coffee_machines = get_room_actuators(home, "Kitchen")
    #     if coffee_machines:
    #         for coffee_machine in coffee_machines:
    #             if coffee_machine.actuator_type == "CoffeeMachine":
    #                 coffee_machine.turn_on()
    #                 coffee_machine.make_coffee("Espresso")

    # Example: control the AC in the LivingRoom
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     ac = get_room_actuators(home, "LivingRoom")
    #     if ac:
    #         for ac in ac:
    #             if ac.actuator_type == "AC":
    #                 ac.set_target_temperature(25)
    #                 temperature_sensors = get_room_sensors(home, "LivingRoom")
    #                 if temperature_sensors:
    #                     for sensor in temperature_sensors:
    #                         if sensor.sensor_type == "IndoorTemperature":
    #                             current_temperature = sensor.get_reading()
    #                             if current_temperature is not None:
    #                                 ac.adjust_temperature(current_temperature)
    # Example: control the CleaningRobot in the LivingRoom
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     cleaning_robots = get_room_actuators(home, "LivingRoom")
    #     if cleaning_robots:
    #         for cleaning_robot in cleaning_robots:
    #             if cleaning_robot.actuator_type == "CleaningRobot":
    #                 cleaning_robot.turn_on()
    #                 cleaning_robot.daily_routine()

    # Example: control the Music Player in the LivingRoom
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     music_players = get_room_actuators(home, "LivingRoom")
    #     if music_players:
    #         for music_player in music_players:
    #             if music_player.actuator_type == "MusicPlayer":
    #                 music_player.turn_on()
    #                 music_player.play_music("Pop")

    # Example: control the SmartTV in the LivingRoom
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     smart_tvs = get_room_actuators(home, "LivingRoom")
    #     if smart_tvs:
    #         for smart_tv in smart_tvs:
    #             if smart_tv.actuator_type == "SmartTV":
    #                 smart_tv.turn_on()
    #                 smart_tv.play_channel("CNN")

    # Example: control the NotificationSender in the LivingRoom
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     notification_senders = get_room_actuators(home, "LivingRoom")
    #     if notification_senders:
    #         for notification_sender in notification_senders:
    #             if notification_sender.actuator_type == "NotificationSender":
    #                 notification_sender.turn_on()
    #                 notification_sender.notification_sender("Hello world!")

    # Example: control the SmartSocket in the LivingRoom
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     smart_sockets = get_room_actuators(home, "LivingRoom")
    #     if smart_sockets:
    #         for smart_socket in smart_sockets:
    #             if smart_socket.actuator_type == "SmartSocket":
    #                 smart_socket.turn_on()

    # Example: control the Door in the LivingRoom
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     doors = get_room_actuators(home, "LivingRoom")
    #     if doors:
    #         for door in doors:
    #             if door.actuator_type == "Door":
    #                 door.lock()
    #                 door.unlock()

    # Example: control the Window in the LivingRoom
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     windows = get_room_actuators(home, "LivingRoom")
    #     if windows:
    #         for window in windows:
    #             if window.actuator_type == "Window":
    #                 window.turn_on()
    #                 window.turn_off()

    # Example: control the Curtain in the LivingRoom
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     curtains = get_room_actuators(home, "LivingRoom")
    #     if curtains:
    #         for curtain in curtains:
    #             if curtain.actuator_type == "Curtain":
    #                 curtain.turn_on()
    #                 curtain.turn_off()

    # Example: control the Light in the LivingRoom
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     lights = get_room_actuators(home, "LivingRoom")
    #     if lights:
    #         for light in lights:
    #             if light.actuator_type == "Light":
    #                 light.turn_on()
    #                 light.set_brightness_level("low")
    #                 light.set_brightness_level("medium")
    #                 light.set_brightness_level("high")
    #                 light.turn_off()

    # Example: control the Humidifier in the LivingRoom
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     humidifiers = get_room_actuators(home, "LivingRoom")
    #     if humidifiers:
    #         for humidifier in humidifiers:
    #             if humidifier.actuator_type == "Humidifier":
    #                 humidifier.increase_humidity()
    #                 humidifier.decrease_humidity()

    # Example: temperature control in the Living Room
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     # Get temperature sensor and heater
    #     temperature_sensors = get_room_sensors(home, "LivingRoom")
    #     heaters = get_room_actuators(home, "LivingRoom")
    #     # Check if they exist
    #     if temperature_sensors and heaters:
    #         # Loop through sensors to get temperature
    #         for sensor in temperature_sensors:
    #             if sensor.sensor_type == "IndoorTemperature":
    #                 current_temperature = sensor.get_reading()
    #                 if current_temperature is not None:
    #                     # Adjust heater based on temperature
    #                     for heater in heaters:
    #                         if heater.actuator_type == "Heater":
    #                             heater.adjust_temperature(current_temperature)
    #                             # Simulate temperature change for demonstration
    #                             if heater.status == "on":
    #                                 logger.info(f"Heater is ON, increasing temperature...")
    #                                 time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    #                                 current_temperature += 1
    #                                 logger.info(f"New temperature: {current_temperature}°C")
    #                             else:
    #                                 logger.info(f"Heater is OFF, decreasing temperature...")
    #                                 time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    #                                 current_temperature -= 1
    #                                 logger.info(f"New temperature: {current_temperature}°C")
    #                             heater.adjust_temperature(current_temperature)

    # Example: humidity control in the Living Room
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     # Get humidity sensor and humidifier
    #     humidity_sensors = get_room_sensors(home, "LivingRoom")
    #     humidifiers = get_room_actuators(home, "LivingRoom")
    #     # Check if they exist
    #     if humidity_sensors and humidifiers:
    #         # Loop through sensors to get humidity
    #         for sensor in humidity_sensors:
    #             if sensor.sensor_type == "Humidity":
    #                 current_humidity = sensor.get_reading()
    #                 if current_humidity is not None:
    #                     # Adjust humidifier based on humidity
    #                     for humidifier in humidifiers:
    #                         if humidifier.actuator_type == "Humidifier":
    #                             if current_humidity < HUMIDITY_LOW:
    #                                 humidifier.increase_humidity()
    #                                 logger.info(f"Humidifier is increasing humidity...")
    #                             elif current_humidity > HUMIDITY_HIGH:
    #                                 humidifier.decrease_humidity()
    #                                 logger.info(f"Humidifier is decreasing humidity...")
    #                             else:
    #                                 logger.info(f"Humidity is within range, humidifier is off.")

    # Example: light control in the Living Room
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     # Get light intensity sensor and light
    #     light_intensity_sensors = get_room_sensors(home, "LivingRoom")
    #     lights = get_room_actuators(home, "LivingRoom")
    #     # Check if they exist
    #     if light_intensity_sensors and lights:
    #         # Loop through sensors to get light intensity
    #         for sensor in light_intensity_sensors:
    #             if sensor.sensor_type == "LightIntensive":
    #                 current_light_intensity = sensor.get_reading()
    #                 if current_light_intensity is not None:
    #                     # Adjust light based on light intensity
    #                     for light in lights:
    #                         if light.actuator_type == "Light":
    #                             if current_light_intensity < LIGHT_INTENSITY_LOW:
    #                                 light.turn_on()
    #                                 logger.info(f"Light is turning ON...")
    #                                 light.set_brightness_level("high")
    #                             elif current_light_intensity > LIGHT_INTENSITY_HIGH:
    #                                 light.turn_off()
    #                                 logger.info(f"Light is turning OFF...")
    #                             else:
    #                                 logger.info(f"Light intensity is within range, light is off.")

    # Example: smart home automation scenario
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     # Get temperature sensor, heater, and AC
    #     temperature_sensors = get_room_sensors(home, "LivingRoom")
    #     heaters = get_room_actuators(home, "LivingRoom")
    #     acs = get_room_actuators(home, "LivingRoom")
    #     # Check if they exist
    #     if temperature_sensors and heaters and acs:
    #         # Loop through sensors to get temperature
    #         for sensor in temperature_sensors:
    #             if sensor.sensor_type == "IndoorTemperature":
    #                 current_temperature = sensor.get_reading()
    #                 if current_temperature is not None:
    #                     # Adjust heater and AC based on temperature
    #                     for heater in heaters:
    #                         if heater.actuator_type == "Heater":
    #                             heater.adjust_temperature(current_temperature)
    #                     for ac in acs:
    #                         if ac.actuator_type == "AC":
    #                             ac.adjust_temperature(current_temperature)
    #                     # Simulate temperature change for demonstration
    #                     if current_temperature < TEMP_LOW:
    #                         logger.info(f"Temperature is too low, heater is turning ON...")
    #                         time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    #                         current_temperature += 1
    #                         logger.info(f"New temperature: {current_temperature}°C")
    #                     elif current_temperature > TEMP_HIGH:
    #                         logger.info(f"Temperature is too high, AC is turning ON...")
    #                         time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    #                         current_temperature -= 1
    #                         logger.info(f"New temperature: {current_temperature}°C")
    #                     else:
    #                         logger.info(f"Temperature is comfortable, heater and AC are off.")

    # Example: smart home automation scenario with multiple sensors and actuators
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     # Get sensors and actuators
    #     temperature_sensors = get_room_sensors(home, "LivingRoom")
    #     humidity_sensors = get_room_sensors(home, "LivingRoom")
    #     light_intensity_sensors = get_room_sensors(home, "LivingRoom")
    #     heaters = get_room_actuators(home, "LivingRoom")
    #     acs = get_room_actuators(home, "LivingRoom")
    #     lights = get_room_actuators(home, "LivingRoom")
    #     # Check if they exist
    #     if temperature_sensors and humidity_sensors and light_intensity_sensors and heaters and acs and lights:
    #         # Loop through sensors to get readings
    #         for sensor in temperature_sensors:
    #             if sensor.sensor_type == "IndoorTemperature":
    #                 current_temperature = sensor.get_reading()
    #                 if current_temperature is not None:
    #                     # Adjust heater and AC based on temperature
    #                     for heater in heaters:
    #                         if heater.actuator_type == "Heater":
    #                             heater.adjust_temperature(current_temperature)
    #                     for ac in acs:
    #                         if ac.actuator_type == "AC":
    #                             ac.adjust_temperature(current_temperature)
    #         for sensor in humidity_sensors:
    #             if sensor.sensor_type == "Humidity":
    #                 current_humidity = sensor.get_reading()
    #                 if current_humidity is not None:
    #                     # Adjust humidifier based on humidity
    #                     for humidifier in humidifiers:
    #                         if humidifier.actuator_type == "Humidifier":
    #                             if current_humidity < HUMIDITY_LOW:
    #                                 humidifier.increase_humidity()
    #                                 logger.info(f"Humidifier is increasing humidity...")
    #                             elif current_humidity > HUMIDITY_HIGH:
    #                                 humidifier.decrease_humidity()
    #                                 logger.info(f"Humidifier is decreasing humidity...")
    #                             else:
    #                                 logger.info(f"Humidity is within range, humidifier is off.")
    #         for sensor in light_intensity_sensors:
    #             if sensor.sensor_type == "LightIntensive":
    #                 current_light_intensity = sensor.get_reading()
    #                 if current_light_intensity is not None:
    #                     # Adjust light based on light intensity
    #                     for light in lights:
    #                         if light.actuator_type == "Light":
    #                             if current_light_intensity < LIGHT_INTENSITY_LOW:
    #                                 light.turn_on()
    #                                 logger.info(f"Light is turning ON...")
    #                                 light.set_brightness_level("high")
    #                             elif current_light_intensity > LIGHT_INTENSITY_HIGH:
    #                                 light.turn_off()
    #                                 logger.info(f"Light is turning OFF...")
    #                             else:
    #                                 logger.info(f"Light intensity is within range, light is off.")
    #                     # Simulate sensor readings for demonstration
    #                     if current_temperature < TEMP_LOW:
    #                         logger.info(f"Temperature is too low, heater is turning ON...")
    #                         time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    #                         current_temperature += 1
    #                         logger.info(f"New temperature: {current_temperature}°C")
    #                     elif current_temperature > TEMP_HIGH:
    #                         logger.info(f"Temperature is too high, AC is turning ON...")
    #                         time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    #                         current_temperature -= 1
    #                         logger.info(f"New temperature: {current_temperature}°C")
    #                     else:
    #                         logger.info(f"Temperature is comfortable, heater and AC are off.")
    #                     if current_humidity < HUMIDITY_LOW:
    #                         logger.info(f"Humidity is too low, humidifier is turning ON...")
    #                         time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    #                         current_humidity += 1
    #                         logger.info(f"New humidity: {current_humidity}%")
    #                     elif current_humidity > HUMIDITY_HIGH:
    #                         logger.info(f"Humidity is too high, humidifier is turning OFF...")
    #                         time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    #                         current_humidity -= 1
    #                         logger.info(f"New humidity: {current_humidity}%")
    #                     else:
    #                         logger.info(f"Humidity is comfortable, humidifier is off.")
    #                     if current_light_intensity < LIGHT_INTENSITY_LOW:
    #                         logger.info(f"Light intensity is too low, light is turning ON...")
    #                         time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    #                         current_light_intensity += 100
    #                         logger.info(f"New light intensity: {current_light_intensity} lux")
    #                     elif current_light_intensity > LIGHT_INTENSITY_HIGH:
    #                         logger.info(f"Light intensity is too high, light is turning OFF...")
    #                         time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    #                         current_light_intensity -= 100
    #                         logger.info(f"New light intensity: {current_light_intensity} lux")
    #                     else:
    #                         logger.info(f"Light intensity is comfortable, light is off.")
    #                     # Adjust heater, AC, and light based on new sensor readings
    #                     for heater in heaters:
    #                         if heater.actuator_type == "Heater":
    #                             heater.adjust_temperature(current_temperature)
    #                     for ac in acs:
    #                         if ac.actuator_type == "AC":
    #                             ac.adjust_temperature(current_temperature)
    #                     for light in lights:
    #                         if light.actuator_type == "Light":
    #                             if current_light_intensity < LIGHT_INTENSITY_LOW:
    #                                 light.turn_on()
    #                                 light.set_brightness_level("high")
    #                             elif current_light_intensity > LIGHT_INTENSITY_HIGH:
    #                                 light.turn_off()

if __name__ == "__main__":
    main()

# This function.py file demonstrates various examples of how to use the sensor and actuator classes in your project. It includes:

# - **Getting all sensors/actuators of a specific type**
# - **Turning on a light in a specific room**
# - **Setting the target temperature for a heater in a specific room**
# - **Adjusting the temperature of a heater based on current temperature readings**
# - **Controlling the coffee machine in the kitchen**
# - **Controlling the AC in the living room**
# - **Controlling the cleaning robot in the living room**
# - **Controlling the music player in the living room**
# - **Controlling the smart TV in the living room**
# - **Controlling the notification sender in the living room**
# - **Controlling the smart socket in the living room**
# - **Controlling the door in the living room**
# - **Controlling the window in the living room**
# - **Controlling the curtain in the living room**
# - **Controlling the light in the living room**
# - **Controlling the humidifier in the living room**
# - **Temperature control in the living room**
# - **Humidity control in the living room**
# - **Light control in the living room**
# - **Smart home automation scenario**
# - **Smart home automation scenario with multiple sensors and actuators**

# You can use these examples as a starting point and adapt them to fit the specific needs of your smart home project.
