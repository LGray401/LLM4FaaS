from home.home_plan import home_plan, get_room, get_room_actuators, get_room_sensors, get_all_sensors, \
    get_all_actuators
from home.actuator import Heater, AC, CoffeeMachine, Window, Door, Curtain, CleaningRobot, NotificationSender, MusicPlayer, \
    Light, SmartTV, SmartSocket, Humidifier
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, OutdoorTemperatureSensor
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
import time


def main():
    # Create the home plan
    home = home_plan()

    # Example scenarios
    # Scenario 1: Adjust temperature in the LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        living_room_sensors = get_room_sensors(home, "LivingRoom")
        living_room_actuators = get_room_actuators(home, "LivingRoom")

        # Get temperature sensor and actuators
        temperature_sensor = None
        heater = None
        ac = None
        for sensor in living_room_sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                temperature_sensor = sensor
                break
        for actuator in living_room_actuators:
            if isinstance(actuator, Heater):
                heater = actuator
            elif isinstance(actuator, AC):
                ac = actuator

        if temperature_sensor and heater and ac:
            # Turn on the sensors
            temperature_sensor.turn_on()

            # Set target temperature
            target_temperature = 22
            heater.set_target_temperature(target_temperature)
            ac.set_target_temperature(target_temperature)

            # Simulate temperature changes
            while True:
                current_temperature = temperature_sensor.get_reading()
                if current_temperature is not None:
                    heater.adjust_temperature(current_temperature)
                    ac.adjust_temperature(current_temperature)
                    print(f"Current temperature: {current_temperature}°C")
                    time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                else:
                    break
        else:
            print("Error: Could not find temperature sensor, heater, or AC in the LivingRoom.")

    # Scenario 2: Control light in the Bedroom
    bedroom = get_room(home, "Bedroom")
    if bedroom is not None:
        bedroom_actuators = get_room_actuators(home, "Bedroom")
        # Get the light actuator
        light = None
        for actuator in bedroom_actuators:
            if isinstance(actuator, Light):
                light = actuator
                break

        if light:
            # Turn on the light
            light.turn_on()
            light.set_brightness_level("high")

            # Simulate light intensity changes
            # ...
            # Adjust brightness level based on light intensity
            # ...
            # Turn off the light after a while
            time.sleep(10)
            light.turn_off()
        else:
            print("Error: Could not find the light in the Bedroom.")

    # Scenario 3: Use CoffeeMachine in the Kitchen
    kitchen = get_room(home, "Kitchen")
    if kitchen is not None:
        kitchen_actuators = get_room_actuators(home, "Kitchen")
        # Get the CoffeeMachine actuator
        coffee_machine = None
        for actuator in kitchen_actuators:
            if isinstance(actuator, CoffeeMachine):
                coffee_machine = actuator
                break
        if coffee_machine:
            # Turn on the coffee machine
            coffee_machine.turn_on()
            # Make a cup of coffee
            coffee_machine.make_coffee("Espresso")
            # Turn off the coffee machine
            coffee_machine.turn_off()
        else:
            print("Error: Could not find the coffee machine in the Kitchen.")

    # Scenario 4: Use SmartTV in the LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        living_room_actuators = get_room_actuators(home, "LivingRoom")
        # Get the SmartTV actuator
        smart_tv = None
        for actuator in living_room_actuators:
            if isinstance(actuator, SmartTV):
                smart_tv = actuator
                break
        if smart_tv:
            # Turn on the SmartTV
            smart_tv.turn_on()
            # Play a channel
            smart_tv.play_channel("Discovery")
            # Turn off the SmartTV
            smart_tv.turn_off()
        else:
            print("Error: Could not find the SmartTV in the LivingRoom.")

    # Scenario 5: Use CleaningRobot in the LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        living_room_actuators = get_room_actuators(home, "LivingRoom")
        # Get the CleaningRobot actuator
        cleaning_robot = None
        for actuator in living_room_actuators:
            if isinstance(actuator, CleaningRobot):
                cleaning_robot = actuator
                break
        if cleaning_robot:
            # Turn on the CleaningRobot
            cleaning_robot.turn_on()
            # Start daily cleaning routine
            cleaning_robot.daily_routine()
        else:
            print("Error: Could not find the CleaningRobot in the LivingRoom.")

    # Scenario 6: Use NotificationSender in the LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        living_room_actuators = get_room_actuators(home, "LivingRoom")
        # Get the NotificationSender actuator
        notification_sender = None
        for actuator in living_room_actuators:
            if isinstance(actuator, NotificationSender):
                notification_sender = actuator
                break
        if notification_sender:
            # Turn on the NotificationSender
            notification_sender.turn_on()
            # Send a notification
            notification_sender.notification_sender("It's time for dinner!")
        else:
            print("Error: Could not find the NotificationSender in the LivingRoom.")

    # Scenario 7: Use MusicPlayer in the LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        living_room_actuators = get_room_actuators(home, "LivingRoom")
        # Get the MusicPlayer actuator
        music_player = None
        for actuator in living_room_actuators:
            if isinstance(actuator, MusicPlayer):
                music_player = actuator
                break
        if music_player:
            # Turn on the MusicPlayer
            music_player.turn_on()
            # Play a playlist
            music_player.play_music("Pop Hits")
        else:
            print("Error: Could not find the MusicPlayer in the LivingRoom.")

    # Scenario 8: Use SmartSocket in the LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        living_room_actuators = get_room_actuators(home, "LivingRoom")
        # Get the SmartSocket actuators
        smart_sockets = []
        for actuator in living_room_actuators:
            if isinstance(actuator, SmartSocket):
                smart_sockets.append(actuator)
        if smart_sockets:
            # Turn on the SmartSockets
            for smart_socket in smart_sockets:
                smart_socket.turn_on()
            # Simulate using the SmartSockets
            # ...
            # Turn off the SmartSockets
            for smart_socket in smart_sockets:
                smart_socket.turn_off()
        else:
            print("Error: Could not find the SmartSockets in the LivingRoom.")

    # Scenario 9: Use Humidifier in the LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        living_room_actuators = get_room_actuators(home, "LivingRoom")
        # Get the Humidifier actuator
        humidifier = None
        for actuator in living_room_actuators:
            if isinstance(actuator, Humidifier):
                humidifier = actuator
                break
        if humidifier:
            # Simulate humidity changes
            # ...
            # Adjust humidity using the Humidifier
            # ...
        else:
            print("Error: Could not find the Humidifier in the LivingRoom.")

    # Scenario 10: Control multiple sensors and actuators
    # ...

    # Scenario 11: Implement rules and automation based on sensor readings
    # ...

    # Scenario 12: Integrate with other smart home systems or cloud services
    # ...

