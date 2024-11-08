# Based on the functional description and the provided source code, I will create a `function.py` file that includes a main function to control and monitor the sensors and actuators in your smart home. This script will be placed in the `functions` folder.
# 
# The main function will:
# - Initialize the home plan.
# - Print the home plan.
# - Allow for querying and controlling specific sensors and actuators based on user input.
# 
# Here is the `function.py` file:

# functions/function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, OutdoorTemperatureSensor
from home.actuator import Heater, AC, Humidifier, Light, CleaningRobot, NotificationSender
from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    # Initialize the home plan
    home = home_plan()
    print_home_plan(home)

    while True:
        print("\n--- Smart Home Control ---")
        print("1. Get temperature")
        print("2. Get humidity")
        print("3. Get light intensity")
        print("4. Adjust temperature (Heater/AC)")
        print("5. Adjust humidity (Humidifier)")
        print("6. Turn on/off lights")
        print("7. Start cleaning robot")
        print("8. Send notification")
        print("9. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            room_name = input("Enter room name: ")
            sensors = get_room_sensors(home, room_name)
            if sensors:
                for sensor in sensors:
                    if isinstance(sensor, (IndoorTemperatureSensor, OutdoorTemperatureSensor)):
                        sensor.turn_on()
                        reading = sensor.get_reading()
                        if reading is not None:
                            print(f"Temperature in {room_name} is {reading}°C")
                        sensor.turn_off()

        elif choice == '2':
            room_name = input("Enter room name: ")
            sensors = get_room_sensors(home, room_name)
            if sensors:
                for sensor in sensors:
                    if isinstance(sensor, HumiditySensor):
                        sensor.turn_on()
                        reading = sensor.get_reading()
                        if reading is not None:
                            print(f"Humidity in {room_name} is {reading}%")
                        sensor.turn_off()

        elif choice == '3':
            room_name = input("Enter room name: ")
            sensors = get_room_sensors(home, room_name)
            if sensors:
                for sensor in sensors:
                    if isinstance(sensor, LightIntensiveSensor):
                        sensor.turn_on()
                        reading = sensor.get_reading()
                        if reading is not None:
                            print(f"Light intensity in {room_name} is {reading} lux")
                        sensor.turn_off()

        elif choice == '4':
            room_name = input("Enter room name: ")
            target_temperature = float(input("Enter target temperature: "))
            actuators = get_room_actuators(home, room_name)
            if actuators:
                for actuator in actuators:
                    if isinstance(actuator, (Heater, AC)):
                        actuator.set_target_temperature(target_temperature)
                        actuator.adjust_temperature(20)  # Example current temperature

        elif choice == '5':
            room_name = input("Enter room name: ")
            action = input("Increase or decrease humidity? (increase/decrease): ")
            actuators = get_room_actuators(home, room_name)
            if actuators:
                for actuator in actuators:
                    if isinstance(actuator, Humidifier):
                        if action == "increase":
                            actuator.increase_humidity()
                        elif action == "decrease":
                            actuator.decrease_humidity()

        elif choice == '6':
            room_name = input("Enter room name: ")
            action = input("Turn on or off lights? (on/off): ")
            actuators = get_room_actuators(home, room_name)
            if actuators:
                for actuator in actuators:
                    if isinstance(actuator, Light):
                        if action == "on":
                            actuator.turn_on()
                        elif action == "off":
                            actuator.turn_off()

        elif choice == '7':
            room_name = input("Enter room name: ")
            actuators = get_room_actuators(home, room_name)
            if actuators:
                for actuator in actuators:
                    if isinstance(actuator, CleaningRobot):
                        actuator.turn_on()
                        actuator.daily_routine()

        elif choice == '8':
            room_name = input("Enter room name: ")
            message = input("Enter message: ")
            actuators = get_room_actuators(home, room_name)
            if actuators:
                for actuator in actuators:
                    if isinstance(actuator, NotificationSender):
                        actuator.turn_on()
                        actuator.notification_sender(message)

        elif choice == '9':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()