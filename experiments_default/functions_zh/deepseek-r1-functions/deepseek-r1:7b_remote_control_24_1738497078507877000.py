# <think>
# Okay, so I'm trying to figure out how to implement the Light sensor in the home_plan function of config.py. Let me see what the user is asking for here.
# 
# Wait, actually, looking at the provided code, it seems like there's a mix-up between config.py and another file because in the main section after home_plan(), there's a reference to TEMP_LOW as 15°C, which doesn't make sense for temperature. Oh wait, maybe that was intended for light intensity? Or perhaps I'm misunderstanding.
# 
# Wait no, looking again: The user included some code snippets labeled as config.py and another part called 'main'. Hmm, but the problem is about implementing a Light sensor in home_plan(). So probably the correct place to put it is into config.py. Let me think about what parameters are relevant for light intensity.
# 
# In the existing code, they have TEMP_LOW=15°C which doesn't make sense because temp is usually higher than that in most homes during winter and lower in summer, but 15°C seems a bit low. But maybe it's not related to light.
# 
# Wait, perhaps the user wants to set thresholds for light intensity based on certain values. So I should look at how they're handling temperature first. In config.py, they have TEMP_LOW=15, TEMP_HIGH=25. That might be intended for room temperature control. But since it's not applicable for light, maybe that line is a mistake.
# 
# Then there are HUMIDITY_LOW and HIGH set to 30% and 50%, which makes sense because humidity levels can vary but comfortable environments usually keep them between those ranges.
# 
# For light intensity, probably the user wants something like:
# - LIGHT_INTENSITY_LOW = 300 lx (lux)
# - LIGHT_INTENSITY_HIGH = 900 lx
# 
# That would mean that when the light is below 300, maybe the system can trigger some routine. Or perhaps it's for adjusting lighting based on ambient conditions.
# 
# But looking at the existing code in home_plan(), they have LightIntensiveSensor which might be part of the actuators or sensors in a room. So I need to add these new light-related variables into config.py so that the system knows when to adjust lights automatically.
# 
# So, putting it all together, the steps are:
# 
# 1. Identify where to insert the new light intensity thresholds.
# 2. Make sure the variable names match what's expected by the rest of the code, like LightIntensiveSensor.
# 3. Ensure units are correct if necessary (lux is standard for light intensity).
# 4. Test that these values affect the system correctly when run.
# 
# I think adding the LIGHT_INTENSITY_LOW and HIGH in config.py should enable the home_plan function to adjust lighting based on those thresholds, similar to how it's done for temperature.
# </think>
# 
# To implement the Light sensor configuration, we'll add the appropriate light intensity thresholds to the `config.py` file. These values will help regulate the system's response based on ambient light levels.
# 
# **Step-by-step Explanation:**
# 
# 1. **Identify Appropriate Intensity Ranges:** Determine the suitable low and high bounds for light intensity that trigger specific actions.
# 2. **Add Configurations to `config.py`:** Insert these new variables with sensible default values (300 lx for low, 900 lx for high) into the configuration file.
# 
# Here's how the updated code should look:
# 
# ```python
# wait duration
TEMP_CHANGE_DURATION_WINDOW = 1

# threshold
TEMP_LOW = 15  # Celsius degree (adjust as needed)
TEMP_HIGH = 25  # Celsius degree
HUMIDITY_LOW = 30  # percentage
HUMIDITY_HIGH = 50  # percentage

L盏光低阈值 = 300  # lux: 每平方米流过的 Lux 数量
L盏光高阈值 = 900  # lux
# ```
# 
# **Note:** Adjust the temperature values (`TEMP_LOW` and `TEMP_HIGH`) based on your specific climate to ensure comfort while leaving other thresholds as per the existing code.