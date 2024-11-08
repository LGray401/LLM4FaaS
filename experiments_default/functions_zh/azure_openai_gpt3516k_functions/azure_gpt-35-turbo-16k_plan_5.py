# Here is the "function.py" file that you requested:

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators, \
    get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Light, AC, Curtain


def main():
    # Create the home plan
    home = home_plan()

    # Print the home plan
    print_home_plan(home)

    # Example usage: Get room and its sensors and actuators
    room = get_room(home, "LivingRoom")
    sensors = get_room_sensors(home, "LivingRoom")
    actuators = get_room_actuators(home, "LivingRoom")

    # Example usage: Get all sensors and actuators of a specific type
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    light_actuators = get_all_actuators(home, "Light")

    # Example usage: Control the lights in the living room based on the indoor temperature
    for sensor in sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            temp = sensor.get_reading()
            if temp is not None:
                if temp < TEMP_LOW:
                    for actuator in actuators:
                        if isinstance(actuator, Light):
                            actuator.turn_on()
                elif temp > TEMP_HIGH:
                    for actuator in actuators:
                        if isinstance(actuator, Light):
                            actuator.turn_off()
                else:
                    for actuator in actuators:
                        if isinstance(actuator, Light):
                            actuator.get_status()
            break

    # Example usage: Control the AC in the living room based on the indoor humidity
    for sensor in sensors:
        if isinstance(sensor, HumiditySensor):
            humidity = sensor.get_reading()
            if humidity is not None:
                if humidity < HUMIDITY_LOW:
                    for actuator in actuators:
                        if isinstance(actuator, AC):
                            actuator.turn_on()
                            actuator.set_target_temperature(22)
                elif humidity > HUMIDITY_HIGH:
                    for actuator in actuators:
                        if isinstance(actuator, AC):
                            actuator.turn_off()
                else:
                    for actuator in actuators:
                        if isinstance(actuator, AC):
                            actuator.get_status()
            break

    # Example usage: Control the curtain in the living room based on the light intensity
    for sensor in sensors:
        if isinstance(sensor, LightIntensiveSensor):
            light_intensity = sensor.get_reading()
            if light_intensity is not None:
                if light_intensity < LIGHT_INTENSITY_LOW:
                    for actuator in actuators:
                        if isinstance(actuator, Curtain):
                            actuator.turn_on()
                elif light_intensity > LIGHT_INTENSITY_HIGH:
                    for actuator in actuators:
                        if isinstance(actuator, Curtain):
                            actuator.turn_off()
                else:
                    for actuator in actuators:
                        if isinstance(actuator, Curtain):
                            actuator.get_status()
            break

if __name__ == "__main__":
    main()