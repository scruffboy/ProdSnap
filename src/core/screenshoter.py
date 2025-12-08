# Import Libraries

import pyautogui
import time
import os
from datetime import datetime


# Function


def screenshoter(
    save_directory_screenshot="src/data/screenshots", interval_time_minutes=30
):
    """"""

    #
    os.makedirs(save_directory_screenshot, exist_ok=True)
    print(f"Directory for screenshots '{save_directory_screenshot}' exists.")

    while True:

        convertion_time = interval_time_minutes * 60

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_name = f"screenshot_{timestamp}.jpg"
        screenshot_path = os.path.join(save_directory_screenshot, screenshot_name)

        try:
            screenshot_body = pyautogui.screenshot()
            screenshot_body.save(screenshot_path, quality=85)
            print(f"Screenshot {screenshot_name} was done.")

            time.sleep(convertion_time)

        except KeyboardInterrupt:
            print(f"Program was closed.")
        except Exception as e:
            print(f"Error: {e}")
