# Import Libraries

import pyautogui
import time
import os
from datetime import datetime


def screenshoter(save_directory_screenshot="src/data/screenshots", interval_minutes=30):
    """Creating/checking a directory for screenshots and creating screenshots at intervals"""

    os.makedirs(
        save_directory_screenshot, exist_ok=True
    )  # Checking the directory. If the directory doesn't exist, create it.

    print(f"Directory for screenshots '{save_directory_screenshot}' exists.")

    interval_seconds = interval_minutes * 60  # Convertion minutes to seconds

    next_time = time.time() + interval_seconds  # Calculating the next screenshot time

    try:
        while True:  # Iterations for creating screenshots

            time_to_wait = next_time - time.time()

            if time_to_wait > 0:
                time.sleep(time_to_wait)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_name = f"screenshot_{timestamp}.jpg"
            screenshot_path = os.path.join(save_directory_screenshot, screenshot_name)

            try:
                screenshot_body = pyautogui.screenshot()
                screenshot_body.save(screenshot_path, quality=85)
                print(f"Screenshot {screenshot_name} was done.")

            except Exception as e:
                print(f"Error: {e}")
                print(f"Screenshot was not taken.")
                continue

            next_time += interval_seconds

    except KeyboardInterrupt:  # Ctrl + C - quit
        print("Program was closed.")


if __name__ == "__main__":  # Entry point
    screenshoter(save_directory_screenshot="src/data/screenshots", interval_minutes=1)
