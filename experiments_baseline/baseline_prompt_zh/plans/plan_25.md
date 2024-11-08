# Preparation
Hi, I want you to provide a smart home application in Python based on my given functional description, in conjunction with my smart home layout.

The required application should be able to be run in a linux terminal with one command. Provide me the command as well.

I will first give you the functional description, then show you the smart home layout.


# Functional Description
MORNING PLAN:
当传感器感应到光强达到一定值吋，打开窗帘，关闭卧室灯，打开音乐播放器，听听音乐，启动咖啡机，冲杯咖啡

LEAVE HOME PLAN:
当下达锁上入户门指令后，窗帘拉上，关闭室内灯，插座断电

MOVIE PLAN:
当下达打开电视机指令后，拉上窗帘，将室内卡了光调暗


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