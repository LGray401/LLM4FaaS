# Based on your functional description and the provided source code, I will create the `function.py` file that implements the energy-saving mode you described. This mode will include:
# 
# 1. **Cooling Mode 1**: If the outdoor temperature is lower than the indoor temperature, the window should be opened.
# 2. **Cooling Mode 2**: If the indoor temperature is lower than the outdoor temperature and sunlight is strong, the curtains should be drawn.
# 
# Here's how the `function.py` file will look:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, LIGHT_INTENSITY_LOW
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, LightIntensiveSensor
from home.actuator import Window, Curtain

def check_energy_saving_mode(home):
    for room in home:
        indoor_temp_sensor = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
        outdoor_temp_sensor = [sensor for sensor in room.sensors if isinstance(sensor, OutdoorTemperatureSensor)]
        light_sensor = [sensor for sensor in room.sensors if isinstance(sensor, LightIntensiveSensor)]

        # Ensure we have the necessary sensors
        if indoor_temp_sensor and outdoor_temp_sensor and light_sensor:
            indoor_temp = indoor_temp_sensor[0].get_reading()
            outdoor_temp = outdoor_temp_sensor[0].get_reading()
            light_intensity = light_sensor[0].get_reading()

            # Cooling Mode 1: Open window if outdoor temperature < indoor temperature
            if outdoor_temp is not None and indoor_temp is not None:
                if outdoor_temp < indoor_temp:
                    window = Window(room.name)
                    window.turn_on()  # Open the window
                    print(f"Opening window in {room.name} as outdoor temperature ({outdoor_temp}°C) is lower than indoor temperature ({indoor_temp}°C).")

            # Cooling Mode 2: Draw curtains if indoor temperature < outdoor temperature and light intensity is high
            if light_intensity is not None and indoor_temp is not None:
                if indoor_temp < outdoor_temp and light_intensity > LIGHT_INTENSITY_LOW:
                    curtain = Curtain(room.name)
                    curtain.turn_on()  # Draw the curtains
                    print(f"Drawing curtains in {room.name} as indoor temperature ({indoor_temp}°C) is lower than outdoor temperature ({outdoor_temp}°C) and light intensity is high ({light_intensity} lux).")

def main():
    home = home_plan()
    check_energy_saving_mode(home)

if __name__ == "__main__":
    main()