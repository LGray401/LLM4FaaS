# Based on the provided functional description and the source code files, we will create a `function.py` file. This file will be placed in the `functions` folder and will include the main function as described. 
# 
# Here's the `function.py` file:

import time
from home.home_plan import home_plan, get_room, get_room_actuators, get_room_sensors
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import AC, Window, NotificationSender

def main():
    home = home_plan()
    
    while True:
        user_input = input("Please enter your request (e.g., 'open window in LivingRoom', 'it's too hot', 'exit'): ")
        
        if user_input == 'exit':
            print("Exiting the smart home system.")
            break
        
        if 'open window' in user_input:
            room_name = user_input.split(' in ')[1]
            room = get_room(home, room_name)
            if room:
                outdoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, OutdoorTemperatureSensor)]
                if outdoor_temp_sensors:
                    outdoor_temp = outdoor_temp_sensors[0].get_reading()
                    if outdoor_temp > 25:
                        print("It's too hot outside. Suggest using AC instead.")
                        acs = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
                        if acs:
                            acs[0].turn_on()
                    elif outdoor_temp < 15:
                        print("It's too cold outside. Suggest using Heater instead.")
                    else:
                        windows = [actuator for actuator in room.actuators if isinstance(actuator, Window)]
                        if windows:
                            windows[0].turn_on()
                
        elif 'too hot' in user_input:
            for room in home:
                indoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
                outdoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, OutdoorTemperatureSensor)]
                
                if indoor_temp_sensors:
                    indoor_temp = indoor_temp_sensors[0].get_reading()
                    if indoor_temp > 25:
                        if outdoor_temp_sensors:
                            outdoor_temp = outdoor_temp_sensors[0].get_reading()
                            if outdoor_temp < 25:
                                windows = [actuator for actuator in room.actuators if isinstance(actuator, Window)]
                                if windows:
                                    windows[0].turn_on()
                            else:
                                acs = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
                                if acs:
                                    acs[0].turn_on()
                                    
        elif 'window open with AC' in user_input:
            for room in home:
                windows = [actuator for actuator in room.actuators if isinstance(actuator, Window)]
                acs = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
                
                if any(window.get_status() == 'on' for window in windows) and any(ac.get_status() == 'on' for ac in acs):
                    notification_senders = [actuator for actuator in room.actuators if isinstance(actuator, NotificationSender)]
                    if notification_senders:
                        notification_senders[0].turn_on()
                        notification_senders[0].notification_sender("The window is open while AC is on. Do you want to turn off the AC?")
        
        time.sleep(2)  # Delay for 2 seconds before the next iteration

if __name__ == "__main__":
    main()