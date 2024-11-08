# Sure! I have created the 'function.py' file that contains the main function based on your functional description. You can find the file in the 'functions' folder.
# 
# Here is the content of the 'function.py' file:

from home.home_plan import home_plan, get_room_actuators, get_all_actuators, get_all_sensors, get_room_sensors, print_home_plan
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.logger_config import logger
from home.actuator import Light, AC, Heater

def adjust_device_status(device_type, action, param=None, room_name=None):
    home = home_plan()

    if room_name is not None:
        room_actuators = get_room_actuators(home, room_name)
        if room_actuators is None:
            return

        for actuator in room_actuators:
            if actuator.actuator_type == device_type:
                if action == "turn_on":
                    actuator.turn_on()
                elif action == "turn_off":
                    actuator.turn_off()

                if param is not None:
                    if device_type == "Light":
                        actuator.set_brightness_level(param)
                    elif device_type == "AC" or device_type == "Heater":
                        actuator.set_target_temperature(param)

    else:
        all_actuators = get_all_actuators(home, device_type)
        if all_actuators is None:
            return

        for actuator in all_actuators:
            if action == "turn_on":
                actuator.turn_on()
            elif action == "turn_off":
                actuator.turn_off()

            if param is not None:
                if device_type == "Light":
                    actuator.set_brightness_level(param)
                elif device_type == "AC" or device_type == "Heater":
                    actuator.set_target_temperature(param)    


def get_sensor_reading(sensor_type, room_name=None):
    home = home_plan()

    if room_name is not None:
        room_sensors = get_room_sensors(home, room_name)
        if room_sensors is None:
            return None

        for sensor in room_sensors:
            if sensor.sensor_type == sensor_type:
                return sensor.get_reading()

    else:
        all_sensors = get_all_sensors(home, sensor_type)
        if all_sensors is None:
            return None

        readings = []
        for sensor in all_sensors:
            readings.append(sensor.get_reading())

        return readings


if __name__ == "__main__":
    # print_home_plan(home_plan())

    # Example usage
    # Adjust the brightness level of the Light in the LivingRoom to medium
    adjust_device_status(device_type="Light", action="turn_on", param="medium", room_name="LivingRoom")
    # Get the reading of the IndoorTemperatureSensor in the Bedroom
    reading = get_sensor_reading(sensor_type="IndoorTemperature", room_name="Bedroom")
    logger.info(f"Reading of IndoorTemperatureSensor in Bedroom: {reading}")