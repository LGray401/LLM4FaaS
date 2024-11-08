# Preparation
Hi, I want you to provide a smart home application in Python based on my given functional description, in conjunction with my smart home layout.

The required application should be able to be run in a linux terminal with one command. Provide me the command as well.

I will first give you the functional description, then show you the smart home layout.


# Functional Description
Temperature:
室内温度超过25度就自动开启空调，同时关闭窗户

Humidity:
室内湿度不合理（过于干燥时），开启加湿器

Light Intensity:
通过室内日照情况，自动调节灯光


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