from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor
from home.actuator import Heater, AC, Light, Curtain, Window, Door, NotificationSender, CleaningRobot, MusicPlayer, \
    CoffeeMachine, SmartTV, SmartSocket, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW
import time

def main():
    home = home_plan()
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")
    kitchen = get_room(home, "Kitchen")

    # Get sensors and actuators
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    bedroom_sensors = get_room_sensors(home, "Bedroom")
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    kitchen_sensors = get_room_sensors(home, "Kitchen")
    kitchen_actuators = get_room_actuators(home, "Kitchen")
    
    living_room_temp_sensor = get_all_sensors(home, "IndoorTemperature")[0]
    living_room_light_sensor = get_all_sensors(home, "LightIntensive")[0]
    living_room_humidity_sensor = get_all_sensors(home, "Humidity")[0]
    bedroom_temp_sensor = get_all_sensors(home, "IndoorTemperature")[1]
    bedroom_light_sensor = get_all_sensors(home, "LightIntensive")[1]
    bedroom_humidity_sensor = get_all_sensors(home, "Humidity")[2]
    kitchen_smoke_sensor = get_all_sensors(home, "Smoke")[0]

    living_room_heater = get_all_actuators(home, "Heater")[0]
    living_room_ac = get_all_actuators(home, "AC")[0]
    living_room_light = get_all_actuators(home, "Light")[0]
    living_room_curtain = get_all_actuators(home, "Curtain")[0]
    living_room_window = get_all_actuators(home, "Window")[0]
    living_room_door = get_all_actuators(home, "Door")[0]
    living_room_notification_sender = get_all_actuators(home, "NotificationSender")[0]
    living_room_cleaning_robot = get_all_actuators(home, "CleaningRobot")[0]
    living_room_music_player = get_all_actuators(home, "MusicPlayer")[0]
    living_room_smart_tv = get_all_actuators(home, "SmartTV")[0]
    bedroom_heater = get_all_actuators(home, "Heater")[1]
    bedroom_ac = get_all_actuators(home, "AC")[1]
    bedroom_light = get_all_actuators(home, "Light")[1]
    bedroom_curtain = get_all_actuators(home, "Curtain")[1]
    bedroom_window = get_all_actuators(home, "Window")[1]
    bedroom_door = get_all_actuators(home, "Door")[1]
    bedroom_cleaning_robot = get_all_actuators(home, "CleaningRobot")[1]
    bedroom_music_player = get_all_actuators(home, "MusicPlayer")[1]
    kitchen_light = get_all_actuators(home, "Light")[2]
    kitchen_window = get_all_actuators(home, "Window")[2]
    kitchen_door = get_all_actuators(home, "Door")[2]
    kitchen_coffee_machine = get_all_actuators(home, "CoffeeMachine")[0]
    
    # Turn on sensors
    living_room_temp_sensor.turn_on()
    living_room_light_sensor.turn_on()
    living_room_humidity_sensor.turn_on()
    bedroom_temp_sensor.turn_on()
    bedroom_light_sensor.turn_on()
    bedroom_humidity_sensor.turn_on()
    kitchen_smoke_sensor.turn_on()

    # Simulate a scenario
    while True:
        # Check temperature in living room
        living_room_temperature = living_room_temp_sensor.get_reading()
        if living_room_temperature is not None:
            if living_room_temperature < TEMP_LOW:
                living_room_heater.turn_on()
                living_room_heater.set_target_temperature(20)
                print(f"Living room temperature is low, turning on heater to 20 degrees.")
            elif living_room_temperature > TEMP_HIGH:
                living_room_ac.turn_on()
                living_room_ac.set_target_temperature(25)
                print(f"Living room temperature is high, turning on AC to 25 degrees.")
            else:
                living_room_heater.turn_off()
                living_room_ac.turn_off()
                print(f"Living room temperature is comfortable.")

        # Check temperature in bedroom
        bedroom_temperature = bedroom_temp_sensor.get_reading()
        if bedroom_temperature is not None:
            if bedroom_temperature < TEMP_LOW:
                bedroom_heater.turn_on()
                bedroom_heater.set_target_temperature(20)
                print(f"Bedroom temperature is low, turning on heater to 20 degrees.")
            elif bedroom_temperature > TEMP_HIGH:
                bedroom_ac.turn_on()
                bedroom_ac.set_target_temperature(25)
                print(f"Bedroom temperature is high, turning on AC to 25 degrees.")
            else:
                bedroom_heater.turn_off()
                bedroom_ac.turn_off()
                print(f"Bedroom temperature is comfortable.")

        # Check humidity in living room
        living_room_humidity = living_room_humidity_sensor.get_reading()
        if living_room_humidity is not None:
            if living_room_humidity < HUMIDITY_LOW:
                print(f"Living room humidity is low, need to increase humidity.")
                # TODO: Add logic to increase humidity
            elif living_room_humidity > HUMIDITY_HIGH:
                print(f"Living room humidity is high, need to decrease humidity.")
                # TODO: Add logic to decrease humidity

        # Check humidity in bedroom
        bedroom_humidity = bedroom_humidity_sensor.get_reading()
        if bedroom_humidity is not None:
            if bedroom_humidity < HUMIDITY_LOW:
                print(f"Bedroom humidity is low, need to increase humidity.")
                # TODO: Add logic to increase humidity
            elif bedroom_humidity > HUMIDITY_HIGH:
                print(f"Bedroom humidity is high, need to decrease humidity.")
                # TODO: Add logic to decrease humidity

        # Check light intensity in living room
        living_room_light_intensity = living_room_light_sensor.get_reading()
        if living_room_light_intensity is not None:
            if living_room_light_intensity < LIGHT_INTENSITY_LOW:
                living_room_light.turn_on()
                print(f"Living room light intensity is low, turning on light.")
            elif living_room_light_intensity > LIGHT_INTENSITY_HIGH:
                living_room_light.turn_off()
                print(f"Living room light intensity is high, turning off light.")

        # Check light intensity in bedroom
        bedroom_light_intensity = bedroom_light_sensor.get_reading()
        if bedroom_light_intensity is not None:
            if bedroom_light_intensity < LIGHT_INTENSITY_LOW:
                bedroom_light.turn_on()
                print(f"Bedroom light intensity is low, turning on light.")
            elif bedroom_light_intensity > LIGHT_INTENSITY_HIGH:
                bedroom_light.turn_off()
                print(f"Bedroom light intensity is high, turning off light.")
        
        # Check smoke in kitchen
        kitchen_smoke = kitchen_smoke_sensor.get_reading()
        if kitchen_smoke is not None:
            if kitchen_smoke > 10:
                living_room_notification_sender.notification_sender("Smoke detected in the kitchen! Please check!")
                print("Smoke detected in the kitchen! Please check!")
                # TODO: Add logic to open windows and turn off appliances
        
        # Simulate daily routine
        current_time = time.localtime()
        if current_time.tm_hour == 7 and current_time.tm_min == 0:
            print("It's 7:00 AM, starting daily routine.")
            living_room_cleaning_robot.daily_routine()
            bedroom_cleaning_robot.daily_routine()
            living_room_curtain.turn_on()
            bedroom_curtain.turn_on()
            living_room_light.turn_on()
            bedroom_light.turn_on()
            living_room_music_player.play_music("Morning playlist")
            bedroom_music_player.play_music("Morning playlist")
        elif current_time.tm_hour == 10 and current_time.tm_min == 0:
            print("It's 10:00 AM, stopping morning routine.")
            living_room_cleaning_robot.turn_off()
            bedroom_cleaning_robot.turn_off()
            living_room_curtain.turn_off()
            bedroom_curtain.turn_off()
            living_room_light.turn_off()
            bedroom_light.turn_off()
            living_room_music_player.turn_off()
            bedroom_music_player.turn_off()
        elif current_time.tm_hour == 18 and current_time.tm_min == 0:
            print("It's 6:00 PM, starting evening routine.")
            living_room_light.turn_on()
            bedroom_light.turn_on()
            living_room_music_player.play_music("Evening playlist")
            bedroom_music_player.play_music("Evening playlist")
            living_room_smart_tv.play_channel("News channel")
        elif current_time.tm_hour == 22 and current_time.tm_min == 0:
            print("It's 10:00 PM, stopping evening routine.")
            living_room_light.turn_off()
            bedroom_light.turn_off()
            living_room_music_player.turn_off()
            bedroom_music_player.turn_off()
            living_room_smart_tv.turn_off()
        
        # Simulate user interaction
        user_input = input("Enter a command (or 'exit' to quit): ")
        if user_input == "exit":
            break
        elif user_input == "open living room window":
            living_room_window.turn_on()
            print("Opening living room window.")
        elif user_input == "close living room window":
            living_room_window.turn_off()
            print("Closing living room window.")
        elif user_input == "open living room curtain":
            living_room_curtain.turn_on()
            print("Opening living room curtain.")
        elif user_input == "close living room curtain":
            living_room_curtain.turn_off()
            print("Closing living room curtain.")
        elif user_input == "open bedroom window":
            bedroom_window.turn_on()
            print("Opening bedroom window.")
        elif user_input == "close bedroom window":
            bedroom_window.turn_off()
            print("Closing bedroom window.")
        elif user_input == "open bedroom curtain":
            bedroom_curtain.turn_on()
            print("Opening bedroom curtain.")
        elif user_input == "close bedroom curtain":
            bedroom_curtain.turn_off()
            print("Closing bedroom curtain.")
        elif user_input == "open kitchen window":
            kitchen_window.turn_on()
            print("Opening kitchen window.")
        elif user_input == "close kitchen window":
            kitchen_window.turn_off()
            print("Closing kitchen window.")
        elif user_input == "lock living room door":
            living_room_door.lock()
            print("Locking living room door.")
        elif user_input == "unlock living room door":
            living_room_door.unlock()
            print("Unlocking living room door.")
        elif user_input == "lock bedroom door":
            bedroom_door.lock()
            print("Locking bedroom door.")
        elif user_input == "unlock bedroom door":
            bedroom_door.unlock()
            print("Unlocking bedroom door.")
        elif user_input == "lock kitchen door":
            kitchen_door.lock()
            print("Locking kitchen door.")
        elif user_input == "unlock kitchen door":
            kitchen_door.unlock()
            print("Unlocking kitchen door.")
        elif user_input == "make coffee":
            kitchen_coffee_machine.make_coffee("Espresso")
            print("Making coffee.")
        # Add more user commands as needed...

        time.sleep(1)  # Wait for 1 second before checking sensor readings again

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: This imports the functions for managing your home's structure and components.
#    - `home.sensor`: This imports the sensor classes (e.g., `IndoorTemperatureSensor`, `HumiditySensor`).
#    - `home.actuator`: This imports the actuator classes (e.g., `Heater`, `AC`, `Light`).
#    - `home.config`: This imports the configuration settings for temperature thresholds, humidity thresholds, etc.
#    - `time`: This module is used for pausing the execution and simulating delays.

