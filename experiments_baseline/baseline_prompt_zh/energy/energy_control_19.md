# Preparation
Hi, I want you to provide a smart home application in Python based on my given functional description, in conjunction with my smart home layout.

The required application should be able to be run in a linux terminal with one command. Provide me the command as well.

I will first give you the functional description, then show you the smart home layout.


# Functional Description
我觉得这里逻辑有点问题。应该是系统内部预设好节能模式，然后在具体执行时候来问客户的意见。比如说两个例子，
1.我早上刚睡醒希望通通风。那我会跟ai说打开窗户。这时候系统应该自己去检测外界的气候环境，或者自动检索今天的天气预报，来给出相应的建议。比如现在外面在下大雨，建议不要开窗。是否开启空调换气模式。
2.我跟ai说太热了，ai同样根据外部环境建议我是要开窗通风还是开空调。
再或者，我忘了我开着空调就把窗户打开了。那ai是不是可以自动检测到这个操作，来询问我是否需要关闭空调？
像题目里说的例子，打开空调自动关窗，这些应该是在默认的“节能模式”里面就设定好的基础设置。
如果是说我对节能模式设置的期待。那可能有几个经常碰到的情况，比如出门忘了关电器，夏天睡着了自动把温度调高两度之类的。
我觉得，不如问一些希望哪种或哪些电器可以自动化，希望达到什么样的预期。比如，你厨房放了烟雾传感器，为啥不把油烟机也加进来/doge


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