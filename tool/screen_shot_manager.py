from android_testing_utils.log import my_logger
from android_testing_utils.tool import adb_cmd
import traceback
import pickle
from typing import Dict, List

class ScreenShotManager:
    def __init__(self, device_id, need_screenshot):
        self._device_id = device_id
        self._need_screenshot = need_screenshot

        if self._need_screenshot:
            my_logger.auto_hint(my_logger.LogLevel.INFO, self, True, "Screenshot is enabled.")
            self._screenshot_map: Dict[str, List[str]] = {}
        else:
            my_logger.auto_hint(my_logger.LogLevel.INFO, self, True, "Screenshot is disabled.")

    def take_screenshot(self, current_screenshot_file_path) -> bool:
        if not self._need_screenshot:
            my_logger.auto_hint(my_logger.LogLevel.INFO, self, True, "Screenshot is disabled! Skip take.")
            return False

        try:
            adb_cmd.ADBSystemOperation.screencap_to_path(self._device_id, current_screenshot_file_path)
        except Exception as e:
            my_logger.auto_hint(my_logger.LogLevel.EXCEPTION, self, True, traceback.print_exc())
            my_logger.auto_hint(my_logger.LogLevel.WARNING, self, True, "Screencap failed!")
            return False

        return True

    def record_screenshot(self, state_hash, current_screenshot_file_path):
        if not self._need_screenshot:
            my_logger.auto_hint(my_logger.LogLevel.INFO, self, True, "Screenshot is disabled! Skip record.")
            return

        if state_hash not in self._screenshot_map:
            self._screenshot_map[state_hash] = [current_screenshot_file_path]
        else:
            self._screenshot_map[state_hash].append(current_screenshot_file_path)

    def save_screenshot_map(self, file_path_without_extension):
        if not self._need_screenshot:
            my_logger.auto_hint(my_logger.LogLevel.INFO, self, True, "Screenshot is disabled! Skip save.")
            return

        pickle.dump(self._screenshot_map, open(f"{file_path_without_extension}.pickle", "wb"))

        with open(f"{file_path_without_extension}.txt", "w") as f:
            for state_hash, screenshot_list in self._screenshot_map.items():
                f.write(f"{state_hash}:\n")
                for screenshot in screenshot_list:
                    f.write(f"\t- {screenshot}\n")

        my_logger.auto_hint(
            my_logger.LogLevel.INFO, self, True,
            f"Screenshot map saved to {file_path_without_extension}."
        )