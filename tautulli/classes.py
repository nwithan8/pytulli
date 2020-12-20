from typing import Union


class HomeStatsCategory:
    def __init__(self, data: dict):
        self._data = data
        self.name = data.get('stat_id')
        self.type = data.get('stat_type')
        self.rows = data.get('rows')


class HomeStats:
    def __init__(self, data: dict):
        self._data = data
        self.stats = [HomeStatsCategory(data=category) for category in data]

    def get_category(self, category_name: str) -> Union[HomeStatsCategory, None]:
        for category in self.stats:
            if category.name == category_name:
                return category
        return None


class WatchTimeStat:
    def __init__(self, data: dict):
        self._data = data
        self.days = data.get('query_days')
        self.plays = data.get('total_plays')
        self.time = data.get('total_time')


class WatchTimeStats:
    def __init__(self, data: dict):
        self._data = data
        self.stats = [WatchTimeStat(data=stat) for stat in data]

    def get_by_day(self, days: int) -> Union[WatchTimeStat, None]:
        for stat in self.stats:
            if stat.days == days:
                return stat
        return None


class User:
    def __init__(self, data: dict, api):
        self._data = data
        self._api = api
        self.username = data.get('username')
        self.id = data.get('user_id')
        self.shared_libraries = data.get('shared_libraries').split(";")