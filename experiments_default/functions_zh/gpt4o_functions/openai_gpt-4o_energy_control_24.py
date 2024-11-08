# Based on the functional description you provided, the `function.py` file will be responsible for implementing the energy-saving modes. Specifically:
# 
# 1. If the outdoor temperature is lower than the indoor temperature, open the window.
# 2. If the indoor temperature is lower than the outdoor temperature and the sunlight is intense, close the curtain.
# 
# Here's the Python code to implement this logic in the `function.py` file:

from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, LightIntensiveSensor
from home.actuator import Window, Curtain
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import LIGHT_INTENSITY_HIGH

def main():
    # Initialize the home plan
    home = home_plan()

    # Iterate over all rooms
    for room in home:
        # Get all sensors and actuators for the current room
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        indoor_temp_sensor = None
        outdoor_temp_sensor = None
        light_intensity_sensor = None

        window = None
        curtain = None

        # Identify sensors and actuators in the room
        for sensor in sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                indoor_temp_sensor = sensor
            elif isinstance(sensor, OutdoorTemperatureSensor):
                outdoor_temp_sensor = sensor
            elif isinstance(sensor, LightIntensiveSensor):
                light_intensity_sensor = sensor

        for actuator in actuators:
            if isinstance(actuator, Window):
                window = actuator
            elif isinstance(actuator, Curtain):
                curtain = actuator

        # Ensure sensors and actuators are turned on
        if indoor_temp_sensor: indoor_temp_sensor.turn_on()
        if outdoor_temp_sensor: outdoor_temp_sensor.turn_on()
        if light_intensity_sensor: light_intensity_sensor.turn_on()

        if window: window.turn_on()
        if curtain: curtain.turn_on()

        # Get sensor readings
        indoor_temp = indoor_temp_sensor.get_reading() if indoor_temp_sensor else None
        outdoor_temp = outdoor_temp_sensor.get_reading() if outdoor_temp_sensor else None
        light_intensity = light_intensity_sensor.get_reading() if light_intensity_sensor else None

        # Apply energy-saving mode
        if outdoor_temp is not None and indoor_temp is not None:
            if outdoor_temp < indoor_temp and window:
                print(f"Opening the window in {room.name} to save energy.")
                window.turn_on()
            elif indoor_temp < outdoor_temp and light_intensity is not None and light_intensity > LIGHT_INTENSITY_HIGH and curtain:
                print(f"Closing the curtain in {room.name} to save energy.")
                curtain.turn_on()

if __name__ == "__main__":
    main()