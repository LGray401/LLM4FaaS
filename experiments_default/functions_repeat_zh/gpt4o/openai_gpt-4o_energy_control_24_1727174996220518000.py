# Sure, based on your functional description and the provided code, I'll create the `function.py` file. The main function will implement the described energy-saving mode functionalities.
# 
# Below is the content for `functions/function.py`:

import time
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, LightIntensiveSensor
from home.actuator import Window, Curtain
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_CHANGE_DURATION_WINDOW

def energy_saving_mode(home):
    # Iterate over all rooms
    for room in home:
        # Retrieve sensors and actuators for the room
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        indoor_temp_sensor = next((sensor for sensor in sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        outdoor_temp_sensor = next((sensor for sensor in sensors if isinstance(sensor, OutdoorTemperatureSensor)), None)
        light_intensive_sensor = next((sensor for sensor in sensors if isinstance(sensor, LightIntensiveSensor)), None)

        window = next((actuator for actuator in actuators if isinstance(actuator, Window)), None)
        curtain = next((actuator for actuator in actuators if isinstance(actuator, Curtain)), None)

        if indoor_temp_sensor and outdoor_temp_sensor and window:
            indoor_temp_sensor.turn_on()
            outdoor_temp_sensor.turn_on()
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()

            if indoor_temp is not None and outdoor_temp is not None:
                if outdoor_temp < indoor_temp:
                    print(f"室外温度 ({outdoor_temp}°C) 低于室内温度 ({indoor_temp}°C)，开窗。")
                    window.turn_on()
                    time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                    window.turn_off()
                elif indoor_temp < outdoor_temp and light_intensive_sensor and curtain:
                    light_intensive_sensor.turn_on()
                    light_intensity = light_intensive_sensor.get_reading()
                    if light_intensity is not None and light_intensity > 900:
                        print(f"室内温度 ({indoor_temp}°C) 低于室外温度 ({outdoor_temp}°C)，日照强烈 ({light_intensity} lux)，拉帘。")
                        curtain.turn_on()
                        time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                        curtain.turn_off()

def main():
    home = home_plan()
    energy_saving_mode(home)

if __name__ == "__main__":
    main()