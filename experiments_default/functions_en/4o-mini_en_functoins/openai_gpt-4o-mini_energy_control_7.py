# Based on your functional description and the provided source code, I will create a `function.py` file that implements the desired behavior for your smart home project. The main function will automatically close doors and windows when the air conditioner is on and will prompt to open windows if the indoor temperature is high and the outdoor temperature is low.
# 
# Here's the content for `function.py`:

# function.py
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH
from home.actuator import Window, Door, AC
from home.logger_config import logger

def close_doors_and_windows(home):
    for room in home:
        ac_instances = get_all_actuators(home, "AC")
        for ac in ac_instances:
            if ac.get_status() == "on":
                for actuator in room.actuators:
                    if isinstance(actuator, Window) or isinstance(actuator, Door):
                        actuator.turn_off()
                        logger.info(f"{actuator.id} is turned OFF because AC is ON.")

def check_temperature_and_open_windows(home):
    indoor_sensors = get_all_sensors(home, "IndoorTemperature")
    outdoor_sensors = get_all_sensors(home, "OutdoorTemperature")
    
    for indoor_sensor in indoor_sensors:
        indoor_temp = indoor_sensor.get_reading()
        
        for outdoor_sensor in outdoor_sensors:
            outdoor_temp = outdoor_sensor.get_reading()
            
            if indoor_temp is not None and outdoor_temp is not None:
                if indoor_temp > TEMP_HIGH and outdoor_temp < TEMP_LOW:
                    print("Indoor temperature is high and outdoor temperature is low.")
                    response = input("Would you like to open the windows to cool down? (yes/no): ")
                    if response.lower() == 'yes':
                        for room in home:
                            for actuator in room.actuators:
                                if isinstance(actuator, Window):
                                    actuator.turn_on()  # Assuming 'turn_on' would open the window
                                    logger.info(f"{actuator.id} is turned ON to open the window.")

def main():
    home = home_plan()
    close_doors_and_windows(home)
    check_temperature_and_open_windows(home)

if __name__ == "__main__":
    main()