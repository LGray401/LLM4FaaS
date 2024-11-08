# Sure, here is the `function.py` file based on your functional description and the given source codes:

# function.py

from home.home_plan import home_plan, get_all_sensors, get_room_actuators
from home.config import TEMP_HIGH, LIGHT_INTENSITY_HIGH

def main():
    # Initialize home
    home = home_plan()

    # Temperature Adjustment
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        if current_temp is not None and current_temp > TEMP_HIGH:
            room_name = sensor.room_name
            acs = get_room_actuators(home, room_name)
            for ac in acs:
                if ac.actuator_type == "AC":
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(current_temp)

    # Humidity Adjustment (湿度调节正常)
    # Assuming the humidity is controlled manually or by some other means.

    # Light Intensity Adjustment
    light_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in light_sensors:
        sensor.turn_on()
        current_light_intensity = sensor.get_reading()
        if current_light_intensity is not None and current_light_intensity > LIGHT_INTENSITY_HIGH:
            room_name = sensor.room_name
            curtains = get_room_actuators(home, room_name)
            for curtain in curtains:
                if curtain.actuator_type == "Curtain":
                    curtain.turn_on()

if __name__ == "__main__":
    main()