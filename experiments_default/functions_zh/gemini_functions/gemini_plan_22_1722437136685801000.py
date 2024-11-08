from home.home_plan import home_plan, get_room, get_room_actuators, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def morning_plan(home):
    """Executes the morning plan for the smart home."""

    # Get the bedroom room
    bedroom = get_room(home, "Bedroom")

    # Turn on the bedroom light
    bedroom_lights = get_room_actuators(home, "Bedroom")
    for light in bedroom_lights:
        if light.actuator_type == "Light":
            light.turn_on()

    # Open the bedroom window
    for window in bedroom_lights:
        if window.actuator_type == "Window":
            window.turn_on()

    # Set the music player to play at 6 am
    music_players = get_all_actuators(home, "MusicPlayer")
    for music_player in music_players:
        music_player.play_music("Morning playlist")

    # Turn on the coffee machine
    kitchen = get_room(home, "Kitchen")
    kitchen_actuators = get_room_actuators(home, "Kitchen")
    for actuator in kitchen_actuators:
        if actuator.actuator_type == "CoffeeMachine":
            actuator.turn_on()
            actuator.make_coffee("Espresso")

    logger.info("Morning plan executed successfully.")
    print("Morning plan executed successfully.")


def leave_home_plan(home):
    """Executes the leave home plan for the smart home."""

    # Turn off all lights in the house
    all_lights = get_all_actuators(home, "Light")
    for light in all_lights:
        light.turn_off()

    # Lock the front door
    front_door = get_room_actuators(home, "LivingRoom")
    for door in front_door:
        if door.actuator_type == "Door":
            door.lock()

    # Turn off all smart sockets
    all_sockets = get_all_actuators(home, "SmartSocket")
    for socket in all_sockets:
        socket.turn_off()

    logger.info("Leave home plan executed successfully.")
    print("Leave home plan executed successfully.")


def movie_plan(home):
    """Executes the movie plan for the smart home."""

    # Get the living room room
    living_room = get_room(home, "LivingRoom")

    # Close the living room curtains
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    for curtain in living_room_actuators:
        if curtain.actuator_type == "Curtain":
            curtain.turn_on()

    # Dim the living room lights
    for light in living_room_actuators:
        if light.actuator_type == "Light":
            light.set_brightness_level("low")

    # Turn on the TV and play a movie
    for tv in living_room_actuators:
        if tv.actuator_type == "SmartTV":
            tv.turn_on()
            tv.play_channel("Netflix")

    logger.info("Movie plan executed successfully.")
    print("Movie plan executed successfully.")


def temperature_control(home):
    """Controls the temperature in the home based on sensor readings."""

    # Get all indoor temperature sensors
    all_indoor_temp_sensors = get_all_actuators(home, "IndoorTemperature")

    # Iterate through each temperature sensor
    for sensor in all_indoor_temp_sensors:
        current_temp = sensor.get_reading()

        # Get the room the sensor is in
        room = get_room(home, sensor.room_name)

        # Get the heater and AC for the room
        room_actuators = get_room_actuators(home, sensor.room_name)
        heater = None
        ac = None
        for actuator in room_actuators:
            if actuator.actuator_type == "Heater":
                heater = actuator
            elif actuator.actuator_type == "AC":
                ac = actuator

        # Adjust the heater and AC based on the temperature
        if heater:
            if current_temp < TEMP_LOW:
                heater.turn_on()
                heater.set_target_temperature(TEMP_HIGH)
            else:
                heater.turn_off()
        if ac:
            if current_temp > TEMP_HIGH:
                ac.turn_on()
                ac.set_target_temperature(TEMP_LOW)
            else:
                ac.turn_off()

        logger.info(f"Temperature control in {room.name}: Current temperature is {current_temp}°C. "
                    f"Heater is {'on' if heater and heater.status == 'on' else 'off'}. "
                    f"AC is {'on' if ac and ac.status == 'on' else 'off'}.")
        print(f"Temperature control in {room.name}: Current temperature is {current_temp}°C. "
              f"Heater is {'on' if heater and heater.status == 'on' else 'off'}. "
              f"AC is {'on' if ac and ac.status == 'on' else 'off'}.")

