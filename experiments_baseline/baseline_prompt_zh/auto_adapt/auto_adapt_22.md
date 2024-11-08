# Preparation
Hi, I want you to provide a smart home application in Python based on my given functional description, in conjunction with my smart home layout.

The required application should be able to be run in a linux terminal with one command. Provide me the command as well.

I will first give you the functional description, then show you the smart home layout.


# Functional Description
Temperature:
家中所有空间温度高于26度，自动开启所有空调，开启空调时同时关闭所有窗户

Humidity:
湿度小于30％，自动启动加湿器

Light Intensity:
室内光照强度小于150lux，调亮灯光，大于11080lux，拉上窗帘，打开室内灯


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