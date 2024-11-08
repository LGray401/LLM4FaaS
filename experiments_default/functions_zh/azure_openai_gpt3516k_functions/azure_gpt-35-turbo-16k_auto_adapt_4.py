# Sure! I have created the 'function.py' file based on your given functional description and the provided source code. Here is the content of the 'function.py' file:

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor

# Function to get the temperature reading of a specific room
def get_temperature(room_name):
    home = home_plan()
    room = get_room(home, room_name)

    if room:
        sensors = get_room_sensors(home, room_name)
        for sensor in sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                return sensor.get_reading()
    
    return None

# Function to get the humidity reading of a specific room
def get_humidity(room_name):
    home = home_plan()
    room = get_room(home, room_name)
    
    if room:
        sensors = get_room_sensors(home, room_name)
        for sensor in sensors:
            if isinstance(sensor, HumiditySensor):
                return sensor.get_reading()
    
    return None

# Function to get the light intensity reading of a specific room
def get_light_intensity(room_name):
    home = home_plan()
    room = get_room(home, room_name)
    
    if room:
        sensors = get_room_sensors(home, room_name)
        for sensor in sensors:
            if isinstance(sensor, LightIntensiveSensor):
                return sensor.get_reading()
    
    return None

# Function to set the target temperature of a heater or AC in a specific room
def set_target_temperature(room_name, target_temperature):
    home = home_plan()
    room = get_room(home, room_name)
    
    if room:
        actuators = get_room_actuators(home, room_name)
        for actuator in actuators:
            if isinstance(actuator, Heater) or isinstance(actuator, AC):
                actuator.set_target_temperature(target_temperature)

# Function to set the brightness level of a light in a specific room
def set_brightness_level(room_name, level_name):
    home = home_plan()
    room = get_room(home, room_name)
    
    if room:
        actuators = get_room_actuators(home, room_name)
        for actuator in actuators:
            if isinstance(actuator, Light):
                actuator.set_brightness_level(level_name)

# Function to get the average temperature of all the rooms in the house
def get_average_temperature():
    home = home_plan()
    sensors = get_all_sensors(home, "IndoorTemperature")
    total_temperature = 0
    count = 0
    
    for sensor in sensors:
        reading = sensor.get_reading()
        if reading is not None:
            total_temperature += reading
            count += 1
    
    if count > 0:
        average_temperature = total_temperature / count
        return average_temperature
    
    return None

# Function to get the average humidity of all the rooms in the house
def get_average_humidity():
    home = home_plan()
    sensors = get_all_sensors(home, "Humidity")
    total_humidity = 0
    count = 0
    
    for sensor in sensors:
        reading = sensor.get_reading()
        if reading is not None:
            total_humidity += reading
            count += 1
    
    if count > 0:
        average_humidity = total_humidity / count
        return average_humidity
    
    return None

# Function to get the average light intensity of all the rooms in the house
def get_average_light_intensity():
    home = home_plan()
    sensors = get_all_sensors(home, "LightIntensive")
    total_light_intensity = 0
    count = 0
    
    for sensor in sensors:
        reading = sensor.get_reading()
        if reading is not None:
            total_light_intensity += reading
            count += 1
    
    if count > 0:
        average_light_intensity = total_light_intensity / count
        return average_light_intensity
    
    return None


# Example usage
# print_home_plan(home_plan())
# print(get_temperature("LivingRoom"))
# print(get_humidity("LivingRoom"))
# print(get_light_intensity("LivingRoom"))
# set_target_temperature("LivingRoom", 25)
# set_brightness_level("LivingRoom", "medium")
# print(get_average_temperature())
# print(get_average_humidity())
# print(get_average_light_intensity())