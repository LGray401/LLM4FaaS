import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.logger_config import logger
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import random

def start_smart_home():
    # Home plan setup
    home = home_plan()
    print_home_plan(home)

    # Interactive loop
    while True:
        command = input("Enter your command: ")
        command_list = command.split()
        
        if command_list[0] == 'turn':
            if command_list[1] == 'on':
                if command_list[2] == 'light':
                    room_name = command_list[3]
                    room = get_room(home, room_name)
                    if room is None:
                        continue
                    lights = get_room_actuators(home, room_name)
                    for light in lights:
                        if light.actuator_type == 'Light':
                            light.turn_on()
                elif command_list[2] == 'tv':
                    room_name = command_list[3]
                    room = get_room(home, room_name)
                    if room is None:
                        continue
                    tvs = get_room_actuators(home, room_name)
                    for tv in tvs:
                        if tv.actuator_type == 'SmartTV':
                            tv.turn_on()
                elif command_list[2] == 'music':
                    room_name = command_list[3]
                    room = get_room(home, room_name)
                    if room is None:
                        continue
                    music_players = get_room_actuators(home, room_name)
                    for player in music_players:
                        if player.actuator_type == 'MusicPlayer':
                            player.turn_on()
                elif command_list[2] == 'coffee':
                    room_name = command_list[3]
                    room = get_room(home, room_name)
                    if room is None:
                        continue
                    coffee_machines = get_room_actuators(home, room_name)
                    for machine in coffee_machines:
                        if machine.actuator_type == 'CoffeeMachine':
                            machine.turn_on()
                elif command_list[2] == 'cleaning':
                    room_name = command_list[3]
                    room = get_room(home, room_name)
                    if room is None:
                        continue
                    cleaning_robots = get_room_actuators(home, room_name)
                    for robot in cleaning_robots:
                        if robot.actuator_type == 'CleaningRobot':
                            robot.turn_on()
                else:
                    print(f"Invalid actuator type: {command_list[2]}")
                    continue
            elif command_list[1] == 'off':
                if command_list[2] == 'light':
                    room_name = command_list[3]
                    room = get_room(home, room_name)
                    if room is None:
                        continue
                    lights = get_room_actuators(home, room_name)
                    for light in lights:
                        if light.actuator_type == 'Light':
                            light.turn_off()
                elif command_list[2] == 'tv':
                    room_name = command_list[3]
                    room = get_room(home, room_name)
                    if room is None:
                        continue
                    tvs = get_room_actuators(home, room_name)
                    for tv in tvs:
                        if tv.actuator_type == 'SmartTV':
                            tv.turn_off()
                elif command_list[2] == 'music':
                    room_name = command_list[3]
                    room = get_room(home, room_name)
                    if room is None:
                        continue
                    music_players = get_room_actuators(home, room_name)
                    for player in music_players:
                        if player.actuator_type == 'MusicPlayer':
                            player.turn_off()
                elif command_list[2] == 'coffee':
                    room_name = command_list[3]
                    room = get_room(home, room_name)
                    if room is None:
                        continue
                    coffee_machines = get_room_actuators(home, room_name)
                    for machine in coffee_machines:
                        if machine.actuator_type == 'CoffeeMachine':
                            machine.turn_off()
                elif command_list[2] == 'cleaning':
                    room_name = command_list[3]
                    room = get_room(home, room_name)
                    if room is None:
                        continue
                    cleaning_robots = get_room_actuators(home, room_name)
                    for robot in cleaning_robots:
                        if robot.actuator_type == 'CleaningRobot':
                            robot.turn_off()
                else:
                    print(f"Invalid actuator type: {command_list[2]}")
                    continue
            else:
                print("Invalid action: Please enter 'on' or 'off'")
                continue
        elif command_list[0] == 'set':
            if command_list[1] == 'brightness':
                room_name = command_list[2]
                brightness_level = command_list[3]
                room = get_room(home, room_name)
                if room is None:
                    continue
                lights = get_room_actuators(home, room_name)
                for light in lights:
                    if light.actuator_type == 'Light':
                        light.set_brightness_level(brightness_level)
            elif command_list[1] == 'temperature':
                room_name = command_list[2]
                target_temperature = float(command_list[3])
                room = get_room(home, room_name)
                if room is None:
                    continue
                heaters = get_room_actuators(home, room_name)
                for heater in heaters:
                    if heater.actuator_type == 'Heater':
                        heater.set_target_temperature(target_temperature)
                acs = get_room_actuators(home, room_name)
                for ac in acs:
                    if ac.actuator_type == 'AC':
                        ac.set_target_temperature(target_temperature)
            elif command_list[1] == 'channel':
                room_name = command_list[2]
                channel_name = command_list[3]
                room = get_room(home, room_name)
                if room is None:
                    continue
                tvs = get_room_actuators(home, room_name)
                for tv in tvs:
                    if tv.actuator_type == 'SmartTV':
                        tv.play_channel(channel_name)
            elif command_list[1] == 'playlist':
                room_name = command_list[2]
                playlist = command_list[3]
                room = get_room(home, room_name)
                if room is None:
                    continue
                music_players = get_room_actuators(home, room_name)
                for player in music_players:
                    if player.actuator_type == 'MusicPlayer':
                        player.play_music(playlist)
            elif command_list[1] == 'coffee':
                room_name = command_list[2]
                coffee_type = command_list[3]
                room = get_room(home, room_name)
                if room is None:
                    continue
                coffee_machines = get_room_actuators(home, room_name)
                for machine in coffee_machines:
                    if machine.actuator_type == 'CoffeeMachine':
                        machine.make_coffee(coffee_type)
            else:
                print(f"Invalid setting type: {command_list[1]}")
                continue
        elif command_list[0] == 'clean':
            room_name = command_list[1]
            room = get_room(home, room_name)
            if room is None:
                continue
            cleaning_robots = get_room_actuators(home, room_name)
            for robot in cleaning_robots:
                if robot.actuator_type == 'CleaningRobot':
                    robot.daily_routine()
        elif command_list[0] == 'send':
            room_name = command_list[1]
            message = ' '.join(command_list[2:])
            room = get_room(home, room_name)
            if room is None:
                continue
            notification_senders = get_room_actuators(home, room_name)
            for sender in notification_senders:
                if sender.actuator_type == 'NotificationSender':
                    sender.notification_sender(message)
        elif command_list[0] == 'get':
            if command_list[1] == 'temperature':
                room_name = command_list[2]
                room = get_room(home, room_name)
                if room is None:
                    continue
                temperature_sensors = get_room_sensors(home, room_name)
                for sensor in temperature_sensors:
                    if sensor.sensor_type == 'IndoorTemperature':
                        print(f"Temperature in {room_name}: {sensor.get_reading()}°C")
            elif command_list[1] == 'humidity':
                room_name = command_list[2]
                room = get_room(home, room_name)
                if room is None:
                    continue
                humidity_sensors = get_room_sensors(home, room_name)
                for sensor in humidity_sensors:
                    if sensor.sensor_type == 'Humidity':
                        print(f"Humidity in {room_name}: {sensor.get_reading()}%")
            elif command_list[1] == 'light':
                room_name = command_list[2]
                room = get_room(home, room_name)
                if room is None:
                    continue
                light_intensity_sensors = get_room_sensors(home, room_name)
                for sensor in light_intensity_sensors:
                    if sensor.sensor_type == 'LightIntensive':
                        print(f"Light intensity in {room_name}: {sensor.get_reading()} lux")
            else:
                print(f"Invalid data type: {command_list[1]}")
                continue
        elif command_list[0] == 'exit':
            break
        else:
            print("Invalid command. Please try again.")
            continue

        # Smart Home Logic (Auto-adjustments based on sensor readings)
        # Example: Adjust AC based on temperature and humidity
        for room in home:
            if room.name == 'LivingRoom':
                temperature_sensors = get_room_sensors(home, 'LivingRoom')
                for sensor in temperature_sensors:
                    if sensor.sensor_type == 'IndoorTemperature':
                        current_temperature = sensor.get_reading()
                        acs = get_room_actuators(home, 'LivingRoom')
                        for ac in acs:
                            if ac.actuator_type == 'AC':
                                ac.adjust_temperature(current_temperature)
                humidity_sensors = get_room_sensors(home, 'LivingRoom')
                for sensor in humidity_sensors:
                    if sensor.sensor_type == 'Humidity':
                        current_humidity = sensor.get_reading()
                        acs = get_room_actuators(home, 'LivingRoom')
                        for ac in acs:
                            if ac.actuator_type == 'AC':
                                if current_humidity > HUMIDITY_HIGH:
                                    ac.turn_on()
                                elif current_humidity < HUMIDITY_LOW:
                                    ac.turn_off()
            elif room.name == 'Bedroom':
                temperature_sensors = get_room_sensors(home, 'Bedroom')
                for sensor in temperature_sensors:
                    if sensor.sensor_type == 'IndoorTemperature':
                        current_temperature = sensor.get_reading()
                        heaters = get_room_actuators(home, 'Bedroom')
                        for heater in heaters:
                            if heater.actuator_type == 'Heater':
                                heater.adjust_temperature(current_temperature)
                        acs = get_room_actuators(home, 'Bedroom')
                        for ac in acs:
                            if ac.actuator_type == 'AC':
                                ac.adjust_temperature(current_temperature)
                humidity_sensors = get_room_sensors(home, 'Bedroom')
                for sensor in humidity_sensors:
                    if sensor.sensor_type == 'Humidity':
                        current_humidity = sensor.get_reading()
                        acs = get_room_actuators(home, 'Bedroom')
                        for ac in acs:
                            if ac.actuator_type == 'AC':
                                if current_humidity > HUMIDITY_HIGH:
                                    ac.turn_on()
                                elif current_humidity < HUMIDITY_LOW:
                                    ac.turn_off()
            elif room.name == 'Kitchen':
                smoke_sensors = get_room_sensors(home, 'Kitchen')
                for sensor in smoke_sensors:
                    if sensor.sensor_type == 'Smoke':
                        current_smoke_level = sensor.get_reading()
                        notification_senders = get_room_actuators(home, 'Kitchen')
                        for sender in notification_senders:
                            if sender.actuator_type == 'NotificationSender':
                                if current_smoke_level > 50:
                                    sender.notification_sender(f"Smoke detected in Kitchen! Please check.")
            elif room.name == 'Bathroom':
                temperature_sensors = get_room_sensors(home, 'Bathroom')
                for sensor in temperature_sensors:
                    if sensor.sensor_type == 'IndoorTemperature':
                        current_temperature = sensor.get_reading()
                        heaters = get_room_actuators(home, 'Bathroom')
                        for heater in heaters:
                            if heater.actuator_type == 'Heater':
                                heater.adjust_temperature(current_temperature)
                humidity_sensors = get_room_sensors(home, 'Bathroom')
                for sensor in humidity_sensors:
                    if sensor.sensor_type == 'Humidity':
                        current_humidity = sensor.get_reading()
                        notification_senders = get_room_actuators(home, 'Bathroom')
                        for sender in notification_senders:
                            if sender.actuator_type == 'NotificationSender':
                                if current_humidity > HUMIDITY_HIGH:
                                    sender.notification_sender(f"Humidity in Bathroom is high. Please check.")
        
        # Wait for a short duration to simulate real-time updates
        time.sleep(1)

    # Exit the program
    print("Exiting Smart Home System")

