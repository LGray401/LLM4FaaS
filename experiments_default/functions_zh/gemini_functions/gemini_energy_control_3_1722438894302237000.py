from home.home_plan import home_plan, get_room, get_room_actuators, get_all_actuators
from home.sensor import IndoorTemperatureSensor
from home.actuator import AC, Window, Heater

def main():
    """
    This function demonstrates the main logic for the smart home system based on the provided code.
    It includes functions for opening windows and turning on/off AC based on temperature.
    """
    home = home_plan()

    # Get the living room and its AC
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        living_room_acs = get_room_actuators(home, "LivingRoom")
        living_room_ac = next((ac for ac in living_room_acs if ac.actuator_type == "AC"), None)

    # Get all windows in the home
    all_windows = get_all_actuators(home, "Window")

    # Simulate temperature changes and react accordingly
    for i in range(1, 11):
        print(f"---- Iteration {i} ----")
        # Simulate a temperature reading in the living room
        living_room_temperature = IndoorTemperatureSensor("LivingRoom")._generate_reading()
        print(f"Living Room Temperature: {living_room_temperature}°C")

        # Check if AC should be turned on/off
        if living_room_temperature > 25:
            if living_room_ac is not None and living_room_ac.status == "off":
                print(f"Turning on AC in the Living Room.")
                living_room_ac.turn_on()
        elif living_room_temperature < 15:
            if living_room_ac is not None and living_room_ac.status == "on":
                print(f"Turning off AC in the Living Room.")
                living_room_ac.turn_off()

        # Check if windows should be opened/closed
        for window in all_windows:
            if living_room_temperature > 25 and window.status == "off":
                print(f"Opening window in {window.room_name}")
                window.turn_on()
            elif living_room_temperature < 15 and window.status == "on":
                print(f"Closing window in {window.room_name}")
                window.turn_off()

        print("-----------------------")

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:**
#    - `home.home_plan`: Import functions for creating the home plan and accessing rooms and actuators.
#    - `home.sensor`: Import the `IndoorTemperatureSensor` to simulate temperature readings.
#    - `home.actuator`: Import the `AC`, `Window`, and `Heater` classes to control the devices.

# 2. **`main()` function:**
#    - Creates the `home` plan using `home_plan()`.
#    - Gets the `LivingRoom` and its `AC` using `get_room` and `get_room_actuators`.
#    - Retrieves all `Window` actuators using `get_all_actuators`.
#    - Simulates temperature changes in the living room using a loop (iterations 1 to 10).
#    - Inside the loop:
#      - Simulates a temperature reading using `IndoorTemperatureSensor._generate_reading()`.
#      - Checks if the temperature is above 25°C and turns on the AC if it's off.
#      - Checks if the temperature is below 15°C and turns off the AC if it's on.
#      - Iterates through all windows and opens them if the temperature is above 25°C and closes them if below 15°C.

# **Key Points:**

# - The code simulates the logic of opening windows and controlling AC based on temperature.
# - It demonstrates the use of sensor data and actuator control in a smart home environment.
# - The `main()` function provides a simple example of how to interact with the home plan, sensors, and actuators.

# **To use this code:**

# 1. Make sure you have the other Python files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) in the same directory as `function.py`.
# 2. Run `python function.py` in your terminal.
# 3. You will see the simulated temperature changes, AC status updates, and window actions in the console output.
