# Based on your functional description and the provided source codes, I'll create a `function.py` file that implements the required functionalities for your smart home project. This file will check for light intensity, temperature, workdays for the cleaning robot, and humidity levels to control different actuators accordingly.
# 
# Here's the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import LIGHT_INTENSITY_LOW, TEMP_LOW, HUMIDITY_LOW
from home.actuator import Light, Heater, Humidifier, CleaningRobot
from home.logger_config import logger

def main():
    # Initialize home plan
    home = home_plan()

    # Iterate through rooms and check sensor readings
    for room in home:
        # Get sensors and actuators for the room
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        light_sensor = next((s for s in sensors if s.sensor_type == "LightIntensive"), None)
        temp_sensor = next((s for s in sensors if s.sensor_type == "IndoorTemperature"), None)
        humidity_sensor = next((s for s in sensors if s.sensor_type == "Humidity"), None)
        cleaning_robot = next((a for a in actuators if isinstance(a, CleaningRobot)), None)
        heater = next((a for a in actuators if isinstance(a, Heater)), None)
        humidifier = next((a for a in actuators if isinstance(a, Humidifier)), None)
        light = next((a for a in actuators if isinstance(a, Light)), None)

        # Check light intensity
        if light_sensor and light_sensor.get_reading() > LIGHT_INTENSITY_LOW:
            if light and light.get_status() == "on":
                light.turn_off()
        
        # Check indoor temperature
        if temp_sensor:
            current_temp = temp_sensor.get_reading()
            if current_temp is not None and current_temp < TEMP_LOW:
                if heater and heater.get_status() == "off":
                    heater.turn_on()
                    heater.set_target_temperature(22)  # Set target temperature for heater

        # Check humidity
        if humidity_sensor:
            current_humidity = humidity_sensor.get_reading()
            if current_humidity is not None and current_humidity < HUMIDITY_LOW:
                if humidifier and humidifier.get_status() == "off":
                    humidifier.turn_on()
                    humidifier.increase_humidity()  # Trigger the humidifier to increase humidity

        # Control cleaning robot on weekdays
        if cleaning_robot:
            # For simplicity, assuming it's Monday to Friday (1-5)
            import datetime
            current_day = datetime.datetime.now().weekday()  # 0 = Monday, 6 = Sunday
            if 0 <= current_day <= 4:  # Monday to Friday
                if cleaning_robot.get_status() == "off":
                    cleaning_robot.turn_on()
                cleaning_robot.daily_routine()

if __name__ == "__main__":
    main()