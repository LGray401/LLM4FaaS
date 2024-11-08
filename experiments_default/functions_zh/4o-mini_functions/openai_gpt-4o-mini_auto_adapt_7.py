# Based on your functional description and the provided source code, the `function.py` file will implement the logic to respond to the conditions of temperature, humidity, and light intensity in the smart home environment. It will use the sensors to check the readings and actuators to adjust the environment as needed.
# 
# Here is the `function.py` file that meets your requirements:

# function.py
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.actuator import Heater, AC, Humidifier, Light, NotificationSender

def main():
    # Initialize the home plan
    home = home_plan()

    # Iterate through each room and check the sensors and actuators
    for room in home:
        print(f"Checking room: {room.name}")
        
        # Get the sensors in the room
        temperature_sensors = [s for s in room.sensors if s.sensor_type == "IndoorTemperature"]
        humidity_sensors = [s for s in room.sensors if s.sensor_type == "Humidity"]
        light_sensors = [s for s in room.sensors if s.sensor_type == "LightIntensive"]

        # Get the actuators in the room
        heater = next((a for a in room.actuators if isinstance(a, Heater)), None)
        ac = next((a for a in room.actuators if isinstance(a, AC)), None)
        humidifier = next((a for a in room.actuators if isinstance(a, Humidifier)), None)
        light = next((a for a in room.actuators if isinstance(a, Light)), None)
        notification_sender = next((a for a in room.actuators if isinstance(a, NotificationSender)), None)

        # Check temperature
        if temperature_sensors:
            current_temp = temperature_sensors[0].get_reading()  # Assuming one temperature sensor for simplicity
            if current_temp is not None:
                if current_temp < TEMP_LOW:
                    if heater:
                        heater.set_target_temperature(TEMP_HIGH)
                        heater.adjust_temperature(current_temp)
                        notification_sender.notification_sender("屋里太冷了, 启动加热器.")
                elif current_temp > TEMP_HIGH:
                    if ac:
                        ac.set_target_temperature(TEMP_LOW)
                        ac.adjust_temperature(current_temp)
                        notification_sender.notification_sender("屋里太热了, 启动空调.")

        # Check humidity
        if humidity_sensors:
            current_humidity = humidity_sensors[0].get_reading()  # Assuming one humidity sensor for simplicity
            if current_humidity is not None:
                if current_humidity < HUMIDITY_LOW:
                    if humidifier:
                        humidifier.increase_humidity()
                        notification_sender.notification_sender("屋里有点干, 启动加湿器.")
        
        # Check light intensity
        if light_sensors:
            current_light = light_sensors[0].get_reading()  # Assuming one light sensor for simplicity
            if current_light is not None:
                if current_light < LIGHT_INTENSITY_LOW:
                    if light:
                        light.turn_on()
                        light.set_brightness_level("high")
                        notification_sender.notification_sender("屋里太暗了, 启动灯光.")

if __name__ == "__main__":
    main()