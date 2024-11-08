from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
import time

# ======================================================================================================================

# ----------------------------------- MORNING PLAN ---------------------------------------------
def morning_plan(home):
    print("\n---MORNING PLAN---")
    # 1. Open the Curtains
    print("Opening all curtains...")
    for room in home:
        for curtain in get_room_actuators(home, room.name):
            if curtain.actuator_type == "Curtain":
                curtain.turn_on()

    # 2. Turn on the light in living room
    print(f"Turning on the lights in LivingRoom...")
    for light in get_room_actuators(home, "LivingRoom"):
        if light.actuator_type == "Light":
            light.turn_on()

    # 3. Turn on the Coffee Machine
    print(f"Turning on the coffee machine in Kitchen...")
    for coffee_machine in get_room_actuators(home, "Kitchen"):
        if coffee_machine.actuator_type == "CoffeeMachine":
            coffee_machine.turn_on()

    # 4. Make a cup of coffee
    print(f"Making a cup of coffee...")
    for coffee_machine in get_room_actuators(home, "Kitchen"):
        if coffee_machine.actuator_type == "CoffeeMachine":
            coffee_machine.make_coffee("espresso")

    # 5. Play some music in living room
    print("Playing some music in LivingRoom...")
    for music_player in get_room_actuators(home, "LivingRoom"):
        if music_player.actuator_type == "MusicPlayer":
            music_player.play_music("morning playlist")

    # 6. Adjust temperature
    # Check the Indoor Temperature
    print(f"Checking Indoor Temperature in LivingRoom...")
    for sensor in get_room_sensors(home, "LivingRoom"):
        if sensor.sensor_type == "IndoorTemperature":
            current_temperature = sensor.get_reading()
    if current_temperature is not None:
        # Adjust the temperature
        print(f"Adjusting temperature in LivingRoom...")
        for heater in get_room_actuators(home, "LivingRoom"):
            if heater.actuator_type == "Heater":
                heater.set_target_temperature(20)
                heater.adjust_temperature(current_temperature)
        for ac in get_room_actuators(home, "LivingRoom"):
            if ac.actuator_type == "AC":
                ac.set_target_temperature(20)
                ac.adjust_temperature(current_temperature)
    else:
        print("Error getting Indoor Temperature.")

    # 7. Check the Humidity
    print(f"Checking humidity in LivingRoom...")
    for sensor in get_room_sensors(home, "LivingRoom"):
        if sensor.sensor_type == "Humidity":
            current_humidity = sensor.get_reading()
    if current_humidity is not None:
        # Adjust the humidity
        print(f"Adjusting humidity in LivingRoom...")
        for humidifier in get_room_actuators(home, "LivingRoom"):
            if humidifier.actuator_type == "Humidifier":
                if current_humidity < HUMIDITY_LOW:
                    print(f"Increasing humidity in LivingRoom...")
                    humidifier.increase_humidity()
                    time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                elif current_humidity > HUMIDITY_HIGH:
                    print(f"Decreasing humidity in LivingRoom...")
                    humidifier.decrease_humidity()
                    time.sleep(TEMP_CHANGE_DURATION_WINDOW)
        print("The humidity is adjusted now.")
    else:
        print("Error getting humidity.")

    print("\nMorning plan completed!")

# ----------------------------------- LEAVE HOME PLAN ---------------------------------------------
def leave_home_plan(home):
    print("\n---LEAVE HOME PLAN---")
    # 1. Turn off lights in living room
    print(f"Turning off lights in LivingRoom...")
    for light in get_room_actuators(home, "LivingRoom"):
        if light.actuator_type == "Light":
            light.turn_off()

    # 2. Turn off music in living room
    print("Turning off music in LivingRoom...")
    for music_player in get_room_actuators(home, "LivingRoom"):
        if music_player.actuator_type == "MusicPlayer":
            music_player.turn_off()

    # 3. Turn off coffee machine in kitchen
    print(f"Turning off coffee machine in Kitchen...")
    for coffee_machine in get_room_actuators(home, "Kitchen"):
        if coffee_machine.actuator_type == "CoffeeMachine":
            coffee_machine.turn_off()

    # 4. Close the curtains
    print("Closing all curtains...")
    for room in home:
        for curtain in get_room_actuators(home, room.name):
            if curtain.actuator_type == "Curtain":
                curtain.turn_off()

    # 5. Lock the door
    print(f"Locking the door in LivingRoom...")
    for door in get_room_actuators(home, "LivingRoom"):
        if door.actuator_type == "Door":
            door.lock()

    # 6. Turn off Smart Socket in Living Room
    print(f"Turning off smart sockets in LivingRoom...")
    for smart_socket in get_room_actuators(home, "LivingRoom"):
        if smart_socket.actuator_type == "SmartSocket":
            smart_socket.turn_off()

    # 7. Turn off Smart Socket in Kitchen
    print(f"Turning off smart sockets in Kitchen...")
    for smart_socket in get_room_actuators(home, "Kitchen"):
        if smart_socket.actuator_type == "SmartSocket":
            smart_socket.turn_off()

    print("\nLeave home plan completed!")

