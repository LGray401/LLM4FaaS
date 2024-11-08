# Based on the functional description and the provided source code, here's a `function.py` file that contains the main function to automate the smart home operations as described:

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.sensor import LightIntensiveSensor
from home.actuator import Light, Heater, AC, Window, Door
import home.config as config

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Get all relevant sensors and actuators
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    windows = get_all_actuators(home, "Window")
    doors = get_all_actuators(home, "Door")
    
    # Turn off lights when not needed
    for sensor in light_sensors:
        if sensor.get_status() == "on":
            reading = sensor.get_reading()
            if reading and reading < config.LIGHT_INTENSITY_LOW:
                for light in lights:
                    if light.room_name == sensor.room_name and light.status == "on":
                        light.turn_off()
    
    # Turn off sockets when not in use (assuming all sockets are SmartSockets and should be off when no device is using them)
    # This may need additional logic to determine actual usage, for now, turning them off as default behavior
    smart_sockets = get_all_actuators(home, "SmartSocket")
    for socket in smart_sockets:
        socket.turn_off()
    
    # Manage indoor temperature
    for heater in heaters:
        indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
        for sensor in indoor_temp_sensors:
            if sensor.room_name == heater.room_name:
                reading = sensor.get_reading()
                if reading and reading >= config.TEMP_LOW:
                    heater.turn_off()
    
    for ac in acs:
        indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
        for sensor in indoor_temp_sensors:
            if sensor.room_name == ac.room_name:
                reading = sensor.get_reading()
                if reading and reading <= config.TEMP_HIGH:
                    ac.turn_off()
    
    # Open windows for ventilation if temperature allows
    for window in windows:
        outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
        for sensor in outdoor_temp_sensors:
            # Assuming all outdoor sensors are in the same "general" area, using the first one found
            reading = sensor.get_reading()
            if reading and reading < config.TEMP_HIGH:
                window.turn_on()  # Open window (turn_on represents open in this context)
            else:
                window.turn_off()  # Close window (turn_off represents close in this context)
    
    # Check if AC should be on and windows/doors are closed
    for ac in acs:
        indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
        for sensor in indoor_temp_sensors:
            if sensor.room_name == ac.room_name:
                reading = sensor.get_reading()
                if reading and reading > config.TEMP_HIGH:
                    ac.turn_on()
                    # Ensure windows and doors are closed
                    for window in windows:
                        if window.room_name == ac.room_name and window.status == "on":
                            window.turn_off()
                    for door in doors:
                        if door.room_name == ac.room_name and door.status != "locked":  # Assuming locked means closed
                            door.lock()
    
    # Additional logic could be added here for other automation scenarios
    
if __name__ == "__main__":
    main()