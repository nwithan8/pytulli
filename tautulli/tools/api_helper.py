import objectrest

from tautulli.internal import static
from tautulli.models.activity import build_summary_from_activity_json


# noinspection PyTypeChecker
class APIShortcuts:
    def __init__(self, api: "RawAPI"):
        self._api = api

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

    def ping(self) -> bool:
        """
        Ping the Tautulli server

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        name = self._api.server_friendly_name
        return name is not None and name is not static.empty_string

    def ping_plex(self, pms_url: str = None) -> bool:
        """
        Ping the Plex Media Server
        :param pms_url: URL of the Plex Media Server, defaults to default PMS URL
        :type pms_url: str, optional
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        pms_url = pms_url or self._api.server_info.get('pms_url', None)

        if pms_url is None:
            return False
        try:
            status_code = objectrest.get(url=pms_url, verify_ssl=False).status_code
            return 200 <= status_code < 300 or status_code == 401 # 401 is a valid response
        except Exception:
            return False

    @property
    def has_plex_pass(self) -> bool:
        """
        Check if the Plex Media Server has Plex Pass

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return self._api.server_info.get('pms_plexpass', 0) == 1

    @property
    def api_version(self) -> str:
        """
        Get the Tautulli API version

        :returns: API version
        :rtype: str
        """
        return self._api.tautulli_info.get('tautulli_version', None)

    def get_library_by_name(self, library_name: str) -> dict:
        """
        Get a Plex Media Server library using its name

        :returns: Dict of data
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

        :returns: Dict of data
        :rtype: dict
        """
        _activity_data = self._api.activity()
        return build_summary_from_activity_json(activity_data=_activity_data).dict()

    @property
    def activity_summary_message(self) -> str:
        """
        Get a summary message of current activity on the Plex Media Server

        :returns: Activity summary message
        :rtype: str
        """
        _activity_data = self._api.activity()
        # Yes, this is the JSON API using an object as a middleman.
        return build_summary_from_activity_json(activity_data=_activity_data).message
