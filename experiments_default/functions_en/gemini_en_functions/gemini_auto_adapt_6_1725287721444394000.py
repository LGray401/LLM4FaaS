from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_CHANGE_DURATION_WINDOW, TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, \
    LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def main():
    home = home_plan()
    # print_home_plan(home)

    # Example usage: Control a light in the LivingRoom
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     living_room_lights = get_room_actuators(home, "LivingRoom")
    #     if living_room_lights:
    #         for light in living_room_lights:
    #             if light.actuator_type == "Light":
    #                 light.turn_on()
    #                 light.set_brightness_level("medium")
    #                 time.sleep(5)
    #                 light.turn_off()

    # Example usage: Get a sensor reading
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     living_room_sensors = get_room_sensors(home, "LivingRoom")
    #     if living_room_sensors:
    #         for sensor in living_room_sensors:
    #             if sensor.sensor_type == "IndoorTemperature":
    #                 sensor.turn_on()
    #                 temperature_reading = sensor.get_reading()
    #                 print(f"Temperature in LivingRoom: {temperature_reading}°C")
    #                 sensor.turn_off()

    # Example usage: Control a smart TV in the LivingRoom
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     living_room_actuators = get_room_actuators(home, "LivingRoom")
    #     if living_room_actuators:
    #         for actuator in living_room_actuators:
    #             if actuator.actuator_type == "SmartTV":
    #                 actuator.turn_on()
    #                 actuator.play_channel("Discovery Channel")
    #                 time.sleep(5)
    #                 actuator.turn_off()

    # Example usage: Control the cleaning robot
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     living_room_actuators = get_room_actuators(home, "LivingRoom")
    #     if living_room_actuators:
    #         for actuator in living_room_actuators:
    #             if actuator.actuator_type == "CleaningRobot":
    #                 actuator.turn_on()
    #                 actuator.daily_routine()

    # Example usage: Get all the lights in the home
    # all_lights = get_all_actuators(home, "Light")
    # if all_lights:
    #     print("All Lights:")
    #     for light in all_lights:
    #         print(light.id)
    #         light.turn_on()
    #         time.sleep(5)
    #         light.turn_off()

    # Example usage: Get all the indoor temperature sensors in the home
    # all_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    # if all_temp_sensors:
    #     print("All Indoor Temperature Sensors:")
    #     for sensor in all_temp_sensors:
    #         print(sensor.id)
    #         sensor.turn_on()
    #         temperature_reading = sensor.get_reading()
    #         print(f"Temperature reading from {sensor.id}: {temperature_reading}°C")
    #         sensor.turn_off()

    # Example usage: Control the AC based on temperature
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     living_room_actuators = get_room_actuators(home, "LivingRoom")
    #     if living_room_actuators:
    #         for actuator in living_room_actuators:
    #             if actuator.actuator_type == "AC":
    #                 ac = actuator
    #     living_room_sensors = get_room_sensors(home, "LivingRoom")
    #     if living_room_sensors:
    #         for sensor in living_room_sensors:
    #             if sensor.sensor_type == "IndoorTemperature":
    #                 temp_sensor = sensor
    #                 temp_sensor.turn_on()
    #                 ac.turn_on()
    #                 while True:
    #                     current_temperature = temp_sensor.get_reading()
    #                     print(f"Current temperature in LivingRoom: {current_temperature}°C")
    #                     if current_temperature > TEMP_HIGH:
    #                         print(f"Turning AC ON - Temperature is above {TEMP_HIGH}°C")
    #                         ac.set_target_temperature(TEMP_HIGH - 1)
    #                         ac.adjust_temperature(current_temperature)
    #                         time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    #                     elif current_temperature < TEMP_LOW:
    #                         print(f"Turning AC OFF - Temperature is below {TEMP_LOW}°C")
    #                         ac.set_target_temperature(TEMP_LOW + 1)
    #                         ac.adjust_temperature(current_temperature)
    #                         time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    #                     else:
    #                         print(f"AC OFF - Temperature is within range ({TEMP_LOW}°C - {TEMP_HIGH}°C)")
    #                         ac.turn_off()
    #                         time.sleep(TEMP_CHANGE_DURATION_WINDOW)

    # Example usage: Control the heater based on temperature
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     living_room_actuators = get_room_actuators(home, "LivingRoom")
    #     if living_room_actuators:
    #         for actuator in living_room_actuators:
    #             if actuator.actuator_type == "Heater":
    #                 heater = actuator
    #     living_room_sensors = get_room_sensors(home, "LivingRoom")
    #     if living_room_sensors:
    #         for sensor in living_room_sensors:
    #             if sensor.sensor_type == "IndoorTemperature":
    #                 temp_sensor = sensor
    #                 temp_sensor.turn_on()
    #                 heater.turn_on()
    #                 while True:
    #                     current_temperature = temp_sensor.get_reading()
    #                     print(f"Current temperature in LivingRoom: {current_temperature}°C")
    #                     if current_temperature < TEMP_LOW:
    #                         print(f"Turning Heater ON - Temperature is below {TEMP_LOW}°C")
    #                         heater.set_target_temperature(TEMP_LOW + 1)
    #                         heater.adjust_temperature(current_temperature)
    #                         time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    #                     elif current_temperature > TEMP_HIGH:
    #                         print(f"Turning Heater OFF - Temperature is above {TEMP_HIGH}°C")
    #                         heater.set_target_temperature(TEMP_HIGH - 1)
    #                         heater.adjust_temperature(current_temperature)
    #                         time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    #                     else:
    #                         print(f"Heater OFF - Temperature is within range ({TEMP_LOW}°C - {TEMP_HIGH}°C)")
    #                         heater.turn_off()
    #                         time.sleep(TEMP_CHANGE_DURATION_WINDOW)

    # Example usage: Control the humidifier based on humidity
    # bathroom = get_room(home, "Bathroom")
    # if bathroom:
    #     bathroom_actuators = get_room_actuators(home, "Bathroom")
    #     if bathroom_actuators:
    #         for actuator in bathroom_actuators:
    #             if actuator.actuator_type == "Humidifier":
    #                 humidifier = actuator
    #     bathroom_sensors = get_room_sensors(home, "Bathroom")
    #     if bathroom_sensors:
    #         for sensor in bathroom_sensors:
    #             if sensor.sensor_type == "Humidity":
    #                 humidity_sensor = sensor
    #                 humidity_sensor.turn_on()
    #                 humidifier.turn_on()
    #                 while True:
    #                     current_humidity = humidity_sensor.get_reading()
    #                     print(f"Current humidity in Bathroom: {current_humidity}%")
    #                     if current_humidity < HUMIDITY_LOW:
    #                         print(f"Turning Humidifier ON - Humidity is below {HUMIDITY_LOW}%")
    #                         humidifier.increase_humidity()
    #                         time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    #                     elif current_humidity > HUMIDITY_HIGH:
    #                         print(f"Turning Humidifier OFF - Humidity is above {HUMIDITY_HIGH}%")
    #                         humidifier.decrease_humidity()
    #                         time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    #                     else:
    #                         print(f"Humidifier OFF - Humidity is within range ({HUMIDITY_LOW}% - {HUMIDITY_HIGH}%)")
    #                         humidifier.turn_off()
    #                         time.sleep(TEMP_CHANGE_DURATION_WINDOW)

    # Example usage: Control the lights based on light intensity
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     living_room_actuators = get_room_actuators(home, "LivingRoom")
    #     if living_room_actuators:
    #         for actuator in living_room_actuators:
    #             if actuator.actuator_type == "Light":
    #                 light = actuator
    #     living_room_sensors = get_room_sensors(home, "LivingRoom")
    #     if living_room_sensors:
    #         for sensor in living_room_sensors:
    #             if sensor.sensor_type == "LightIntensive":
    #                 light_sensor = sensor
    #                 light_sensor.turn_on()
    #                 light.turn_on()
    #                 while True:
    #                     current_light_intensity = light_sensor.get_reading()
    #                     print(f"Current light intensity in LivingRoom: {current_light_intensity} lux")
    #                     if current_light_intensity < LIGHT_INTENSITY_LOW:
    #                         print(f"Turning light ON - Light intensity is below {LIGHT_INTENSITY_LOW} lux")
    #                         light.set_brightness_level("high")
    #                         time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    #                     elif current_light_intensity > LIGHT_INTENSITY_HIGH:
    #                         print(f"Turning light OFF - Light intensity is above {LIGHT_INTENSITY_HIGH} lux")
    #                         light.turn_off()
    #                         time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    #                     else:
    #                         print(f"Light OFF - Light intensity is within range ({LIGHT_INTENSITY_LOW} lux - {LIGHT_INTENSITY_HIGH} lux)")
    #                         light.set_brightness_level("medium")
    #                         time.sleep(TEMP_CHANGE_DURATION_WINDOW)

if __name__ == "__main__":
    main()