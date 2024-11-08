# Here is the `function.py` file for your smart home project based on the provided functional descriptions and source code.
# 
# ### functions/function.py

from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW
from home.actuator import AC, Humidifier, Light, NotificationSender
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor

def main():
    # Initialize home
    home = home_plan()
    
    # Define your rooms
    room_names = ["LivingRoom", "Bedroom", "Kitchen", "Bathroom", "Balcony"]

    for room_name in room_names:
        room = get_room(home, room_name)
        if room:
            sensors = get_room_sensors(home, room_name)
            actuators = get_room_actuators(home, room_name)
            
            for sensor in sensors:
                sensor.turn_on()
                reading = sensor.get_reading()
                
                if isinstance(sensor, IndoorTemperatureSensor) and reading > TEMP_HIGH:
                    notification = next((actuator for actuator in actuators if isinstance(actuator, NotificationSender)), None)
                    ac = next((actuator for actuator in actuators if isinstance(actuator, AC)), None)
                    
                    if notification:
                        notification.turn_on()
                        notification.notification_sender("Xiaog is too hot")
                    
                    if ac:
                        ac.turn_on()
                        ac.set_target_temperature(TEMP_HIGH)
                        ac.adjust_temperature(reading)
                
                if isinstance(sensor, HumiditySensor) and reading < HUMIDITY_LOW:
                    notification = next((actuator for actuator in actuators if isinstance(actuator, NotificationSender)), None)
                    humidifier = next((actuator for actuator in actuators if isinstance(actuator, Humidifier)), None)
                    
                    if notification:
                        notification.turn_on()
                        notification.notification_sender("Little G is too dry")
                    
                    if humidifier:
                        humidifier.turn_on()
                        humidifier.increase_humidity()
                
                if isinstance(sensor, LightIntensiveSensor) and reading < LIGHT_INTENSITY_LOW:
                    notification = next((actuator for actuator in actuators if isinstance(actuator, NotificationSender)), None)
                    light = next((actuator for actuator in actuators if isinstance(actuator, Light)), None)
                    
                    if notification:
                        notification.turn_on()
                        notification.notification_sender("Little G is too dark")
                    
                    if light:
                        light.turn_on()
                        light.set_brightness_level("high")

if __name__ == "__main__":
    main()