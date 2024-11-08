# Based on the functional description you provided, the `function.py` file will implement the energy-saving mode that activates specific actions based on the temperature readings from indoor and outdoor sensors. The actions include opening the window when the outdoor temperature is lower than the indoor temperature, and closing the curtains when the indoor temperature is lower than the outdoor temperature and sunlight is strong.
# 
# Here's how you can implement the `function.py` file:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH
from home.actuator import Window, Curtain
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor

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
                # Check for Cooling Mode 1: Open window if outdoor temperature is lower
                if outdoor_temp < indoor_temp:
                    print(f"Opening window in {room.name}. Outdoor temperature ({outdoor_temp}) is lower than indoor temperature ({indoor_temp}).")
                    window.turn_on()  # Open the window

                # Check for Cooling Mode 2: Close curtains if indoor temperature is lower and sunlight is strong
                if indoor_temp < outdoor_temp and outdoor_temp > TEMP_HIGH:
                    print(f"Closing curtains in {room.name}. Indoor temperature ({indoor_temp}) is lower than outdoor temperature ({outdoor_temp}) and sunlight is strong.")
                    curtain.turn_on()  # Close the curtains

def main():
    home = home_plan()
    energy_saving_mode(home)

if __name__ == "__main__":
    main()