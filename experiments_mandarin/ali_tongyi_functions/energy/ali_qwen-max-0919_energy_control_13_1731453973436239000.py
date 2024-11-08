# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to control the smart home system. This function will handle the logic for turning off lights when not needed, closing sockets, managing the heating and cooling, and controlling the air conditioning based on the indoor and outdoor temperatures, as well as the presence of people in the room.
# 
# Here is the `function.py` file:

# functions/function.py

from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, LightIntensiveSensor
from home.actuator import Light, AC, Heater, Window, SmartSocket
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, TEMP_CHANGE_DURATION_WINDOW
import time

def main():
    # Initialize the home plan
    home = home_plan()

    while True:
        for room in home:
            # Get sensors and actuators for the current room
            sensors = get_room_sensors(home, room.name)
            actuators = get_room_actuators(home, room.name)

            # Check if the room is occupied (for simplicity, assume it's always occupied)
            is_occupied = True

            # Get sensor readings
            indoor_temp_sensor = next((s for s in sensors if isinstance(s, IndoorTemperatureSensor)), None)
            outdoor_temp_sensor = next((s for s in sensors if isinstance(s, OutdoorTemperatureSensor)), None)
            light_intensive_sensor = next((s for s in sensors if isinstance(s, LightIntensiveSensor)), None)

            if indoor_temp_sensor:
                indoor_temp_sensor.turn_on()
                indoor_temperature = indoor_temp_sensor.get_reading()
                indoor_temp_sensor.turn_off()
            else:
                indoor_temperature = None

            if outdoor_temp_sensor:
                outdoor_temp_sensor.turn_on()
                outdoor_temperature = outdoor_temp_sensor.get_reading()
                outdoor_temp_sensor.turn_off()
            else:
                outdoor_temperature = None

            if light_intensive_sensor:
                light_intensive_sensor.turn_on()
                light_intensity = light_intensive_sensor.get_reading()
                light_intensive_sensor.turn_off()
            else:
                light_intensity = None

            # Control lights
            for actuator in actuators:
                if isinstance(actuator, Light):
                    if light_intensity and light_intensity > LIGHT_INTENSITY_HIGH:
                        actuator.turn_off()
                    else:
                        actuator.turn_on()

            # Control sockets
            for actuator in actuators:
                if isinstance(actuator, SmartSocket):
                    if not is_occupied:
                        actuator.turn_off()
                    else:
                        actuator.turn_on()

            # Control heating and cooling
            heater = next((a for a in actuators if isinstance(a, Heater)), None)
            ac = next((a for a in actuators if isinstance(a, AC)), None)
            window = next((a for a in actuators if isinstance(a, Window)), None)

            if heater and ac:
                if is_occupied:
                    if indoor_temperature and indoor_temperature < TEMP_LOW:
                        heater.set_target_temperature(TEMP_HIGH)
                        heater.adjust_temperature(indoor_temperature)
                    elif indoor_temperature and indoor_temperature > TEMP_HIGH:
                        ac.set_target_temperature(TEMP_LOW)
                        ac.adjust_temperature(indoor_temperature)
                    else:
                        heater.turn_off()
                        ac.turn_off()
                else:
                    heater.turn_off()
                    ac.turn_off()

            # Control windows for natural ventilation
            if window and outdoor_temperature and indoor_temperature:
                if abs(outdoor_temperature - indoor_temperature) < 5 and outdoor_temperature < TEMP_HIGH:
                    window.turn_on()
                    time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                    if ac:
                        ac.turn_off()
                else:
                    window.turn_off()

        # Sleep for a while before the next iteration
        time.sleep(60)

if __name__ == "__main__":
    main()