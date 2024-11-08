# Sure! Based on the functional descriptions and the provided code files, I will create a `function.py` file within the `functions` folder. I will assume that the main function will initialize the home plan and demonstrate some of the functionalities of the sensors and actuators. 
# 
# Here's the `function.py` content:

# functions/function.py

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH

def main():
    # Initialize home plan
    home = home_plan()

    # Print the entire home plan
    print_home_plan(home)

    # Example Functionality Demonstrations:

    # Get and print the status of all sensors and actuators in the LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room:
        print("\nLivingRoom Sensors:")
        for sensor in get_room_sensors(home, "LivingRoom"):
            sensor.get_status()

        print("\nLivingRoom Actuators:")
        for actuator in get_room_actuators(home, "LivingRoom"):
            actuator.get_status()

    # Turn on all sensors in the Bedroom and get their readings
    bedroom = get_room(home, "Bedroom")
    if bedroom:
        print("\nTurning on Bedroom Sensors and getting readings:")
        for sensor in get_room_sensors(home, "Bedroom"):
            sensor.turn_on()
            sensor.get_reading()

    # Adjust the temperature in the Kitchen using Heater and AC
    kitchen = get_room(home, "Kitchen")
    if kitchen:
        print("\nAdjusting Kitchen temperature:")
        temperature_sensors = [sensor for sensor in get_room_sensors(home, "Kitchen") if sensor.sensor_type == "IndoorTemperature"]
        heaters = [actuator for actuator in get_room_actuators(home, "Kitchen") if actuator.actuator_type == "Heater"]
        ac_units = [actuator for actuator in get_room_actuators(home, "Kitchen") if actuator.actuator_type == "AC"]

        if temperature_sensors:
            temperature_sensors[0].turn_on()
            current_temp = temperature_sensors[0].get_reading()

            if heaters:
                heaters[0].set_target_temperature(TEMP_LOW + (TEMP_HIGH - TEMP_LOW) / 2)
                heaters[0].adjust_temperature(current_temp)

            if ac_units:
                ac_units[0].set_target_temperature(TEMP_HIGH - (TEMP_HIGH - TEMP_LOW) / 2)
                ac_units[0].adjust_temperature(current_temp)

    # Simulate a daily routine of the CleaningRobot in the LivingRoom
    if living_room:
        print("\nSimulating CleaningRobot's daily routine in the LivingRoom:")
        cleaning_robots = [actuator for actuator in get_room_actuators(home, "LivingRoom") if actuator.actuator_type == "CleaningRobot"]
        if cleaning_robots:
            cleaning_robots[0].turn_on()
            cleaning_robots[0].daily_routine()

if __name__ == "__main__":
    main()