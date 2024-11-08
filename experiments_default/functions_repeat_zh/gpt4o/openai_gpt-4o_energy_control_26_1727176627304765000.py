# Sure! Based on the provided functional description and the source code of your smart home project, here is the `function.py` file. 
# 
# This file will contain a main function that implements the described logic:
# 
# - When the air conditioner in the bedroom or living room is turned on, the window in that room should be closed.
# - When the indoor temperature exceeds 26°C, and the outdoor temperature is below 26°C, the window should be opened.
# 
# Here's the `function.py` file:

from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import Window, AC
from home.home_plan import home_plan, get_room_actuators, get_room_sensors

def manage_windows_based_on_ac_and_temperature(home):
    rooms_of_interest = ["Bedroom", "LivingRoom"]
    for room_name in rooms_of_interest:
        room_actuators = get_room_actuators(home, room_name)
        room_sensors = get_room_sensors(home, room_name)
        
        # Get the AC and Window actuators
        ac_unit = next((act for act in room_actuators if isinstance(act, AC)), None)
        windows = [act for act in room_actuators if isinstance(act, Window)]
        
        # Get the indoor temperature sensor
        indoor_temp_sensor = next((sen for sen in room_sensors if isinstance(sen, IndoorTemperatureSensor)), None)
        
        # Check if the AC is on and close windows
        if ac_unit and ac_unit.get_status() == "on":
            for window in windows:
                window.turn_off()  # Close the window
        
        # Check temperatures and manage windows
        if indoor_temp_sensor:
            indoor_temp = indoor_temp_sensor.get_reading()
            if indoor_temp and indoor_temp > 26:
                outdoor_temp_sensor = next((sen for sen in room_sensors if isinstance(sen, OutdoorTemperatureSensor)), None)
                if outdoor_temp_sensor:
                    outdoor_temp = outdoor_temp_sensor.get_reading()
                    if outdoor_temp and outdoor_temp < 26:
                        for window in windows:
                            window.turn_on()  # Open the window

def main():
    home = home_plan()
    
    # Turn on relevant sensors and actuators for testing
    for room in home:
        for sensor in room.sensors:
            sensor.turn_on()
        for actuator in room.actuators:
            actuator.turn_on()
    
    manage_windows_based_on_ac_and_temperature(home)

if __name__ == "__main__":
    main()