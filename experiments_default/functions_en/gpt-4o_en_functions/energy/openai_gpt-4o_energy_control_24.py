# Here's the `function.py` file that implements the energy-saving mode as described. This script will leverage the existing classes to create a smart home environment that adjusts windows and curtains based on temperature readings and light intensity.

# function.py

from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, LightIntensiveSensor
from home.actuator import Window, Curtain
from home.home_plan import home_plan, get_room_sensors, get_room_actuators

def energy_saving_mode(home):
    for room in home:
        indoor_temp_sensor = None
        outdoor_temp_sensor = None
        light_intensive_sensor = None
        
        # Find necessary sensors in the room
        for sensor in room.sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                indoor_temp_sensor = sensor
            elif isinstance(sensor, OutdoorTemperatureSensor):
                outdoor_temp_sensor = sensor
            elif isinstance(sensor, LightIntensiveSensor):
                light_intensive_sensor = sensor
        
        # Find necessary actuators in the room
        window = None
        curtain = None
        for actuator in room.actuators:
            if isinstance(actuator, Window):
                window = actuator
            elif isinstance(actuator, Curtain):
                curtain = actuator
        
        # Perform the cooling logic
        if indoor_temp_sensor and outdoor_temp_sensor and window:
            indoor_temp_sensor.turn_on()
            outdoor_temp_sensor.turn_on()
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()
            if indoor_temp > outdoor_temp:
                window.turn_on()  # Open window
            else:
                window.turn_off()  # Close window
        
        if indoor_temp_sensor and light_intensive_sensor and curtain:
            indoor_temp_sensor.turn_on()
            light_intensive_sensor.turn_on()
            indoor_temp = indoor_temp_sensor.get_reading()
            light_intensity = light_intensive_sensor.get_reading()
            if indoor_temp < outdoor_temp and light_intensity > 900:  # Assuming 900 is the threshold for strong sunlight
                curtain.turn_on()  # Draw curtain
            else:
                curtain.turn_off()  # Open curtain

def main():
    home = home_plan()
    energy_saving_mode(home)

if __name__ == "__main__":
    main()