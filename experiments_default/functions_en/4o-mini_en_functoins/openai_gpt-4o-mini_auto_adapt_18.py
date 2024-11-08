# Based on your functional description and the provided source code, I will create the `function.py` file that includes a main function. This function will simulate a basic operation of your smart home system, such as reading values from sensors and adjusting actuators accordingly.
# 
# Here's the content for the `function.py` file:

# function.py

from home.home_plan import home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light, NotificationSender

def main():
    # Create home with rooms and components
    home = home_plan()

    # Example room names
    living_room = "LivingRoom"
    bedroom = "Bedroom"

    # Get sensors and actuators from the living room
    living_room_sensors = get_room_sensors(home, living_room)
    living_room_actuators = get_room_actuators(home, living_room)

    # Simulate readings from the living room sensors
    temperature_sensor = next((s for s in living_room_sensors if isinstance(s, IndoorTemperatureSensor)), None)
    humidity_sensor = next((s for s in living_room_sensors if isinstance(s, HumiditySensor)), None)
    light_sensor = next((s for s in living_room_sensors if isinstance(s, LightIntensiveSensor)), None)

    # Turn on sensors
    if temperature_sensor:
        temperature_sensor.turn_on()
    if humidity_sensor:
        humidity_sensor.turn_on()
    if light_sensor:
        light_sensor.turn_on()

    # Get readings
    temperature = temperature_sensor.get_reading() if temperature_sensor else None
    humidity = humidity_sensor.get_reading() if humidity_sensor else None
    light_intensity = light_sensor.get_reading() if light_sensor else None

    # Print the readings
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Light Intensity: {light_intensity} lux")

    # Control actuators based on readings
    heater = next((a for a in living_room_actuators if isinstance(a, Heater)), None)
    ac = next((a for a in living_room_actuators if isinstance(a, AC)), None)
    humidifier = next((a for a in living_room_actuators if isinstance(a, Humidifier)), None)
    light = next((a for a in living_room_actuators if isinstance(a, Light)), None)
    notification_sender = next((a for a in living_room_actuators if isinstance(a, NotificationSender)), None)

    # Example control logic
    target_temperature = 28  # Set target temperature for the heater/AC
    if temperature is not None:
        if temperature < target_temperature:
            if heater:
                heater.set_target_temperature(target_temperature)
                heater.adjust_temperature(temperature)
        elif temperature > target_temperature:
            if ac:
                ac.set_target_temperature(target_temperature)
                ac.adjust_temperature(temperature)

    # Example humidity adjustment
    if humidity is not None:
        if humidity < 30:  # Threshold for humidity
            if humidifier:
                humidifier.increase_humidity()
        elif humidity > 50:  # Threshold for humidity
            if humidifier:
                humidifier.decrease_humidity()

    # Control lights based on light intensity
    if light_intensity is not None:
        if light_intensity < 300:  # Threshold for light intensity
            if light:
                light.turn_on()
        else:
            if light:
                light.turn_off()

    # Send a notification about the status
    if notification_sender:
        notification_sender.turn_on()
        message = f"Current readings - Temperature: {temperature}°C, Humidity: {humidity}%, Light Intensity: {light_intensity} lux"
        notification_sender.notification_sender(message)

if __name__ == "__main__":
    main()