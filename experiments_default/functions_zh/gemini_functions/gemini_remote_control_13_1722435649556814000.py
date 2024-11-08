from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger
import time

def main():
    home = home_plan()

    # 调控灯的适合亮度
    living_room = get_room(home, "LivingRoom")
    living_room_lights = get_room_actuators(home, "LivingRoom")
    for light in living_room_lights:
        if light.actuator_type == "Light":
            light_intensive_sensor = get_room_sensors(home, "LivingRoom")[0]
            if light_intensive_sensor.get_reading() < LIGHT_INTENSITY_LOW:
                light.turn_on()
                light.set_brightness_level("high")
            elif light_intensive_sensor.get_reading() > LIGHT_INTENSITY_HIGH:
                light.set_brightness_level("low")
            else:
                light.set_brightness_level("medium")

    # 调控室内温度
    for room in home:
        if room.name == "LivingRoom" or room.name == "Bedroom":
            temp_sensor = get_room_sensors(home, room.name)[0]
            temperature = temp_sensor.get_reading()
            for actuator in room.actuators:
                if actuator.actuator_type == "Heater":
                    actuator.adjust_temperature(temperature)
                elif actuator.actuator_type == "AC":
                    actuator.adjust_temperature(temperature)

    # 调控窗帘开关
    for room in home:
        if room.name == "LivingRoom" or room.name == "Bedroom":
            light_sensor = get_room_sensors(home, room.name)[0]
            light_intensity = light_sensor.get_reading()
            for actuator in room.actuators:
                if actuator.actuator_type == "Curtain":
                    if light_intensity < LIGHT_INTENSITY_LOW:
                        actuator.turn_on()
                    else:
                        actuator.turn_off()

    # 加湿器调控房间
    for room in home:
        humidity_sensor = get_room_sensors(home, room.name)[0]
        humidity = humidity_sensor.get_reading()
        for actuator in room.actuators:
            if actuator.actuator_type == "Humidifier":
                if humidity < HUMIDITY_LOW:
                    actuator.increase_humidity()
                elif humidity > HUMIDITY_HIGH:
                    actuator.decrease_humidity()


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:** Imports necessary modules from your project.
# 2. **`main()` Function:**
#    - **Home Initialization:** Calls `home_plan()` to create your home structure.
#    - **Control Light Brightness:** 
#      - Retrieves the "LivingRoom" and its light actuators.
#      - Gets the "LightIntensiveSensor" reading from the living room.
#      - Adjusts the brightness of the lights based on the light intensity.
#    - **Control Indoor Temperature:** 
#      - Iterates through rooms ("LivingRoom" and "Bedroom").
#      - Gets the temperature sensor reading.
#      - Adjusts the "Heater" or "AC" based on the temperature and desired setting (you can add target temperature logic).
#    - **Control Curtains:** 
#      - Similar to the light control, it opens or closes the curtains based on the light intensity.
#    - **Humidifier Control:**
#      - Retrieves the humidity sensor readings for each room.
#      - Adjusts the "Humidifier" to increase or decrease humidity based on the current reading.

# **Key Points:**

# - **Logic:** This is a basic implementation. You can enhance it with:
#     - Target temperature settings for the "Heater" and "AC".
#     - Smart rules based on time of day, weather, etc.
#     - User interactions (e.g., voice commands, app controls).
# - **Error Handling:** Add error handling and logging to your code for debugging.
# - **Real-World Integration:** This is a simplified example. In a real smart home, you'd connect sensors and actuators to a hardware platform, using APIs and protocols (e.g., MQTT, Z-Wave) for communication.

# **To Run the Code:**

# 1. Make sure you have the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files in the 'home' folder.
# 2. Place `function.py` in the `functions` folder.
# 3. Run `python functions/function.py`.

# This code demonstrates a basic implementation of your smart home functionalities. You can expand it with more complex rules, user interactions, and real-world hardware integration to make your smart home project more comprehensive.
