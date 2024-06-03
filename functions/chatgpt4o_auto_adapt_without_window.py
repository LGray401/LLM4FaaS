# functions/ensure_comfort.py

from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Curtain, NotificationSender

def ensure_comfort(home):
    for room in home:
        sensors = {type(sensor).__name__: sensor for sensor in room.sensors}
        actuators = {type(actuator).__name__: actuator for actuator in room.actuators}

        # Temperature control
        if 'IndoorTemperatureSensor' in sensors:
            temp_sensor = sensors['IndoorTemperatureSensor']
            temp_sensor.turn_on()
            temp = temp_sensor.get_reading()
            if temp is not None:
                if temp < TEMP_LOW and 'Heater' in actuators:
                    actuators['Heater'].turn_on()
                elif temp > TEMP_HIGH and 'AC' in actuators:
                    actuators['AC'].turn_on()

        # Humidity control
        if 'HumiditySensor' in sensors:
            humidity_sensor = sensors['HumiditySensor']
            humidity_sensor.turn_on()
            humidity = humidity_sensor.get_reading()
            if humidity is not None:
                if humidity < HUMIDITY_LOW and 'Humidifier' in actuators:
                    actuators['Humidifier'].turn_on()
                    actuators['Humidifier'].increase_humidity()
                elif humidity > HUMIDITY_HIGH and 'Humidifier' in actuators:
                    actuators['Humidifier'].turn_on()
                    actuators['Humidifier'].decrease_humidity()

        # Light intensity control
        if 'LightIntensiveSensor' in sensors:
            light_sensor = sensors['LightIntensiveSensor']
            light_sensor.turn_on()
            light_intensity = light_sensor.get_reading()
            if light_intensity is not None:
                if light_intensity < LIGHT_INTENSITY_LOW and 'Curtain' in actuators:
                    actuators['Curtain'].turn_on()
                    print(f"Opening curtain in {room.name} due to low light intensity.")
                elif light_intensity > LIGHT_INTENSITY_HIGH and 'Curtain' in actuators:
                    actuators['Curtain'].turn_off()
                    notification_sender = actuators.get('NotificationSender')
                    if notification_sender:
                        notification_sender.turn_on()
                        notification_sender.notification_sender(f"Curtains in {room.name} were closed due to high light intensity.")

if __name__ == "__main__":
    from home.home_plan import home_plan
    home = home_plan()
    ensure_comfort(home)
