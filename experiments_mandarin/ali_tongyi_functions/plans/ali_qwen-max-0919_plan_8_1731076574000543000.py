# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to execute the morning, leave home, and movie plans. This file will be placed in the `functions` folder.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators, get_all_sensors
from home.actuator import Light, SmartTV, Door, AC, Heater, NotificationSender
from home.sensor import IndoorTemperatureSensor, HumiditySensor
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH

def execute_morning_plan(home):
    print("\n--- Executing Morning Plan ---")
    
    # Get all rooms with actuators and sensors
    for room in home:
        # Turn on lights
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("medium")
        
        # Open curtains
        for actuator in room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()
        
        # Open windows
        for actuator in room.actuators:
            if isinstance(actuator, Window):
                actuator.turn_on()
        
        # Adjust temperature
        indoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
        if indoor_temp_sensors:
            current_temp = indoor_temp_sensors[0].get_reading()
            if current_temp < TEMP_LOW:
                for actuator in room.actuators:
                    if isinstance(actuator, Heater):
                        actuator.turn_on()
            elif current_temp > TEMP_HIGH:
                for actuator in room.actuators:
                    if isinstance(actuator, AC):
                        actuator.turn_on()
        
        # Adjust humidity
        humidity_sensors = [sensor for sensor in room.sensors if isinstance(sensor, HumiditySensor)]
        if humidity_sensors:
            current_humidity = humidity_sensors[0].get_reading()
            if current_humidity < HUMIDITY_LOW:
                for actuator in room.actuators:
                    if isinstance(actuator, Humidifier):
                        actuator.turn_on()
                        actuator.increase_humidity()
            elif current_humidity > HUMIDITY_HIGH:
                for actuator in room.actuators:
                    if isinstance(actuator, Humidifier):
                        actuator.turn_on()
                        actuator.decrease_humidity()
        
        # Make coffee in the kitchen
        if room.name == "Kitchen":
            for actuator in room.actuators:
                if isinstance(actuator, CoffeeMachine):
                    actuator.turn_on()
                    actuator.make_coffee("Latte")
        
        # Play music in the living room
        if room.name == "LivingRoom":
            for actuator in room.actuators:
                if isinstance(actuator, MusicPlayer):
                    actuator.turn_on()
                    actuator.play_music("Morning Playlist")

def execute_leave_home_plan(home):
    print("\n--- Executing Leave Home Plan ---")
    
    # Lock all doors
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Door):
                actuator.turn_off()
                actuator.lock()
    
    # Turn off all lights
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()
    
    # Turn off all other actuators
    for room in home:
        for actuator in room.actuators:
            if not isinstance(actuator, (Door, Light)):
                actuator.turn_off()
    
    # Send notification
    notification_sender = next((act for room in home for act in room.actuators if isinstance(act, NotificationSender)), None)
    if notification_sender:
        notification_sender.turn_on()
        notification_sender.notification_sender("Home is now secure. Have a nice day!")

def execute_movie_plan(home):
    print("\n--- Executing Movie Plan ---")
    
    # Turn on TV in the living room
    living_room = get_room(home, "LivingRoom")
    if living_room:
        for actuator in living_room.actuators:
            if isinstance(actuator, SmartTV):
                actuator.turn_on()
                actuator.play_channel("Movie Channel")
    
    # Turn off lights in the living room
    if living_room:
        for actuator in living_room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()

def main():
    home = home_plan()
    
    while True:
        print("\n--- Smart Home Control Menu ---")
        print("1. Execute Morning Plan")
        print("2. Execute Leave Home Plan")
        print("3. Execute Movie Plan")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            execute_morning_plan(home)
        elif choice == "2":
            execute_leave_home_plan(home)
        elif choice == "3":
            execute_movie_plan(home)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()