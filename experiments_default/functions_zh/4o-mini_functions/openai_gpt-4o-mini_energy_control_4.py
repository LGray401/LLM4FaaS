# Based on your functional description, which translates to "Open the window to cool down," we will create a `function.py` file that utilizes the existing classes from your project. The main function will be responsible for opening the window when the indoor temperature is too high compared to the outdoor temperature.
# 
# Here's the implementation of `function.py`:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH
from home.actuator import Window
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor

def main():
    # Create the home layout
    home = home_plan()

    # Assuming we are interested in the Living Room for this functionality
    living_room = next((room for room in home if room.name == "LivingRoom"), None)

    if living_room:
        # Get the indoor temperature sensor and outdoor temperature sensor
        indoor_temp_sensor = next((sensor for sensor in living_room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        outdoor_temp_sensor = next((sensor for room in home for sensor in room.sensors if isinstance(sensor, OutdoorTemperatureSensor)), None)

        if indoor_temp_sensor and outdoor_temp_sensor:
            indoor_temp_sensor.turn_on()
            outdoor_temp_sensor.turn_on()

            # Get current temperature readings
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()

            # Check if indoor temperature exceeds the threshold
            if indoor_temp is not None and indoor_temp > TEMP_HIGH:
                # Find the window actuator in the living room
                window = next((actuator for actuator in living_room.actuators if isinstance(actuator, Window)), None)
                if window:
                    window.turn_on()  # Open the window
                    print("Window opened to cool down.")
                else:
                    print("No window actuator found in the living room.")
            else:
                print("Indoor temperature is within acceptable limits. No need to open the window.")
        else:
            print("Required temperature sensors are not found in the living room.")
    else:
        print("Living room not found in the home plan.")

if __name__ == "__main__":
    main()