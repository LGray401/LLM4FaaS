# Given the functional description and the provided source code, here is the `function.py` file. This file will contain the main function to control the smart home system. For the sake of brevity, I'll assume "控制" translates to "control" and that the main function will involve initializing the home plan and performing some basic operations.

# functions/function.py
from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, TEMP_CHANGE_DURATION_WINDOW
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, OutdoorTemperatureSensor
from home.actuator import Heater, AC, Humidifier, Light, Window, NotificationSender

def control_home():
    # Initialize home plan
    home = home_plan()
    print_home_plan(home)

    # Example control logic
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Check temperature and adjust Heater or AC
        temp_sensors = [sensor for sensor in living_room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
        if temp_sensors:
            temp_sensor = temp_sensors[0]
            temp_sensor.turn_on()
            current_temp = temp_sensor.get_reading()
            heaters = [actuator for actuator in living_room.actuators if isinstance(actuator, Heater)]
            ac_units = [actuator for actuator in living_room.actuators if isinstance(actuator, AC)]
            if current_temp < TEMP_LOW and heaters:
                heater = heaters[0]
                heater.set_target_temperature(TEMP_HIGH)
                heater.turn_on()
            elif current_temp > TEMP_HIGH and ac_units:
                ac = ac_units[0]
                ac.set_target_temperature(TEMP_LOW)
                ac.turn_on()

        # Check humidity and adjust Humidifier
        humidity_sensors = [sensor for sensor in living_room.sensors if isinstance(sensor, HumiditySensor)]
        if humidity_sensors:
            humidity_sensor = humidity_sensors[0]
            humidity_sensor.turn_on()
            current_humidity = humidity_sensor.get_reading()
            humidifiers = [actuator for actuator in living_room.actuators if isinstance(actuator, Humidifier)]
            if current_humidity < HUMIDITY_LOW and humidifiers:
                humidifier = humidifiers[0]
                humidifier.turn_on()
                humidifier.increase_humidity()
            elif current_humidity > HUMIDITY_HIGH and humidifiers:
                humidifier = humidifiers[0]
                humidifier.turn_on()
                humidifier.decrease_humidity()

        # Check light intensity and adjust Light
        light_sensors = [sensor for sensor in living_room.sensors if isinstance(sensor, LightIntensiveSensor)]
        if light_sensors:
            light_sensor = light_sensors[0]
            light_sensor.turn_on()
            current_light_intensity = light_sensor.get_reading()
            lights = [actuator for actuator in living_room.actuators if isinstance(actuator, Light)]
            if current_light_intensity < LIGHT_INTENSITY_LOW and lights:
                light = lights[0]
                light.turn_on()
                light.set_brightness_level("high")
            elif current_light_intensity > LIGHT_INTENSITY_HIGH and lights:
                light = lights[0]
                light.turn_off()

    # Example notification
    notification_senders = [actuator for actuator in living_room.actuators if isinstance(actuator, NotificationSender)]
    if notification_senders:
        notification_sender = notification_senders[0]
        notification_sender.turn_on()
        notification_sender.notification_sender("Control operations completed.")

if __name__ == "__main__":
    control_home()