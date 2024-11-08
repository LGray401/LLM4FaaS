# To create a smart home application that opens windows to cool down based on the given functional description "开窗户降温" (open windows to cool down), we will need to utilize the existing sensor and actuator classes. The application will monitor the indoor temperature and, if it's above a certain threshold (defined in `config.py`), it will open the windows to cool down the room.
# 
# Here is a Python script to achieve this functionality:
# 
# ```python
# smart_home_app.py
from home.sensor import IndoorTemperatureSensor
from home.actuator import Window
from home.home_plan import home_plan, get_room_actuators
from home.config import TEMP_HIGH

def cool_down_room(room_name):
    # Load the home plan
    home = home_plan()

    # Get the room's actuators
    actuators = get_room_actuators(home, room_name)

    # Find windows in the room
    windows = [actuator for actuator in actuators if isinstance(actuator, Window)]

    if not windows:
        print(f"No windows found in {room_name}.")
        return

    # Get the room's sensors
    sensors = get_room_sensors(home, room_name)
    
    # Find the indoor temperature sensor in the room
    temperature_sensors = [sensor for sensor in sensors if isinstance(sensor, IndoorTemperatureSensor)]

    if not temperature_sensors:
        print(f"No indoor temperature sensor found in {room_name}.")
        return

    # Assume we are using the first temperature sensor found
    temp_sensor = temperature_sensors[0]
    temp_sensor.turn_on()
    current_temp = temp_sensor.get_reading()

    if current_temp is not None and current_temp > TEMP_HIGH:
        print(f"Current temperature in {room_name} is {current_temp}°C, which is above {TEMP_HIGH}°C. Opening windows.")
        for window in windows:
            window.turn_on()
    else:
        print(f"Current temperature in {room_name} is {current_temp}°C, no need to open windows.")

if __name__ == "__main__":
    room_name = "LivingRoom"  # You can change the room name as needed
    cool_down_room(room_name)
# ```
# 
# ### Command to Run the Application
# 
# To run this application from the Linux terminal, you can use:
# 
# ```bash
# python3 smart_home_app.py
# ```
# 
# ### Explanation
# 
# - **Sensors and Actuators**: The script uses `IndoorTemperatureSensor` to get the temperature reading for a specific room. It uses `Window` actuators to open windows when the temperature exceeds the threshold specified in `config.py`.
# - **Configuration**: The temperature threshold is set in `config.py` with `TEMP_HIGH`. This script checks the temperature against this threshold.
# - **Room Selection**: By default, the script checks the "LivingRoom". You can change `room_name` to any other room defined in your home plan.
# 
# Make sure that the `smart_home_app.py` file is in the same directory as the `home` folder and all necessary dependencies are correctly set up.