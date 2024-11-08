# Based on the content of the markdown file, you are working on a smart home project and you need a new Python file named `function.py` that should be located in the 'functions' folder. This file should contain the main function for your project.
#
# The functional description you provided indicates that you want to:
#
# 1. Turn up your air conditioner to 26°
# 2. Turn up your TV volume by three degrees
# 3. Heat the kettle to 100°
#
# However, the source code provided does not include a TV or a kettle in the list of actuators. The source code includes classes for different types of sensors and actuators that are used in a smart home system. The sensors include temperature, humidity, light intensity, and smoke sensors. The actuators include a notification sender, light, window, curtain, music player, heater, AC, coffee machine, smart socket, door, cleaning robot, smart TV, and humidifier.
#
# The `home_plan.py` file contains a `Room` class that can have multiple sensors and actuators. The `home_plan()` function creates a list of rooms with their respective sensors and actuators.
#
# The `config.py` file contains some configuration constants for the smart home system.
#
# To fulfill your requirements, the `function.py` file should include functions to control the air conditioner and the TV volume. However, since there is no kettle in the provided actuators, a new actuator class for the kettle should be created. The new file should import the necessary classes from the `sensor.py`, `actuator.py`, and `home_plan.py` files. The main function should create a home plan, find the required actuators, and perform the required operations.