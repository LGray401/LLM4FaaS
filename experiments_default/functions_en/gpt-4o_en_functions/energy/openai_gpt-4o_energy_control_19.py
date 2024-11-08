# Based on the functional description and the source code provided, I'll create a `function.py` file that will reside in the `functions` folder. This file will contain a `main` function that integrates the described energy-saving mode logic. The `main` function will also provide the necessary logic to interact with the sensors and actuators defined in the provided code.
# 
# Here's how the `function.py` file might look:

import time
from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.actuator import AC, Window, NotificationSender
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH

def energy_saving_mode(home):
    """
    Energy-saving mode logic:
    - Automatically check if AC and window are both on, and prompt the user to turn off one.
    - Automatically adjust indoor conditions based on outdoor conditions.
    """
    # Retrieve all ACs and Windows
    acs = get_all_actuators(home, "AC")
    windows = get_all_actuators(home, "Window")
    notification_senders = get_all_actuators(home, "NotificationSender")

    # Check if any AC and window are both on in the same room
    for ac in acs:
        for window in windows:
            if ac.room_name == window.room_name and ac.get_status() == "on" and window.get_status() == "on":
                notification_sender = next((n for n in notification_senders if n.room_name == ac.room_name), None)
                if notification_sender:
                    notification_sender.turn_on()
                    notification_sender.notification_sender(f"AC and window are both on in {ac.room_name}. Would you like to turn off the AC?")
                    # Simulate user response
                    user_response = "yes"  # Change this based on actual user response
                    if user_response.lower() == "yes":
                        ac.turn_off()
                    notification_sender.turn_off()
    
    # Adjust indoor conditions based on outdoor conditions
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")

    for indoor_temp_sensor in indoor_temp_sensors:
        outdoor_temp_sensor = next((s for s in outdoor_temp_sensors if s.room_name == indoor_temp_sensor.room_name), None)
        humidity_sensor = next((s for s in humidity_sensors if s.room_name == indoor_temp_sensor.room_name), None)
        if indoor_temp_sensor and outdoor_temp_sensor and humidity_sensor:
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()
            humidity = humidity_sensor.get_reading()
            ac = next((a for a in acs if a.room_name == indoor_temp_sensor.room_name), None)
            window = next((w for w in windows if w.room_name == indoor_temp_sensor.room_name), None)
            if ac and window:
                if indoor_temp > TEMP_HIGH and outdoor_temp < indoor_temp:
                    window.turn_on()
                    ac.turn_off()
                elif indoor_temp < TEMP_LOW and outdoor_temp > indoor_temp:
                    window.turn_off()
                    ac.turn_on()
                elif humidity < HUMIDITY_LOW:
                    # Handle low humidity
                    pass
                elif humidity > HUMIDITY_HIGH:
                    # Handle high humidity
                    pass

def main():
    home = home_plan()
    energy_saving_mode(home)

if __name__ == "__main__":
    main()