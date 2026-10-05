from android_testing_utils.tool import app_info_getter
from android_testing_utils.log import my_logger


class ActivityAliasManager:
    def __init__(self, apk_file_path):
        self._apk_file_path = apk_file_path

        self._alias_map = self.__construct_alias_map()

    def __construct_alias_map(self):
        res = {}
        alias_pairs = app_info_getter.GetActivityAliasPairs.get_all_activity_alias_pair_from_apk_file_by_aapt_dump_xmltree(self._apk_file_path)
        for item in alias_pairs:
            res[item.alias] = item.target_activity
        my_logger.auto_hint(my_logger.LogLevel.INFO, self, True, f"Alias map constructed. Total {len(res)} items.")

        for key, value in res.items():
            my_logger.auto_hint(my_logger.LogLevel.DEBUG, self, True, f"    [Alias] {key} -> [Actual] {value}")
        return res

    def get_actual_activity(self, current_activity):
        if current_activity in self._alias_map:
            actual = self._alias_map[current_activity]
            my_logger.auto_hint(
                my_logger.LogLevel.INFO, self, True,
                f"Activity {current_activity} is an alias, actual activity is {actual}."
            )
            return actual
        return current_activity

    def filter_out_alias(self, all_activities: set):
        all_alias_set = set(self._alias_map.keys())
        all_actual_set = set(self._alias_map.values())
        res = (all_activities | all_actual_set) - all_alias_set
        my_logger.auto_hint(
            my_logger.LogLevel.INFO, self, True,
            f"Alias filtered. Original {len(all_activities)} with {len(all_alias_set)} alias pairs, Final {len(res)}."
        )
        return res