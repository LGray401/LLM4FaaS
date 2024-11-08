from home.home_plan import home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import Heater, AC, CoffeeMachine, Light, SmartTV, Humidifier, CleaningRobot
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    DAILY_ROUTINE_DURATION
from home.logger_config import logger

def adjust_temperature(home):
    """
    Adjusts the temperature of rooms based on sensor readings and user preferences.
    """
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")

    for sensor in indoor_temp_sensors:
        temperature = sensor.get_reading()
        if temperature is not None:
            for heater in heaters:
                if sensor.room_name == heater.room_name:
                    heater.adjust_temperature(temperature)
            for ac in acs:
                if sensor.room_name == ac.room_name:
                    ac.adjust_temperature(temperature)

def adjust_humidity(home):
    """
    Adjusts the humidity of rooms based on sensor readings and user preferences.
    """
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in humidity_sensors:
        humidity = sensor.get_reading()
        if humidity is not None:
            for humidifier in humidifiers:
                if sensor.room_name == humidifier.room_name:
                    if humidity < HUMIDITY_LOW:
                        humidifier.increase_humidity()
                    elif humidity > HUMIDITY_HIGH:
                        humidifier.decrease_humidity()

def adjust_light_intensity(home):
    """
    Adjusts the light intensity of rooms based on sensor readings and user preferences.
    """
    light_intensive_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")

    for sensor in light_intensive_sensors:
        light_intensity = sensor.get_reading()
        if light_intensity is not None:
            for light in lights:
                if sensor.room_name == light.room_name:
                    if light_intensity < LIGHT_INTENSITY_LOW:
                        light.turn_on()
                        light.set_brightness_level("high")
                    elif light_intensity > LIGHT_INTENSITY_HIGH:
                        light.turn_off()
                        # Optionally, set a lower brightness level if needed
                        # light.set_brightness_level("medium")

def trigger_cleaning_robot(home):
    """
    Triggers the cleaning robot for daily cleaning routine.
    """
    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    for robot in cleaning_robots:
        robot.daily_routine()

def manage_coffee_machine(home):
    """
    Manages the coffee machine based on user preferences.
    """
    coffee_machines = get_all_actuators(home, "CoffeeMachine")
    for machine in coffee_machines:
        # Example: Check if user preferences trigger coffee making
        # if user_preference_for_coffee:
        #     machine.make_coffee("Espresso")

def manage_smart_tv(home):
    """
    Manages the smart TV based on user preferences.
    """
    smart_tvs = get_all_actuators(home, "SmartTV")
    for tv in smart_tvs:
        # Example: Check if user preferences trigger TV channel change
        # if user_preference_for_channel:
        #     tv.play_channel("News Channel")

def main():
    """
    Main function that orchestrates the smart home system.
    """
    home = home_plan()

    while True:
        adjust_temperature(home)
        adjust_humidity(home)
        adjust_light_intensity(home)
        trigger_cleaning_robot(home)
        manage_coffee_machine(home)
        manage_smart_tv(home)

        # Add other functionalities or logic as needed
        logger.info(format("Smart home system is running"))
        # Wait for a specific time interval or event to occur
        time.sleep(1) # Replace 1 with your desired interval

if __name__ == "__main__":
    main()
