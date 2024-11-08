# Based on the functional description and the provided source code, I've created the `function.py` file for your smart home project. This file implements the energy-saving modes you've described, which involve controlling windows and curtains based on indoor and outdoor temperatures.
# 
# Here's the content for `function.py`:

from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import Window, Curtain
from home.home_plan import home_plan


def check_energy_saving_mode(home):
    # Get all rooms in the home
    for room in home:
        # Find relevant sensors and actuators
        indoor_temp_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        outdoor_temp_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, OutdoorTemperatureSensor)), None)
        window = next((actuator for actuator in room.actuators if isinstance(actuator, Window)), None)
        curtain = next((actuator for actuator in room.actuators if isinstance(actuator, Curtain)), None)

        if indoor_temp_sensor and outdoor_temp_sensor and window and curtain:
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()

            if indoor_temp is not None and outdoor_temp is not None:
                # Check for cooling mode 1
                if outdoor_temp < indoor_temp:
                    window.turn_on()  # Open window
                    print(f"Opened window in {room.name} to cool down.")
                else:
                    window.turn_off()  # Close window
                    print(f"Closed window in {room.name}.")

                # Check for cooling mode 2
                if indoor_temp < outdoor_temp and outdoor_temp > 30:  # Assuming 30 as a threshold for strong sunlight
                    curtain.turn_on()  # Close curtain
                    print(f"Closed curtain in {room.name} to block sunlight.")
                else:
                    curtain.turn_off()  # Open curtain
                    print(f"Opened curtain in {room.name}.")

def main():
    home = home_plan()  # Initialize home plan
    check_energy_saving_mode(home)  # Execute energy-saving mode check

if __name__ == "__main__":
    main()