# Here is the 'function.py' file for your smart home project based on your functional description:

from home.home_plan import home_plan, print_home_plan, get_room_sensors, get_room_actuators, \
    get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import AC, Window


def main():
    home = home_plan()

    # Print Home Plan
    print_home_plan(home)

    # Example usages:
    bedroom_sensors = get_room_sensors(home, "Bedroom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    all_indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    all_light_actuators = get_all_actuators(home, "Light")

    # Create AC object for the Bedroom
    bedroom_ac = AC("Bedroom")
    bedroom_ac.set_target_temperature(20)

    # Create Window object for the LivingRoom
    living_room_window = Window("LivingRoom")

    # Create IndoorTemperatureSensor object for the Kitchen
    kitchen_indoor_temp_sensor = IndoorTemperatureSensor("Kitchen")
    kitchen_indoor_temp_sensor.turn_on()
    kitchen_temp = kitchen_indoor_temp_sensor.get_reading()
    kitchen_indoor_temp_sensor.turn_off()

    # Create OutdoorTemperatureSensor object for the Balcony
    balcony_outdoor_temp_sensor = OutdoorTemperatureSensor("Balcony")
    balcony_outdoor_temp_sensor.turn_on()
    balcony_temp = balcony_outdoor_temp_sensor.get_reading()
    balcony_outdoor_temp_sensor.turn_off()

    # Example logic:
    if kitchen_temp > 30:
        bedroom_ac.turn_on()

    if bedroom_ac.get_status() == "on" and balcony_temp < 10:
        living_room_window.turn_on()

    # TODO: Add more logic based on your functional description


if __name__ == "__main__":
    main()