# Below is the `function.py` file that adheres to your functional description. It will automatically close doors and windows when the air conditioner (AC) is on, and ask whether to open windows to cool down when the indoor temperature is high and the outdoor temperature is low.
# 
# ## `function.py`

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW, TEMP_CHANGE_DURATION_WINDOW
import time

def main():
    # Create home plan
    home = home_plan()
    
    # Get all ACs, Doors, and Windows in the home
    acs = get_all_actuators(home, "AC")
    doors = get_all_actuators(home, "Door")
    windows = get_all_actuators(home, "Window")
    
    # Get all Indoor and Outdoor temperature sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")

    while True:
        for ac in acs:
            ac_status = ac.get_status()
            if ac_status == "on":
                # Close all doors and windows if AC is on
                for door in doors:
                    door.lock()
                for window in windows:
                    window.turn_off()
            else:
                # Check temperature readings
                for indoor_sensor in indoor_temp_sensors:
                    indoor_temp = indoor_sensor.get_reading()
                    if indoor_temp and indoor_temp > TEMP_HIGH:
                        for outdoor_sensor in outdoor_temp_sensors:
                            outdoor_temp = outdoor_sensor.get_reading()
                            if outdoor_temp and outdoor_temp < TEMP_LOW:
                                # Send notification to open windows to cool down
                                notification_senders = get_all_actuators(home, "NotificationSender")
                                for notifier in notification_senders:
                                    notifier.turn_on()
                                    notifier.notification_sender(
                                        "Indoor temperature is high and outdoor temperature is low. "
                                        "Would you like to open windows to cool down?"
                                    )
                                    notifier.turn_off()

        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

if __name__ == "__main__":
    main()