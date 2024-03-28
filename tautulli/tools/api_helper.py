import objectrest

from tautulli.internal import static
from tautulli.models.activity import build_summary_from_activity_json
from tautulli.tools.utils import url_encode


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
            return 200 <= status_code < 300 or status_code == 401  # 401 is a valid response
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
        return build_summary_from_activity_json(activity_data=_activity_data).model_dump()

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

    def get_plex_image_url_from_proxy(self, plex_image_path: str, image_type: str = 'poster') -> str:
        """
        Get a URL to a Plex Media Server image hosted by the Tautulli image proxy

        :param plex_image_path: Path to the image on the Plex Media Server
        :type plex_image_path: str
        :param image_type: Image type, defaults to 'poster'
        :type image_type: str, optional
        :return: The URL to the image
        :rtype: str
        """
        return f"{self._api._base_url}/pms_image_proxy?img={url_encode(plex_image_path)}&fallback={image_type}"

    def download_plex_image_from_proxy(self, plex_image_path: str, file_path: str, file_format: str = 'png',
                                       image_type: str = 'poster') -> None:
        """
        Download an image from the Plex Media Server using the Tautulli API and save it to a local file

        :param plex_image_path: Path to the image on the Plex Media Server
        :type plex_image_path: str
        :param file_path: Path to the file to save the image to
        :type file_path: str
        :param file_format: Image file format, defaults to 'png'
        :type file_format: str, optional
        :param image_type: Image type, defaults to 'poster'
        :type image_type: str, optional
        :returns: None
        """
        data = self._api.pms_image_proxy(img=plex_image_path, fallback=image_type, img_format=file_format)

        with open(file_path, 'wb') as file:
            file.write(data)

    def get_link_to_open_media_item_in_browser(self, media_item_id: int) -> str:
        """
        Get a link to open a media item in the Plex Web app

        :param media_item_id: ID of the media item
        :type media_item_id: int
        :returns: URL to open the media item in the Plex Web app
        :rtype: str
        """
        plex_server_details = self._api.server_info
        pms_url = plex_server_details.get('pms_url')
        pms_id = plex_server_details.get('pms_identifier')

        if not pms_url or not pms_id:
            return None

        key = url_encode(f"/library/metadata/{media_item_id}")

        return f"{pms_url}#!/server/{pms_id}/details?key={key}"
