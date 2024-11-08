# Based on the provided functional description and source code files, I will create a `function.py` file that includes a `main` function to interact with your smart home system. This function will demonstrate how to use the components defined in your `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`.
# 
# Here's the content of `function.py`:

# functions/function.py
from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Light, Heater, AC, CoffeeMachine, NotificationSender, CleaningRobot

def main():
    # Initialize home plan
    home = home_plan()
    
    # Print home plan
    print_home_plan(home)

    # Example of getting a specific room and its components
    room_name = "LivingRoom"
    living_room = get_room(home, room_name)
    
    if living_room:
        sensors = get_room_sensors(home, room_name)
        actuators = get_room_actuators(home, room_name)

        # Turn on all sensors in the Living Room
        for sensor in sensors:
            sensor.turn_on()
            sensor.get_reading()

        # Turn on all actuators in the Living Room
        for actuator in actuators:
            actuator.turn_on()

        # Example usage of specific actuators
        heater = next((a for a in actuators if a.actuator_type == "Heater"), None)
        if heater:
            heater.set_target_temperature(22)  # Set target temperature for the heater
            heater.adjust_temperature(20)  # Simulate current temperature as 20°C

        coffee_machine = next((a for a in actuators if isinstance(a, CoffeeMachine)), None)
        if coffee_machine:
            coffee_machine.turn_on()
            coffee_machine.make_coffee("Espresso")

        # Example of sending a notification
        notification_sender = next((a for a in actuators if isinstance(a, NotificationSender)), None)
        if notification_sender:
            notification_sender.turn_on()
            notification_sender.notification_sender("All systems are functioning normally.")

        # Example of the cleaning robot's daily routine
        cleaning_robot = next((a for a in actuators if isinstance(a, CleaningRobot)), None)
        if cleaning_robot:
            cleaning_robot.turn_on()
            cleaning_robot.daily_routine()

if __name__ == "__main__":
    main()