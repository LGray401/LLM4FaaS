# To create the smart home application according to your functional description, we need to implement the logic that controls the air conditioning and curtains based on temperature and light intensity readings. We'll make use of the existing `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files to manage sensors and actuators within a home setting.
# 
# Here's a new Python script that implements the required functionality:
# 
# ### smart_home.py
# ```python
from home.sensor import IndoorTemperatureSensor, LightIntensiveSensor
from home.actuator import AC, Curtain
from home.home_plan import home_plan, get_room
from home.config import TEMP_HIGH, LIGHT_INTENSITY_HIGH
import time

def main():
    # Initialize the home with the defined home plan
    home = home_plan()

    # Select the room to monitor, e.g., "LivingRoom"
    room_name = "LivingRoom"
    room = get_room(home, room_name)

    if not room:
        print(f"Room {room_name} not found.")
        return

    # Get sensors and actuators from the room
    temperature_sensor = next((s for s in room.sensors if isinstance(s, IndoorTemperatureSensor)), None)
    light_sensor = next((s for s in room.sensors if isinstance(s, LightIntensiveSensor)), None)
    ac = next((a for a in room.actuators if isinstance(a, AC)), None)
    curtain = next((a for a in room.actuators if isinstance(a, Curtain)), None)

    # Ensure all components are available
    if not temperature_sensor or not light_sensor or not ac or not curtain:
        print("Some sensors or actuators are missing in the room.")
        return

    # Turn on sensors and actuators
    temperature_sensor.turn_on()
    light_sensor.turn_on()

    ac.turn_on()
    ac.set_target_temperature(TEMP_HIGH)
    
    curtain.turn_on()

    try:
        while True:
            # Get current readings
            current_temperature = temperature_sensor.get_reading()
            current_light_intensity = light_sensor.get_reading()

            # Control AC based on temperature
            ac.adjust_temperature(current_temperature)

            # Control Curtain based on light intensity
            if current_light_intensity > LIGHT_INTENSITY_HIGH:
                curtain.turn_on()
            else:
                curtain.turn_off()

            # Wait before the next reading
            time.sleep(5)  # Delay between readings
    except KeyboardInterrupt:
        print("Stopping the smart home application.")

if __name__ == "__main__":
    main()
# ```
# 
# ### How to Run the Application
# 
# 1. Save the above code as `smart_home.py` in the same directory as your `'home'` folder containing `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`.
# 2. Open your terminal and navigate to the directory where `smart_home.py` is located.
# 3. Run the application with the following command:
# 
#    ```bash
#    python3 smart_home.py
#    ```
# 
# ### Explanation
# 
# - The script initializes the home environment using `home_plan()` and retrieves the specified room.
# - It identifies sensors and actuators of interest (temperature sensor, light sensor, AC, and curtain) within the room.
# - It continuously monitors the temperature and light intensity.
# - When the temperature exceeds 26°C, the air conditioning is activated to adjust the temperature.
# - When the light intensity is high, the curtain is automatically opened, and it closes otherwise.
# - The loop runs until you stop the program manually (e.g., by pressing `Ctrl+C`).
# 
# Feel free to modify the script and configurations to tailor it to your specific needs or room setup.