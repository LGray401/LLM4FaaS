# To implement the smart home application based on your functional description, we need to use the provided sensor and actuator classes to automate the behavior described. Let's break down the requirements and implement the logic accordingly:
# 
# 1. **Kitchen Smoke Detection**: If the smoke level in the kitchen is above a certain threshold, turn on the smoke alarm.
# 2. **Temperature Control in Summer**:
#    - Turn off the air conditioning if the temperature is below 20°C.
#    - Turn on the air conditioning if the temperature is above 25°C.
# 3. **Motion-Activated Light**: Turn on lights when motion is detected and turn them off when no motion is detected.
# 
# First, let's make some assumptions and define thresholds for the smoke level and the motion detection. We will assume a smoke level threshold of 50 for triggering the alarm, and we'll simulate motion detection with a simple toggle.
# 
# Here's how the code can be structured:
# 
# ### Smart Home Application (`smart_home.py`)
# 
# ```python
from home.sensor import SmokeSensor, IndoorTemperatureSensor
from home.actuator import AC, Light
from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from time import sleep

# Thresholds
SMOKE_THRESHOLD = 50
SUMMER_TEMP_LOW = 20
SUMMER_TEMP_HIGH = 25

# Simulated function for detecting motion
def detect_motion():
    # Replace this logic with actual motion detection logic if available
    return True  # Assume motion is detected for demonstration

def main():
    home = home_plan()

    # Get kitchen and living room
    kitchen = get_room(home, "Kitchen")
    living_room = get_room(home, "LivingRoom")

    # Get sensors and actuators
    smoke_sensors = get_room_sensors(home, "Kitchen")
    indoor_temp_sensors = get_room_sensors(home, "LivingRoom")
    ac_units = get_room_actuators(home, "LivingRoom")
    lights = get_room_actuators(home, "LivingRoom")

    # Turn on sensors to get readings
    for sensor in smoke_sensors + indoor_temp_sensors:
        sensor.turn_on()

    # Main loop to simulate the smart home behavior
    while True:
        # Check smoke levels in the kitchen
        for sensor in smoke_sensors:
            if isinstance(sensor, SmokeSensor):
                smoke_level = sensor.get_reading()
                if smoke_level and smoke_level > SMOKE_THRESHOLD:
                    print("Smoke level high! Activating smoke alarm.")
                    # Assuming there's an alarm actuator, we would turn it on here

        # Check indoor temperature and control AC
        for sensor in indoor_temp_sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                temp = sensor.get_reading()
                for ac in ac_units:
                    if isinstance(ac, AC):
                        if temp < SUMMER_TEMP_LOW:
                            ac.turn_off()
                        elif temp > SUMMER_TEMP_HIGH:
                            ac.turn_on()

        # Motion detection for lights
        if detect_motion():
            print("Motion detected! Turning on lights.")
            for light in lights:
                light.turn_on()
        else:
            print("No motion detected. Turning off lights.")
            for light in lights:
                light.turn_off()

        # Sleep for a while before next check
        sleep(5)

if __name__ == "__main__":
    main()
# ```
# 
# ### Running the Application
# 
# To run this application in a Linux terminal:
# 
# 1. Ensure you have the `home` directory with the provided Python files (`sensor.py`, `actuator.py`, `home_plan.py`, `config.py`).
# 2. Save the above code as `smart_home.py` in the same directory level as the `home` directory.
# 3. Run the following command in the terminal:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# This implementation assumes that the smoke alarm is integrated into the system, but the actual actuator for the alarm is not defined in the provided code. You would need to implement an `Alarm` class as an actuator if you wanted to simulate turning on an alarm.