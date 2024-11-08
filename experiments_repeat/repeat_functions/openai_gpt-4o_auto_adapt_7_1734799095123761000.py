# To create the `function.py` file that meets your requirements, let's define a main function that utilizes the provided components from your project. This main function will simulate the smart home environment, focusing on temperature, humidity, and light intensity as mentioned in the functional description. 
# 
# Here's a proposed implementation for the `function.py`:
# 
# ```python
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Light, NotificationSender
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW

def main():
    # Generate the home plan
    home = home_plan()
    
    # Iterate through each room to perform actions based on sensor readings
    for room in home:
        print(f"Checking room: {room.name}")
        
        # Get sensors and actuators in the current room
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)
        
        # Initialize actuators
        ac = next((a for a in actuators if isinstance(a, AC)), None)
        heater = next((a for a in actuators if isinstance(a, Heater)), None)
        humidifier = next((a for a in actuators if isinstance(a, Humidifier)), None)
        light = next((a for a in actuators if isinstance(a, Light)), None)
        notification_sender = next((a for a in actuators if isinstance(a, NotificationSender)), None)
        
        # Turn on actuators for this session
        if notification_sender:
            notification_sender.turn_on()
        
        # Check the sensors and take actions
        for sensor in sensors:
            sensor.turn_on()
            reading = sensor.get_reading()
            
            if isinstance(sensor, IndoorTemperatureSensor):
                if reading > TEMP_HIGH:
                    if ac:
                        ac.set_target_temperature(TEMP_HIGH)
                        ac.adjust_temperature(reading)
                    if notification_sender:
                        notification_sender.notification_sender("屋里太热了")
                elif reading < TEMP_LOW:
                    if heater:
                        heater.set_target_temperature(TEMP_LOW)
                        heater.adjust_temperature(reading)

            elif isinstance(sensor, HumiditySensor):
                if reading < HUMIDITY_LOW:
                    if humidifier:
                        humidifier.turn_on()
                        humidifier.increase_humidity()
                    if notification_sender:
                        notification_sender.notification_sender("屋里有点干")
                elif reading > HUMIDITY_HIGH:
                    if humidifier:
                        humidifier.turn_on()
                        humidifier.decrease_humidity()

            elif isinstance(sensor, LightIntensiveSensor):
                if reading < LIGHT_INTENSITY_LOW:
                    if light:
                        light.turn_on()
                        light.set_brightness_level("high")
                    if notification_sender:
                        notification_sender.notification_sender("屋里太暗了")

            # Turn off the sensor after use
            sensor.turn_off()

    print("Finished checking all rooms.")

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# - The script imports necessary components from your project.
# - It defines a `main()` function that:
#   - Creates a home plan using `home_plan()`.
#   - Iterates through each room in the home, checking sensors and adjusting actuators accordingly.
#   - Utilizes predefined configuration thresholds for temperature, humidity, and light intensity.
#   - Sends notifications if conditions are met (e.g., "屋里太热了" when the room is too hot).
# - The main function is executed when the script is run directly.
# 
# Ensure that the `functions` folder exists and save this script as `function.py` within that folder. Adjust paths and module imports as necessary to fit your project's structure.