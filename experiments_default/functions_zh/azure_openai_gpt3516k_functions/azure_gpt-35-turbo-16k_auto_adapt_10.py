# Sure, here is the 'function.py' file based on your given functional description and the source code files provided:

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import NotificationSender, Light

def main():
    # Create sensor objects
    indoor_temp_sensor = IndoorTemperatureSensor("LivingRoom")
    humidity_sensor = HumiditySensor("LivingRoom")
    light_sensor = LightIntensiveSensor("LivingRoom")

    # Get sensor readings
    indoor_temp = indoor_temp_sensor.get_reading()
    humidity = humidity_sensor.get_reading()
    light_intensity = light_sensor.get_reading()

    # Print the sensor readings
    print("Temperature:", indoor_temp, "°C")
    print("Humidity:", humidity)
    print("Light Intensity:", light_intensity)

    # Create actuator objects
    notification_sender = NotificationSender("LivingRoom")
    light = Light("LivingRoom")

    # Send notification based on temperature and humidity
    if indoor_temp < 20:
        notification_sender.notification_sender("Temperature is too low!")
    elif indoor_temp > 30:
        notification_sender.notification_sender("Temperature is too high!")

    if humidity < 40:
        notification_sender.notification_sender("Humidity is too low!")
    elif humidity > 60:
        notification_sender.notification_sender("Humidity is too high!")

    # Adjust the light intensity based on the current light intensity
    if light_intensity < 500:
        light.set_brightness_level("low")
    elif light_intensity < 800:
        light.set_brightness_level("medium")
    else:
        light.set_brightness_level("high")

if __name__ == "__main__":
    main()