# Sure! Based on your functional description and the provided source code, I have prepared the 'function.py' file for your smart home project. Here is the content of the 'function.py' file:

from home.home_plan import home_plan, print_home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    home = home_plan()
    print_home_plan(home)

    # Get sensors and actuators in the specific room
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Get all temperature sensors in the home
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")

    # Get all light actuators in the home
    light_actuators = get_all_actuators(home, "Light")

    # Perform actions based on sensor readings
    for sensor in temperature_sensors:
        reading = sensor.get_reading()
        if reading is not None:
            if reading < TEMP_LOW:
                for actuator in living_room_actuators:
                    if actuator.actuator_type == "Heater":
                        actuator.set_target_temperature(TEMP_HIGH)
                        actuator.adjust_temperature(reading)
            elif reading > TEMP_HIGH:
                for actuator in living_room_actuators:
                    if actuator.actuator_type == "AC":
                        actuator.set_target_temperature(TEMP_LOW)
                        actuator.adjust_temperature(reading)

    for sensor in living_room_sensors:
        if sensor.sensor_type == "LightIntensive":
            reading = sensor.get_reading()
            if reading is not None:
                if reading > LIGHT_INTENSITY_HIGH:
                    for actuator in light_actuators:
                        actuator.turn_off()

    # Add more conditions and actions based on other sensors and actuators in the home

if __name__ == "__main__":
    main()