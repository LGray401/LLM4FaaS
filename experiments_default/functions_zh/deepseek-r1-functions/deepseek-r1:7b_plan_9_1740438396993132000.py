# <think>
# Okay, so I need to figure out how to handle the Light intensity in this home automation system. The user wants the light to adjust based on temperature and humidity levels. Let me think about how to structure this.
# 
# First, I should probably create a Light class that can monitor its own state and interact with sensors. That makes sense because each room has its own light sensor. So, the Light object would need to know which sensor it's connected to. When the environment changes—like temperature or humidity—the light should adjust accordingly.
# 
# Wait, but how do I track when the conditions change? Maybe using a while loop that runs until the routine is done. But in Python, you can't just run an infinite loop like that without some condition. Oh right, maybe use time.sleep with a timeout for each interval.
# 
# So, I'll need to import the datetime module to get current time and compare it with previous time minus the routine duration. That way, every few minutes, I check if the routine has completed since the last check.
# 
# Now, how do I store the sensor data? Maybe as a dictionary in the Light class that includes temperature, humidity, and light intensity. That way, each time the routine runs, it can check against this data.
# 
# Wait, but what's the order of operations here? The main loop should check if enough time has passed since the last update. If so, it updates the current time and fetches the latest sensor values. Then, based on those values, adjust the light intensity.
# 
# Hmm, I should also consider the thresholds for each condition. For example, when temperature is below a certain low, or above a high, humidity similarly, then set the intensity accordingly.
# 
# But how do I handle overlapping conditions? Like if both temperature and humidity are too high. Maybe use elif statements to check in order of priority. Or maybe assign weights to each condition for more nuanced control.
# 
# Oh right, using elif makes sense—check the highest thresholds first to avoid lower ones being triggered unintentionally.
# 
# I also need to write a function that runs this loop periodically. Let's call it routine_check, which takes the Light instance and an interval in seconds. It will execute every 'interval' seconds until the main process exits or something.
# 
# But wait, how do I handle multiple lights? Each room has its own sensor and light, so each should have their own instance of the Light class with their specific sensor reference.
# 
# Now, putting it all together: when a routine starts, for each light in home Planned rooms, call routine_check every few minutes. In the loop, update current time, get sensors data, then set intensity based on conditions.
# 
# I think that's the general approach. Now I'll outline the steps:
# 
# 1. Create Light class with methods to fetch sensor data and adjust intensity.
# 2. Implement a routine_check function to run periodically.
# 3. In main, initialize all lights for each room in home_plan().
# 4. Start the routine_check for each light every specified interval.
# 
# Wait, but how do I handle the initial setup? Maybe after creating home_plan(), loop through each room's actuators (lights) and create a Light object per light sensor, storing their reference to the sensor.
# 
# Yes, that makes sense. Then, schedule the routine_check function calls for each light at the specified intervals.
# 
# I should also make sure that when the routine runs, it uses the latest data from the sensors without waiting too long between checks—like every few minutes so it's responsive but not overburdening the system.
# 
# So, putting this into code: in config.py, we have the necessary thresholds. The Light class will check against these to determine if intensity needs adjusting. Then, the main script sets up each light and schedules their routine checks.
# </think>
# 
# To implement the Light automation based on temperature and humidity conditions, follow these steps:
# 
# 1. **Create a `Light` Class:**
#    - Each room's light is represented by an instance of this class.
#    - The class will:
#      - Accept a sensor reference (sensor_type) to monitor environmental conditions.
#      - Fetch current environmental data from the sensor via `get_sensor_data`.
#      - Adjust intensity based on temperature and humidity thresholds using `adjust_intensity`.
# 
# 2. **Define Thresholds:**
#    - Establish minimum and maximum values for temperature, humidity, and light intensity.
# 
# 3. **Implement the Routine Check Function:**
#    - Create a function `routine_check` that runs periodically.
#    - This function will:
#      - Fetch current time and compare it with last check time minus routine duration.
#      - Retrieve environmental data from the sensor.
#      - Adjust light intensity based on conditions using if-elif statements.
# 
# 4. **Schedule Routine Checks:**
#    - In the main script, for each room's lights, initialize a `Light` object and schedule its routine check at specified intervals (e.g., every 5 minutes).
# 
# Here is the implementation:
# 
# ```python
import time
from datetime import datetime

class Light:
    def __init__(self, sensor_type):
        self.sensor_type = sensor_type
        self.current_intensity = 0
        self.RoutineDuration = 300  # 5 minutes in seconds
        
    def get_sensor_data(self):
        return {
            'temperature': self._sensor.get_value('temperature'),
            'humidity': self._sensor.get_value('humidity')
        }
        
    def adjust_intensity(self, data):
        temperature = data['temperature']
        humidity = data['humidity']
        
        if (temperature < config.MIN_TEMP and
                humidity < config.MIN_HUMIDITY):
            self.set_max_intensity()
            
        elif (temperature > config.MAX_TEMP or
              humidity > config.MAX_HUMIDITY):
            self.set_min_intensity()
            
        else:
            # Default to moderate intensity
            pass
            
    def set_max_intensity(self):
        max_int = min(config.MAX_LI, 100)
        self.current_intensity = int(max_int * 2)
        print(f"Setting light {self.sensor_type} to {max_int}%")
        
    def set_min_intensity(self):
        min_int = config.MIN_LI
        if min_int < 5:
            min_int = 5
        self.current_intensity = max(0, int(min_int))
        print(f"Setting light {self.sensor_type} to {min_int}%")

def routine_check(light):
    current_time = datetime.now()
    last_checked = getattr(light, 'last_checked', None)
    
    if not last_checked:
        light.last_checked = current_time
        
    now = time.time()
    while True:
        elapsed = now - time.time()
        seconds_elapsed = int(elapsed)  # Elapsed in whole seconds
        if (seconds_elapsed % light.RoutineDuration == 0):
            light.last_checked = datetime.now()
            data = light.sensor_type.get_sensor_data()
            light.adjust_intensity(data)
        time.sleep(1)

def main():
    home = home_planet()  # Assume this function returns the list of rooms
    
    for room in home:
        if isinstance(room, Room) and hasattr(room, 'lights'):
            lights = room.lights
            for sensor in lights:
                light = Light(sensor)
                schedule(routine_check(light), interval=300)

if __name__ == "__main__":
    main()
# ```
# 
# This implementation ensures that each light adjusts its intensity based on environmental conditions every few minutes, providing responsive yet controlled automation.