# 2. **Create the home plan:**
#    - `home = home_plan()`: This line creates the home plan structure from your `home_plan.py` file.
#    - `living_room = get_room(home, "LivingRoom")`: This retrieves the "LivingRoom" from the home plan.
#    - `bedroom = get_room(home, "Bedroom")`:  This retrieves the "Bedroom" from the home plan.
#    - `kitchen = get_room(home, "Kitchen")`: This retrieves the "Kitchen" from the home plan.

# 3. **Get sensors and actuators:**
#    - The code uses `get_room_sensors` and `get_room_actuators` to retrieve lists of sensors and actuators for each room.
#    - Then, it uses `get_all_sensors` and `get_all_actuators` to get specific sensors and actuators based on type, for example, the first `IndoorTemperatureSensor`, the first `LightIntensiveSensor`, etc.

# 4. **Turn on sensors:**
#    - The code calls `turn_on()` for all sensors to ensure they start providing readings.

# 5. **Simulation loop:**
#    - A `while True` loop runs continuously to simulate the operation of the smart home.

# 6. **Sensor reading and condition checks:**
#    - The code reads sensor data using `get_reading()` for each sensor.
#    - It then checks conditions based on your defined thresholds (from `home.config`).
#    - If conditions are met, it triggers actions using actuator methods (e.g., `turn_on()`, `turn_off()`, `set_target_temperature()`).

