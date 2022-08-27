from tautulli.internal import static
from tautulli.models.activity_summary import build_summary_from_activity_json


# noinspection PyTypeChecker
class APIShortcuts:
    def __init__(self, api: "RawAPI"):
        self._api = api

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

    def ping(self) -> bool:
        """
        Ping the Tautulli server
        :return: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        name = self._api.server_friendly_name
        return name is not None and name is not static.empty_string

    def get_library_by_name(self, library_name: str) -> dict:
        """
        Get a Plex Media Server library using its name

        :return: Dict of data
        :rtype: dict
        """
        for library in self._api.library_names:
            if library.get('section_name') == library_name:
                return library
        return {}

    @property
    def activity_summary(self) -> dict:
        """
        Get a summary of current activity on the Plex Media Server

        :return: Dict of data
        :rtype: dict
        """
        _activity_data = self._api.activity()
        return build_summary_from_activity_json(activity_data=_activity_data).dict()

    @property
    def activity_summary_message(self) -> str:
        """
        Get a summary message of current activity on the Plex Media Server

        :return: Activity summary message
        :rtype: str
        """
        _activity_data = self._api.activity()
        # Yes, this is the JSON API using an object as a middleman.
        return build_summary_from_activity_json(activity_data=_activity_data).message
