# Based on your provided functional description and the existing code files, we'll create a `function.py` file that will be located in the `functions` folder. This file will contain the main function which will create a home plan, get readings from sensors, and adjust actuators as needed based on the provided temperature, humidity, and light intensity values.
# 
# Here's the `functions/function.py` file:

import sys
sys.path.append('../home')  # Adding the home directory to the system path

from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW


def main():
    # Create the home plan
    home = home_plan()

    # Define the target values based on the functional description
    target_temperature = 23
    target_humidity = 23
    target_light_intensity = 35

    # Iterate through each room in the home
    for room in home:
        print(f"\nChecking room: {room.name}")

        # Get sensors and actuators for the room
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        # Iterate through each sensor in the room
        for sensor in sensors:
            sensor.turn_on()  # Ensure the sensor is on to get a reading
            reading = sensor.get_reading()

            if reading is None:
                continue

            # Adjust actuators based on sensor type and reading
            for actuator in actuators:
                if isinstance(sensor, type(sensor).__bases__[0]):  # Check if sensor is a subclass of Sensor
                    if sensor.sensor_type == "IndoorTemperature":
                        if isinstance(actuator, type(actuator).__bases__[0]):  # Check if actuator is a subclass of Actuator
                            if reading < TEMP_LOW:
                                if hasattr(actuator, 'adjust_temperature'):
                                    actuator.set_target_temperature(target_temperature)
                                    actuator.adjust_temperature(reading)
                            elif reading > TEMP_HIGH:
                                if hasattr(actuator, 'adjust_temperature'):
                                    actuator.set_target_temperature(target_temperature)
                                    actuator.adjust_temperature(reading)

                    elif sensor.sensor_type == "Humidity":
                        if isinstance(actuator, type(actuator).__bases__[0]):  # Check if actuator is a subclass of Actuator
                            if reading < HUMIDITY_LOW:
                                if hasattr(actuator, 'increase_humidity'):
                                    actuator.turn_on()
                                    actuator.increase_humidity()
                            elif reading > HUMIDITY_HIGH:
                                if hasattr(actuator, 'decrease_humidity'):
                                    actuator.turn_on()
                                    actuator.decrease_humidity()

                    elif sensor.sensor_type == "LightIntensive":
                        if isinstance(actuator, type(actuator).__bases__[0]):  # Check if actuator is a subclass of Actuator
                            if reading < LIGHT_INTENSITY_LOW:
                                if hasattr(actuator, 'turn_on'):
                                    actuator.turn_on()
                            elif reading > LIGHT_INTENSITY_HIGH:
                                if hasattr(actuator, 'turn_off'):
                                    actuator.turn_off()

        print(f"Finished checking room: {room.name}")

if __name__ == "__main__":
    main()