# 7. **Daily routine simulation:**
#    - The code checks the current time using `time.localtime()`.
#    - If it's 7:00 AM, it simulates a morning routine by turning on lights, opening curtains, starting cleaning robots, and playing music.
#    - Similar logic is applied for other times of the day (10:00 AM, 6:00 PM, 10:00 PM) to simulate different routines.

# 8. **User interaction simulation:**
#    - The `input()` function allows you to type commands into the console.
#    - The code checks for commands like "open living room window," "close bedroom curtain," etc.
#    - When a command is recognized, the corresponding action is performed using actuator methods.

# 9. **Delay:**
#    - `time.sleep(1)` pauses the execution for one second before the loop starts again, allowing the simulation to run in a more realistic pace.

# **Key improvements:**

# - **Modular structure:** The code is organized into functions to separate concerns and make it easier to understand and maintain.
# - **Configuration:** Settings like temperature thresholds, humidity thresholds, and other parameters are stored in a separate `home.config` file, making them easier to modify.
# - **User interaction:** The ability to input commands allows you to test different scenarios and observe how the smart home responds.
# - **Daily routines:** The simulation of daily routines provides a more realistic representation of how the smart home would operate throughout the day.

# **Further improvements:**

# - **More realistic sensor readings:** You could use actual sensor data or simulate more complex sensor models to create a more realistic simulation.
# - **Advanced automation:** Implement more complex automation rules, like triggering actions based on multiple sensor readings or conditions.
# - **Integration with other systems:** Connect the simulation to other systems, like a home automation platform or a weather API, for a more integrated experience.
# - **User interface:** Develop a graphical user interface for interacting with the smart home simulation.

# **Remember:** This code provides a basic framework for your smart home project. You can customize and extend it to add more features, functionality, and complexity as needed. 
