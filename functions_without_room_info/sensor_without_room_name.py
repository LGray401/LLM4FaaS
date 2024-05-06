import random


class Sensor:
    sensor_count = 0  # Class variable to keep track of sensor count

    def __init__(self, sensor_type):
        # e.g. a temperature sensor's type is 'temperature'
        self.sensor_type = sensor_type
        self.status = "off"

    def turn_on(self):
        self.status = "on"
        print(f"{self.sensor_type} sensor is now ON.")

    def turn_off(self):
        self.status = "off"
        print(f"{self.sensor_type} sensor is now OFF.")

    def get_reading(self):
        if self.status == "off":
            print(f"{self.sensor_type} sensor is currently OFF. Cannot get reading.")
            return None
        else:
            reading = self._generate_reading()
            print(f"{self.sensor_type} reading: {reading}")
            return reading

    def get_status(self):
        print(f"{self.sensor_type} current status is " f"{self.status}")
        return self.status

    def _generate_reading(self):
        raise NotImplementedError("Subclasses must implement _generate_reading method.")

# temperature can be negative as well.
class IndoorTemperatureSensor(Sensor):
    def __init__(self):
        super().__init__("IndoorTemperature")

    def _generate_reading(self):
        return round(random.uniform(35, 40), 2)


class OutdoorTemperatureSensor(Sensor):
    def __init__(self):
        super().__init__("OutdoorTemperature")

    def _generate_reading(self):
        return round(random.uniform(10, 12), 2)


class HumiditySensor(Sensor):
    def __init__(self):
        super().__init__("Humidity")

    def _generate_reading(self):
        return round(random.uniform(0, 100), 2)


class UVSensor(Sensor):
    def __init__(self):
        super().__init__("UV")

    def _generate_reading(self):
        return round(random.uniform(0, 1000), 2)

    # def is_light_too_bright(self, threshold=800):
    #     reading = self.get_reading()
    #     if reading is not None and reading > threshold:
    #         print("Warning: Light intensity is too high!")


class SmokeSensor(Sensor):
    def __init__(self):
        super().__init__("Humidity")

    # todo: correct range of the reading
    def _generate_reading(self):
        return round(random.uniform(0, 100), 2)


# Testing the Sensor classes
if __name__ == "__main__":
    sensors = [IndoorTemperatureSensor(), OutdoorTemperatureSensor(), HumiditySensor(), UVSensor()]

    for sensor in sensors:
        sensor.get_status()

    # Turn on sensors
    for sensor in sensors:
        sensor.turn_on()

    # Get readings from all sensors
    for sensor in sensors:
        sensor.get_reading()

    # Turn off sensors
    for sensor in sensors:
        sensor.turn_off()

    # Try to get readings when sensors are off
    for sensor in sensors:
        sensor.get_reading()

    # Special functionality for UVSensor
    uv_sensor = UVSensor()
    uv_sensor.turn_on()
    uv_sensor.is_light_too_bright()
