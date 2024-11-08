from home.home_plan import home_plan, get_room, get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Light
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH


def energy_saving_mode():
    home = home_plan()

    # Adjust AC/Heater based on temperature
    for room_name in ["LivingRoom", "Bedroom", "Kitchen", "Bathroom"]:
        room = get_room(home, room_name)
        if room:
            temperature_sensor = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)][0]
            current_temperature = temperature_sensor.get_reading()
            if current_temperature is not None:
                acs = get_all_actuators(home, "AC")
                heaters = get_all_actuators(home, "Heater")
                for ac in acs:
                    if ac.room_name == room_name:
                        ac.set_target_temperature(TEMP_HIGH)
                        ac.adjust_temperature(current_temperature)
                for heater in heaters:
                    if heater.room_name == room_name:
                        heater.set_target_temperature(TEMP_LOW)
                        heater.adjust_temperature(current_temperature)

    # Adjust lights based on light intensity
    for room_name in ["LivingRoom", "Bedroom", "Kitchen", "Bathroom"]:
        room = get_room(home, room_name)
        if room:
            light_sensor = [sensor for sensor in room.sensors if isinstance(sensor, LightIntensiveSensor)][0]
            current_light_intensity = light_sensor.get_reading()
            if current_light_intensity is not None:
                lights = get_all_actuators(home, "Light")
                for light in lights:
                    if light.room_name == room_name:
                        if current_light_intensity > LIGHT_INTENSITY_HIGH:
                            light.set_brightness_level("low")
                        elif current_light_intensity < LIGHT_INTENSITY_LOW:
                            light.set_brightness_level("high")

    # Adjust humidifiers based on humidity
    # (Implement humidifier logic if needed)
    # for room_name in ["LivingRoom", "Bedroom", "Kitchen", "Bathroom"]:
    #     room = get_room(home, room_name)
    #     if room:
    #         humidity_sensor = [sensor for sensor in room.sensors if isinstance(sensor, HumiditySensor)][0]
    #         current_humidity = humidity_sensor.get_reading()
    #         if current_humidity is not None:
    #             # Adjust humidifier based on humidity level
    #             pass

    print("Energy saving mode activated.")

if __name__ == "__main__":
    energy_saving_mode()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: For managing the home layout and accessing rooms and devices.
#    - `home.sensor`: To access sensor classes like `IndoorTemperatureSensor`, `HumiditySensor`, `LightIntensiveSensor`.
#    - `home.actuator`: To access actuator classes like `AC`, `Heater`, `Light`.
#    - `home.config`: To access configuration parameters like temperature thresholds and light intensity thresholds.

# 2. **Define `energy_saving_mode` function:**
#    - **Create a home plan:** `home = home_plan()`
#    - **Adjust AC/Heater based on temperature:**
#      - Iterate through relevant rooms: "LivingRoom", "Bedroom", "Kitchen", "Bathroom"
#      - Get the `IndoorTemperatureSensor` from the room.
#      - Get the current temperature reading.
#      - Retrieve all `AC` and `Heater` actuators.
#      - For each `AC` and `Heater` in the current room:
#        - Set the target temperature (TEMP_HIGH for AC, TEMP_LOW for Heater).
#        - Adjust the actuator's state based on the current temperature using `adjust_temperature` method.
#    - **Adjust lights based on light intensity:**
#      - Iterate through relevant rooms: "LivingRoom", "Bedroom", "Kitchen", "Bathroom"
#      - Get the `LightIntensiveSensor` from the room.
#      - Get the current light intensity reading.
#      - Retrieve all `Light` actuators.
#      - For each `Light` in the current room:
#        - Adjust the brightness level based on the light intensity using `set_brightness_level` method.
#    - **Adjust humidifiers based on humidity:** (Not implemented in this example)
#      - This section is commented out as you haven't provided specific humidifier functionality in your code. You can implement this section similarly to the temperature and light adjustment logic.
#    - **Print a confirmation message:** "Energy saving mode activated."

# 3. **Main execution:**
#    - The `if __name__ == "__main__":` block calls the `energy_saving_mode` function when the script is run directly.

# **Remember to:**

# - Update the `home_plan` function in `home_plan.py` to match your actual smart home configuration.
# - Implement the humidifier logic in the `energy_saving_mode` function if you have humidifiers in your system.
# - Configure the thresholds in `config.py` according to your desired energy-saving settings.
