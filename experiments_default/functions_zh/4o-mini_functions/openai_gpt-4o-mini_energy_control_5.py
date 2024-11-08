# Based on the provided functional description and existing code files for your smart home project, I will create a `function.py` file that serves as the main entry point for your application. This file will utilize the classes and functions defined in your other files to demonstrate basic interactions within your smart home system.
# 
# Here is the content for `function.py`:

# function.py

from home.home_plan import home_plan, print_home_plan, get_room, get_all_sensors, get_all_actuators
from home.logger_config import logger

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Print the home plan
    print_home_plan(home)

    # Example: Interact with a specific room
    room_name = "LivingRoom"
    room = get_room(home, room_name)

    if room:
        # Turn on all lights in the Living Room
        for actuator in get_all_actuators(home, "Light"):
            actuator.turn_on()

        # Get readings from all temperature sensors in the Living Room
        for sensor in get_all_sensors(home, "IndoorTemperature"):
            sensor.turn_on()  # Ensure the sensor is on before getting readings
            sensor.get_reading()

        # Example to interact with a specific actuator (Heater)
        heater = next((a for a in room.actuators if a.actuator_type == "Heater"), None)
        if heater:
            heater.set_target_temperature(22)  # Set the desired temperature
            current_temp = next((s.get_reading() for s in room.sensors if s.sensor_type == "IndoorTemperature"), 20)
            heater.adjust_temperature(current_temp)  # Adjust the heater based on current temperature

        # Example of sending a notification
        notifier = next((a for a in room.actuators if a.actuator_type == "NotificationSender"), None)
        if notifier:
            notifier.turn_on()
            notifier.notification_sender("Living Room temperature adjusted.")

if __name__ == "__main__":
    main()