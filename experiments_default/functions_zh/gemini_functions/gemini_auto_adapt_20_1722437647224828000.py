from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import AC, Heater, Light, NotificationSender, MusicPlayer, CleaningRobot, SmartTV, CoffeeMachine, \
    Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW
from home.logger_config import logger
import time

def main():
    # Create the home plan
    home = home_plan()
    print_home_plan(home)

    # Define a dictionary to store the status of sensors
    sensor_status = {}

    # Function to update sensor status
    def update_sensor_status(sensor):
        reading = sensor.get_reading()
        if reading is not None:
            sensor_status[sensor.id] = reading
        else:
            sensor_status[sensor.id] = "OFF"

    # Define a dictionary to store the status of actuators
    actuator_status = {}

    # Function to update actuator status
    def update_actuator_status(actuator):
        actuator_status[actuator.id] = actuator.get_status()

    # Function to control temperature
    def control_temperature(room_name):
        indoor_temp_sensor = get_room_sensors(home, room_name)[0]  # Assuming only one indoor temperature sensor per room
        update_sensor_status(indoor_temp_sensor)
        ac = get_room_actuators(home, room_name)[0]  # Assuming only one AC per room
        heater = get_room_actuators(home, room_name)[1]  # Assuming only one heater per room

        # Check if the AC is already on
        if ac.get_status() == "on":
            print(f"AC in {room_name} is already on.")
            logger.info(f"AC in {room_name} is already on.")
        else:
            # Check the temperature
            temperature = sensor_status[indoor_temp_sensor.id]
            if temperature > TEMP_HIGH:
                print(f"Temperature in {room_name} is {temperature}°C, turning on AC.")
                logger.info(f"Temperature in {room_name} is {temperature}°C, turning on AC.")
                ac.turn_on()
                ac.set_target_temperature(TEMP_HIGH)

        # Check if the heater is already on
        if heater.get_status() == "on":
            print(f"Heater in {room_name} is already on.")
            logger.info(f"Heater in {room_name} is already on.")
        else:
            # Check the temperature
            temperature = sensor_status[indoor_temp_sensor.id]
            if temperature < TEMP_LOW:
                print(f"Temperature in {room_name} is {temperature}°C, turning on heater.")
                logger.info(f"Temperature in {room_name} is {temperature}°C, turning on heater.")
                heater.turn_on()
                heater.set_target_temperature(TEMP_LOW)

    # Function to control humidity
    def control_humidity(room_name):
        humidity_sensor = get_room_sensors(home, room_name)[0]  # Assuming only one humidity sensor per room
        update_sensor_status(humidity_sensor)
        humidifier = get_room_actuators(home, room_name)[0]  # Assuming only one humidifier per room

        # Check the humidity
        humidity = sensor_status[humidity_sensor.id]
        if humidity < HUMIDITY_LOW:
            print(f"Humidity in {room_name} is {humidity}%, turning on humidifier.")
            logger.info(f"Humidity in {room_name} is {humidity}%, turning on humidifier.")
            humidifier.increase_humidity()

    # Function to control light intensity
    def control_light_intensity(room_name):
        light_sensor = get_room_sensors(home, room_name)[0]  # Assuming only one light intensity sensor per room
        update_sensor_status(light_sensor)
        light = get_room_actuators(home, room_name)[0]  # Assuming only one light per room

        # Check the light intensity
        light_intensity = sensor_status[light_sensor.id]
        if light_intensity < LIGHT_INTENSITY_LOW:
            print(f"Light intensity in {room_name} is {light_intensity} lux, turning on light.")
            logger.info(f"Light intensity in {room_name} is {light_intensity} lux, turning on light.")
            light.turn_on()
            light.set_brightness_level("high")

    # Function to control coffee machine
    def control_coffee_machine(room_name):
        coffee_machine = get_room_actuators(home, room_name)[0]  # Assuming only one coffee machine per room
        update_actuator_status(coffee_machine)

        if coffee_machine.get_status() == "on":
            print(f"Coffee machine in {room_name} is already on.")
            logger.info(f"Coffee machine in {room_name} is already on.")
        else:
            print(f"Turning on coffee machine in {room_name}")
            logger.info(f"Turning on coffee machine in {room_name}")
            coffee_machine.turn_on()
            coffee_machine.make_coffee("Espresso")

    # Function to control music player
    def control_music_player(room_name):
        music_player = get_room_actuators(home, room_name)[0]  # Assuming only one music player per room
        update_actuator_status(music_player)

        if music_player.get_status() == "on":
            print(f"Music player in {room_name} is already on.")
            logger.info(f"Music player in {room_name} is already on.")
        else:
            print(f"Turning on music player in {room_name}")
            logger.info(f"Turning on music player in {room_name}")
            music_player.turn_on()
            music_player.play_music("Rock")

    # Function to control smart TV
    def control_smart_tv(room_name):
        smart_tv = get_room_actuators(home, room_name)[0]  # Assuming only one smart TV per room
        update_actuator_status(smart_tv)

        if smart_tv.get_status() == "on":
            print(f"Smart TV in {room_name} is already on.")
            logger.info(f"Smart TV in {room_name} is already on.")
        else:
            print(f"Turning on Smart TV in {room_name}")
            logger.info(f"Turning on Smart TV in {room_name}")
            smart_tv.turn_on()
            smart_tv.play_channel("CNN")

    # Function to control cleaning robot
    def control_cleaning_robot(room_name):
        cleaning_robot = get_room_actuators(home, room_name)[0]  # Assuming only one cleaning robot per room
        update_actuator_status(cleaning_robot)

        if cleaning_robot.get_status() == "on":
            print(f"Cleaning robot in {room_name} is already on.")
            logger.info(f"Cleaning robot in {room_name} is already on.")
        else:
            print(f"Turning on cleaning robot in {room_name}")
            logger.info(f"Turning on cleaning robot in {room_name}")
            cleaning_robot.turn_on()
            cleaning_robot.daily_routine()

    # Main loop
    while True:
        # Update sensor status
        for room in home:
            for sensor in room.sensors:
                update_sensor_status(sensor)

        # Control temperature
        control_temperature("LivingRoom")

        # Control humidity
        control_humidity("LivingRoom")

        # Control light intensity
        control_light_intensity("LivingRoom")

        # Control coffee machine
        control_coffee_machine("Kitchen")

        # Control music player
        control_music_player("LivingRoom")

        # Control smart TV
        control_smart_tv("LivingRoom")

        # Control cleaning robot
        control_cleaning_robot("LivingRoom")

        # Simulate sensor readings
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Simulate time passing for temperature change

        # Print sensor status
        print("Sensor Status:")
        for sensor_id, reading in sensor_status.items():
            print(f"{sensor_id}: {reading}")
        print("Actuator Status:")
        for actuator_id, status in actuator_status.items():
            print(f"{actuator_id}: {status}")

        print("------------------------")

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:** Imports necessary modules from `home` package and `time` for sleep function.
# 2. **Main Function (`main()`):**
#    - Creates the `home` object using `home_plan()` function.
#    - Defines dictionaries `sensor_status` and `actuator_status` to store their respective states.
#    - Creates functions to update sensor and actuator status:
#      - `update_sensor_status(sensor)`: Gets sensor readings and updates `sensor_status`.
#      - `update_actuator_status(actuator)`: Gets actuator status and updates `actuator_status`.
#    - Creates functions for controlling different aspects of the smart home:
#      - `control_temperature(room_name)`: Controls AC and heater based on temperature.
#      - `control_humidity(room_name)`: Controls humidifier based on humidity.
#      - `control_light_intensity(room_name)`: Controls light based on light intensity.
#      - `control_coffee_machine(room_name)`: Controls coffee machine.
#      - `control_music_player(room_name)`: Controls music player.
#      - `control_smart_tv(room_name)`: Controls smart TV.
#      - `control_cleaning_robot(room_name)`: Controls cleaning robot.
#    - **Main Loop:**
#      - Continuously updates sensor status for each room.
#      - Calls control functions for each room.
#      - Simulates time passing using `time.sleep()`.
#      - Prints sensor and actuator status.
#      - Repeats the process.

# **Key Changes:**

# - **Actuator Control:** The code now includes control functions for various actuators, allowing you to simulate different smart home functionalities.
# - **Sensor Data Usage:** Sensor readings are used to trigger actions for actuators.
# - **Time Simulation:** `time.sleep()` is used to simulate the passage of time, allowing for changes in sensor readings and actuator behavior.
# - **Logger:** The `logger` is used to record information and warnings throughout the code.

# **To Run:**

# 1. Save the code as `function.py` in the `functions` folder.
# 2. Make sure the `home` folder and its contents are in the same directory.
# 3. Run the script: `python functions/function.py`

# This code will simulate a basic smart home system that responds to changes in temperature, humidity, and light intensity, and also control other devices like a coffee machine, music player, smart TV, and a cleaning robot.
