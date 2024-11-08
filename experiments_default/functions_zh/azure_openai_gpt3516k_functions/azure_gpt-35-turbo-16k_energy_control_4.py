# Sure! Here is the 'function.py' file as per your requirement:

from home.home_plan import home_plan, print_home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH

def main():
    home = home_plan()
    # print_home_plan(home)

    # Identify sensors and actuators
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Process sensor data
    for sensor in living_room_sensors:
        if sensor.sensor_type == "IndoorTemperature":
            temperature = sensor.get_reading()
            if temperature is not None:
                if temperature < TEMP_LOW:
                    for actuator in living_room_actuators:
                        if actuator.actuator_type == "Heater":
                            actuator.set_target_temperature(TEMP_HIGH)
                            actuator.adjust_temperature(temperature)
                elif temperature > TEMP_HIGH:
                    for actuator in living_room_actuators:
                        if actuator.actuator_type == "AC":
                            actuator.set_target_temperature(TEMP_LOW)
                            actuator.adjust_temperature(temperature)

        elif sensor.sensor_type == "Humidity":
            humidity = sensor.get_reading()
            if humidity is not None:
                if humidity < HUMIDITY_LOW:
                    for actuator in living_room_actuators:
                        if actuator.actuator_type == "Humidifier":
                            actuator.increase_humidity()
                elif humidity > HUMIDITY_HIGH:
                    for actuator in living_room_actuators:
                        if actuator.actuator_type == "Humidifier":
                            actuator.decrease_humidity()

if __name__ == "__main__":
    main()