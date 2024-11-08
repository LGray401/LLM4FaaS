# Here is the 'function.py' file based on your given functional description:

from home.home_plan import get_room_actuators, get_room_sensors, get_all_actuators, get_all_sensors, print_home_plan

def main():
    home = home_plan()
    
    # Get sensors and actuators for each plan
    morning_plan_sensors = get_all_sensors(home, "IndoorTemperature")
    morning_plan_actuators = get_all_actuators(home, "Light")
    
    leave_home_plan_sensors = get_all_sensors(home, "IndoorTemperature")
    leave_home_plan_actuators = get_all_actuators(home, "Light")
    
    movie_plan_sensors = get_all_sensors(home, "LightIntensive")
    movie_plan_actuators = get_all_actuators(home, "Light")
    
    # Execute morning plan
    execute_plan("Morning Plan", morning_plan_sensors, morning_plan_actuators)
    
    # Execute leave home plan
    execute_plan("Leave Home Plan", leave_home_plan_sensors, leave_home_plan_actuators)
    
    # Execute movie plan
    execute_plan("Movie Plan", movie_plan_sensors, movie_plan_actuators)
    
def execute_plan(plan_name, sensors, actuators):
    print(f"Executing {plan_name}")
    
    # Turn on all sensors
    for sensor in sensors:
        sensor.turn_on()
        
    # Perform actions based on sensor readings and actuator settings
    for sensor in sensors:
        reading = sensor.get_reading()
        if sensor.sensor_type == "IndoorTemperature":
            if reading < 20:
                for actuator in actuators:
                    actuator.turn_on()
        elif sensor.sensor_type == "LightIntensive":
            if reading > 800:
                for actuator in actuators:
                    actuator.turn_off()
                    
    # Turn off all sensors
    for sensor in sensors:
        sensor.turn_off()
        
    print(f"{plan_name} executed successfully!")
    
if __name__ == "__main__":
    main()