# Sure! Here is the 'function.py' file based on your functional description:

from home.home_plan import home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators

def main():
    # Create home plan
    home = home_plan()

    # Get all sensors in the living room
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    print("Living Room Sensors:")
    for sensor in living_room_sensors:
        reading = sensor.get_reading()
        if reading == 26:
            print("The temperature is 26 degrees.")
        elif reading == 50:
            print("The humidity is 50%.")
        elif reading == "光适中":
            print("The light intensity is moderate.")

    # Get all actuators in the bedroom
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    print("\nBedroom Actuators:")
    for actuator in bedroom_actuators:
        actuator.turn_on()
        actuator.set_target_temperature(20)

    # Get all indoor temperature sensors
    indoor_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    print("\nIndoor Temperature Sensors:")
    for sensor in indoor_temperature_sensors:
        print(sensor.get_reading())

    # Get all light actuators
    light_actuators = get_all_actuators(home, "Light")
    print("\nLight Actuators:")
    for actuator in light_actuators:
        actuator.turn_on()
        actuator.set_brightness_level("high")

if __name__ == "__main__":
    main()