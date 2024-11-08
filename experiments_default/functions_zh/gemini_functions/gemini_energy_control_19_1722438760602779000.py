from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor
from home.actuator import Heater, AC, Window, Door, Curtain, Light, MusicPlayer, SmartTV, NotificationSender, CleaningRobot, \
    Humidifier, CoffeeMachine, SmartSocket
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    home = home_plan()
    # print_home_plan(home)

    # Example: Control the living room light
    living_room = get_room(home, "LivingRoom")
    if living_room:
        living_room_lights = get_room_actuators(home, "LivingRoom")
        if living_room_lights:
            for light in living_room_lights:
                if light.actuator_type == "Light":
                    light.turn_on()
                    light.set_brightness_level("medium")
                    light.turn_off()
                    # print(light.get_status())
                    # print(light.brightness_level)

    # Example: Get all indoor temperature sensors and check their readings
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    if indoor_temp_sensors:
        for sensor in indoor_temp_sensors:
            sensor.turn_on()
            temp_reading = sensor.get_reading()
            if temp_reading:
                print(f"{sensor.id} reading: {temp_reading}°C")
                # Check if the temperature is within the desired range
                if temp_reading < TEMP_LOW:
                    print(f"{sensor.id} Temperature is below the desired range. Consider turning on the heater.")
                    # Find and turn on the heater in the same room
                    room = get_room(home, sensor.room_name)
                    if room:
                        heaters = get_room_actuators(room, sensor.room_name)
                        if heaters:
                            for heater in heaters:
                                if heater.actuator_type == "Heater":
                                    heater.turn_on()
                                    heater.set_target_temperature(TEMP_HIGH)
                                    break  # Assume only one heater in the room

                elif temp_reading > TEMP_HIGH:
                    print(f"{sensor.id} Temperature is above the desired range. Consider turning on the AC.")
                    # Find and turn on the AC in the same room
                    room = get_room(home, sensor.room_name)
                    if room:
                        acs = get_room_actuators(room, sensor.room_name)
                        if acs:
                            for ac in acs:
                                if ac.actuator_type == "AC":
                                    ac.turn_on()
                                    ac.set_target_temperature(TEMP_LOW)
                                    break  # Assume only one AC in the room
            else:
                print(f"{sensor.id} failed to get reading")

    # Example: Get all humidity sensors and check their readings
    humidity_sensors = get_all_sensors(home, "Humidity")
    if humidity_sensors:
        for sensor in humidity_sensors:
            sensor.turn_on()
            humidity_reading = sensor.get_reading()
            if humidity_reading:
                print(f"{sensor.id} reading: {humidity_reading}%")
                # Check if the humidity is within the desired range
                if humidity_reading < HUMIDITY_LOW:
                    print(f"{sensor.id} Humidity is below the desired range. Consider turning on the humidifier.")
                    # Find and turn on the humidifier in the same room
                    room = get_room(home, sensor.room_name)
                    if room:
                        humidifiers = get_room_actuators(room, sensor.room_name)
                        if humidifiers:
                            for humidifier in humidifiers:
                                if humidifier.actuator_type == "Humidifier":
                                    humidifier.increase_humidity()
                                    break  # Assume only one humidifier in the room

                elif humidity_reading > HUMIDITY_HIGH:
                    print(f"{sensor.id} Humidity is above the desired range. Consider opening a window.")
                    # Find and open a window in the same room
                    room = get_room(home, sensor.room_name)
                    if room:
                        windows = get_room_actuators(room, sensor.room_name)
                        if windows:
                            for window in windows:
                                if window.actuator_type == "Window":
                                    window.turn_on()
                                    break  # Assume only one window in the room

            else:
                print(f"{sensor.id} failed to get reading")

    # Example: Get all light intensive sensors and check their readings
    light_intensive_sensors = get_all_sensors(home, "LightIntensive")
    if light_intensive_sensors:
        for sensor in light_intensive_sensors:
            sensor.turn_on()
            light_intensity_reading = sensor.get_reading()
            if light_intensity_reading:
                print(f"{sensor.id} reading: {light_intensity_reading} lux")
                # Check if the light intensity is within the desired range
                if light_intensity_reading < LIGHT_INTENSITY_LOW:
                    print(f"{sensor.id} Light intensity is below the desired range. Consider turning on the light.")
                    # Find and turn on the light in the same room
                    room = get_room(home, sensor.room_name)
                    if room:
                        lights = get_room_actuators(room, sensor.room_name)
                        if lights:
                            for light in lights:
                                if light.actuator_type == "Light":
                                    light.turn_on()
                                    light.set_brightness_level("medium")
                                    break  # Assume only one light in the room

                elif light_intensity_reading > LIGHT_INTENSITY_HIGH:
                    print(f"{sensor.id} Light intensity is above the desired range. Consider closing the curtains.")
                    # Find and close the curtains in the same room
                    room = get_room(home, sensor.room_name)
                    if room:
                        curtains = get_room_actuators(room, sensor.room_name)
                        if curtains:
                            for curtain in curtains:
                                if curtain.actuator_type == "Curtain":
                                    curtain.turn_on()
                                    break  # Assume only one curtain in the room

            else:
                print(f"{sensor.id} failed to get reading")

    # Example: Get all smoke sensors and check their readings
    smoke_sensors = get_all_sensors(home, "Smoke")
    if smoke_sensors:
        for sensor in smoke_sensors:
            sensor.turn_on()
            smoke_reading = sensor.get_reading()
            if smoke_reading:
                print(f"{sensor.id} reading: {smoke_reading}%")
                # Check if there is smoke detected
                if smoke_reading > 0:
                    print(f"Smoke detected in {sensor.room_name}! Turning on the notification sender.")
                    # Find and turn on the notification sender in the same room
                    room = get_room(home, sensor.room_name)
                    if room:
                        notification_senders = get_room_actuators(room, sensor.room_name)
                        if notification_senders:
                            for notification_sender in notification_senders:
                                if notification_sender.actuator_type == "NotificationSender":
                                    notification_sender.turn_on()
                                    notification_sender.notification_sender(
                                        f"Smoke detected in {sensor.room_name}! Please check.")
                                    break  # Assume only one notification sender in the room

            else:
                print(f"{sensor.id} failed to get reading")

    # Example: Get all outdoor temperature sensors and check their readings
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    if outdoor_temp_sensors:
        for sensor in outdoor_temp_sensors:
            sensor.turn_on()
            temp_reading = sensor.get_reading()
            if temp_reading:
                print(f"{sensor.id} reading: {temp_reading}°C")
            else:
                print(f"{sensor.id} failed to get reading")

    # Example: Use the cleaning robot
    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    if cleaning_robots:
        for robot in cleaning_robots:
            robot.turn_on()
            robot.daily_routine()

