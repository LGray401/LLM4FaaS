# Based on the functional description and the provided source code, we can create the `function.py` file. The main function will utilize the sensors and actuators to simulate a smart home environment where temperature, humidity, and light intensity are monitored and controlled.
# 
# Here's how the `function.py` could look:

# functions/function.py

from home.home_plan import home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light, NotificationSender

def main():
    # Create home plan
    home = home_plan()
    
    # Get the Living Room for demonstration
    living_room = next((room for room in home if room.name == "LivingRoom"), None)

    if living_room is None:
        print("Living Room not found!")
        return

    # Get sensors and actuators
    temperature_sensor = next((sensor for sensor in living_room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
    humidity_sensor = next((sensor for sensor in living_room.sensors if isinstance(sensor, HumiditySensor)), None)
    light_sensor = next((sensor for sensor in living_room.sensors if isinstance(sensor, LightIntensiveSensor)), None)

    heater = next((actuator for actuator in living_room.actuators if isinstance(actuator, Heater)), None)
    ac = next((actuator for actuator in living_room.actuators if isinstance(actuator, AC)), None)
    light = next((actuator for actuator in living_room.actuators if isinstance(actuator, Light)), None)
    notification_sender = next((actuator for actuator in living_room.actuators if isinstance(actuator, NotificationSender)), None)

    # Start monitoring and controlling
    if temperature_sensor and humidity_sensor and light_sensor and heater and ac and light and notification_sender:
        # Turn on sensors
        temperature_sensor.turn_on()
        humidity_sensor.turn_on()
        light_sensor.turn_on()

        # Set target temperatures for heater and AC
        heater.set_target_temperature(27)  # Target temperature for heater
        ac.set_target_temperature(27)       # Target temperature for AC

        # Example loop to monitor and control the environment
        for _ in range(5):  # Simulate 5 cycles of monitoring
            current_temperature = temperature_sensor.get_reading()
            current_humidity = humidity_sensor.get_reading()
            current_light = light_sensor.get_reading()

            # Control logic for heater and AC based on readings
            if current_temperature is not None:
                heater.adjust_temperature(current_temperature)
                ac.adjust_temperature(current_temperature)

            # Notify if humidity is outside desired range
            if current_humidity is not None:
                if current_humidity < 30:
                    notification_sender.notification_sender("Humidity is too low!")
                elif current_humidity > 50:
                    notification_sender.notification_sender("Humidity is too high!")

            # Control light based on light intensity
            if current_light is not None:
                if current_light < 300:
                    light.turn_on()
                else:
                    light.turn_off()

        # Turn off sensors after monitoring
        temperature_sensor.turn_off()
        humidity_sensor.turn_off()
        light_sensor.turn_off()

    else:
        print("Failed to get all required sensors and actuators.")

if __name__ == "__main__":
    main()