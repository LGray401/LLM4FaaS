# Based on the functional description and the provided source code files, the `function.py` will be created to implement the energy-saving modes for temperature control. The main function will be responsible for utilizing the sensors and actuators to make decisions based on the given logic.
# 
# Here's the `function.py` file:

# function.py
import time
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, LightIntensiveSensor
from home.actuator import Window, Curtain
from home.home_plan import home_plan, get_room_sensors, get_room_actuators

def energy_saving_mode(home):
    for room in home:
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)
        
        indoor_temp_sensor = next((s for s in sensors if isinstance(s, IndoorTemperatureSensor)), None)
        outdoor_temp_sensor = next((s for s in sensors if isinstance(s, OutdoorTemperatureSensor)), None)
        light_intensive_sensor = next((s for s in sensors if isinstance(s, LightIntensiveSensor)), None)
        
        window = next((a for a in actuators if isinstance(a, Window)), None)
        curtain = next((a for a in actuators if isinstance(a, Curtain)), None)
        
        if indoor_temp_sensor and outdoor_temp_sensor and window:
            indoor_temp_sensor.turn_on()
            outdoor_temp_sensor.turn_on()
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()
            
            # Cooling mode 1: Open window if outdoor temperature is lower than indoor temperature
            if indoor_temp > outdoor_temp:
                window.turn_on()
            else:
                window.turn_off()
            
            indoor_temp_sensor.turn_off()
            outdoor_temp_sensor.turn_off()
        
        if indoor_temp_sensor and outdoor_temp_sensor and light_intensive_sensor and curtain:
            indoor_temp_sensor.turn_on()
            outdoor_temp_sensor.turn_on()
            light_intensive_sensor.turn_on()
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()
            light_intensity = light_intensive_sensor.get_reading()
            
            # Cooling mode 2: Close curtain if indoor temperature is higher than outdoor temperature and light intensity is high
            if indoor_temp < outdoor_temp and light_intensity > 900:
                curtain.turn_on()
            else:
                curtain.turn_off()
            
            indoor_temp_sensor.turn_off()
            outdoor_temp_sensor.turn_off()
            light_intensive_sensor.turn_off()

def main():
    home = home_plan()
    while True:
        energy_saving_mode(home)
        time.sleep(60) # check every 60 seconds

if __name__ == "__main__":
    main()