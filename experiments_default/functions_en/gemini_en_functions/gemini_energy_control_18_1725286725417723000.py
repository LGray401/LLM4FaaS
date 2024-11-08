from home.home_plan import get_room, get_room_actuators
from home.actuator import Window


def open_windows(home):
    """
    Opens all windows in the given home.

    Args:
        home: A list of rooms representing the home.
    """
    for room in home:
        windows = get_room_actuators(home, room.name)
        if windows:
            for window in windows:
                if window.actuator_type == "Window":
                    window.turn_on()
                    print(f"Opening {window.id} in {room.name}.")


if __name__ == "__main__":
    # Replace this with your actual home plan.
    home = []  # Initialize your home plan here

    open_windows(home)

# **Explanation:**

# 1. **Imports:**
#    - `get_room` and `get_room_actuators` are imported from `home.home_plan` to access the home structure and find specific rooms and actuators.
#    - `Window` is imported from `home.actuator` to specifically target windows.

# 2. **`open_windows` Function:**
#    - Takes `home` as input, representing the home plan.
#    - Iterates through each room in the home:
#      - Retrieves the actuators (windows, lights, etc.) in the current room.
#      - If actuators are found, further iterates through them.
#      - Checks if the current actuator is a `Window`.
#      - If it is a window, it calls `window.turn_on()` to open the window and prints a message confirming the action.

# 3. **`if __name__ == "__main__":` Block:**
#    - This block ensures that the code inside it only runs when the script is executed directly (not imported as a module).
#    - You should replace `home = []` with your actual home plan (using the `home_plan` function from your `home_plan.py` file).

# **How to Use:**

# 1. **Import the Function:**
#    - In your main script where you want to use the `open_windows` function, import it:
#      ```python
#      from functions.function import open_windows
#      ```

# 2. **Create Your Home Plan:**
#    - Use the `home_plan` function from `home.home_plan` to create your home structure:
#      ```python
#      home = home_plan() 
#      ```

# 3. **Call the Function:**
#    - Pass your home plan to the `open_windows` function:
#      ```python
#      open_windows(home)
#      ```

# **Important Notes:**

# - Make sure your `home` variable contains your actual home plan created using the `home_plan` function.
# - You might need to adjust the code based on the specific implementation of your `Window` class and how you manage your home plan (e.g., using dictionaries or other data structures).
# - This code only opens windows; you might want to add logic for other actions, like checking if the windows are already open or adding conditions based on weather or other factors.
