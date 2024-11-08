from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor
from home.actuator import AC
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW
from home.logger_config import logger


def energy_saving_mode(home):
    """
    根据室外温湿度 自主选择空调启用与否
    """
    # 获取室外温度和湿度传感器
    outdoor_temp_sensor = get_all_sensors(home, "OutdoorTemperature")[0]
    outdoor_humidity_sensor = get_all_sensors(home, "Humidity")[0]

    # 获取所有空调
    acs = get_all_actuators(home, "AC")

    # 获取室外温度和湿度读数
    outdoor_temp = outdoor_temp_sensor.get_reading()
    outdoor_humidity = outdoor_humidity_sensor.get_reading()

    # 根据室外温湿度判断是否启用空调
    if outdoor_temp > TEMP_HIGH or outdoor_humidity > HUMIDITY_HIGH:
        # 启用空调
        for ac in acs:
            ac.turn_on()
            logger.info(f"Turning on AC in {ac.room_name} due to high outdoor temperature or humidity.")
    else:
        # 关闭空调
        for ac in acs:
            ac.turn_off()
            logger.info(f"Turning off AC in {ac.room_name} due to suitable outdoor temperature and humidity.")


if __name__ == "__main__":
    home = home_plan()
    energy_saving_mode(home)

# **Explanation:**

# 1. **Imports:** Imports necessary functions and classes from `home.home_plan`, `home.sensor`, `home.actuator`, and `home.config`.
# 2. **`energy_saving_mode` function:**
#    - Takes the `home` object (representing the smart home plan) as input.
#    - Retrieves the outdoor temperature and humidity sensors using `get_all_sensors`.
#    - Retrieves all AC actuators using `get_all_actuators`.
#    - Gets readings from the outdoor sensors using `get_reading`.
#    - Based on the temperature and humidity readings and the defined thresholds in `home.config`, the function decides whether to turn on or off the ACs:
#      - If outdoor temperature is greater than `TEMP_HIGH` or humidity is greater than `HUMIDITY_HIGH`, all ACs are turned on.
#      - Otherwise, all ACs are turned off.
# 3. **`if __name__ == "__main__":` block:**
#    - Creates the home plan using `home_plan()`.
#    - Calls the `energy_saving_mode` function to start the energy-saving mode logic.

# **To use this code:**

# 1. Place the `function.py` file in the `functions` folder of your smart home project.
# 2. Ensure that the other required files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) are in the `home` folder.
# 3. You can call `energy_saving_mode(home)` from your main script to implement this function.

# **Remember to adjust the temperature and humidity thresholds in `home.config.py` to match your specific requirements.**
