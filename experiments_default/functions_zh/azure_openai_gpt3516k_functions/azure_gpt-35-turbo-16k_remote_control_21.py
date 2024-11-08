# Here is the `function.py` file that you requested:

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, CleaningRobot, SmartTV
from home.logger_config import logger
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    home = home_plan()
    print_home_plan(home)

    room_name = "LivingRoom"
    room = get_room(home, room_name)
    if room:
        sensors = get_room_sensors(home, room_name)
        if sensors:
            for sensor in sensors:
                if isinstance(sensor, IndoorTemperatureSensor):
                    temperature = sensor.get_reading()
                    if temperature < TEMP_LOW:
                        logger.info(f"Temperature in {room_name} is too low: {temperature}. Turning on the heater.")
                        print(f"Temperature in {room_name} is too low: {temperature}. Turning on the heater.")
                        actuator = get_all_actuators(home, "Heater")
                        if actuator:
                            actuator.turn_on()

                    elif temperature > TEMP_HIGH:
                        logger.info(f"Temperature in {room_name} is too high: {temperature}. Turning on the AC.")
                        print(f"Temperature in {room_name} is too high: {temperature}. Turning on the AC.")
                        actuator = get_all_actuators(home, "AC")
                        if actuator:
                            actuator.turn_on()
                
                elif isinstance(sensor, HumiditySensor):
                    humidity = sensor.get_reading()
                    if humidity < HUMIDITY_LOW:
                        logger.info(f"Humidity in {room_name} is too low: {humidity}. Turning on the humidifier.")
                        print(f"Humidity in {room_name} is too low: {humidity}. Turning on the humidifier.")
                        actuator = get_all_actuators(home, "Humidifier")
                        if actuator:
                            actuator.turn_on()

                    elif humidity > HUMIDITY_HIGH:
                        logger.info(f"Humidity in {room_name} is too high: {humidity}. Turning off the humidifier.")
                        print(f"Humidity in {room_name} is too high: {humidity}. Turning off the humidifier.")
                        actuator = get_all_actuators(home, "Humidifier")
                        if actuator:
                            actuator.turn_off()
                            
                elif isinstance(sensor, LightIntensiveSensor):
                    light_intensity = sensor.get_reading()
                    if light_intensity < LIGHT_INTENSITY_LOW:
                        logger.info(f"Light intensity in {room_name} is too low: {light_intensity}. Turning on the light.")
                        print(f"Light intensity in {room_name} is too low: {light_intensity}. Turning on the light.")
                        actuator = get_all_actuators(home, "Light")
                        if actuator:
                            actuator.turn_on()

                    elif light_intensity > LIGHT_INTENSITY_HIGH:
                        logger.info(f"Light intensity in {room_name} is too high: {light_intensity}. Turning off the light.")
                        print(f"Light intensity in {room_name} is too high: {light_intensity}. Turning off the light.")
                        actuator = get_all_actuators(home, "Light")
                        if actuator:
                            actuator.turn_off()
                            
    room_name = "Kitchen"
    room = get_room(home, room_name)
    if room:
        sensors = get_room_sensors(home, room_name)
        if sensors:
            for sensor in sensors:
                if isinstance(sensor, SmokeSensor):
                    smoke = sensor.get_reading()
                    if smoke > 50:
                        logger.info(f"Smoke detected in {room_name}. Sending notification.")
                        print(f"Smoke detected in {room_name}. Sending notification.")
                        actuator = get_all_actuators(home, "NotificationSender")
                        if actuator:
                            actuator.notification_sender("Smoke detected in the kitchen!")
                            
if __name__ == "__main__":
    main()