from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION


def main():
    home = home_plan()
    print_home_plan(home)

    # Example usage of functions:

    # Get a specific room
    living_room = get_room(home, "LivingRoom")

    # Get sensors in a room
    living_room_sensors = get_room_sensors(home, "LivingRoom")

    # Get actuators in a room
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Get all sensors of a specific type
    all_temperature_sensors = get_all_sensors(home, "IndoorTemperature")

    # Get all actuators of a specific type
    all_lights = get_all_actuators(home, "Light")

    # Example interaction with sensors and actuators:
    if living_room:
        # Turn on the lights in the living room
        for light in living_room_actuators:
            if light.actuator_type == "Light":
                light.turn_on()
                light.set_brightness_level("high")

        # Get temperature reading in the living room
        for sensor in living_room_sensors:
            if sensor.sensor_type == "IndoorTemperature":
                temperature_reading = sensor.get_reading()

        # Adjust the AC based on the temperature reading
        for ac in living_room_actuators:
            if ac.actuator_type == "AC":
                ac.adjust_temperature(temperature_reading)

    # Example of a rule-based automation:
    # Check if the outdoor temperature is below a certain threshold and turn on the heater
    for sensor in all_temperature_sensors:
        if sensor.sensor_type == "OutdoorTemperature":
            outdoor_temperature = sensor.get_reading()

    for heater in get_all_actuators(home, "Heater"):
        if outdoor_temperature < TEMP_LOW:
            heater.turn_on()
            print(f"Turning on heater in {heater.room_name}")
        elif outdoor_temperature > TEMP_HIGH:
            heater.turn_off()
            print(f"Turning off heater in {heater.room_name}")

    # Example of a daily routine:
    # Start the cleaning robot's daily cleaning routine
    for cleaning_robot in get_all_actuators(home, "CleaningRobot"):
        cleaning_robot.turn_on()
        cleaning_robot.daily_routine()

    # Example of a timed event:
    # Simulate waiting for a temperature change
    time.sleep(TEMP_CHANGE_DURATION_WINDOW)

    # Example of a notification:
    # Send a notification if the humidity in a room exceeds a certain threshold
    for sensor in get_all_sensors(home, "Humidity"):
        if sensor.get_reading() > HUMIDITY_HIGH:
            notification_sender = get_room_actuators(home, sensor.room_name)
            notification_sender.notification_sender(
                f"Humidity in {sensor.room_name} is high, consider opening a window.")


if __name__ == "__main__":
    main()
