# Sure, here is the 'function.py' file according to your functional description:

# functions/function.py

def close_unnecessary_switches(home):
    for room in home:
        for actuator in room.actuators:
            if actuator.status == "on":
                if isinstance(actuator, Light):
                    light_sensors = get_room_sensors(home, room.name, "LightIntensive")
                    if light_sensors:
                        max_intensity = max([sensor.get_reading() for sensor in light_sensors])
                        if max_intensity < LIGHT_INTENSITY_LOW:
                            actuator.turn_off()
                elif isinstance(actuator, AC):
                    temperature_sensors = get_room_sensors(home, room.name, "IndoorTemperature")
                    if temperature_sensors:
                        min_temperature = min([sensor.get_reading() for sensor in temperature_sensors])
                        if min_temperature > TEMP_HIGH:
                            actuator.turn_off()
                elif isinstance(actuator, Heater):
                    temperature_sensors = get_room_sensors(home, room.name, "IndoorTemperature")
                    if temperature_sensors:
                        max_temperature = max([sensor.get_reading() for sensor in temperature_sensors])
                        if max_temperature < TEMP_LOW:
                            actuator.turn_off()
                elif isinstance(actuator, Humidifier):
                    humidity_sensors = get_room_sensors(home, room.name, "Humidity")
                    if humidity_sensors:
                        max_humidity = max([sensor.get_reading() for sensor in humidity_sensors])
                        if max_humidity < HUMIDITY_LOW:
                            actuator.turn_off()
    print("Unnecessary switches are closed.")