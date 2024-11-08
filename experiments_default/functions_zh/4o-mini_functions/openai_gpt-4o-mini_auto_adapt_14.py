# Based on the functional description and code files you provided, I will create a `function.py` file that will implement a basic control logic for your smart home project. The main function will check the readings from sensors and, based on their values, will send notifications accordingly.
# 
# Here's the `function.py` file:

# function.py
from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW
from home.actuator import NotificationSender

def main():
    # Get the home plan (rooms and their components)
    home = home_plan()

    # Iterate through each room
    for room in home:
        # Get sensors and actuators for the room
        sensors = room.sensors
        actuators = room.actuators
        
        # Initialize notification sender for the room
        notification_sender = next((act for act in actuators if isinstance(act, NotificationSender)), None)
        
        # Check each sensor reading
        for sensor in sensors:
            reading = sensor.get_reading()
            if reading is not None:
                # Temperature sensor logic
                if isinstance(sensor, IndoorTemperatureSensor):
                    if reading > TEMP_HIGH:
                        if notification_sender:
                            notification_sender.turn_on()
                            notification_sender.notification_sender("小g 太热了")
                
                # Humidity sensor logic
                elif isinstance(sensor, HumiditySensor):
                    if reading < HUMIDITY_LOW:
                        if notification_sender:
                            notification_sender.turn_on()
                            notification_sender.notification_sender("小g 太干了")
                
                # Light intensity sensor logic
                elif isinstance(sensor, LightIntensiveSensor):
                    if reading < LIGHT_INTENSITY_LOW:
                        if notification_sender:
                            notification_sender.turn_on()
                            notification_sender.notification_sender("小g 太暗了")

if __name__ == "__main__":
    main()