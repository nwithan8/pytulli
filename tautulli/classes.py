from typing import Union


class TautulliObject:
    def __init__(self, data: dict):
        self._data = data


class Docs(TautulliObject):
    def __init__(self, data: dict):
        super().__init__(data=data)


class Activity(TautulliObject):
    def __init__(self, data: dict):
        super().__init__(data=data)


class DateFormats(TautulliObject):
    def __init__(self, data: dict):
        super().__init__(data=data)


class LibraryNames(TautulliObject):
    def __init__(self, data: dict):
        super().__init__(data=data)


class Newsletters(TautulliObject):
    def __init__(self, data: dict):
        super().__init__(data=data)


class NotifierParameters(TautulliObject):
    def __init__(self, data: dict):
        super().__init__(data=data)


class PMSUpdate(TautulliObject):
    def __init__(self, data: dict):
        super().__init__(data=data)


class ServerIdentity(TautulliObject):
    def __init__(self, data: dict):
        super().__init__(data=data)


class ServerInfo(TautulliObject):
    def __init__(self, data: dict):
        super().__init__(data=data)


class ServerList(TautulliObject):
    def __init__(self, data: dict):
        super().__init__(data=data)


class ServersInfo(TautulliObject):
    def __init__(self, data: dict):
        super().__init__(data=data)


class UserNames(TautulliObject):
    def __init__(self, data: dict):
        super().__init__(data=data)


class Users(TautulliObject):
    def __init__(self, data: dict):
        super().__init__(data=data)


class UpdateCheck(TautulliObject):
    def __init__(self, data: dict):
        super().__init__(data=data)




















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
