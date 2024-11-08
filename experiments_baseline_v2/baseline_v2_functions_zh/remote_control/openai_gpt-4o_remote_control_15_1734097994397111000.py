# To create a smart home application based on the provided source code, we can develop a main script that utilizes the existing components from the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files. This script will initialize a home environment, interact with sensors, and control actuators based on simulated sensor readings.
# 
# Below is an example of a main script that demonstrates how you can use the provided classes to create a simple smart home application:
# 
# ```python
# main.py
import time
from home.home_plan import home_plan, print_home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW

def main():
    # Initialize the home with rooms, sensors, and actuators
    home = home_plan()
    print_home_plan(home)

    # Simulate a control loop for the smart home
    for _ in range(3):  # Run the loop a few times
        print("\n--- Smart Home Control Loop ---")

        # Iterate over each room
        for room in home:
            print(f"\nChecking {room.name}...")

            # Get sensors and actuators for the room
            sensors = get_room_sensors(home, room.name)
            actuators = get_room_actuators(home, room.name)

            # Turn on all sensors to get readings
            for sensor in sensors:
                sensor.turn_on()
                reading = sensor.get_reading()

                # Perform actions based on sensor type and readings
                if sensor.sensor_type == "IndoorTemperature":
                    for actuator in actuators:
                        if isinstance(actuator, (Heater, AC)):
                            actuator.turn_on()
                            if reading < TEMP_LOW:
                                if isinstance(actuator, Heater):
                                    actuator.set_target_temperature(TEMP_HIGH)
                            elif reading > TEMP_HIGH:
                                if isinstance(actuator, AC):
                                    actuator.set_target_temperature(TEMP_LOW)
                
                elif sensor.sensor_type == "Humidity":
                    for actuator in actuators:
                        if isinstance(actuator, Humidifier):
                            actuator.turn_on()
                            if reading < HUMIDITY_LOW:
                                actuator.increase_humidity()
                            elif reading > HUMIDITY_HIGH:
                                actuator.decrease_humidity()

                elif sensor.sensor_type == "LightIntensive":
                    for actuator in actuators:
                        if isinstance(actuator, Light):
                            actuator.turn_on()
                            if reading < LIGHT_INTENSITY_LOW:
                                actuator.set_brightness_level("high")
                            elif reading > LIGHT_INTENSITY_HIGH:
                                actuator.set_brightness_level("low")

            # Turn off all sensors after getting readings
            for sensor in sensors:
                sensor.turn_off()

        # Pause before the next loop iteration
        time.sleep(5)

if __name__ == "__main__":
    main()
# ```
# 
# ### Running the Application
# 
# To run this script in a Linux terminal, you can execute the following command:
# 
# ```bash
# python3 main.py
# ```
# 
# This command assumes that you have saved the script as `main.py` and that it is located in the same directory as the `home` folder containing the provided source files. Ensure your Python environment is set up correctly and that you have the necessary permissions to execute the script.