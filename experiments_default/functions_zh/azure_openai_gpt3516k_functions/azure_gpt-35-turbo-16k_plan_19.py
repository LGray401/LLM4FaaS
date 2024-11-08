# Here is the 'function.py' file based on your functional description and the given source code:

from home.sensor import IndoorTemperatureSensor, LightIntensiveSensor, CoffeeMachine, Window, Door
from home.actuator import NotificationSender, Curtain
from home.home_plan import get_room, get_room_sensors, get_room_actuators

def morning_plan(home):
    # Get the required sensors and actuators for the morning plan
    living_room = get_room(home, "LivingRoom")
    indoor_temp_sensor = get_room_sensors(home, "LivingRoom")[0]
    light_sensor = get_room_sensors(home, "LivingRoom")[1]
    coffee_machine = get_room_actuators(home, "LivingRoom")[2]
    curtain = get_room_actuators(home, "LivingRoom")[5]

    # Check and turn on the indoor temperature sensor and light sensor
    if indoor_temp_sensor.get_status() == "off":
        indoor_temp_sensor.turn_on()
    if light_sensor.get_status() == "off":
        light_sensor.turn_on()

    # Check the temperature and adjust actuator accordingly
    current_temp = indoor_temp_sensor.get_reading()
    if current_temp < 20:
        heater = get_room_actuators(home, "LivingRoom")[12]
        heater.set_target_temperature(25)
        heater.adjust_temperature(current_temp)

    # Check the light intensity and set curtain position accordingly
    light_intensity = light_sensor.get_reading()
    if light_intensity > 800:
        curtain.turn_on()
    else:
        curtain.turn_off()

    # Check and turn on the coffee machine
    if coffee_machine.get_status() == "off":
        coffee_machine.turn_on()
    coffee_type = "coffee"
    coffee_machine.make_coffee(coffee_type)

    # Send notification
    notification_sender = get_room_actuators(home, "LivingRoom")[10]
    notification_sender.notification_sender("Good morning! Your coffee is ready.")


def leave_home_plan(home):
    # Get the required sensors and actuators for the leave home plan
    front_door = get_room_actuators(home, "LivingRoom")[7]

    # Check and lock the door
    front_door.lock()

    # Send notification
    notification_sender = get_room_actuators(home, "LivingRoom")[10]
    notification_sender.notification_sender("The front door has been locked.")


def movie_plan(home):
    # Get the required sensors and actuators for the movie plan
    living_room = get_room(home, "LivingRoom")
    light_sensor = get_room_sensors(home, "LivingRoom")[1]
    curtain = get_room_actuators(home, "LivingRoom")[5]

    # Check and turn off the light sensor
    if light_sensor.get_status() == "on":
        light_sensor.turn_off()

    # Close the curtain
    curtain.turn_on()

    # Send notification
    notification_sender = get_room_actuators(home, "LivingRoom")[10]
    notification_sender.notification_sender("Enjoy your movie!")

    # Additional actions for the movie plan can be added here


def main():
    home = home_plan()
    # Perform the morning plan
    morning_plan(home)

    # Perform the leave home plan
    leave_home_plan(home)

    # Perform the movie plan
    movie_plan(home)


if __name__ == "__main__":
    main()