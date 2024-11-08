# # function.py
# Based on your description, we need to create a function that implements the energy-saving mode (节能模式) in your smart home project. The function should check the indoor and outdoor temperatures and control the windows and curtains accordingly. Below is the 'function.py' file which should be placed in the 'functions' folder.

from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, LightIntensiveSensor
from home.actuator import Window, Curtain
from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, LIGHT_INTENSITY_HIGH

def energy_saving_mode(home):
    for room in home:
        indoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
        outdoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, OutdoorTemperatureSensor)]
        light_sensors = [sensor for sensor in room.sensors if isinstance(sensor, LightIntensiveSensor)]
        windows = [actuator for actuator in room.actuators if isinstance(actuator, Window)]
        curtains = [actuator for actuator in room.actuators if isinstance(actuator, Curtain)]

        if not indoor_temp_sensors or not outdoor_temp_sensors:
            continue

        indoor_temp = indoor_temp_sensors[0].get_reading()
        outdoor_temp = outdoor_temp_sensors[0].get_reading()
        light_intensity = light_sensors[0].get_reading() if light_sensors else LIGHT_INTENSITY_HIGH + 1  # Default to high light intensity if no sensor present

        if indoor_temp is None or outdoor_temp is None:
            continue

        if outdoor_temp < indoor_temp:
            for window in windows:
                window.turn_on()  # Open the window
            for curtain in curtains:
                curtain.turn_off()  # Close the curtain
        elif indoor_temp < outdoor_temp and light_intensity > LIGHT_INTENSITY_HIGH:
            for window in windows:
                window.turn_off()  # Close the window
            for curtain in curtains:
                curtain.turn_on()  # Open the curtain

def main():
    home = home_plan()
    energy_saving_mode(home)

if __name__ == "__main__":
    main()