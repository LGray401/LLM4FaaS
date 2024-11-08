# Based on your provided functional description and source code, I will create a `function.py` file that includes the main function to handle the different modes: 睡觉模式 (Sleep Mode), 起床模式 (Wake Up Mode), 关灯模式 (Turn Off Lights Mode), and 关窗模式 (Close Windows Mode). 
# 
# Here is the `function.py` file:

# functions/function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, SmartSocket, Door, CleaningRobot, SmartTV, Humidifier
from home.home_plan import home_plan, get_room_actuators, get_room_sensors
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION

def sleep_mode(home):
    print("Entering Sleep Mode...")
    for room in home:
        if room.name == "Bedroom":
            # Turn off lights
            for actuator in get_room_actuators(home, room.name):
                if isinstance(actuator, Light):
                    actuator.turn_off()
            
            # Close windows
            for actuator in get_room_actuators(home, room.name):
                if isinstance(actuator, Window):
                    actuator.turn_off()
            
            # Close curtains
            for actuator in get_room_actuators(home, room.name):
                if isinstance(actuator, Curtain):
                    actuator.turn_off()
            
            # Set temperature
            for actuator in get_room_actuators(home, room.name):
                if isinstance(actuator, AC) or isinstance(actuator, Heater):
                    current_temp = get_room_sensors(home, room.name)[0].get_reading()
                    if current_temp < TEMP_LOW:
                        actuator.set_target_temperature(TEMP_LOW)
                        actuator.adjust_temperature(current_temp)
                    elif current_temp > TEMP_HIGH:
                        actuator.set_target_temperature(TEMP_HIGH)
                        actuator.adjust_temperature(current_temp)
            
            # Play soft music
            for actuator in get_room_actuators(home, room.name):
                if isinstance(actuator, MusicPlayer):
                    actuator.turn_on()
                    actuator.play_music("SoftMusic")
                    time.sleep(30)  # Play for 30 seconds
                    actuator.turn_off()

def wake_up_mode(home):
    print("Entering Wake Up Mode...")
    for room in home:
        if room.name == "Bedroom":
            # Turn on lights
            for actuator in get_room_actuators(home, room.name):
                if isinstance(actuator, Light):
                    actuator.turn_on()
                    actuator.set_brightness_level("medium")
            
            # Open windows
            for actuator in get_room_actuators(home, room.name):
                if isinstance(actuator, Window):
                    actuator.turn_on()
            
            # Open curtains
            for actuator in get_room_actuators(home, room.name):
                if isinstance(actuator, Curtain):
                    actuator.turn_on()
            
            # Set temperature
            for actuator in get_room_actuators(home, room.name):
                if isinstance(actuator, AC) or isinstance(actuator, Heater):
                    current_temp = get_room_sensors(home, room.name)[0].get_reading()
                    if current_temp < TEMP_LOW:
                        actuator.set_target_temperature(TEMP_LOW)
                        actuator.adjust_temperature(current_temp)
                    elif current_temp > TEMP_HIGH:
                        actuator.set_target_temperature(TEMP_HIGH)
                        actuator.adjust_temperature(current_temp)
            
            # Make coffee
            for actuator in get_room_actuators(home, "Kitchen"):
                if isinstance(actuator, CoffeeMachine):
                    actuator.turn_on()
                    actuator.make_coffee("Espresso")
            
            # Play morning music
            for actuator in get_room_actuators(home, room.name):
                if isinstance(actuator, MusicPlayer):
                    actuator.turn_on()
                    actuator.play_music("MorningMusic")
                    time.sleep(30)  # Play for 30 seconds
                    actuator.turn_off()

def turn_off_lights_mode(home):
    print("Turning Off All Lights...")
    for room in home:
        for actuator in get_room_actuators(home, room.name):
            if isinstance(actuator, Light):
                actuator.turn_off()

def close_windows_mode(home):
    print("Closing All Windows...")
    for room in home:
        for actuator in get_room_actuators(home, room.name):
            if isinstance(actuator, Window):
                actuator.turn_off()

def main():
    home = home_plan()
    
    while True:
        print("\n--- Smart Home Control ---")
        print("1. Sleep Mode")
        print("2. Wake Up Mode")
        print("3. Turn Off Lights Mode")
        print("4. Close Windows Mode")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            sleep_mode(home)
        elif choice == '2':
            wake_up_mode(home)
        elif choice == '3':
            turn_off_lights_mode(home)
        elif choice == '4':
            close_windows_mode(home)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()