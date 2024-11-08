# Based on your provided functional description and the given source code files, I have created a `function.py` file for your smart home project. You can find the file below:

from home.home_plan import home_plan, get_all_sensors, get_all_actuators

def dim_bedroom_light():
    home = home_plan()
    light_sensors = get_all_sensors(home, "LightIntensive")
    light_actuators = get_all_actuators(home, "Light")

    if not light_sensors:
        print("No light sensors found.")
        return

    if not light_actuators:
        print("No light actuators found.")
        return

    for sensor in light_sensors:
        if sensor.room_name == "Bedroom":
            light_sensor = sensor
            break
    else:
        print("No light sensor found in the Bedroom.")
        return

    for actuator in light_actuators:
        if actuator.room_name == "Bedroom":
            light_actuator = actuator
            break
    else:
        print("No light actuator found in the Bedroom.")
        return

    reading = light_sensor.get_reading()

    if reading is not None:
        if reading > 50:
            light_actuator.set_brightness_level("low")
            print("Bedroom light dimmed.")
        else:
            print("Bedroom light is already dim.")

if __name__ == "__main__":
    dim_bedroom_light()