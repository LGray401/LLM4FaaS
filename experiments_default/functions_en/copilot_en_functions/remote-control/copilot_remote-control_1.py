# Based on the functional description and the provided source code, you need to create a `function.py` file that contains a main function to control the smart home. The function should perform the following actions:
#
# 1. Start the cleaning robot for sweeping.
#     2. Select a song on the music player.
# 3. Select a voice channel on the TV.
# 4. Start on-demand movie or TV series on the TV.
# 5. Adjust the bedroom lighting (on, off, brightness adjustment).
#
# Here is a Python code snippet that you can use as a starting point for your `function.py` file:
#
# ```python
from home.actuator import CleaningRobot, MusicPlayer, SmartTV, Light
from home.home_plan import home_plan, get_room_actuators

def main():
    # Get the home plan
    home = home_plan()

    # Start the cleaning robot for sweeping
    cleaning_robots = [actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, CleaningRobot)]
    for robot in cleaning_robots:
        robot.turn_on()
        robot.daily_routine()

    # Select a song on the music player
    living_room_music_players = [actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, MusicPlayer)]
    for music_player in living_room_music_players:
        music_player.turn_on()
        music_player.play_music("Your favorite song")

    # Select a voice channel on the TV
    living_room_tvs = [actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, SmartTV)]
    for tv in living_room_tvs:
        tv.turn_on()
        tv.play_channel("Your favorite voice channel")

    # Start on-demand movie or TV series on the TV
    for tv in living_room_tvs:
        tv.play_channel("Your favorite movie or TV series")

    # Adjust the bedroom lighting (on, off, brightness adjustment)
    bedroom_lights = [actuator for actuator in get_room_actuators(home, "Bedroom") if isinstance(actuator, Light)]
    for light in bedroom_lights:
        light.turn_on()
        light.set_brightness_level("medium")

if __name__ == "__main__":
    main()
# ```
#
# This code first retrieves the home plan, then it finds the relevant actuators in each room and performs the required actions. Please replace `"Your favorite song"`, `"Your favorite voice channel"`, and `"Your favorite movie or TV series"` with the actual song, voice channel, and movie or TV series you want to play or watch.