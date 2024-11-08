# Below is the `function.py` file for your smart home project, implementing the energy-saving mode functionality as described. This file contains the main function that orchestrates the behavior of the system based on the readings from the sensors and controls the actuators accordingly.
# 
# ### `function.py`

from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.actuator import Window, Curtain

def energy_saving_mode(home):
    for room in home:
        # Get sensors and actuators in the room
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)
        
        indoor_temp_sensor = next((s for s in sensors if s.sensor_type == "IndoorTemperature"), None)
        outdoor_temp_sensor = next((s for s in sensors if s.sensor_type == "OutdoorTemperature"), None)
        light_sensor = next((s for s in sensors if s.sensor_type == "LightIntensive"), None)
        
        window = next((a for a in actuators if isinstance(a, Window)), None)
        curtain = next((a for a in actuators if isinstance(a, Curtain)), None)

        if indoor_temp_sensor and outdoor_temp_sensor:
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()

            # Cooling 1: Open the window if outdoor temperature is lower than indoor temperature
            if outdoor_temp is not None and indoor_temp is not None and outdoor_temp < indoor_temp:
                if window:
                    window.turn_on()  # Open the window
                print(f"Opening window in {room.name} as outdoor temperature ({outdoor_temp}) is lower than indoor temperature ({indoor_temp}).")

            # Cooling 2: Draw the curtain if indoor temperature is lower than outdoor temperature and sunlight is strong
            if light_sensor:
                light_intensity = light_sensor.get_reading()
                if indoor_temp is not None and outdoor_temp is not None and indoor_temp < outdoor_temp and light_intensity is not None and light_intensity > LIGHT_INTENSITY_HIGH:
                    if curtain:
                        curtain.turn_on()  # Draw the curtain
                    print(f"Drawing curtain in {room.name} as indoor temperature ({indoor_temp}) is lower than outdoor temperature ({outdoor_temp}) and sunlight is strong (intensity: {light_intensity}).")

def main():
    home = home_plan()
    energy_saving_mode(home)

if __name__ == "__main__":
    main()