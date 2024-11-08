# Alright! Based on your functional description and the provided code files, I will create the `function.py` file that will be located in the `functions` folder. This file will contain the main function that will manage the indoor temperature, humidity, and light intensity according to the specified requirements.
# 
# Here's the `function.py`:

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Curtain, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, HUMIDITY_HIGH, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW

def main():
    # Initialize home
    home = home_plan()

    # Iterate through each room
    for room in home:
        print(f"Checking room: {room.name}")

        # Get sensors and actuators for the room
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        # Create dictionaries to easily access sensors and actuators by type
        sensor_dict = {sensor.sensor_type: sensor for sensor in sensors}
        actuator_dict = {actuator.actuator_type: actuator for actuator in actuators}

        # Temperature control
        if "IndoorTemperature" in sensor_dict:
            temp_sensor = sensor_dict["IndoorTemperature"]
            temp_sensor.turn_on()
            current_temp = temp_sensor.get_reading()
            if current_temp > TEMP_HIGH:
                if "AC" in actuator_dict:
                    ac = actuator_dict["AC"]
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(current_temp)
            elif current_temp < TEMP_HIGH:
                if "Heater" in actuator_dict:
                    heater = actuator_dict["Heater"]
                    heater.set_target_temperature(TEMP_HIGH)
                    heater.adjust_temperature(current_temp)

        # Humidity control
        if "Humidity" in sensor_dict:
            humidity_sensor = sensor_dict["Humidity"]
            humidity_sensor.turn_on()
            current_humidity = humidity_sensor.get_reading()
            if current_humidity > HUMIDITY_HIGH:
                if "Humidifier" in actuator_dict:
                    humidifier = actuator_dict["Humidifier"]
                    humidifier.decrease_humidity()

        # Light intensity control
        if "LightIntensive" in sensor_dict:
            light_sensor = sensor_dict["LightIntensive"]
            light_sensor.turn_on()
            current_light_intensity = light_sensor.get_reading()
            if current_light_intensity > LIGHT_INTENSITY_HIGH:
                if "Curtain" in actuator_dict:
                    curtain = actuator_dict["Curtain"]
                    curtain.turn_on()
            elif current_light_intensity < LIGHT_INTENSITY_LOW:
                if "Light" in actuator_dict:
                    light = actuator_dict["Light"]
                    light.turn_on()

if __name__ == "__main__":
    main()