def humidity_control(home):
    """Controls the humidity in the home based on sensor readings."""

    # Get all humidity sensors
    all_humidity_sensors = get_all_actuators(home, "Humidity")

    # Iterate through each humidity sensor
    for sensor in all_humidity_sensors:
        current_humidity = sensor.get_reading()

        # Get the room the sensor is in
        room = get_room(home, sensor.room_name)

        # Get the humidifier for the room
        room_actuators = get_room_actuators(home, sensor.room_name)
        humidifier = None
        for actuator in room_actuators:
            if actuator.actuator_type == "Humidifier":
                humidifier = actuator

        # Adjust the humidifier based on the humidity
        if humidifier:
            if current_humidity < HUMIDITY_LOW:
                humidifier.increase_humidity()
            elif current_humidity > HUMIDITY_HIGH:
                humidifier.decrease_humidity()

        logger.info(f"Humidity control in {room.name}: Current humidity is {current_humidity}%. "
                    f"Humidifier is {'on' if humidifier and humidifier.status == 'on' else 'off'}.")
        print(f"Humidity control in {room.name}: Current humidity is {current_humidity}%. "
              f"Humidifier is {'on' if humidifier and humidifier.status == 'on' else 'off'}.")


def light_intensity_control(home):
    """Controls the light intensity in the home based on sensor readings."""

    # Get all light intensity sensors
    all_light_intensity_sensors = get_all_actuators(home, "LightIntensive")

    # Iterate through each light intensity sensor
    for sensor in all_light_intensity_sensors:
        current_light_intensity = sensor.get_reading()

        # Get the room the sensor is in
        room = get_room(home, sensor.room_name)

        # Get the lights for the room
        room_actuators = get_room_actuators(home, sensor.room_name)
        lights = []
        for actuator in room_actuators:
            if actuator.actuator_type == "Light":
                lights.append(actuator)

        # Adjust the lights based on the light intensity
        for light in lights:
            if current_light_intensity < LIGHT_INTENSITY_LOW:
                light.turn_on()
                light.set_brightness_level("high")
            elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                light.turn_off()

        logger.info(f"Light intensity control in {room.name}: Current light intensity is {current_light_intensity} lux. "
                    f"Lights are {'on' if lights and any(light.status == 'on' for light in lights) else 'off'}.")
        print(f"Light intensity control in {room.name}: Current light intensity is {current_light_intensity} lux. "
              f"Lights are {'on' if lights and any(light.status == 'on' for light in lights) else 'off'}.")


def main():
    """Main function for the smart home system."""
    home = home_plan()
    # print(home)

    # Execute the morning plan
    morning_plan(home)

    # Execute the leave home plan
    leave_home_plan(home)

    # Execute the movie plan
    movie_plan(home)

    # Control the temperature in the home
    temperature_control(home)

    # Control the humidity in the home
    humidity_control(home)

    # Control the light intensity in the home
    light_intensity_control(home)


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:**
#    - `home.home_plan`: Imports functions for creating the home plan, getting rooms, actuators, and sensors.
#    - `home.config`: Imports configuration parameters like temperature, humidity, and light intensity thresholds.
#    - `home.logger_config`: Imports the logger for logging events and messages.

# 2. **Plan Functions:**
#    - `morning_plan(home)`: Turns on bedroom lights, opens the bedroom window, sets a morning playlist, and starts the coffee machine.
#    - `leave_home_plan(home)`: Turns off all lights, locks the front door, and turns off all smart sockets.
#    - `movie_plan(home)`: Closes the living room curtains, dims the lights, turns on the TV, and starts playing Netflix.

# 3. **Control Functions:**
#    - `temperature_control(home)`: Controls the temperature in each room by turning on heaters when it's too cold and ACs when it's too hot.
#    - `humidity_control(home)`: Controls humidity by adjusting humidifiers in rooms based on sensor readings.
#    - `light_intensity_control(home)`: Controls light intensity by turning on/off lights based on sensor readings.

# 4. **`main()` function:**
#    - Creates the home plan.
#    - Executes the morning, leave home, and movie plans.
#    - Calls the control functions to adjust temperature, humidity, and light intensity based on sensor data.

# **Key points:**

# - The code uses functions to encapsulate different actions (plans and controls).
# - It utilizes the provided `home.home_plan` module to get information about the home, rooms, and devices.
# - It interacts with actuators to perform actions like turning on/off lights, adjusting temperature, and playing music.
# - It uses the logger to record events and messages for debugging and troubleshooting.

# **To run the code:**

# 1. Make sure you have the `home` folder with the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files in the same directory as `function.py`.
# 2. Run the `function.py` file from your terminal using the command `python function.py`.