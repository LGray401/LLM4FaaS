# Here is the 'function.py' file that you requested:

from home.home_plan import home_plan, get_room_actuators, get_room_sensors, get_all_sensors, get_all_actuators
from home.logger_config import logger
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

home = home_plan()

def open_window_turn_off_ac(room_name):
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if actuator.actuator_type == "AC":
            actuator.turn_off()
        elif actuator.actuator_type == "Window":
            actuator.turn_on()
        else:
            logger.warning(f"Cannot perform the action for {actuator.actuator_type} in {room_name}")

def close_window_turn_on_ac(room_name):
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if actuator.actuator_type == "AC":
            actuator.turn_on()
        elif actuator.actuator_type == "Window":
            actuator.turn_off()
        else:
            logger.warning(f"Cannot perform the action for {actuator.actuator_type} in {room_name}")

def check_indoor_temperature(room_name):
    sensors = get_room_sensors(home, room_name)
    for sensor in sensors:
        if sensor.sensor_type == "IndoorTemperature":
            temperature = sensor.get_reading()
            return temperature
    logger.warning(f"Cannot find IndoorTemperature sensor in {room_name}")

def check_outdoor_temperature(room_name):
    sensors = get_room_sensors(home, room_name)
    for sensor in sensors:
        if sensor.sensor_type == "OutdoorTemperature":
            temperature = sensor.get_reading()
            return temperature
    logger.warning(f"Cannot find OutdoorTemperature sensor in {room_name}")

def check_humidity(room_name):
    sensors = get_room_sensors(home, room_name)
    for sensor in sensors:
        if sensor.sensor_type == "Humidity":
            humidity = sensor.get_reading()
            return humidity
    logger.warning(f"Cannot find Humidity sensor in {room_name}")

def check_light_intensity(room_name):
    sensors = get_room_sensors(home, room_name)
    for sensor in sensors:
        if sensor.sensor_type == "LightIntensive":
            light_intensity = sensor.get_reading()
            return light_intensity
    logger.warning(f"Cannot find LightIntensive sensor in {room_name}")

def check_indoor_temperature_range(room_name):
    temperature = check_indoor_temperature(room_name)
    if temperature is not None:
        if temperature < TEMP_LOW:
            logger.info(f"Indoor temperature in {room_name} is too low: {temperature}°C")
        elif temperature > TEMP_HIGH:
            logger.info(f"Indoor temperature in {room_name} is too high: {temperature}°C")
        else:
            logger.info(f"Indoor temperature in {room_name} is within the desired range: {temperature}°C")
    else:
        logger.warning(f"Cannot check indoor temperature range for {room_name}")

def check_humidity_range(room_name):
    humidity = check_humidity(room_name)
    if humidity is not None:
        if humidity < HUMIDITY_LOW:
            logger.info(f"Humidity in {room_name} is too low: {humidity}%")
        elif humidity > HUMIDITY_HIGH:
            logger.info(f"Humidity in {room_name} is too high: {humidity}%")
        else:
            logger.info(f"Humidity in {room_name} is within the desired range: {humidity}%")
    else:
        logger.warning(f"Cannot check humidity range for {room_name}")

def check_light_intensity_range(room_name):
    light_intensity = check_light_intensity(room_name)
    if light_intensity is not None:
        if light_intensity < LIGHT_INTENSITY_LOW:
            logger.info(f"Light intensity in {room_name} is too low: {light_intensity} lux")
        elif light_intensity > LIGHT_INTENSITY_HIGH:
            logger.info(f"Light intensity in {room_name} is too high: {light_intensity} lux")
        else:
            logger.info(f"Light intensity in {room_name} is within the desired range: {light_intensity} lux")
    else:
        logger.warning(f"Cannot check light intensity range for {room_name}")

def check_outdoor_temperature_range(room_name):
    temperature = check_outdoor_temperature(room_name)
    if temperature is not None:
        if temperature < TEMP_LOW:
            logger.info(f"Outdoor temperature in {room_name} is too low: {temperature}°C")
        elif temperature > TEMP_HIGH:
            logger.info(f"Outdoor temperature in {room_name} is too high: {temperature}°C")
        else:
            logger.info(f"Outdoor temperature in {room_name} is within the desired range: {temperature}°C")
    else:
        logger.warning(f"Cannot check outdoor temperature range for {room_name}")

def check_all_indoor_temperatures():
    temperatures = {}
    sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in sensors:
        temperature = sensor.get_reading()
        room_name = sensor.room_name
        if room_name not in temperatures:
            temperatures[room_name] = []
        temperatures[room_name].append(temperature)
    return temperatures

def check_all_humidities():
    humidities = {}
    sensors = get_all_sensors(home, "Humidity")
    for sensor in sensors:
        humidity = sensor.get_reading()
        room_name = sensor.room_name
        if room_name not in humidities:
            humidities[room_name] = []
        humidities[room_name].append(humidity)
    return humidities

def check_all_light_intensities():
    light_intensities = {}
    sensors = get_all_sensors(home, "LightIntensive")
    for sensor in sensors:
        light_intensity = sensor.get_reading()
        room_name = sensor.room_name
        if room_name not in light_intensities:
            light_intensities[room_name] = []
        light_intensities[room_name].append(light_intensity)
    return light_intensities

def check_all_outdoor_temperatures():
    temperatures = {}
    sensors = get_all_sensors(home, "OutdoorTemperature")
    for sensor in sensors:
        temperature = sensor.get_reading()
        room_name = sensor.room_name
        if room_name not in temperatures:
            temperatures[room_name] = []
        temperatures[room_name].append(temperature)
    return temperatures

print("Smart home functions have been defined.")