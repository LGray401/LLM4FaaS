# Preparation
Hi, I want you to provide a smart home application in Python based on my given functional description, in conjunction with my smart home layout.

The required application should be able to be run in a linux terminal with one command. Provide me the command as well.

I will first give you the functional description, then show you the smart home layout.


# Functional Description
不需要灯光时能自动关闭，不用电时插座关闭，室内无人温度不很低时不必开暖气，开窗通风能降温时，不必开空调，需要开空调时先关好门窗。


# Smart Home Layout
- **Living Room**
    - Sensors:
        - Temperature, Humidity, Light Intensity
    - Smart Devices:
        - Light, Light, Window, Window, Socket, Socket, Door, Heater, AC, Curtain, Humidifier, Cleaning Robot, Music Player, TV, Notification Sender

- **Bedroom**
    - Sensors:
        - Temperature, Humidity, Light Intensity
    - Smart Devices:
        - Light, Light, Window, Curtain, AC, Heater, Music Player, Door, Socket, Socket, Cleaning Robot, Humidifier

- **Bathroom**
    - Sensors:
        - Temperature, Humidity
    - Smart Devices:
        - Light, Window, Heater, Door, Socket, Socket

- **Kitchen**
    - Sensors:
        - Humidity, Smoke
    - Smart Devices:
        - Light, Window, Heater, Coffee Machine, Socket, Socket, Socket, Door

- **Balcony**
    - Outdoor Sensors:
        - Temperature, Humidity
    - Smart Devices:
        - Door  