import random


class Sensor:
    sensor_count = {}  # Dictionary to keep track of sensor count for each room and sensor type

    def __init__(self, sensor_type, room_name):
        if room_name not in Sensor.sensor_count:
            Sensor.sensor_count[room_name] = {}  # Initialize sensor count for the room if not already present
        if sensor_type not in Sensor.sensor_count[room_name]:
            Sensor.sensor_count[room_name][sensor_type] = 0  # Initialize sensor count for the sensor type if not already present

        Sensor.sensor_count[room_name][sensor_type] += 1  # Increment sensor count for the sensor type in the room

        self.id = f"/Sensor/{sensor_type}/{room_name}/{Sensor.sensor_count[room_name][sensor_type]}"
        self.sensor_type = sensor_type
        self.room_name = room_name
        self.status = "off"

    def turn_on(self):
        self.status = "on"
        print(f"{self.sensor_type} sensor '{self.id}' in {self.room_name} is now ON.")

    def turn_off(self):
        self.status = "off"
        print(f"{self.sensor_type} sensor in {self.room_name} is now OFF.")

    def get_reading(self):
        if self.status == "off":
            print(f"{self.sensor_type} sensor in {self.room_name} is currently OFF. Cannot get reading.")
            return None
        else:
            reading = self._generate_reading()
            print(f"{self.sensor_type} reading in {self.room_name}: {reading}")
            return reading

    def get_status(self):
        print(f"{self.sensor_type} sensor in {self.room_name} current status is {self.status}")
        return self.status

    def _generate_reading(self):
        raise NotImplementedError("Subclasses must implement _generate_reading method.")


class IndoorTemperatureSensor(Sensor):
    def __init__(self, room_name):
        super().__init__("IndoorTemperature", room_name)

    def _generate_reading(self):
        return round(random.uniform(25, 40), 2)


class OutdoorTemperatureSensor(Sensor):
    def __init__(self, room_name):
        super().__init__("OutdoorTemperature", room_name)

    def _generate_reading(self):
        return round(random.uniform(0, 40), 2)


class HumiditySensor(Sensor):
    def __init__(self, room_name):
        super().__init__("Humidity", room_name)

    def _generate_reading(self):
        return round(random.uniform(0, 100), 2)


class LightIntensiveSensor(Sensor):
    def __init__(self, room_name):
        super().__init__("LightIntensive", room_name)

    def _generate_reading(self):
        return round(random.uniform(900, 1000), 2)


class SmokeSensor(Sensor):
    def __init__(self, room_name):
        super().__init__("Smoke", room_name)

    def _generate_reading(self):
        return round(random.uniform(0, 100), 2)


# def get_all_sensor_info():
#     for room_name, sensor_types in Sensor.sensor_count.items():
#         print(f"Sensors in {sensor_types}:")
#         for room_name, count in sensor_types.items():
#             for i in range(1, count + 1):
#                 sensor_id = f"{sensor_type}_{room_name}_{i}"
#                 print(f"- {sensor_id}")


if __name__ == "__main__":
    uv_sensor = LightIntensiveSensor("test room")
    print(uv_sensor.get_reading())
    uv_sensor.turn_on()
    print(uv_sensor.get_reading())
