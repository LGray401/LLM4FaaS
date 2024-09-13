# import unittest
# from unittest.mock import patch
# from home.actuator import Actuator
# from home.sensor import Sensor
#
#
# class TestActuator(unittest.TestCase):
#     def setUp(self):
#         self.actuator = Actuator("TestActuator", "TestRoom")
#
#     def test_turn_on(self):
#         self.actuator.turn_on()
#         self.assertEqual(self.actuator.status, "on")
#
#     def test_turn_off(self):
#         self.actuator.turn_off()
#         self.assertEqual(self.actuator.status, "off")
#
#
# class TestSensor(unittest.TestCase):
#     def setUp(self):
#         self.sensor = Sensor("TestSensor", "TestRoom")
#
#     @patch.object(Sensor, '_generate_reading')
#     def test_get_reading(self, mock_generate_reading):
#         mock_generate_reading.return_value = 10
#         self.sensor.turn_on()
#         self.assertEqual(self.sensor.get_reading(), 10)
#
#     def test_get_reading_when_off(self):
#         self.sensor.turn_off()
#         self.assertIsNone(self.sensor.get_reading())
#
#
# if __name__ == '__main__':
#     unittest.main()
