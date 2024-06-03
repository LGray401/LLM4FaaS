import time
from datetime import datetime
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.home_plan import home_plan, get_room_actuators, get_room


def morning_routine(home):
    # Get the current time
    now = datetime.now().time()

    # Check if it's 7 am
    if now.hour == 11 and now.minute == 35:
        print("Morning Routine started at 7:00 AM")

        # Get the LivingRoom actuators
        living_room_actuators = get_room_actuators(home, "LivingRoom")

        # Open the curtain
        curtain_actuator = [actuator for actuator in living_room_actuators if actuator.actuator_type == "Curtain"][0]
        curtain_actuator.turn_on()

        # Turn on the light if it's too dark
        light_actuator = [actuator for actuator in living_room_actuators if actuator.actuator_type == "Light"][0]
        if light_actuator.get_status() == "off":
            light_actuator.set_brightness_level("medium")

        # Play daily news
        music_player_actuator = [actuator for actuator in living_room_actuators if actuator.actuator_type == "MusicPlayer"][0]
        music_player_actuator.play_music("daily news")

        # Make a cup of coffee
        coffee_machine_actuator = [actuator for actuator in living_room_actuators if actuator.actuator_type == "Coffee"][0]
        coffee_machine_actuator.turn_on()

def evening_routine(home):
    # Get the current time
    now = datetime.now().time()

    # Check if it's 11 pm
    if now.hour == 11 and now.minute == 31:
        print("Evening Routine started at 11:00 PM")

        # Get the Bedroom actuators
        bedroom_actuators = get_room_actuators(home, "Bedroom")

        # Close the curtain
        curtain_actuator = [actuator for actuator in bedroom_actuators if actuator.actuator_type == "Curtain"][0]
        curtain_actuator.turn_off()

        # Play bedtime music
        music_player_actuator = [actuator for actuator in bedroom_actuators if actuator.actuator_type == "MusicPlayer"][0]
        music_player_actuator.play_music("bedtime music")

        # Turn the light to medium level
        light_actuator = [actuator for actuator in bedroom_actuators if actuator.actuator_type == "Light"][0]
        light_actuator.set_brightness_level("medium")

        # Turn off the light after half an hour
        time.sleep(18)  # Half an hour in seconds
        light_actuator.turn_off()

def home_plan_execution(home, plan_name):
    print(f"Executing {plan_name} Plan")

    if plan_name == "Home":
        # Get the LivingRoom actuators
        living_room_actuators = get_room_actuators(home, "LivingRoom")

        # Turn on Livingroom light
        light_actuator = [actuator for actuator in living_room_actuators if actuator.actuator_type == "Light"][0]
        light_actuator.turn_on()

        # Close Living room curtain
        curtain_actuator = [actuator for actuator in living_room_actuators if actuator.actuator_type == "Curtain"][0]
        curtain_actuator.turn_on()

        # Turn on all sockets
        sockets_actuators = get_room_actuators(home, "Kitchen")
        for socket_actuator in sockets_actuators:
            socket_actuator.turn_on()

    elif plan_name == "Away":
        # Turn off all lights at home
        for room in home:
            for actuator in room.actuators:
                if actuator.actuator_type == "Light":
                    actuator.turn_off()

        # Close all windows
        for room in home:
            for actuator in room.actuators:
                if actuator.actuator_type == "Window":
                    actuator.turn_off()

        # Lock the home door
        home_door_actuator = get_room_actuators(home, "Balcony")[0]
        home_door_actuator.turn_on()

        # Start the cleaning robot
        # cleaning_robot_actuator = get_room_actuators(home, "LivingRoom")[0]
        # cleaning_robot_actuator.daily_routine()

        # Turn off all sockets except for the kitchen ones
        for room in home:
            for actuator in room.actuators:
                if actuator.actuator_type == "SmartSocket" and room.name != "Kitchen":
                    actuator.turn_off()

    elif plan_name == "Movie":
        # Turn off all lights except for the living room
        for room in home:
            for actuator in room.actuators:
                if actuator.actuator_type == "Light" and room.name != "LivingRoom":
                    actuator.turn_off()

        # Set the light in living room to medium level
        living_room_light_actuator = [actuator for actuator in get_room_actuators(home, "LivingRoom") if actuator.actuator_type == "Light"][0]
        living_room_light_actuator.set_brightness_level("medium")

        # Close the curtain
        living_room_curtain_actuator = [actuator for actuator in get_room_actuators(home, "LivingRoom") if actuator.actuator_type == "Curtain"][0]
        living_room_curtain_actuator.turn_on()

        # Turn on the TV
        living_room_tv_actuator = [actuator for actuator in get_room_actuators(home, "LivingRoom") if actuator.actuator_type == "SmartTV"][0]
        living_room_tv_actuator.turn_on()


if __name__ == '__main__':

    # Get the home plan
    home = home_plan()

    # Execute morning routine and evening routine
    # morning_routine(home)
    # evening_routine(home)
    # #
    # # # Execute plans
    # home_plan_execution(home, "Home")
    home_plan_execution(home, "Away")
    # home_plan_execution(home, "Movie")

# testing_prompts:
# 1.	I would like to have morning routine at 7 am and evening routine at 11 pm every day.
# Additionally, I also want to set plans for Home, Away and Movie times.
# Here are what I want for each of the plan or routine.
# 1)	For the morning routine:
# I want to get up at 7am and have a cup of coffee. I also want to listen to the daily news.
#  So, at 7am, please open the curtain, turn on the light if it is too dark, play daily news and make a cup of coffee for me.
# 2)	For the evening routine:
# I want to go to bed at 11pm. So, at 11 pm, please close the curtain, play bedtime music for me. Turn the light to medium level, then turn it off after half an hour.
# (if the prompt do not include turning off music player -> won't do that)
# 3)	For the Home plan:
# Please turn on the Livingroom light for me, close Living room curtain, and turn on all sockets.
# 4)	For the Away plan:
# Please turn off all lights at home, close all windows, lock the home door, and start the cleaning robot. Also, turn off all sockets except for the kitchen ones.
# 5)	For the Movie plan:
# Please turn off all lights except for the one or ones in the living room.
# And set the light in living room to medium level.
# Close the curtain and turn on the TV.