# Based on your provided functional description and source code, I will now provide a `function.py` file that contains the main function to interact with your smart home system. This `function.py` will be located in the `functions` folder and will utilize the classes and methods defined in the `sensor.py`, `actuator.py`, and `home_plan.py` files.
# 
# Here's the `function.py` file:

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import Sensor
from home.actuator import Actuator
from home.logger_config import logger

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Print the home plan
    print_home_plan(home)
    
    # Example of turning on a light in the LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room:
        for actuator in living_room.actuators:
            if actuator.actuator_type == "Light":
                actuator.turn_on()
                break
    
    # Example of getting temperature readings from all IndoorTemperature sensors
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in temperature_sensors:
        sensor.turn_on()
        print(f"Temperature reading from {sensor.id}: {sensor.get_reading()}°C")
        sensor.turn_off()
    
    # Example of adjusting the heater in the LivingRoom based on temperature
    living_room_heaters = get_all_actuators(home, "Heater")
    living_room_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    if living_room_heaters and living_room_temp_sensors:
        heater = living_room_heaters[0]  # Assuming only one heater in the LivingRoom
        temp_sensor = living_room_temp_sensors[0]  # Assuming only one temperature sensor in the LivingRoom
        temp_sensor.turn_on()
        current_temp = temp_sensor.get_reading()
        temp_sensor.turn_off()
        
        # Set a target temperature
        target_temp = 22  # Celsius degree
        heater.set_target_temperature(target_temp)
        heater.adjust_temperature(current_temp)
    
    # Example of sending a notification
    living_room_notification_senders = get_all_actuators(home, "NotificationSender")
    if living_room_notification_senders:
        notification_sender = living_room_notification_senders[0]  # Assuming only one NotificationSender in the LivingRoom
        notification_sender.turn_on()
        notification_sender.notification_sender("The temperature in the LivingRoom has been adjusted.")
        notification_sender.turn_off()
    
    # Example of daily routine for CleaningRobot
    living_room_cleaning_robots = get_all_actuators(home, "CleaningRobot")
    if living_room_cleaning_robots:
        cleaning_robot = living_room_cleaning_robots[0]  # Assuming only one CleaningRobot in the LivingRoom
        cleaning_robot.turn_on()
        cleaning_robot.daily_routine()

if __name__ == "__main__":
    main()