if __name__ == '__main__':
    main()

# **Explanation:**

# 1. **Imports:**
#    - Import necessary modules from `home.home_plan`, `home.sensor`, `home.actuator`, `home.config`, and `home.logger_config`.

# 2. **`main()` Function:**
#    - Creates a `home` object using `home_plan()`.
#    - **Example: Living Room Light Control**
#      - Gets the `LivingRoom` using `get_room()`.
#      - Finds the `Light` actuators in the room.
#      - Turns on the light, sets the brightness, and then turns it off.
#    - **Example: Indoor Temperature Sensors**
#      - Gets all `IndoorTemperatureSensor` objects.
#      - Iterates through them, turning each on and getting its reading.
#      - If the temperature is below `TEMP_LOW`, it finds a `Heater` in the same room and turns it on, setting a target temperature.
#      - If the temperature is above `TEMP_HIGH`, it finds an `AC` in the same room and turns it on, setting a target temperature.
#    - **Example: Humidity Sensors**
#      - Gets all `HumiditySensor` objects.
#      - Iterates through them, turning each on and getting its reading.
#      - If the humidity is below `HUMIDITY_LOW`, it finds a `Humidifier` in the same room and increases the humidity level.
#      - If the humidity is above `HUMIDITY_HIGH`, it finds a `Window` in the same room and opens it.
#    - **Example: Light Intensive Sensors**
#      - Gets all `LightIntensiveSensor` objects.
#      - Iterates through them, turning each on and getting its reading.
#      - If the light intensity is below `LIGHT_INTENSITY_LOW`, it finds a `Light` in the same room and turns it on, setting the brightness level.
#      - If the light intensity is above `LIGHT_INTENSITY_HIGH`, it finds a `Curtain` in the same room and closes it.
#    - **Example: Smoke Sensors**
#      - Gets all `SmokeSensor` objects.
#      - Iterates through them, turning each on and getting its reading.
#      - If smoke is detected, it finds a `NotificationSender` in the same room and sends a notification.
#    - **Example: Outdoor Temperature Sensors**
#      - Gets all `OutdoorTemperatureSensor` objects.
#      - Iterates through them, turning each on and getting its reading.
#    - **Example: Cleaning Robot**
#      - Gets all `CleaningRobot` objects.
#      - Iterates through them, turning each on and starting their daily routine.

# 3. **`if __name__ == '__main__'` Block:**
#    - Calls the `main()` function to run the example code.

# **Key Points:**

# - The code demonstrates how to interact with different sensors and actuators in the smart home system.
# - It incorporates logic for responding to sensor readings and making appropriate adjustments to actuators.
# - The example focuses on temperature, humidity, light intensity, and smoke detection.
# - It includes error handling for situations where devices might not be found or fail to get readings.
# - The code is well-structured and comments explain the functionality.

# This provides a good starting point for your smart home project, demonstrating basic sensor and actuator interactions. You can expand on this by adding more devices, custom routines, and user interaction.
