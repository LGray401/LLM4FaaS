# Based on the functional description you provided, the `function.py` file will implement the energy-saving mode functionality. This involves two conditions where actions should be taken based on temperature readings from sensors. The actions include opening a window or adjusting curtains based on the temperature difference between the indoor and outdoor readings.
# 
# Here's the `function.py` file based on your specifications:

# functions/function.py
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import Window, Curtain
from home.home_plan import home_plan

def energy_saving_mode(home):
    for room in home:
        indoor_temp_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        outdoor_temp_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, OutdoorTemperatureSensor)), None)
        
        window = next((actuator for actuator in room.actuators if isinstance(actuator, Window)), None)
        curtain = next((actuator for actuator in room.actuators if isinstance(actuator, Curtain)), None)

        if indoor_temp_sensor and outdoor_temp_sensor:
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()

            if indoor_temp is not None and outdoor_temp is not None:
                # Cooling Mode 1: Open the window if outdoor temp is lower than indoor temp
                if outdoor_temp < indoor_temp:
                    if window:
                        window.turn_on()  # Open the window
                        print(f"Window in {room.name} opened to cool down.")
                
                # Cooling Mode 2: Close the window if indoor temp is greater than outdoor temp and sunlight is strong
                elif indoor_temp < outdoor_temp and curtain:
                    curtain.turn_on()  # Draw the curtain
                    print(f"Curtain in {room.name} drawn to block sunlight.")

def main():
    home = home_plan()
    energy_saving_mode(home)

if __name__ == "__main__":
    main()