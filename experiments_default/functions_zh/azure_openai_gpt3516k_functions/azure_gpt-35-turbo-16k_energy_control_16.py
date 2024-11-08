# Sure! Here is the content of the `function.py` file based on the given functional description and the provided source code:

def energy_saving(home):
    from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

    for room in home:
        # Get the sensors in the room
        sensors = room.sensors

        # Get the actuators in the room
        actuators = room.actuators

        # Check if there is an IndoorTemperatureSensor in the room
        indoor_temperature_sensor = None
        for sensor in sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                indoor_temperature_sensor = sensor
                break

        if indoor_temperature_sensor is not None:
            # Get the temperature reading from the IndoorTemperatureSensor
            temperature = indoor_temperature_sensor.get_reading()

            # Adjust the temperature based on the temperature reading and the threshold values
            if temperature is not None:
                if temperature < TEMP_LOW:
                    for actuator in actuators:
                        if isinstance(actuator, Heater):
                            actuator.turn_on()
                        elif isinstance(actuator, AC):
                            actuator.turn_off()
                elif temperature > TEMP_HIGH:
                    for actuator in actuators:
                        if isinstance(actuator, Heater):
                            actuator.turn_off()
                        elif isinstance(actuator, AC):
                            actuator.turn_on()
                else:
                    for actuator in actuators:
                        if isinstance(actuator, Heater) or isinstance(actuator, AC):
                            actuator.turn_off()

        # Check if there is a HumiditySensor in the room
        humidity_sensor = None
        for sensor in sensors:
            if isinstance(sensor, HumiditySensor):
                humidity_sensor = sensor
                break

        if humidity_sensor is not None:
            # Get the humidity reading from the HumiditySensor
            humidity = humidity_sensor.get_reading()

            # Adjust the humidity based on the humidity reading and the threshold values
            if humidity is not None:
                if humidity < HUMIDITY_LOW:
                    for actuator in actuators:
                        if isinstance(actuator, Humidifier):
                            actuator.increase_humidity()
                elif humidity > HUMIDITY_HIGH:
                    for actuator in actuators:
                        if isinstance(actuator, Humidifier):
                            actuator.decrease_humidity()

        # Check if there is a LightIntensiveSensor in the room
        light_intensive_sensor = None
        for sensor in sensors:
            if isinstance(sensor, LightIntensiveSensor):
                light_intensive_sensor = sensor
                break

        if light_intensive_sensor is not None:
            # Get the light intensity reading from the LightIntensiveSensor
            light_intensity = light_intensive_sensor.get_reading()

            # Adjust the light intensity based on the light intensity reading and the threshold values
            if light_intensity is not None:
                if light_intensity < LIGHT_INTENSITY_LOW:
                    for actuator in actuators:
                        if isinstance(actuator, Light):
                            actuator.set_brightness_level("high")
                elif light_intensity > LIGHT_INTENSITY_HIGH:
                    for actuator in actuators:
                        if isinstance(actuator, Light):
                            actuator.set_brightness_level("low")

def main():
    from home.home_plan import home_plan, print_home_plan
    home = home_plan()
    print_home_plan(home)
    energy_saving(home)

if __name__ == "__main__":
    main()