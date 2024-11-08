from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW, \
    TEMP_CHANGE_DURATION_WINDOW

import time


def main():
    # Step 1: Create the home plan
    home = home_plan()

    # Step 2: Simulate sensor readings and actuator actions
    while True:
        # Temperature control (Living Room)
        living_room = get_room(home, "LivingRoom")
        if living_room:
            indoor_temp_sensor = get_room_sensors(home, "LivingRoom")[0]
            ac = get_room_actuators(home, "LivingRoom")[10]
            heater = get_room_actuators(home, "LivingRoom")[11]
            if indoor_temp_sensor.get_reading() > TEMP_HIGH:
                ac.turn_on()
                ac.set_target_temperature(TEMP_HIGH - 1)
                print(f"AC in Living Room turned on, target temperature: {ac.target_temperature}")
            elif indoor_temp_sensor.get_reading() < TEMP_LOW:
                heater.turn_on()
                heater.set_target_temperature(TEMP_LOW + 1)
                print(f"Heater in Living Room turned on, target temperature: {heater.target_temperature}")
            else:
                ac.turn_off()
                heater.turn_off()
                print(f"AC and Heater in Living Room are off.")

            time.sleep(TEMP_CHANGE_DURATION_WINDOW)

        # Humidity control (Bathroom)
        bathroom = get_room(home, "Bathroom")
        if bathroom:
            humidity_sensor = get_room_sensors(home, "Bathroom")[1]
            humidifier = get_room_actuators(home, "Bathroom")[4]
            if humidity_sensor.get_reading() < HUMIDITY_LOW:
                humidifier.increase_humidity()
                print(f"Humidifier in Bathroom turned on.")
            elif humidity_sensor.get_reading() > HUMIDITY_HIGH:
                humidifier.decrease_humidity()
                print(f"Humidifier in Bathroom turned off.")
            time.sleep(TEMP_CHANGE_DURATION_WINDOW)

        # Light control (Living Room)
        living_room = get_room(home, "LivingRoom")
        if living_room:
            light_sensor = get_room_sensors(home, "LivingRoom")[0]
            light = get_room_actuators(home, "LivingRoom")[1]
            curtain = get_room_actuators(home, "LivingRoom")[5]
            if light_sensor.get_reading() > LIGHT_INTENSITY_HIGH:
                curtain.turn_on()
                print(f"Curtain in Living Room opened.")
            elif light_sensor.get_reading() < LIGHT_INTENSITY_LOW:
                curtain.turn_off()
                print(f"Curtain in Living Room closed.")
            time.sleep(TEMP_CHANGE_DURATION_WINDOW)

        # Cleaning Robot (Living Room)
        living_room = get_room(home, "LivingRoom")
        if living_room:
            cleaning_robot = get_room_actuators(home, "LivingRoom")[9]
            cleaning_robot.daily_routine()

        # Other actions and scenarios can be added here...
        # ...

        time.sleep(1)  # Simulate time passing

    # End of simulation loop


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:** Imports necessary modules from your project files (`home_plan`, `sensor`, `actuator`, `config`).
# 2. **`main()` function:** Contains the main simulation loop.
# 3. **Home Plan Setup:**
#    - Calls `home_plan()` to create the home layout.
# 4. **Simulation Loop:**
#    - Continuously runs until stopped.
#    - **Temperature Control (Living Room):**
#      - Gets the living room and its sensors/actuators using `get_room`, `get_room_sensors`, and `get_room_actuators`.
#      - Reads the temperature from the `IndoorTemperatureSensor`.
#      - Turns on the AC if the temperature is above `TEMP_HIGH` and sets the target temperature.
#      - Turns on the heater if the temperature is below `TEMP_LOW` and sets the target temperature.
#      - Turns off the AC and heater if the temperature is within the desired range.
#    - **Humidity Control (Bathroom):**
#      - Similar logic to temperature control, but using the `HumiditySensor` and `Humidifier`.
#    - **Light Control (Living Room):**
#      - Uses the `LightIntensiveSensor` and the `Curtain` actuator.
#      - Opens the curtain if the light intensity is above `LIGHT_INTENSITY_HIGH`.
#      - Closes the curtain if the light intensity is below `LIGHT_INTENSITY_LOW`.
#    - **Cleaning Robot (Living Room):**
#      - Starts the cleaning robot's daily routine.
#    - **Time Delay:**
#      - `time.sleep(1)` pauses the loop for one second to simulate time passing.

# **Key improvements:**

# - **Clearer Logic:** The code is structured more logically, making it easier to understand.
# - **Modularization:** Uses functions from the `home_plan` module to retrieve rooms, sensors, and actuators.
# - **Flexibility:** Can easily add more scenarios and actions by adding code within the simulation loop.
# - **Comments:** Includes comments to explain the purpose of each section.
# - **Simulates Time:** Uses `time.sleep` to simulate time passing, allowing for more realistic behavior.

# **To run this code:**

# 1. Ensure that all your project files (`sensor.py`, `actuator.py`, `home_plan.py`, `config.py`, and `function.py`) are in their respective folders.
# 2. Run the `function.py` file: `python functions/function.py`

# You should see the simulation output in your console, showing the sensor readings, actuator actions, and the simulated temperature, humidity, and light intensity changes over time.