# **Explanation:**

# 1. **Import Necessary Modules:** 
#    - `home.home_plan`: Provides functions for managing the home plan (rooms, sensors, actuators).
#    - `home.actuator`: Contains definitions for various actuators (Heater, AC, CoffeeMachine, etc.).
#    - `home.sensor`: Defines different types of sensors (IndoorTemperatureSensor, HumiditySensor, etc.).
#    - `home.config`: Contains configuration settings like temperature thresholds, humidity levels, etc.
#    - `time`: Provides functionality for pausing the script.

# 2. **`main()` Function:**
#    - **Create Home Plan:**  The `home_plan()` function from `home.home_plan` is used to generate the home structure with rooms, sensors, and actuators.
#    - **Example Scenarios:**  The code includes several example scenarios demonstrating how to interact with sensors and actuators.
#      - **Scenario 1: Temperature Control in the LivingRoom**
#        - It fetches the LivingRoom from the home plan and finds the temperature sensor, heater, and AC.
#        - Sets a target temperature and simulates temperature changes. The heater or AC turns on/off based on the target temperature.
#      - **Scenario 2: Light Control in the Bedroom**
#        - Similar to the temperature control scenario, it finds the light actuator and controls its brightness.
#      - **Scenario 3: Coffee Machine in the Kitchen**
#        - Finds the CoffeeMachine and makes coffee (simulated).
#      - **Scenario 4: SmartTV in the LivingRoom**
#        - Finds the SmartTV and simulates playing a channel.
#      - **Scenario 5: CleaningRobot in the LivingRoom**
#        - Finds the CleaningRobot and starts a simulated daily cleaning routine.
#      - **Scenario 6: NotificationSender in the LivingRoom**
#        - Finds the NotificationSender and sends a test notification.
#      - **Scenario 7: MusicPlayer in the LivingRoom**
#        - Finds the MusicPlayer and plays a simulated playlist.
#      - **Scenario 8: SmartSocket in the LivingRoom**
#        - Finds all SmartSockets in the LivingRoom and turns them on and off.
#      - **Scenario 9: Humidifier in the LivingRoom**
#        - Finds the Humidifier and prepares to control humidity (implementation not shown).
#      - **Scenario 10, 11, 12:**  These are placeholder comments indicating areas where you can add more complex scenarios involving multiple sensors/actuators, rules, automation, and integration with other systems.

# **Key Points:**

# - **Object-Oriented Approach:** The code uses classes to represent sensors and actuators, making it more organized and reusable.
# - **Flexibility:** You can easily add more rooms, sensors, actuators, or scenarios as needed.
# - **Comments:** The code includes comments to explain the purpose of each section.

# **To Run the Code:**

# 1. Make sure you have the necessary files (`sensor.py`, `actuator.py`, `home_plan.py`, `config.py`, and `function.py`) in their respective folders.
# 2. Run the `function.py` file.

# This code provides a basic framework for controlling a smart home. You can expand upon it to implement more advanced features like automation, rules, and integration with other smart home systems or cloud services.
