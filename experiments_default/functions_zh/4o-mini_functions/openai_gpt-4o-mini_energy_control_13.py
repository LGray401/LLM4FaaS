# Based on your functional description and the provided source code for your smart home project, I will create a `function.py` file that implements the required functionality. The main function will control the logic for turning off lights, sockets, heating, and air conditioning based on sensor readings and the conditions you described.
# 
# Here's the `function.py` code:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def manage_smart_home(home):
    for room in home:
        # Get the sensors and actuators for the room
        light_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"]
        temperature_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"]
        outdoor_temperature_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "OutdoorTemperature"]
        lights = [actuator for actuator in room.actuators if actuator.actuator_type == "Light"]
        smart_sockets = [actuator for actuator in room.actuators if actuator.actuator_type == "SmartSocket"]
        heaters = [actuator for actuator in room.actuators if actuator.actuator_type == "Heater"]
        ac_units = [actuator for actuator in room.actuators if actuator.actuator_type == "AC"]

        # Manage lights based on light intensity
        for light_sensor in light_sensors:
            light_reading = light_sensor.get_reading()
            if light_reading is not None:
                if light_reading < LIGHT_INTENSITY_LOW:
                    for light in lights:
                        light.turn_on()
                else:
                    for light in lights:
                        light.turn_off()

        # Manage smart sockets based on power usage
        for socket in smart_sockets:
            socket_status = socket.get_status()
            if socket_status == "on":
                # Assume some logic here to determine if the socket should be off
                # For example, if no devices are plugged in or not in use
                socket.turn_off()

        # Manage heating and cooling based on indoor and outdoor temperatures
        for temp_sensor in temperature_sensors:
            indoor_temp = temp_sensor.get_reading()
            for outdoor_temp_sensor in outdoor_temperature_sensors:
                outdoor_temp = outdoor_temp_sensor.get_reading()
                if indoor_temp is not None:
                    if indoor_temp < TEMP_LOW:
                        for heater in heaters:
                            heater.turn_on()
                    elif indoor_temp > TEMP_HIGH:
                        for ac in ac_units:
                            ac.turn_on()
                    else:
                        for heater in heaters:
                            heater.turn_off()
                        for ac in ac_units:
                            ac.turn_off()

def main():
    logger.info("Starting smart home management.")
    home = home_plan()
    manage_smart_home(home)

if __name__ == "__main__":
    main()