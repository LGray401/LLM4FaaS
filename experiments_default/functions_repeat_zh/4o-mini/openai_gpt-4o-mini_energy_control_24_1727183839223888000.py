# Based on the provided functional description and the existing code structure, I'll create the `function.py` file in the `functions` folder. This file will contain a main function that implements the described energy-saving modes, specifically for adjusting the indoor environment based on temperature readings from the sensors.
# 
# Here's the `function.py` file:

# functions/function.py

from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import Window, Curtain
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH


def energy_saving_mode(home):
    for room in home:
        indoor_temp_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        outdoor_temp_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, OutdoorTemperatureSensor)), None)
        window = next((actor for actor in room.actuators if isinstance(actor, Window)), None)
        curtain = next((actor for actor in room.actuators if isinstance(actor, Curtain)), None)

        if indoor_temp_sensor and outdoor_temp_sensor and window and curtain:
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()

            if indoor_temp is not None and outdoor_temp is not None:
                # Cooling Mode 1: Open window if outdoor temperature is lower than indoor temperature
                if outdoor_temp < indoor_temp:
                    window.turn_on()  # Open window
                    print(f"Opened the window in {room.name} as outdoor temperature ({outdoor_temp}°C) is lower than indoor temperature ({indoor_temp}°C).")

                # Cooling Mode 2: Close window and pull curtains if indoor temperature is higher than outdoor temperature and sunlight is intense
                elif indoor_temp > outdoor_temp and outdoor_temp > TEMP_HIGH:
                    curtain.turn_on()  # Close curtains
                    print(f"Closed the curtains in {room.name} to reduce sunlight as outdoor temperature ({outdoor_temp}°C) is higher than indoor temperature ({indoor_temp}°C).")

                else:
                    window.turn_off()  # Ensure window is closed if not needed
                    curtain.turn_off()  # Ensure curtains are opened if not needed
                    print(f"Conditions are normal in {room.name}, no actions taken.")
            else:
                print(f"Could not retrieve temperature readings in {room.name}.")


def main():
    home = home_plan()
    energy_saving_mode(home)


if __name__ == "__main__":
    main()