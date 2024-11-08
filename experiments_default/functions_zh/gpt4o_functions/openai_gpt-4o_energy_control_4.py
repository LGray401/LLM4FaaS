# Given the functional description "开窗户降温" (which translates to "Open windows to cool down"), the main function in `function.py` should monitor the indoor temperature and open the windows if the temperature exceeds a certain threshold. Below is the implementation of `function.py` based on the provided source code and functional description.
# 
# ### `function.py`

from home_plan import home_plan, get_room_sensors, get_room_actuators
from config import TEMP_HIGH, TEMP_CHANGE_DURATION_WINDOW
import time

def main():
    home = home_plan()
    
    # Iterate through each room
    for room in home:
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)
        
        # Find the indoor temperature sensor and window actuators in the room
        temp_sensor = next((sensor for sensor in sensors if sensor.sensor_type == "IndoorTemperature"), None)
        windows = [actuator for actuator in actuators if actuator.actuator_type == "Window"]
        
        if temp_sensor and windows:
            temp_sensor.turn_on()
            current_temp = temp_sensor.get_reading()
            
            # If temperature is above the threshold, open the windows
            if current_temp > TEMP_HIGH:
                print(f"Temperature in {room.name} is {current_temp}°C, which is above {TEMP_HIGH}°C. Opening windows...")
                for window in windows:
                    window.turn_on()
                time.sleep(TEMP_CHANGE_DURATION_WINDOW)
            else:
                print(f"Temperature in {room.name} is {current_temp}°C, which is within the safe range.")
        
        # Turn off the sensors and actuators after use
        if temp_sensor:
            temp_sensor.turn_off()
        for window in windows:
            window.turn_off()

if __name__ == "__main__":
    main()