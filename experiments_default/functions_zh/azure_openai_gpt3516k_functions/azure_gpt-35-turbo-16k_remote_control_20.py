# Sure, I will create the 'function.py' file for your smart home project based on the given functional description and the provided source code. Here is the content of the 'function.py' file:

from home.home_plan import home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, LightIntensiveSensor
from home.actuator import AC, TemperatureController, CleaningRobot
from home.config import TEMP_LOW, TEMP_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION

def main():
    # Initialize the smart home plan
    home = home_plan()

    # Get the living room sensors and actuators
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Get all temperature and light intensity sensors
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")

    # Get all ACs and cleaning robots
    acs = get_all_actuators(home, "AC")
    cleaning_robots = get_all_actuators(home, "CleaningRobot")

    # Turn on the ACs
    for ac in acs:
        ac.turn_on()

    # Perform pre-home arrival actions
    if temperature_sensors and light_intensity_sensors:
        # Check if it's the right time to turn on the ACs
        for temperature_sensor in temperature_sensors:
            temperature = temperature_sensor.get_reading()
            if temperature and TEMP_LOW <= temperature <= TEMP_HIGH:
                temperature_controller = TemperatureController(temperature_sensor.room_name, acs)
                temperature_controller.turn_on_ac()

        # Check if it's the right time to start the cleaning robots
        for light_intensity_sensor in light_intensity_sensors:
            light_intensity = light_intensity_sensor.get_reading()
            if light_intensity and LIGHT_INTENSITY_LOW <= light_intensity <= LIGHT_INTENSITY_HIGH:
                cleaning_robot = CleaningRobot(light_intensity_sensor.room_name, cleaning_robots)
                cleaning_robot.start_daily_routine(DAILY_ROUTINE_DURATION)

    # Perform home departure actions
    for temperature_sensor in temperature_sensors:
        temperature_sensor.turn_off()

    # Print the current status of the living room sensors and actuators
    for sensor in living_room_sensors:
        sensor.get_status()
    for actuator in living_room_actuators:
        actuator.get_status()


if __name__ == "__main__":
    main()