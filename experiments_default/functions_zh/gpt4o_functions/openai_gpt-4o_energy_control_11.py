# Based on your functional description, the `function.py` file should check the indoor temperature and open the window if the temperature exceeds 26 degrees Celsius. Here is the `function.py` that performs this function:

from home.sensor import IndoorTemperatureSensor
from home.actuator import Window
from home.home_plan import home_plan, get_room_actuators

def main():
    # Create the home plan
    home = home_plan()

    # Retrieve the sensors and actuators for the LivingRoom
    living_room_sensors = [sensor for sensor in home[0].sensors if isinstance(sensor, IndoorTemperatureSensor)]
    living_room_actuators = [actuator for actuator in home[0].actuators if isinstance(actuator, Window)]

    # Turn on all the sensors in the LivingRoom
    for sensor in living_room_sensors:
        sensor.turn_on()

    # Check the indoor temperature and open the window if it exceeds 26 degrees
    for sensor in living_room_sensors:
        reading = sensor.get_reading()
        if reading is not None and reading > 26:
            print(f"Temperature is {reading}°C, which is higher than 26°C. Opening the window.")
            for actuator in living_room_actuators:
                actuator.turn_on()
        else:
            print(f"Temperature is {reading}°C, which is not higher than 26°C. No action needed.")

if __name__ == "__main__":
    main()