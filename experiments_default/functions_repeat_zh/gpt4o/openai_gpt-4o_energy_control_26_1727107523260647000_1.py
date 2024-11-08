# Based on the provided functional description and source code, I will create a `function.py` file that meets the requirements. The main function will cover the following behaviors:
# - Close the window when the AC is turned on in the bedroom or living room.
# - Open the window when the indoor temperature is above 26°C and the outdoor temperature is below 26°C.
# 
# Here's the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators, get_room_sensors
from home.actuator import AC, Window
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.config import TEMP_HIGH

def main():
    home = home_plan()
    
    # Get rooms
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")
    
    # List of rooms to monitor
    rooms_to_monitor = [living_room, bedroom]
    
    # Check each room for AC status and take actions
    for room in rooms_to_monitor:
        ac_units = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
        windows = [actuator for actuator in room.actuators if isinstance(actuator, Window)]
        
        for ac in ac_units:
            if ac.get_status() == "on":
                for window in windows:
                    window.turn_off()
                    print(f"Window {window.id} in {room.name} has been closed because AC {ac.id} is on.")
                    
    # Check temperature conditions for each room
    for room in home:
        indoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
        outdoor_temp_sensors = [sensor for sensor in home if isinstance(sensor, OutdoorTemperatureSensor)]
        
        for indoor_sensor in indoor_temp_sensors:
            indoor_temp = indoor_sensor.get_reading()
            if indoor_temp is not None and indoor_temp > TEMP_HIGH:
                for outdoor_sensor in outdoor_temp_sensors:
                    outdoor_temp = outdoor_sensor.get_reading()
                    if outdoor_temp is not None and outdoor_temp < TEMP_HIGH:
                        windows = [actuator for actuator in room.actuators if isinstance(actuator, Window)]
                        for window in windows:
                            window.turn_on()
                            print(f"Window {window.id} in {room.name} has been opened because indoor temperature is {indoor_temp}°C and outdoor temperature is {outdoor_temp}°C.")

if __name__ == "__main__":
    main()