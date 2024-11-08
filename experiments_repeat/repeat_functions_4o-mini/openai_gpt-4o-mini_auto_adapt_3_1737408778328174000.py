# Based on your functional description and the provided source code, I'll create a `function.py` file that integrates the sensors and actuators to monitor temperature, humidity, and light intensity in a smart home setup. The main function will gather readings from the sensors and control the actuators accordingly.
# 
# Here’s the content for the `function.py` file:
# 
# ```python
# function.py
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.actuator import Heater, AC, Humidifier, Light, NotificationSender


def monitor_home_conditions(home):
    for room in home:
        print(f"\nMonitoring conditions in {room.name}...")
        
        # Get relevant sensors and actuators
        temperature_sensors = room.sensors[0:2]  # Assuming first two are temperature sensors
        humidity_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"]
        light_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"]
        
        # Get readings
        temp_readings = [sensor.get_reading() for sensor in temperature_sensors if sensor.get_status() == "on"]
        humidity_readings = [sensor.get_reading() for sensor in humidity_sensors if sensor.get_status() == "on"]
        light_readings = [sensor.get_reading() for sensor in light_sensors if sensor.get_status() == "on"]

        # Process temperature readings
        if temp_readings:
            avg_temp = sum(temp_readings) / len(temp_readings)
            print(f"Average Temperature: {avg_temp:.2f}°C")
            # Control heater and AC
            for actuator in room.actuators:
                if isinstance(actuator, Heater):
                    actuator.set_target_temperature(TEMP_HIGH)
                    actuator.adjust_temperature(avg_temp)
                elif isinstance(actuator, AC):
                    actuator.set_target_temperature(TEMP_LOW)
                    actuator.adjust_temperature(avg_temp)

        # Process humidity readings
        if humidity_readings:
            avg_humidity = sum(humidity_readings) / len(humidity_readings)
            print(f"Average Humidity: {avg_humidity:.2f}%")
            # Control humidifier
            for actuator in room.actuators:
                if isinstance(actuator, Humidifier):
                    if avg_humidity < HUMIDITY_LOW:
                        actuator.increase_humidity()
                    elif avg_humidity > HUMIDITY_HIGH:
                        actuator.decrease_humidity()

        # Process light readings
        if light_readings:
            avg_light = sum(light_readings) / len(light_readings)
            print(f"Average Light Intensity: {avg_light:.2f} lux")
            # Control lights
            for actuator in room.actuators:
                if isinstance(actuator, Light):
                    if avg_light < LIGHT_INTENSITY_LOW:
                        actuator.turn_on()
                    elif avg_light > LIGHT_INTENSITY_HIGH:
                        actuator.turn_off()

        # Send notification about the room conditions
        notification_sender = next((a for a in room.actuators if isinstance(a, NotificationSender)), None)
        if notification_sender:
            message = f"Room: {room.name}, Avg Temp: {avg_temp:.2f}°C, Avg Humidity: {avg_humidity:.2f}%, Avg Light: {avg_light:.2f} lux"
            notification_sender.notification_sender(message)

def main():
    home = home_plan()  # Create home plan
    monitor_home_conditions(home)  # Monitor and adjust conditions

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# - **`monitor_home_conditions(home)`**: This function goes through each room, retrieves the sensor readings, and adjusts the actuators based on defined thresholds for temperature, humidity, and light intensity.
# - **Main function**: This initializes the home plan and invokes the monitoring function.
# - The code assumes that the sensors and actuators are properly initialized and turned on before monitoring.
# 
# ### File Structure:
# Ensure that you save this file as `function.py` in the `functions` folder of your project.
# 
# Let me know if you need any further adjustments or additional functionalities!