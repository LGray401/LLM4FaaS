# Based on your functional description and the provided source code, I will create a `function.py` file that includes a `main` function. This function will utilize the classes defined in the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files to simulate a basic interaction in your smart home system.
# 
# Here's the `function.py` file:

# function.py

from home.home_plan import home_plan, print_home_plan, get_room, get_all_sensors, get_all_actuators
from home.logger_config import logger
import random
import time

def main():
    # Initialize the home with rooms and components
    home = home_plan()
    print_home_plan(home)

    # Example interaction with a room
    room_name = "LivingRoom"
    room = get_room(home, room_name)

    if room:
        # Turn on all lights in the Living Room
        lights = get_all_actuators(home, "Light")
        for light in lights:
            light.turn_on()
            time.sleep(0.5)  # Simulate a delay in turning on lights

        # Get temperature readings from all temperature sensors
        temperature_sensors = get_all_sensors(home, "IndoorTemperature")
        for sensor in temperature_sensors:
            sensor.turn_on()
            reading = sensor.get_reading()
            time.sleep(0.5)  # Simulate a delay for reading
            if reading is not None:
                # Example action based on temperature reading
                if reading < 18:
                    heater = get_all_actuators(home, "Heater")[0]  # Get the first heater
                    heater.set_target_temperature(22)
                    heater.adjust_temperature(reading)
                    heater.turn_on()
                elif reading > 24:
                    ac = get_all_actuators(home, "AC")[0]  # Get the first AC
                    ac.set_target_temperature(21)
                    ac.adjust_temperature(reading)
                    ac.turn_on()
                    
        # Turn off all lights after reading
        for light in lights:
            light.turn_off()

        # Notify user of the actions taken
        notifier = get_all_actuators(home, "NotificationSender")[0]
        notifier.turn_on()
        notifier.notification_sender(f"Temperature readings taken and actions performed in {room_name}.")

if __name__ == "__main__":
    main()