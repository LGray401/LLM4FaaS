# Ground Truth Expected Output Request

Given this smart-home requirement, produce the expected runtime console output for a correct implementation.
Target style: very concise, similar to test/standard_log files.

Important: prefer under-specific lines over over-specific lines.
If uncertain, output a short canonical prefix/ID line that is still valid.

## How Comparison Works (must follow)

1) Your stdout is split into lines.
2) These lines must appear in order as one contiguous block in actual runtime output.
3) Each expected line is checked by substring containment against the corresponding actual line.
4) Extra lines in actual output are allowed.

Implication:
- Overly detailed lines are risky and often fail.
- Minimal, canonical, standard-log-like lines are preferred.

## Requirement

{requirement}

## Allowed Console Line Patterns (smart_home)

Use these as canonical possible stdout line patterns produced by the shared smart_home runtime.
Only include lines required by the requirement and the main execution path.

Placeholder legend:
- ACTUATOR_ID: /Actuator/<Type>/<Room>/<N>
- SENSOR_ID: /Sensor/<Type>/<Room>/<N>
- ROOM, MESSAGE, PLAYLIST, CHANNEL, COFFEE_TYPE, LEVEL_NAME: runtime values
- TARGET_TEMP, READING: numeric values
- STATUS_VALUE: runtime status string

Possible stdout lines:
- ACTUATOR_ID is turned on.
- ACTUATOR_ID is turned off.
- ACTUATOR_ID
- Set the target temperature of ACTUATOR_ID to
- ACTUATOR_ID Start making
- ACTUATOR_ID is OFF now
- Lock the door ACTUATOR_ID.
- Unlock the door ACTUATOR_ID.
- Cleaning Robot ACTUATOR_ID Starts Daily Cleaning Routine
- ACTUATOR_ID Finish Daily Cleaning Routine, Will Turn it OFF
- Notification Sender ACTUATOR_ID is OFF, please turn it on then send the message again.
- ACTUATOR_ID start playing 
- Set ACTUATOR_ID light brightness level to LEVEL_NAME_UPPER
- 'ACTUATOR_ID' is OFF now, Need to Turn it ON First.
- ACTUATOR_ID Increasing humidity in ROOM
- ACTUATOR_ID Decreasing humidity in ROOM
- Cannot Get Sensor Reading, SENSOR_ID is Currently OFF. 
- SENSOR_ID reading is: 
- Status Error with status: 
- SENSOR_ID current status is: 

## Strict Output Guidelines

- Keep stdout short: usually 2-8 lines.
- Use exact wording from allowed patterns whenever possible.
- Prefer canonical partial lines like standard logs (for example IDs or stable prefixes).
- Use " || " only when multiple alternatives are genuinely possible for the same requirement step.
- Do not invent summary sentences (for example "Successfully ...") unless explicitly required.
- Do not add explanatory text, assumptions, reasoning, or markdown.
- Keep stderr empty unless an error is explicitly required by the requirement.
- return_code must be 0.

## Style Examples (good)

Good (concise):
/Actuator/CleaningRobot/LivingRoom/1 || /Actuator/CleaningRobot/Bedroom/1
Cleaning Robot /Actuator/CleaningRobot/LivingRoom/1 Starts Daily Cleaning Routine || Cleaning Robot /Actuator/CleaningRobot/Bedroom/1 Starts Daily Cleaning Routine
/Actuator/MusicPlayer/LivingRoom/1 || /Actuator/MusicPlayer/Bedroom/1
/Actuator/SmartTV/LivingRoom/1
Set /Actuator/Light/Bedroom/1 light brightness level to || Set /Actuator/Light/Bedroom/2 light brightness level to

More varied examples from dataset requirements and standard logs:

Requirement snippet (remote_control):
"Turn off the lights in the living room"
Expected stdout:
/Actuator/Light/LivingRoom/1 is turned off.
/Actuator/Light/LivingRoom/2 is turned off.

Requirement snippet (remote_control):
"Open windows"
Expected stdout:
/Actuator/Window/LivingRoom/1 is turned on. || /Actuator/Window/LivingRoom/2 is turned on. || /Actuator/Window/Bedroom/1 is turned on. || /Actuator/Window/Kitchen/1 is turned on. ||/Actuator/Window/Bathroom/1 is turned on.

Requirement snippet (plan):
"Morning: Play music | Away: Unplug the socket | Movie: Open the curtains"
Expected stdout:
/Actuator/MusicPlayer/LivingRoom/1 || /Actuator/MusicPlayer/Bedroom/1
/Actuator/SmartSocket/LivingRoom/1 is turned off.
/Actuator/SmartSocket/LivingRoom/2 is turned off.
/Actuator/SmartSocket/Bedroom/1 is turned off.
/Actuator/SmartSocket/Bedroom/2 is turned off.
/Actuator/SmartSocket/Kitchen/1 is turned off.
/Actuator/SmartSocket/Bathroom/1 is turned off.
/Actuator/Curtain/LivingRoom/1 || /Actuator/Curtain/Bedroom/1

Requirement snippet (auto_adapt):
"Temp: Please adjust to 26° | Humidity: Please adjust to 40 | Light: Moderate Light"
Expected stdout:
'/Sensor/IndoorTemperature/LivingRoom/1' is now ON.
/Sensor/IndoorTemperature/LivingRoom/1 reading is:
/Actuator/Heater/LivingRoom/1 || /Actuator/AC/LivingRoom/1
'/Sensor/Humidity/LivingRoom/1' is now ON.
/Sensor/Humidity/LivingRoom/1 reading is:
/Actuator/Humidifier/LivingRoom/1
'/Sensor/LightIntensive/LivingRoom/1' is now ON.
/Sensor/LightIntensive/LivingRoom/1 reading is:
Set /Actuator/Light/LivingRoom/1 light brightness level to MEDIUM || Set /Actuator/Light/LivingRoom/2 light brightness level to MEDIUM

Requirement snippet (energy_control):
"Turn on the air conditioner to 17 degrees and close the windows"
Expected stdout:
/Actuator/AC/LivingRoom/1 is turned on. || /Actuator/AC/Bedroom/1 is turned on.
/Actuator/Window/LivingRoom/1 is turned off. || /Actuator/Window/LivingRoom/2 is turned off. || /Actuator/Window/Bedroom/1 is turned off. || /Actuator/Window/Kitchen/1 is turned off. || /Actuator/Window/Bathroom/1 is turned off.

Requirement snippet (energy_control):
"Start the energy-saving mode and automatically choose whether to enable the air conditioner according to the outdoor temperature and humidity"
Expected stdout:
/Sensor/OutdoorTemperature/Balcony/1 reading is:

Bad (too detailed and brittle):
/Actuator/CleaningRobot/LivingRoom/1 Starts Daily Cleaning Routine
/Actuator/CleaningRobot/LivingRoom/1 Finish Daily Cleaning Routine, Will Turn it OFF
/Actuator/MusicPlayer/LivingRoom/1 start playing selected song
/Actuator/SmartTV/LivingRoom/1 start playing on-demand movie

## Output Format

Return strict XML using exactly this structure:
<ground_truth_output>
	<stdout>...</stdout>
	<stderr>...</stderr>
	<return_code>0</return_code>
</ground_truth_output>

Do not include markdown fences or explanations.