if __name__ == '__main__':
    start_smart_home()

# **Explanation:**

# 1. **Import Necessary Modules:**
#    - Imports modules for sensors, actuators, home plan, logger configuration, and random.

# 2. **`start_smart_home()` Function:**
#    - **Home Plan Setup:** Calls `home_plan()` to initialize the home layout and its components.
#    - **Interactive Loop:**
#      - Prompts the user for commands using `input()`.
#      - Splits the command into a list of words using `command.split()`.
#      - **Command Handling:**
#        - `turn on/off [device] [room_name]`: Controls devices (light, TV, music, coffee, cleaning).
#        - `set [setting] [room_name] [value]`: Sets brightness, temperature, channel, playlist, coffee type.
#        - `clean [room_name]`: Starts the daily cleaning routine.
#        - `send [room_name] [message]`: Sends a notification.
#        - `get [data_type] [room_name]`: Gets temperature, humidity, or light intensity.
#        - `exit`: Exits the program.
#      - **Smart Home Logic:**
#        - **Temperature and Humidity Control:** Adjusts AC/Heater based on temperature and humidity in rooms.
#        - **Smoke Detection:** Sends a notification if smoke is detected in the kitchen.
#        - **Bathroom Humidity Monitoring:** Sends a notification if humidity is high in the bathroom.
#    - **Wait and Exit:**
#      - Pauses for a short duration to simulate real-time updates.
#      - Prints an exit message and ends the program.

# 3. **Main Execution Block:**
#    - Calls `start_smart_home()` to run the smart home system.

# **Key Points:**

# - **Room-Based Interactions:** Commands are directed to specific rooms.
# - **Multiple Devices:** The system can handle multiple lights, TVs, etc., in each room.
# - **Auto-Adjustments:** The system automatically adjusts actuators based on sensor readings.
# - **Real-Time Simulation:** The `time.sleep()` function provides a basic simulation of real-time behavior.
# - **User Interface:** A simple command-line interface allows for user interaction.

# **Remember:** This is a simplified example. A real smart home system would likely involve more sophisticated logic, communication protocols, and hardware integrations.
