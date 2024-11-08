# Based on your functional description and the provided source code files, I will create a `function.py` file that includes a main function to demonstrate how the smart home system components can be utilized. The main function will create a home plan, activate some sensors and actuators, and display their interactions.
# 
# Here is the content for the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, OutdoorTemperatureSensor
from home.actuator import Light, Heater, AC, CoffeeMachine, NotificationSender

def main():
    # Create the home plan
    home = home_plan()

    # Print the home plan
    print_home_plan(home)

    # Example: Get a specific room and its sensors/actuators
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Get sensors and actuators in the living room
        sensors = get_room_sensors(home, "LivingRoom")
        actuators = get_room_actuators(home, "LivingRoom")

        # Turn on a light in the living room
        for actuator in actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("high")

        # Turn on the heater
        for actuator in actuators:
            if isinstance(actuator, Heater):
                actuator.set_target_temperature(22)
                actuator.turn_on()

        # Get readings from sensors
        for sensor in sensors:
            sensor.turn_on()
            sensor.get_reading()

        # Send a notification
        notification_sender = next((a for a in actuators if isinstance(a, NotificationSender)), None)
        if notification_sender:
            notification_sender.turn_on()
            notification_sender.notification_sender("Living room is ready for use!")

    # Example interaction with an outdoor temperature sensor
    outdoor_sensor = OutdoorTemperatureSensor("Backyard")
    outdoor_sensor.turn_on()
    outdoor_sensor.get_reading()

    # Example: Coffee Machine usage
    coffee_machine = next((a for a in actuators if isinstance(a, CoffeeMachine)), None)
    if coffee_machine:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")

if __name__ == "__main__":
    main()