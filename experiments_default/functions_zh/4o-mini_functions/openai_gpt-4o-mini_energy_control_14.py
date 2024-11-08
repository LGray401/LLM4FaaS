# Based on your functional description and the provided source code, I'll create the `function.py` file for your smart home project. This file will include a main function that initiates the environmental protection plan and coordinates the operation of sensors and actuators.
# 
# Here's the `function.py` file:

# function.py
from home.home_plan import home_plan
from home.logger_config import logger
import time

def environmental_protection_plan():
    # Initialize home setup
    home = home_plan()
    
    logger.info("Starting the Environmental Protection Plan...")

    # Example operation: Check and react to sensor readings
    for room in home:
        print(f"\n--- Monitoring Room: {room.name} ---")
        
        # Get all sensors in the room
        sensors = room.sensors
        for sensor in sensors:
            sensor.turn_on()
            reading = sensor.get_reading()
            if reading is not None:
                # Example logic based on sensor readings
                if isinstance(sensor, IndoorTemperatureSensor) and reading < 20:
                    # If it's cold, turn on the heater
                    heater = next((act for act in room.actuators if isinstance(act, Heater)), None)
                    if heater:
                        heater.set_target_temperature(22)
                        heater.adjust_temperature(reading)

                elif isinstance(sensor, HumiditySensor) and reading < 40:
                    # If humidity is low, turn on the humidifier
                    humidifier = next((act for act in room.actuators if isinstance(act, Humidifier)), None)
                    if humidifier:
                        humidifier.increase_humidity()
                
                elif isinstance(sensor, LightIntensiveSensor) and reading < 500:
                    # If light intensity is low, turn on the lights
                    lights = [act for act in room.actuators if isinstance(act, Light)]
                    for light in lights:
                        light.turn_on()
                        light.set_brightness_level('medium')

            sensor.turn_off()

        # After monitoring all sensors, send a notification
        notification_sender = next((act for act in room.actuators if isinstance(act, NotificationSender)), None)
        if notification_sender:
            notification_sender.turn_on()
            notification_sender.notification_sender(f"Monitoring completed for {room.name}.")
            notification_sender.turn_off()

        time.sleep(1)  # Delay between room operations

    logger.info("Environmental Protection Plan completed.")

def main():
    environmental_protection_plan()

if __name__ == "__main__":
    main()