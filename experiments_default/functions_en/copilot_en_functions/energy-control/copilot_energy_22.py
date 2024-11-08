# Based on the functional description and the provided source code, you need to create a `function.py` file that contains the main function. This function should control the smart home system according to the following rules:
#
# 1. When the kitchen smoke exceeds the standard, turn on the smoke alarm.
# 2. In summer, when the indoor temperature is less than 20 degrees, the air conditioner will be automatically turned off. When the temperature is higher than 25 degrees, turn on the air conditioner.
# 3. Set the sensor light. When there are people, the light will turn on. When there are no people, the light will turn off automatically.
#
# Here is a Python script that implements these functionalities:
#
# ```python
from home.sensor import SmokeSensor, IndoorTemperatureSensor
from home.actuator import AC, Light
from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators

def main():
    # Initialize the home plan
    home = home_plan()

    # Get the kitchen room
    kitchen = get_room(home, "Kitchen")

    # Get the smoke sensor in the kitchen
    smoke_sensor = next((sensor for sensor in get_room_sensors(home, "Kitchen") if isinstance(sensor, SmokeSensor)), None)

    # Get the AC in the living room
    ac = next((actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, AC)), None)

    # Get the light in the living room
    light = next((actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Light)), None)

    # Get the indoor temperature sensor in the living room
    indoor_temp_sensor = next((sensor for sensor in get_room_sensors(home, "LivingRoom") if isinstance(sensor, IndoorTemperatureSensor)), None)

    # Check the smoke level in the kitchen
    if smoke_sensor.get_reading() > 50:  # Assuming the standard smoke level is 50
        # Turn on the smoke alarm
        smoke_sensor.turn_on()

    # Check the indoor temperature in the living room
    indoor_temp = indoor_temp_sensor.get_reading()
    if indoor_temp < 20:
        # Turn off the AC
        ac.turn_off()
    elif indoor_temp > 25:
        # Turn on the AC
        ac.turn_on()

    # Check if there are people in the living room
    # Assuming the presence of people can be determined by the light sensor
    light_sensor = next((sensor for sensor in get_room_sensors(home, "LivingRoom") if isinstance(sensor, LightIntensiveSensor)), None)
    if light_sensor.get_reading() > 500:  # Assuming the light level is high when there are people
        # Turn on the light
        light.turn_on()
    else:
        # Turn off the light
        light.turn_off()

if __name__ == "__main__":
    main()
# ```
#
# Please replace the smoke level, temperature, and light level thresholds with the actual values you want to use. Also, you may need to adjust the room names and sensor/actuator types according to your actual home plan.