# ----------------------
# @Time  : 2026 Oct
# @Author: Ruishen Huang
# ----------------------
from android_testing_utils.log import my_logger
from android_testing_utils.tool.adb_cmd import ADBGetDeviceInfo


class ResolutionConst:
    SCREEN_RESOLUTION_X = 1080
    SCREEN_RESOLUTION_Y = 1920

    @classmethod
    def update_resolution_with_current_device(cls, device_id):
        x, y = ADBGetDeviceInfo.get_window_resolution_ratio(device_id)
        my_logger.auto_hint(my_logger.LogLevel.INFO, cls, True, f"Resolution update to: x={x}, y={y}")
        cls.SCREEN_RESOLUTION_X = x
        cls.SCREEN_RESOLUTION_Y = y
