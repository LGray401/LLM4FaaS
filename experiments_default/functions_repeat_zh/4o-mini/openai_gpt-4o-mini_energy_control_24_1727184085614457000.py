# Based on the functional description you provided for your smart home project, I will create a `function.py` file that implements the energy-saving modes that you specified. The code will check the indoor and outdoor temperatures and take appropriate actions (open window or close curtains) based on the conditions.
# 
# Here is the content for the `function.py` file:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import Window, Curtain

def check_energy_saving_mode(home):
    for room in home:
        indoor_temp_sensor = next((s for s in room.sensors if isinstance(s, IndoorTemperatureSensor)), None)
        outdoor_temp_sensor = next((s for s in room.sensors if isinstance(s, OutdoorTemperatureSensor)), None)
        window = next((a for a in room.actuators if isinstance(a, Window)), None)
        curtain = next((a for a in room.actuators if isinstance(a, Curtain)), None)

        if indoor_temp_sensor and outdoor_temp_sensor and window and curtain:
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()

            if indoor_temp is not None and outdoor_temp is not None:
                # Energy-saving mode: Open window if outdoor temperature is lower than indoor temperature
                if outdoor_temp < indoor_temp:
                    window.turn_on()
                else:
                    window.turn_off()

                # Energy-saving mode: Close curtains if indoor temperature is lower than outdoor temperature and sunlight is strong
                if indoor_temp < outdoor_temp and outdoor_temp > TEMP_HIGH:
                    curtain.turn_on()
                else:
                    curtain.turn_off()

def main():
    # Initialize home and check energy-saving modes
    home = home_plan()
    check_energy_saving_mode(home)

if __name__ == "__main__":
    main()