# Based on your functional description and the provided source code files, I'll create a `function.py` file that will contain a main function to monitor the sensors and activate the corresponding actuators when certain thresholds are met.
# 
# ### Required Logic
# 1. Monitor the temperature, humidity, and light intensity.
# 2. If the temperature is too high (greater than `TEMP_HIGH`), turn on the AC.
# 3. If the temperature is too low (less than `TEMP_LOW`), turn on the heater.
# 4. If humidity is too low (less than `HUMIDITY_LOW`), turn on the humidifier.
# 5. If light intensity is too high (greater than `LIGHT_INTENSITY_HIGH`), turn off the lights.
# 6. If any of these conditions are met, send a notification.
# 
# ### `function.py` Implementation
# Here's how the `function.py` file will look:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH
from home.actuator import AC, Heater, Humidifier, NotificationSender, Light

def monitor_home_conditions():
    home = home_plan()
    
    # Assume we are monitoring the "LivingRoom"
    room_name = "LivingRoom"
    room = next((r for r in home if r.name == room_name), None)
    
    if room is None:
        print(f"Room '{room_name}' not found.")
        return

    # Get sensors from the room
    temperature_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"]
    humidity_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"]
    light_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"]
    
    # Get actuators from the room
    ac = next((actuator for actuator in room.actuators if isinstance(actuator, AC)), None)
    heater = next((actuator for actuator in room.actuators if isinstance(actuator, Heater)), None)
    humidifier = next((actuator for actuator in room.actuators if isinstance(actuator, Humidifier)), None)
    lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
    notification_sender = next((actuator for actuator in room.actuators if isinstance(actuator, NotificationSender)), None)

    # Monitor readings
    for temperature_sensor in temperature_sensors:
        current_temp = temperature_sensor.get_reading()
        if current_temp is not None:
            if current_temp > TEMP_HIGH:
                if ac:
                    ac.turn_on()
                    notification_sender.notification_sender("Temperature is too high! AC turned ON.")
            elif current_temp < TEMP_LOW:
                if heater:
                    heater.turn_on()
                    notification_sender.notification_sender("Temperature is too low! Heater turned ON.")

    for humidity_sensor in humidity_sensors:
        current_humidity = humidity_sensor.get_reading()
        if current_humidity is not None:
            if current_humidity < HUMIDITY_LOW:
                if humidifier:
                    humidifier.increase_humidity()
                    notification_sender.notification_sender("Humidity is too low! Humidifier turned ON.")

    for light_sensor in light_sensors:
        current_light = light_sensor.get_reading()
        if current_light is not None:
            if current_light > LIGHT_INTENSITY_HIGH:
                for light in lights:
                    light.turn_off()
                notification_sender.notification_sender("Light intensity is too high! Lights turned OFF.")

def main():
    monitor_home_conditions()

if __name__ == "__main__":
    main()