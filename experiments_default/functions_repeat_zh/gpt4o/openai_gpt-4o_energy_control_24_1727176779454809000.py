# Given the functional description and the provided source code, here's the `function.py` file that implements the described energy-saving mode:

# function.py
import time
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, LightIntensiveSensor
from home.actuator import Window, Curtain
from home.home_plan import home_plan, get_room_sensors, get_room_actuators

def energy_saving_mode(home):
    for room in home:
        room_name = room.name
        # Get sensors and actuators
        sensors = get_room_sensors(home, room_name)
        actuators = get_room_actuators(home, room_name)

        indoor_temp_sensor = None
        outdoor_temp_sensor = None
        light_sensor = None
        window = None
        curtain = None

        # Identify the relevant sensors and actuators
        for sensor in sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                indoor_temp_sensor = sensor
            elif isinstance(sensor, OutdoorTemperatureSensor):
                outdoor_temp_sensor = sensor
            elif isinstance(sensor, LightIntensiveSensor):
                light_sensor = sensor

        for actuator in actuators:
            if isinstance(actuator, Window):
                window = actuator
            elif isinstance(actuator, Curtain):
                curtain = actuator

        if indoor_temp_sensor and outdoor_temp_sensor and window:
            # Check temperature conditions to control the window
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()

            if outdoor_temp < indoor_temp:
                window.turn_on()  # Open the window
            else:
                window.turn_off()  # Close the window

        if indoor_temp_sensor and light_sensor and curtain:
            # Check light intensity and indoor temperature to control the curtain
            indoor_temp = indoor_temp_sensor.get_reading()
            light_intensity = light_sensor.get_reading()

            if indoor_temp > outdoor_temp and light_intensity >= 900:
                curtain.turn_on()  # Close the curtain
            else:
                curtain.turn_off()  # Open the curtain

def main():
    home = home_plan()
    energy_saving_mode(home)

if __name__ == "__main__":
    main()