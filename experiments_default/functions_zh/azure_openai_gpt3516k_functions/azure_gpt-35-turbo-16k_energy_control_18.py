# Here is the `function.py` file that you requested:

from home.home_plan import home_plan, print_home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def open_window(room_name):
    # Get the home plan
    home = home_plan()

    # Get the room's sensors and actuators
    sensors = get_room_sensors(home, room_name)
    actuators = get_room_actuators(home, room_name)

    if sensors is not None and actuators is not None:
        # Check if the temperature and humidity sensors are within the threshold
        for sensor in sensors:
            if sensor.sensor_type == "IndoorTemperature":
                temperature = sensor.get_reading()
                if temperature is None or temperature < TEMP_LOW or temperature > TEMP_HIGH:
                    print("The temperature is not within the safe range. Open the window is not recommended.")
                    return
            elif sensor.sensor_type == "Humidity":
                humidity = sensor.get_reading()
                if humidity is None or humidity < HUMIDITY_LOW or humidity > HUMIDITY_HIGH:
                    print("The humidity is not within the safe range. Open the window is not recommended.")
                    return
            elif sensor.sensor_type == "LightIntensive":
                light_intensity = sensor.get_reading()
                if light_intensity is None or light_intensity < LIGHT_INTENSITY_LOW or light_intensity > LIGHT_INTENSITY_HIGH:
                    print("The light intensity is not within the safe range. Open the window is not recommended.")
                    return

        # Trigger the window actuator to open
        for actuator in actuators:
            if actuator.actuator_type == "Window":
                actuator.turn_on()
                print("Window is now open.")
                return

    print("Cannot open the window.")

open_window("Living Room")