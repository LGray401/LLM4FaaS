# Sure! I have created the 'function.py' file based on your provided functional description and code files. Please find the code below:

from home.home_plan import home_plan, get_room_actuators, get_room_sensors, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH


def main():
    # Get home plan
    home = home_plan()

    # Get required sensors and actuators
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    window_actuators = get_all_actuators(home, "Window")
    door_actuators = get_all_actuators(home, "Door")
    ac_actuators = get_all_actuators(home, "AC")

    # Check if AC needs to be turned on based on temperature readings
    for indoor_sensor in indoor_temp_sensors:
        indoor_temp = indoor_sensor.get_reading()
        outdoor_temp = outdoor_temp_sensors[0].get_reading()  # Assuming there is only one outdoor temperature sensor

        if indoor_temp is not None and outdoor_temp is not None:
            if indoor_temp > TEMP_HIGH and outdoor_temp < TEMP_LOW:
                # Ask user to open window to cool down the room
                user_input = input("Room temperature is high. Do you want to open the window to cool down the room? (y/n)")

                if user_input.lower() == "y":
                    # Open the window
                    for window in window_actuators:
                        window.turn_on()
                    break

            elif indoor_temp < TEMP_LOW and outdoor_temp > TEMP_HIGH:
                # Ask user to close window to warm up the room
                user_input = input("Room temperature is low. Do you want to close the window to warm up the room? (y/n)")

                if user_input.lower() == "y":
                    # Close the window
                    for window in window_actuators:
                        window.turn_off()
                    break

    # Check if window and door should be closed when AC is turned on
    for ac in ac_actuators:
        ac_status = ac.get_status()

        if ac_status == "on":
            for window in window_actuators:
                window.turn_off()
            
            for door in door_actuators:
                door.lock()
                
            break

    # Check if window and door should be open when AC is turned off
    for ac in ac_actuators:
        ac_status = ac.get_status()

        if ac_status == "off":
            for window in window_actuators:
                window.turn_on()
            
            for door in door_actuators:
                door.unlock()
                
            break


if __name__ == "__main__":
    main()