# ----------------------------------- MOVIE PLAN ---------------------------------------------
def movie_plan(home):
    print("\n---MOVIE PLAN---")
    # 1. Turn on the lights in living room
    print(f"Turning on lights in LivingRoom...")
    for light in get_room_actuators(home, "LivingRoom"):
        if light.actuator_type == "Light":
            light.turn_on()

    # 2. Set the lights brightness level to low
    print(f"Setting lights brightness level to low in LivingRoom...")
    for light in get_room_actuators(home, "LivingRoom"):
        if light.actuator_type == "Light":
            light.set_brightness_level("low")

    # 3. Turn on the TV in living room
    print(f"Turning on Smart TV in LivingRoom...")
    for tv in get_room_actuators(home, "LivingRoom"):
        if tv.actuator_type == "SmartTV":
            tv.turn_on()

    # 4. Play a movie on the TV
    print(f"Playing a movie on the Smart TV in LivingRoom...")
    for tv in get_room_actuators(home, "LivingRoom"):
        if tv.actuator_type == "SmartTV":
            tv.play_channel("Netflix")

    # 5. Adjust the temperature
    # Check the Indoor Temperature
    print(f"Checking Indoor Temperature in LivingRoom...")
    for sensor in get_room_sensors(home, "LivingRoom"):
        if sensor.sensor_type == "IndoorTemperature":
            current_temperature = sensor.get_reading()
    if current_temperature is not None:
        # Adjust the temperature
        print(f"Adjusting temperature in LivingRoom...")
        for heater in get_room_actuators(home, "LivingRoom"):
            if heater.actuator_type == "Heater":
                heater.set_target_temperature(22)
                heater.adjust_temperature(current_temperature)
        for ac in get_room_actuators(home, "LivingRoom"):
            if ac.actuator_type == "AC":
                ac.set_target_temperature(22)
                ac.adjust_temperature(current_temperature)
    else:
        print("Error getting Indoor Temperature.")

    # 6. Check the Humidity
    print(f"Checking humidity in LivingRoom...")
    for sensor in get_room_sensors(home, "LivingRoom"):
        if sensor.sensor_type == "Humidity":
            current_humidity = sensor.get_reading()
    if current_humidity is not None:
        # Adjust the humidity
        print(f"Adjusting humidity in LivingRoom...")
        for humidifier in get_room_actuators(home, "LivingRoom"):
            if humidifier.actuator_type == "Humidifier":
                if current_humidity < HUMIDITY_LOW:
                    print(f"Increasing humidity in LivingRoom...")
                    humidifier.increase_humidity()
                    time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                elif current_humidity > HUMIDITY_HIGH:
                    print(f"Decreasing humidity in LivingRoom...")
                    humidifier.decrease_humidity()
                    time.sleep(TEMP_CHANGE_DURATION_WINDOW)
        print("The humidity is adjusted now.")
    else:
        print("Error getting humidity.")

    # 7. Close the curtains
    print("Closing all curtains...")
    for room in home:
        for curtain in get_room_actuators(home, room.name):
            if curtain.actuator_type == "Curtain":
                curtain.turn_off()

    print("\nMovie plan completed!")

# ----------------------------------- DAILY ROUTINE ---------------------------------------------
def daily_routine(home):
    print("\n---DAILY ROUTINE---")
    print(f"Cleaning Robot Starts Daily Routine")
    # 1. Turn on the Cleaning Robot in Living Room
    for cleaning_robot in get_room_actuators(home, "LivingRoom"):
        if cleaning_robot.actuator_type == "CleaningRobot":
            cleaning_robot.turn_on()
            cleaning_robot.daily_routine()
    print(f"Cleaning Robot Ends Daily Routine")

    print("\nDaily routine completed!")

# ----------------------------------- MAIN FUNCTION ---------------------------------------------

def main():
    home = home_plan()

    # Morning plan
    morning_plan(home)

    # Leave home plan
    leave_home_plan(home)

    # Movie plan
    movie_plan(home)

    # Daily Routine
    daily_routine(home)


if __name__ == "__main__":
    main()
