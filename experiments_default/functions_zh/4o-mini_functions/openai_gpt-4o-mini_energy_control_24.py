# Based on the functional description and the provided source code, I will create a `function.py` file. This file will implement the energy-saving modes you described: opening the window when the outdoor temperature is lower than the indoor temperature and closing the curtains when the indoor temperature is lower than the outdoor temperature and sunlight is strong.
# 
# Here's the `function.py` file:

# functions/function.py

from home.home_plan import home_plan
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, LightIntensiveSensor
from home.actuator import Window, Curtain

def energy_saving_mode(home):
    for room in home:
        indoor_temp_sensor = None
        outdoor_temp_sensor = None
        light_sensor = None
        window = None
        curtain = None

        # Find the relevant sensors and actuators in the room
        for sensor in room.sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                indoor_temp_sensor = sensor
            elif isinstance(sensor, OutdoorTemperatureSensor):
                outdoor_temp_sensor = sensor
            elif isinstance(sensor, LightIntensiveSensor):
                light_sensor = sensor

        for actuator in room.actuators:
            if isinstance(actuator, Window):
                window = actuator
            elif isinstance(actuator, Curtain):
                curtain = actuator

        # Check conditions for energy-saving actions
        if indoor_temp_sensor and outdoor_temp_sensor and window:
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()

            if indoor_temp is not None and outdoor_temp is not None:
                if outdoor_temp < indoor_temp:
                    window.turn_on()  # Open the window
                else:
                    window.turn_off()  # Close the window if the condition is not met

        if indoor_temp_sensor and outdoor_temp_sensor and light_sensor and curtain:
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()
            light_intensity = light_sensor.get_reading()

            if indoor_temp is not None and outdoor_temp is not None and light_intensity is not None:
                if indoor_temp < outdoor_temp and light_intensity > 900:  # Strong sunlight condition
                    curtain.turn_on()  # Pull down the curtains
                else:
                    curtain.turn_off()  # Raise the curtains if the condition is not met

def main():
    home = home_plan()
    energy_saving_mode(home)

if __name__ == "__main__":
    main()