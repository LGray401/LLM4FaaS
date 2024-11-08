from home.home_plan import home_plan, get_all_sensors, get_all_actuators, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW
import time


def main():
    home = home_plan()

    # Example usage
    while True:
        # Temperature Control
        temperature_sensors = get_all_sensors(home, "IndoorTemperature")
        for sensor in temperature_sensors:
            temperature_reading = sensor.get_reading()
            if temperature_reading is not None:
                room_name = sensor.room_name
                room = get_room_actuators(home, room_name)
                if room is not None:
                    for actuator in room:
                        if actuator.actuator_type == "AC":
                            if temperature_reading > TEMP_HIGH:
                                print(f"The temperature in {room_name} is {temperature_reading}°C. Turning on the AC.")
                                actuator.turn_on()
                                time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                        elif actuator.actuator_type == "Heater":
                            if temperature_reading < TEMP_LOW:
                                print(f"The temperature in {room_name} is {temperature_reading}°C. Turning on the Heater.")
                                actuator.turn_on()
                                time.sleep(TEMP_CHANGE_DURATION_WINDOW)

        # Humidity Control
        humidity_sensors = get_all_sensors(home, "Humidity")
        for sensor in humidity_sensors:
            humidity_reading = sensor.get_reading()
            if humidity_reading is not None:
                room_name = sensor.room_name
                room = get_room_actuators(home, room_name)
                if room is not None:
                    for actuator in room:
                        if actuator.actuator_type == "Humidifier":
                            if humidity_reading < HUMIDITY_LOW:
                                print(f"The humidity in {room_name} is {humidity_reading}%. Increasing humidity.")
                                actuator.increase_humidity()
                            elif humidity_reading > HUMIDITY_HIGH:
                                print(f"The humidity in {room_name} is {humidity_reading}%. Decreasing humidity.")
                                actuator.decrease_humidity()

        # Light Control
        light_intensity_sensors = get_all_sensors(home, "LightIntensive")
        for sensor in light_intensity_sensors:
            light_intensity_reading = sensor.get_reading()
            if light_intensity_reading is not None:
                room_name = sensor.room_name
                room = get_room_actuators(home, room_name)
                if room is not None:
                    for actuator in room:
                        if actuator.actuator_type == "Curtain":
                            if light_intensity_reading > LIGHT_INTENSITY_HIGH:
                                print(f"The light intensity in {room_name} is {light_intensity_reading} lux. Opening the curtains.")
                                actuator.turn_on()

        # Other Smart Home Features (e.g., security, entertainment) can be added here

        time.sleep(1)  # Pause for a second before checking again


if __name__ == "__main__":
    main()
