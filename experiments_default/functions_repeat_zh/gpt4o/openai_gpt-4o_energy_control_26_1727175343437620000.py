# Sure! Based on your functional requirements and the provided source code, I'll create the `function.py` file. This file will contain the main function that performs the specified actions: turning off the window when the AC is on in the bedroom or living room, and opening the window if the indoor temperature is above 26°C and the outdoor temperature is below 26°C.
# 
# Here's the `function.py` file to be placed in the `functions` folder:

from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import Window, AC
from home.home_plan import home_plan, get_room

def main():
    # Initialize home plan
    home = home_plan()
    
    # Define the rooms of interest
    rooms_of_interest = ["Bedroom", "LivingRoom"]
    
    for room_name in rooms_of_interest:
        room = get_room(home, room_name)
        
        if room:
            # Check if AC is on and Turn off the Window if AC is on
            ac_unit = next((actuator for actuator in room.actuators if isinstance(actuator, AC)), None)
            window = next((actuator for actuator in room.actuators if isinstance(actuator, Window)), None)
            
            if ac_unit and window:
                ac_unit_status = ac_unit.get_status()
                if ac_unit_status == "on":
                    window.turn_off()

            # Check indoor and outdoor temperatures
            indoor_temp_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
            outdoor_temp_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, OutdoorTemperatureSensor)), None)
            
            if indoor_temp_sensor and outdoor_temp_sensor:
                indoor_temp = indoor_temp_sensor.get_reading()
                outdoor_temp = outdoor_temp_sensor.get_reading()
                
                if indoor_temp is not None and outdoor_temp is not None:
                    if indoor_temp > 26 and outdoor_temp < 26:
                        window.turn_on()

if __name__ == "__main__":
    main()