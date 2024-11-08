# Given your project structure and the functional description, it seems like you want to create a `function.py` file that contains a main function to control and manage the smart home system. This file will interact with the sensors and actuators defined in your `sensor.py` and `actuator.py` files, and use the home plan defined in `home_plan.py`.
# 
# Here's a `function.py` file that you can place in the `functions` folder. This file will include a `main` function that initializes the home, sets up some basic controls, and provides a simple interface to interact with the smart home.
# 
# ### `functions/function.py`

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, SmartSocket, Door, CleaningRobot, SmartTV, Humidifier
from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Print the home plan for verification
    print_home_plan(home)
    
    while True:
        # Example: Control the temperature in the LivingRoom
        living_room = get_room(home, "LivingRoom")
        if living_room:
            indoor_temp_sensor = next((sensor for sensor in living_room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
            heater = next((actuator for actuator in living_room.actuators if isinstance(actuator, Heater)), None)
            ac = next((actuator for actuator in living_room.actuators if isinstance(actuator, AC)), None)
            
            if indoor_temp_sensor and heater and ac:
                current_temp = indoor_temp_sensor.get_reading()
                if current_temp is not None:
                    if current_temp < TEMP_LOW:
                        heater.set_target_temperature(TEMP_HIGH)
                        heater.adjust_temperature(current_temp)
                    elif current_temp > TEMP_HIGH:
                        ac.set_target_temperature(TEMP_LOW)
                        ac.adjust_temperature(current_temp)
        
        # Example: Control the humidity in the Bedroom
        bedroom = get_room(home, "Bedroom")
        if bedroom:
            humidity_sensor = next((sensor for sensor in bedroom.sensors if isinstance(sensor, HumiditySensor)), None)
            humidifier = next((actuator for actuator in bedroom.actuators if isinstance(actuator, Humidifier)), None)
            
            if humidity_sensor and humidifier:
                current_humidity = humidity_sensor.get_reading()
                if current_humidity is not None:
                    if current_humidity < HUMIDITY_LOW:
                        humidifier.increase_humidity()
                    elif current_humidity > HUMIDITY_HIGH:
                        humidifier.decrease_humidity()
        
        # Example: Turn on the lights in the Kitchen
        kitchen = get_room(home, "Kitchen")
        if kitchen:
            light = next((actuator for actuator in kitchen.actuators if isinstance(actuator, Light)), None)
            if light:
                light.turn_on()
                light.set_brightness_level("high")
        
        # Example: Start the cleaning robot in the LivingRoom
        cleaning_robot = next((actuator for actuator in living_room.actuators if isinstance(actuator, CleaningRobot)), None)
        if cleaning_robot:
            cleaning_robot.turn_on()
            cleaning_robot.daily_routine()
        
        # Sleep for a while before the next iteration
        time.sleep(DAILY_ROUTINE_DURATION)

def print_home_plan(home):
    print(f"\n---Home Plan---")
    for room in home:
        room.print_info()

if __name__ == "__main__":
    main()