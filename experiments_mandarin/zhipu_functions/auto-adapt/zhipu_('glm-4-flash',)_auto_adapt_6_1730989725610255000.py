# Based on your provided functional description and the source code from the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files, I will create a `function.py` file with a `main` function that can be used to interact with the smart home system. The `main` function will demonstrate the functionality of the sensors and actuators by simulating some typical user interactions.
# 
# Here is the content for the `function.py` file:

# function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, CleaningRobot, SmartTV
from home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators

# Initialize the home plan
home = home_plan()

def main():
    # Get the Living Room sensors
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    print(f"Living Room Sensors: {[sensor.id for sensor in living_room_sensors]}")

    # Get all the Light Intensive Sensors
    all_light_sensors = get_all_sensors(home, "LightIntensive")
    print(f"All Light Intensive Sensors: {[sensor.id for sensor in all_light_sensors]}")

    # Get the actuators in the Living Room
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    print(f"Living Room Actuators: {[actor.id for actor in living_room_actuators]}")

    # Interact with the actuators
    if living_room_actuators:
        # Turn on the first light in the Living Room
        living_room_actuators[0].turn_on()

        # Adjust the brightness of the light
        if isinstance(living_room_actuators[0], Light):
            living_room_actuators[0].set_brightness_level("medium")

        # Turn off the light
        living_room_actuators[0].turn_off()

    # Send a notification
    notification_actor = home[0].actuators[0]  # Assuming the first actor is a NotificationSender
    if isinstance(notification_actor, NotificationSender):
        notification_actor.notification_sender("Good morning! The coffee is ready.")

    # Print the home plan
    print_home_plan(home)

if __name__ == "__main__":
    main()