import logging
import warnings
from datetime import datetime
from typing import Union, List

import objectrest
import packaging.version
import urllib3

import tautulli.internal.static as static
from tautulli._info import __min_api_version__
from tautulli.exceptions.api_exception import ApiException
from tautulli.exceptions.http_exception import HttpException
from tautulli.exceptions.json_exception import JsonException
from tautulli.internal.decorators import raw_json, set_and_forget
from tautulli.internal.utils import build_optional_params, _get_response_data, _success_result, int_list_to_string, \
    _one_needed, _which_used, bool_to_int, _is_invalid_choice, datetime_to_string, comma_delimit
from tautulli.tools.api_helper import APIShortcuts
from tautulli.tools.utils import redact

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# noinspection PyTypeChecker
class RawAPI:
    def __init__(self, base_url: str, api_key: str, verbose: bool = False, verify: bool = True,
                 ssl_verify: bool = True):
        if base_url.endswith("/"):
            base_url = base_url[:-1]
        self._base_url = base_url
        # Zero knowledge of the API key is kept
        self._url = f"{self._base_url}/api/v2?apikey={api_key}"
        self._redacted_url = f"{self._base_url}/api/v2?apikey={redact(full_string=api_key, to_redact=api_key)}"
        self._session = objectrest.Session()
        self._ssl_verify = ssl_verify
        logging.basicConfig(format='%(levelname)s:%(message)s', level=(logging.DEBUG if verbose else logging.ERROR))
        self._logger = logging.getLogger("tautulli")
        min_api_version = __min_api_version__()
        if verify and not self._verify_compatibility(min_version=min_api_version):
            warnings.warn(f"Tautulli API is older than {min_api_version}, things may not work as expected.")

    def __str__(self):
        return f"RawAPI(url={self._redacted_url})"

    def _verify_compatibility(self, min_version: str) -> bool:
        """
        Verify the client version is compatible with the API

        :param min_version: Minimum API version required
        :type min_version: str
        :returns: True if compatible, False if not
        :rtype: bool
        """
        server_version_string: Union[str, None] = self.tautulli_info.get('tautulli_version', None)

        if server_version_string is None:
            raise ApiException(message="Tautulli did not report a version number.")
        try:
            server_version = packaging.version.parse(server_version_string)
        except:
            raise ApiException(message="Could not parse Tautulli version number.")

        try:
            min_version = packaging.version.parse(min_version)
        except:
            raise ApiException(message="Could not parse minimum compatible version number.")

        self._logger.debug(f"Server version: {server_version}, minimum version: {min_version}")
        return server_version >= min_version

    def _get(self, command: str, params: dict = None) -> objectrest.Response:
        """
        Get response from API call

        :param command: Tautulli endpoint
        :type command: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :returns: Response from the API
        :rtype: objectrest.Response
        """
        if not params:
            params = {}
        params['cmd'] = command
        self._logger.debug(f"Making request to {self._redacted_url} with params {params}")
        response = self._session.get(url=self._url, params=params,
                                     verify=self._ssl_verify)  # Optionally ignore SSL errors for self-signed certificates
        self._logger.debug(f"Response: {response}")
        return response

    def _get_json(self, command: str, params: dict = None) -> dict:
        """
        Get JSON data from API call

        :param command: Tautulli endpoint
        :type command: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :returns: JSON data from the API response
        :rtype: dict
        """
        response = self._get(command=command, params=params)
        if not response:
            raise HttpException.from_response(response=response, logger=self._logger)

        try:
            return response.json()
        except:
            raise JsonException(message="Could not parse JSON from API response.", body=response.text)

    @raw_json
    def _get_x_by(self, endpoint: str, time_range: int = None, y_axis: str = None, user_ids: List[str] = None,
                  grouping: bool = False) -> dict:
        """
        Abstract method for the get_plays_by_X and get_streams_by_X functions

        :param endpoint: Tautulli endpoint
        :type endpoint: str
        :param time_range: Number of days of data to return
        :type time_range: int, optional
        :param y_axis: Stat type ('plays' or 'duration')
        :type y_axis: str, optional
        :param user_ids: List of user IDs to filter data
        :type user_ids: List[str], optional
        :param grouping: Whether to group the results (default: False)
        :type grouping: bool, optional
        :returns: Dict of data
        :rtype: dict
        """
        grouping = bool_to_int(boolean=grouping)
        if _is_invalid_choice(value=y_axis, variable_name='y_axis',
                              choices=static.stats_type):
            return False, None
        if user_ids:
            user_ids = comma_delimit(user_ids)
        params = build_optional_params(time_range=time_range, y_axis=y_axis, user_id=user_ids, grouping=grouping)
        return endpoint, params

    @property
    def shortcuts(self) -> APIShortcuts:
        """
        Shortcuts for common API actions

        :returns: Access to API shortcuts
        :rtype: APIShortcuts
        """
        return APIShortcuts(api=self)

    @set_and_forget
    def add_newsletter_config(self, agent_id: int) -> bool:
        """
        Add a new newsletter notification agent

        :param agent_id: Newsletter type to add
        :type agent_id: int
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return 'add_newsletter_config', {'agent_id': agent_id}

    @set_and_forget
    def add_notifier_config(self, agent_id: int) -> bool:
        """
        Add a new notifier notification agent

        :param agent_id: Notification agent to add
        :type: int
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return 'add_notifier_config', {'agent_id': agent_id}

    @property
    def arnold(self) -> str:
        """
        Get to the chopper!

        :returns: Random Arnold Schwarzenegger quote
        :rtype: str
        """
        json_data = self._get_json(command='arnold')
        if json_data:
            return _get_response_data(json_data=json_data)
        return static.empty_string

    @set_and_forget
    def backup_config(self) -> bool:
        """
        Backup the config.ini file

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return "backup_config", None

    @set_and_forget
    def backup_database(self) -> bool:
        """
        Backup the plexpy.db database

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return "backup_db", None

    @set_and_forget
    def delete_all_library_history(self, server_id: str, section_id: str, row_ids: List[int] = None) -> bool:
        """
        Delete all Tautulli history for a specific library

        :param server_id: Plex server identifier of the library section
        :type server_id: str
        :param section_id: ID of the Plex library section
        :type section_id: str
        :param row_ids: List of row IDS to delete
        :type row_ids: list[int], optional
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        params = {'server_id': server_id, 'section_id': section_id}
        if row_ids:
            params['row_ids'] = int_list_to_string(int_list=row_ids)
        return "delete_all_library_history", params

    @set_and_forget
    def delete_all_user_history(self, user_id: str, row_ids: List[int] = None) -> bool:
        """
        Delete all Tautulli history for a specific user

        :param user_id: ID of the Plex user
        :type user_id: str
        :param row_ids: List of row IDs to delete
        :type row_ids: list[int], optional
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        params = {'user_id': user_id}
        if row_ids:
            params['row_ids'] = int_list_to_string(int_list=row_ids)
        return "delete_all_user_history", params

    @set_and_forget
    def delete_cache(self) -> bool:
        """
        Delete the cache directory

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return "delete_cache", None

    @set_and_forget
    def delete_export(self, export_id: int, delete_all: bool = False) -> bool:
        """
        Delete exports from Tautulli

        :param export_id: Row ID of the exported file to delete
        :type export_id: int
        :param delete_all: Whether to delete all exported files (default: False)
        :type delete_all: bool
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return "delete_export", {'export_id': export_id, 'delete_all': delete_all}

    @set_and_forget
    def delete_history(self, row_ids: List[int]) -> bool:
        """
        Delete history rows from Tautulli

        :param row_ids: List of row IDs to delete
        :type row_ids: list[int]
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        params = {'row_ids': int_list_to_string(int_list=row_ids)}
        return 'delete_history', params

    @set_and_forget
    def delete_hosted_images(self, rating_key: int = None, service: str = None, delete_all: bool = False) -> bool:
        """
        Delete images uploaded to image hosting services

        :param rating_key: Rating key of image
        :type rating_key: int, optional
        :param service: Service to delete image from (i.e. 'imgur', 'cloudinary')
        :type service: str, optional
        :param delete_all: Whether to delete all images from the service (default: False)
        :type delete_all: bool, optional
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        if _is_invalid_choice(value=service, variable_name="service",
                              choices=static.cloud_image_hosts):
            return False, None
        params = build_optional_params(rating_key=rating_key, service=service, delete_all=delete_all)
        return 'delete_hosted_images', params

    @set_and_forget
    def delete_image_cache(self) -> bool:
        """
        Delete image cache directory

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return 'delete_image_cache', None

    @set_and_forget
    def delete_library(self, server_id: str, section_id: str, row_ids: List[int] = None) -> bool:
        """
        Delete library section from Tautulli.

        Also erases library history.

        :param server_id: Plex server identifier of the library section
        :type server_id: str
        :param section_id: ID of the Plex library section
        :type section_id: str
        :param row_ids: List of row IDs to delete
        :type row_ids: list[int], optional
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        params = {'server_id': server_id, 'section_id': section_id}
        if row_ids:
            params['row_ids'] = int_list_to_string(int_list=row_ids)
        return 'delete_library', params

    @set_and_forget
    def delete_login_log(self) -> bool:
        """
        Delete the Tautulli login logs

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return 'delete_login_log', None

    @set_and_forget
    def delete_lookup_info(self, rating_key: int = None, service: str = None, delete_all: bool = False) -> bool:
        """
        Delete the 3rd party API lookup info

        :param rating_key: rating key of image to delete
        :type rating_key: int, optional
        :param service: service to delete from (i.e. 'themoviedb', 'tvmaze', 'musicbrainz')
        :type service: str, optional
        :param delete_all: Whether to delete all images from the service (default: False)
        :type delete_all: bool, optional
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        if _is_invalid_choice(value=service, variable_name="service",
                              choices=static.cloud_lookup_hosts):
            return False, None
        params = build_optional_params(rating_key=rating_key, service=service, delete_all=delete_all)
        return 'delete_lookup_info', params

    @set_and_forget
    def delete_media_info_cache(self, section_id: str) -> bool:
        """
        Delete media info table cache for a specific library

        :param section_id: ID of the Plex library section
        :type section_id: str
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return 'delete_media_info_cache', {'section_id': section_id}

    @set_and_forget
    def delete_mobile_device(self, mobile_device_id: int = None, device_id: str = None) -> bool:
        """
        Remove a mobile device from the database

        :param mobile_device_id: Mobile device database ID to delete
        :type mobile_device_id: int, optional
        :param device_id: Unique device identifier for the mobile device
        :type device_id: str, optional
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        if not _one_needed(mobile_device_id=mobile_device_id, device_id=device_id):
            return False, None
        params = {}
        name, value = _which_used(mobile_device_id=mobile_device_id, device_id=device_id)
        if name:
            params[name] = value
        return 'delete_mobile_device', params

    @set_and_forget
    def delete_newsletter(self, newsletter_id: int) -> bool:
        """
        Remove a newsletter from the database

        :param newsletter_id: ID of the newsletter to delete
        :type newsletter_id: int
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return 'delete_newsletter', {'newsletter_id': newsletter_id}

    @set_and_forget
    def delete_newsletter_log(self) -> bool:
        """
        Delete the Tautulli newsletter logs

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return 'delete_newsletter_log', None

    @set_and_forget
    def delete_notification_log(self) -> bool:
        """
        Delete the Tautulli notification logs

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return 'delete_notification_log', None

    @set_and_forget
    def delete_notifier(self, notifier_id: int) -> bool:
        """
        Remove a notifier from the database

        :param notifier_id: ID of the notifier to delete
        :type notifier_id: int
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return 'delete_notifier', {'notifier_id': notifier_id}

    @set_and_forget
    def delete_recently_added(self) -> bool:
        """
        Flush all the recently added items in the database

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return 'delete_recently_added', None

    @set_and_forget
    def delete_synced_item(self, client_id: str, sync_id: str) -> bool:
        """
        Delete a synced item from a device

        :param client_id: Client ID of the device to delete from
        :type client_id: str
        :param sync_id: Sync ID of the synced item
        :type sync_id: str
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return 'delete_synced_item', {'client_id': client_id, 'sync_id': sync_id}

    @set_and_forget
    def delete_temp_sessions(self) -> bool:
        """
        Flush all temporary sessions in the database

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return 'delete_temp_sessions', None

    @set_and_forget
    def delete_user(self, user_id: str, row_ids: List[int] = None) -> bool:
        """
        Delete a user from Tautulli.
        Also erases all history of the user.

        :param user_id: ID of the Plex user
        :type user_id: str
        :param row_ids: List of row IDs to delete
        :type row_ids: list[int], optional
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        params = {'user_id': user_id}
        if row_ids:
            params['row_ids'] = int_list_to_string(int_list=row_ids)
        return 'delete_user', params

    @property
    def docs(self) -> dict:
        """
        Get the Tautulli API docs as a dict where commands are keys, docstring are value

        :returns: Dict of data
        :rtype: dict
        """
        json_data = self._get_json(command='docs')
        if _success_result(json_data=json_data):
            return _get_response_data(json_data=json_data)
        return static.empty_dict

    @property
    def docs_md(self) -> str:
        """
        Get the Tautulli API docs formatted with markdown

        :returns: API docs str
        :rtype: str
        """
        response = self._get(command='docs_md')
        if response:
            return response.text
        return static.empty_string

    def download_config(self) -> str:
        """
        Download the Tautulli configuration file

        :returns: Config file string
        :rtype: str
        """
        response = self._get(command='download_config')
        if response:
            return response.text
        return static.empty_string

    def download_database(self) -> bytes:
        """
        Download the Tautulli database file

        :returns: Database file byte array
        :rtype: bytes
        """
        response = self._get(command='download_database')
        if response:
            return response.content
        return static.empty_bytes

    def download_export(self, export_id: int) -> bytes:
        """
        Download an exported metadata file

        :returns: Metadata file byte array
        :rtype: bytes
        """
        params = {'export_id': export_id}
        response = self._get(command='download_export', params=params)
        if response:
            return response.content
        return static.empty_bytes

    def download_log(self, logfile: str = None) -> bytes:
        """
        Download the Tautulli log file

        :param logfile: Log file to download
        :type logfile: str, optional
        :returns: Log file byte array
        :rtype: bytes
        """
        if _is_invalid_choice(value=logfile, variable_name="logfile",
                              choices=static.logfile_types):
            return False, None
        params = build_optional_params(logfile=logfile)
        response = self._get(command='download_log', params=params)
        if response:
            return response.content
        return static.empty_bytes

    def download_plex_log(self, logfile: str = None) -> bytes:
        """
        Download the Plex log file

        :param logfile: Log file to download
        :type logfile: str, optional
        :returns: Log file byte array
        :rtype: bytes
        """
        if _is_invalid_choice(value=logfile, variable_name="logfile",
                              choices=static.plex_logfile_types):
            return False, None
        params = build_optional_params(logfile=logfile)
        response = self._get(command='download_plex_log', params=params)
        if response:
            return response.content
        return static.empty_bytes

    # optional or required params now?
    @set_and_forget
    def edit_library(self, section_id: str, custom_thumb: str = None, custom_art: str = None,
                     keep_history: bool = True) -> bool:
        """
        Update a library section on Tautulli

        :param section_id: ID of the Plex library section
        :type section_id: str
        :param custom_thumb: URL of the custom library thumbnail
        :type custom_thumb: str, optional
        :param custom_art: ULR of the custom library background art
        :type custom_art: str, optional
        :param keep_history: Whether to keep library history (default: True)
        :type keep_history: bool, optional
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        keep_history = bool_to_int(boolean=keep_history)
        params = build_optional_params(custom_thumb=custom_thumb, custom_art=custom_art, keep_history=keep_history)
        params['section_id'] = section_id
        return 'edit_library', params

    # optional or required params now?
    @set_and_forget
    def edit_user(self, user_id: str, friendly_name: str = None, custom_thumb: str = None, keep_history: bool = True,
                  allow_guest: bool = False) -> bool:
        """
        Update a user on Tautulli

        :param user_id: ID of the Plex user
        :type user_id: str
        :param friendly_name: Friendly name of the user
        :type friendly_name: str, optional
        :param custom_thumb: ULR of the custom user thumbnail
        :type custom_thumb: str, optional
        :param keep_history: Whether to keep user history (default: True)
        :type keep_history: bool, optional
        :param allow_guest: Whether to allow user as a guest (default: False)
        :type allow_guest: bool, optional
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        keep_history = bool_to_int(boolean=keep_history)
        allow_guest = bool_to_int(boolean=allow_guest)
        params = build_optional_params(friendly_name=friendly_name, custom_thumb=custom_thumb,
                                       keep_history=keep_history, allow_guest=allow_guest)
        params['user_id'] = user_id
        return 'edit_user', params

    @set_and_forget
    def export_metadata(self, section_id: int = None, user_id: int = None, rating_key: int = None,
                        file_format: str = 'csv', metadata_level: int = 1, media_info_level: int = 1,
                        thumb_level: int = 0, art_level: int = 0, custom_fields: List[str] = None,
                        export_type: str = None, individual_files: bool = False) -> bool:
        """
        Export library or media metadata to a file

        :param section_id: Section ID of the library items to export
        :type section_id: int, optional
        :param user_id: User ID of the playlist items to export
        :type user_id: int, optional
        :param rating_key: Rating key of the media items to export
        :type rating_key: int, optional
        :param file_format: File format for export (i.e. 'csv', 'json', 'xml', 'm3u') (default: 'csv')
        :type file_format: str, optional
        :param metadata_level: Level of metadata to export (default: 1)
        :type metadata_level: int, optional
        :param media_info_level: Level of media info to export (default: 1)
        :type media_info_level: int, optional
        :param thumb_level: Level of poster/cover images to export (default: 0)
        :type thumb_level: int, optional
        :param art_level: Level of background artwork images to export (default: 0)
        :type art_level: int, optional
        :param custom_fields: List of custom fields to export
        :type custom_fields: list[str], optional
        :param export_type: Type of export (i.e. 'collection' or 'playlist' for library/user export)
        :type export_type: str, optional
        :param individual_files: Export each item as an individual field for library/user export (default: False)
        :type individual_files: bool, optional
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        if not _one_needed(section_id=section_id, user_id=user_id, rating_key=rating_key):
            return False, None
        if _is_invalid_choice(value=file_format, variable_name="file_format",
                              choices=static.export_file_formats):
            return False, None
        if section_id or user_id:
            if _is_invalid_choice(value=export_type, variable_name="export_type",
                                  choices=static.export_media_types):
                return False, None
        if custom_fields:
            custom_fields = comma_delimit(custom_fields)
        params = build_optional_params(file_format=file_format, metadata_level=metadata_level,
                                       media_info_level=media_info_level, thumb_level=thumb_level, art_level=art_level,
                                       custom_fields=custom_fields, export_type=export_type,
                                       individual_files=individual_files)
        name, value = _which_used(section_id=section_id, user_id=user_id, rating_key=rating_key)
        if name:
            params[name] = value
        return 'export_metadata', params

    @raw_json
    def activity(self, session_key: int = None, session_id: str = None) -> dict:
        """
        Get the current activity on the Plex Media Server

        :param session_key: Session key for the session info to return
        :type session_key: int, optional
        :param session_id: Session ID of the session info to return
        :type session_id: str, optional
        :returns: Dict of data
        :rtype: dict
        """
        params = build_optional_params(session_key=session_key, session_id=session_id)
        return 'get_activity', params

    def get_api_key(self, username: str = None, password: str = None) -> Union[str, None]:
        """
        Get the Tautulli API key.
        Username and password are required if auth is enabled.
        Makes and saves the API key if it does not exist.

        :param username: Tautulli username
        :type username: str, optional
        :param password: Tautulli password
        :type password: str, optional
        :returns: API key
        :rtype: str or None
        """
        params = build_optional_params(username=username, password=password)
        json_data = self._get_json(command='get_apikey', params=params)
        if _success_result(json_data=json_data):
            return _get_response_data(json_data=json_data)
        return None

    @raw_json
    def get_children_metadata(self, rating_key: str, media_type: str) -> dict:
        """
        Get the metadata for the children of a media item.

        :param rating_key: The rating key of the media item
        :type rating_key: str
        :param media_type: The type of media item (movie, show, season, episode)
        :type media_type: str
        :returns: Dict of data
        :rtype: dict
        """
        return 'get_children_metadata', {'rating_key': rating_key, 'media_type': media_type}

    @raw_json
    def get_collections_table(self, section_id: str) -> dict:
        """
        Get the data on the Tautulli collections tables

        :param section_id: ID of the Plex library section
        :type section_id: str
        :returns: Dict of data
        :rtype: dict
        """
        return 'get_collections_table', {'section_id': section_id}

    @property
    @raw_json
    def date_formats(self) -> dict:
        """
        Get the data and time formats used by Tautulli

        :returns: Dict of data
        :rtype: dict
        """
        return 'get_date_formats', None

    @raw_json
    def get_export_fields(self, media_type: str, sub_media_type: str = None) -> dict:
        """
        Get a list of available custom export fields

        :param media_type: Media type of the fields to return
        :type media_type: str, optional
        :param sub_media_type: Child media type for collections (i.e. 'movie', 'show', 'video', 'audio', 'photo')
        :type sub_media_type: str, optional
        :returns: Dict of data
        :rtype: dict
        """
        if _is_invalid_choice(value=media_type, variable_name="media_type", choices=static.export_media_types):
            return False, None
        if sub_media_type:
            if media_type == 'collection':
                if _is_invalid_choice(value=sub_media_type, variable_name="sub_media_type",
                                      choices=static.collections_sub_media_types):
                    return False, None
            elif media_type == 'playlist':
                if _is_invalid_choice(value=sub_media_type, variable_name="sub_media_type",
                                      choices=static.playlist_sub_media_types):
                    return False, None
        params = build_optional_params(sub_media_type=sub_media_type)
        params['media_type'] = media_type
        return 'get_export_fields', params

    @raw_json
    def get_exports_table(self, section_id: str = None, user_id: str = None, rating_key: str = None,
                          order_column: str = None, order_direction: str = None, start: int = 0, length: int = 25,
                          search: str = None) -> dict:
        """
        Get the data on the Tautulli export tables

        :param section_id: ID of the Plex library section
        :type section_id: str, optional
        :param user_id: ID of the Plex user
        :type user_id: str, optional
        :param rating_key: Rating key of the exported item
        :type rating_key: str, optional
        :param order_column: Column to order data by (i.e. 'added_at', 'sort_title', 'last_played')
        :type order_column: str, optional
        :param order_direction: Direction to order the rows ('desc' or 'asc')
        :type order_direction: str, optional
        :param start: Row number to start from (default: 0)
        :type start: int, optional
        :param length: Number of items to return (default: 25)
        :type length: int, optional
        :param search: String to search for
        :type search: str, optional
        :returns: Dict of data
        :rtype: dict
        """
        if not _one_needed(section_id=section_id, user_id=user_id, rating_key=rating_key):
            return False, None
        if _is_invalid_choice(value=order_column, variable_name="order_column",
                              choices=static.exports_order_columns):
            return False, None
        if _is_invalid_choice(value=order_direction, variable_name="order_direction",
                              choices=static.order_direction):
            return False, None
        params = build_optional_params(order_column=order_column, order_dir=order_direction, start=start, length=length,
                                       search=search)
        name, value = _which_used(section_id=section_id, user_id=user_id, rating_key=rating_key)
        if name:
            params[name] = value
        return 'get_exports_table', params

    @raw_json
    def get_geoip_lookup(self, ip_address: str) -> dict:
        """
        Get the Geolocation info for an IP address

        :param ip_address: IP address to look up
        :type ip_address: str
        :returns: Dict of data
        :rtype: dict
        """
        return 'get_geoip_lookup', {'ip_address': ip_address}

    @raw_json
    def get_history(self, grouping: bool = False, include_activity: bool = False, user: str = None, user_id: int = None,
                    rating_key: int = None, parent_rating_key: int = None, grandparent_rating_key: int = None,
                    start_date: datetime = None, before: datetime = None, after: datetime = None,
                    section_id: int = None, media_type: str = None, transcode_decision: str = None, guid: str = None,
                    order_column: str = None, order_direction: str = None, start: int = 0, length: int = 25,
                    search: str = None) -> dict:
        """
        Get the Tautulli history

        :param grouping: Whether to group results (default: False)
        :type grouping: bool, optional
        :param include_activity: Whether to include activity (default: False)
        :type include_activity: bool, optional
        :param user: Name of user
        :type user: str, optional
        :param user_id: ID of user
        :type user_id: int, optional
        :param rating_key: Rating key of item
        :type rating_key: int, optional
        :param parent_rating_key: Parent rating key of item
        :type parent_rating_key: int, optional
        :param grandparent_rating_key: Grandparent rating key of item
        :type grandparent_rating_key: int, optional
        :param start_date: Exact date for results
        :type start_date: datetime, optional
        :param before: Results before and including the date
        :type before: datetime, optional
        :param after: Results after and including the date
        :type after: datetime, optional
        :param section_id: ID of section
        :type section_id: int, optional
        :param media_type: Media type (i.e. 'movie', 'episode', 'track', 'live', 'collection', 'playlist')
        :type media_type: str, optional
        :param transcode_decision: Transcode decision (i.e. 'direct play', 'copy', 'transcode')
        :type transcode_decision: str, optional
        :param guid: Plex GUID for an item (e.g. "com.plexapp.agents.thetvdb://121361/6/1")
        :type guid: str, optional
        :param order_column: Column to order data by (i.e. 'date', 'platform', 'full_title')
        :type order_column: str, optional
        :param order_direction: Direction to order the rows ('desc' or 'asc')
        :type order_direction: str, optional
        :param start: Row number to start from (default: 0)
        :type start: int, optional
        :param length: Number of items to return (default: 25)
        :type length: int, optional
        :param search: String to search for
        :type search: str, optional
        :returns: Dict of data
        :rtype: dict
        """
        grouping = bool_to_int(boolean=grouping)
        include_activity = bool_to_int(boolean=include_activity)
        start_date = datetime_to_string(datetime_object=start_date)
        before = datetime_to_string(datetime_object=before)
        after = datetime_to_string(datetime_object=after)
        if _is_invalid_choice(value=media_type, variable_name="media_type",
                              choices=static.history_media_types):
            return False, None
        if _is_invalid_choice(value=transcode_decision, variable_name="transcode_decision",
                              choices=static.transcode_decisions):
            return False, None
        if _is_invalid_choice(value=order_column, variable_name="order_column",
                              choices=static.history_order_columns):
            return False, None
        if _is_invalid_choice(value=order_direction, variable_name="order_direction",
                              choices=static.order_direction):
            return False, None
        params = build_optional_params(grouping=grouping, include_activity=include_activity, user=user, user_id=user_id,
                                       rating_key=rating_key, parent_rating_key=parent_rating_key,
                                       grandparent_rating_key=grandparent_rating_key, start_date=start_date,
                                       before=before, after=after, section_id=section_id, media_type=media_type,
                                       transcode_decision=transcode_decision, guid=guid, order_column=order_column,
                                       order_dir=order_direction, start=start, length=length, search=search)
        return 'get_history', params

    @raw_json
    def get_home_stats(self, grouping: bool = False, time_range: int = 30, stats_type: str = 'plays', start: int = 0,
                       count: int = 5, stat_id: str = None, user_id: int = None, section_id: int = None,
                       before: datetime = None, after: datetime = None) -> List[dict]:
        """
        Get the homepage watch statistics

        :param grouping: Whether to group results (default: False)
        :type grouping: bool, optional
        :param time_range: Time range to calculate statistics (i.e. 30)
        :type time_range: int, optional
        :param stats_type: Type of stats to get ('plays' or 'duration')
        :type stats_type: str, optional
        :param start: Row number to start from (default: 0)
        :type start: int, optional
        :param count: Number of items to return (default: 5)
        :type count: int, optional
        :param stat_id: Name of a single statistic to return (i.e. 'top_movies', 'popular_tv', 'most_concurrent')
        :type stat_id: str, optional
        :param user_id: The ID of the Plex user
        :type user_id: int, optional
        :param section_id: The ID of the Plex library section
        :type section_id: int, optional
        :param before: Results before and including the date
        :type before: datetime, optional
        :param after: Results after and including the date
        :type after: datetime, optional
        :returns: List of data
        :rtype: List[dict]
        """
        grouping = bool_to_int(boolean=grouping)
        if _is_invalid_choice(value=stats_type, variable_name="stats_type",
                              choices=static.stats_type):
            return False, None
        if _is_invalid_choice(value=stat_id, variable_name='stat_id',
                              choices=static.stats_category):
            return False, None
        before = datetime_to_string(datetime_object=before)
        after = datetime_to_string(datetime_object=after)
        params = build_optional_params(grouping=grouping, time_range=time_range, stats_type=stats_type,
                                       stats_start=start, stats_count=count, stat_id=stat_id, section_id=section_id,
                                       user_id=user_id, before=before, after=after)
        return 'get_home_stats', params

    @raw_json
    def get_item_user_stats(self, rating_key: str, grouping: bool = False, media_type: str = None) -> List[dict]:
        """
        Get the user statistics for the media item

        :param rating_key: Rating key of the media item
        :type rating_key: str
        :param grouping: Whether to group results (default: False)
        :type grouping: bool, optional
        :param media_type: Media type of the item (only required for a collection)
        :type media_type: str, optional
        :returns: List of data
        :rtype: List[dict]
        """
        grouping = bool_to_int(boolean=grouping)
        params = build_optional_params(rating_key=rating_key, grouping=grouping, media_type=media_type)
        return 'get_item_user_stats', params

    @raw_json
    def get_item_watch_time_stats(self, rating_key: str, grouping: bool = False, query_days: List[int] = None,
                                  media_type: str = None) \
            -> List[dict]:

        """
        Get the watch time stats for the media item

        :param rating_key: Rating key of the media item
        :type rating_key: str
        :param grouping: Whether to group results (default: False)
        :type grouping: bool, optional
        :param query_days: List of days to get results for (i.e. [0, 1, 14, 30])
        :type query_days: list[int], optional
        :param media_type: Media type of the item (only required for a collection)
        :type media_type: str, optional
        :returns: Dict of data
        :rtype: dict
        """
        grouping = bool_to_int(boolean=grouping)
        params = build_optional_params(grouping=grouping, media_type=media_type)
        params['rating_key'] = rating_key
        if query_days:
            params['query_days'] = int_list_to_string(int_list=query_days)
        return 'get_item_watch_time_stats', params

    @property
    @raw_json
    def libraries(self) -> List[dict]:
        """
        Get a list of all libraries on your server

        :returns: List of data
        :rtype: List[dict]
        """
        return 'get_libraries', None

    @raw_json
    def get_libraries_table(self, grouping: bool = False, order_column: str = None, order_direction: str = None,
                            start: int = 0, length: int = 25, search: str = None) -> dict:
        """
        Get the data on the Tautulli libraries table

        :param grouping: Whether to group results (default: False)
        :type grouping: bool, optional
        :param order_column: Column to order rows by (i.e. 'section_name', 'count', 'last_played')
        :type order_column: str, optional
        :param order_direction: Direction to order rows by ('desc' or 'asc')
        :type order_direction: str, optional
        :param start: Row number to start from (default: 0)
        :type start: int, optional
        :param length: Number of items to return (default: 25)
        :type length: int, optional
        :param search: String to search for
        :type search: str, optional
        :returns: Dict of data
        :rtype: dict
        """
        grouping = bool_to_int(boolean=grouping)
        if _is_invalid_choice(value=order_column, variable_name="order_column",
                              choices=static.libraries_order_columns):
            return False, None
        if _is_invalid_choice(value=order_direction, variable_name='order_direction',
                              choices=static.order_direction):
            return False, None
        params = build_optional_params(grouping=grouping, order_column=order_column, order_dir=order_direction,
                                       start=start, length=length, search=search)
        return 'get_libraries_table', params

    @raw_json
    def get_library(self, section_id: str, include_last_accessed: bool = False) -> dict:
        """
        Get a library's details

        :param section_id: ID of the Plex library section
        :type section_id: str
        :param include_last_accessed: Whether to include the last_accessed value for the library (default: False)
        :type include_last_accessed: bool, optional
        :returns: Dict of data
        :rtype: dict
        """
        params = build_optional_params(section_id=section_id, include_last_accessed=include_last_accessed)
        return 'get_library', params

    @raw_json
    def get_library_media_info(self, section_id: str = None, rating_key: str = None, section_type: str = None,
                               order_column: str = None, order_direction: str = None, start: int = 0, length: int = 25,
                               search: str = None, refresh: bool = False) -> dict:
        """
        Get the data on the Tautulli media info tables.

        :param section_id: ID of the Plex library section
        :type section_id: str
        :param rating_key: Grandparent or parent rating key
        :type rating_key: str
        :param section_type: Type of section (i.e. 'movie', 'show', 'artist', 'photo')
        :type section_type: str
        :param order_column: Column to order rows by (i.e. 'added_at', 'sort_title', 'file_size')
        :type order_column: str, optional
        :param order_direction: Direction to order rows ('desc' or 'asc')
        :type order_direction: str, optional
        :param start: Row number to start from (default: 0)
        :type start: int, optional
        :param length: Number of items to return (default: 25)
        :type length: int, optional
        :param search: String to search for
        :type search: str, optional
        :param refresh: Whether to refresh the media info table (default: False)
        :type refresh: bool, optional
        :returns: Dict of data
        :rtype: dict
        """
        if not _one_needed(section_id=section_id, rating_key=rating_key):
            return False, None
        if _is_invalid_choice(value=section_type, variable_name="section_type",
                              choices=static.library_media_info_types):
            return False, None
        if _is_invalid_choice(value=order_column, variable_name="order_column",
                              choices=static.library_order_columns):
            return False, None
        if _is_invalid_choice(value=order_direction, variable_name='order_direction',
                              choices=static.order_direction):
            return False, None
        params = build_optional_params(section_type=section_type, order_column=order_column, order_dir=order_direction,
                                       start=start, length=length, search=search, refresh=refresh)
        name, value = _which_used(section_id=section_id, rating_key=rating_key)
        if name:
            params[name] = value
        return 'get_library_media_info', params

    @property
    @raw_json
    def library_names(self) -> List[dict]:
        """
        Get list of library names and IDs on the Plex Media Server

        :returns: List of names
        :rtype: list[str]
        """
        return 'get_library_names', None

    @raw_json
    def get_library_user_stats(self, section_id: str, grouping: bool = False) -> dict:
        """
        Get a library's user statistics

        :param section_id: ID of the Plex library section
        :type section_id: str
        :param grouping: Whether to group results (default: False)
        :type grouping: bool, optional
        :returns: Dict of data
        :rtype: dict
        """
        grouping = bool_to_int(boolean=grouping)
        params = build_optional_params(grouping=grouping)
        params['section_id'] = section_id
        return 'get_library_user_stats', params

    @raw_json
    def get_library_watch_time_stats(self, section_id: str, grouping: bool = False,
                                     query_days: List[int] = None) -> dict:
        """
        Get a library's watch time statistics

        :param section_id: ID of the Plex library section
        :type section_id: str
        :param grouping: Whether to group results (default: False)
        :type grouping: bool, optional
        :param query_days: List of days to get results for (i.e. [0, 1, 14, 30])
        :type query_days: list[int], optional
        :returns: Dict of data
        :rtype: dict
        """
        grouping = bool_to_int(boolean=grouping)
        params = build_optional_params(grouping=grouping)
        params['section_id'] = section_id
        if query_days:
            params['query_days'] = int_list_to_string(int_list=query_days)
        return 'get_library_watch_time_stats', params

    @raw_json
    def get_logs(self, sort: str = None, search: str = None, order_direction: str = None, regex: str = None,
                 start: int = None, end: int = None) -> List[dict]:
        """
        Get the Tautulli logs

        :param sort: What to sort the logs by (i.e. 'time', 'thread', 'msg', 'loglevel')
        :type sort: str, optional
        :param search: String to search for
        :type search: str, optional
        :param order_direction: Direction to order rows ('desc' or 'asc')
        :type order_direction: str, optional
        :param regex: Regex string to search for
        :type regex: str, optional
        :param start: Row number to start from
        :type start: int, optional
        :param end: Row number to end at
        :type end: int, optional
        :returns: List of data
        :rtype: List[dict]
        """
        if _is_invalid_choice(value=sort, variable_name='sort',
                              choices=static.log_sorting):
            return False, None
        if _is_invalid_choice(value=order_direction, variable_name='order_direction',
                              choices=static.order_direction):
            return False, None
        params = build_optional_params(sort=sort, search=search, order=order_direction, regex=regex, start=start,
                                       end=end)
        return 'get_logs', params

    @raw_json
    def get_metadata(self, rating_key: str = None, sync_id: str = None) -> dict:
        """
        Get the metadata for a media item

        :param rating_key: Rating key of the media item
        :type rating_key: str, optional
        :param sync_id: Sync ID of a synced item
        :type sync_id: str, optional
        :returns: Dict of data
        :rtype: dict
        """
        if not _one_needed(sync_id=sync_id, rating_key=rating_key):
            return False, None
        params = {}
        name, value = _which_used(sync_id=sync_id, rating_key=rating_key)
        if name:
            params[name] = value
        return 'get_metadata', params

    @raw_json
    def get_new_rating_keys(self, rating_key: str, media_type: str) -> dict:
        """
        Get a list of new rating keys for the Plex Media Server of all the item's parent/children

        :param rating_key: Rating key of item
        :type rating_key: str
        :param media_type: Type of media (i.e. 'movie', 'show', 'episode', 'album', 'track')
        :type media_type: str
        :returns: Dict of data
        :rtype: dict
        """
        if _is_invalid_choice(value=media_type, variable_name='media_type',
                              choices=static.all_media_types):
            return False, None
        params = {'rating_key': rating_key, 'media_type': media_type}
        return 'get_new_rating_keys', params

    @raw_json
    def get_newsletter_config(self, newsletter_id: int) -> dict:
        """
        Get the configuration for an existing newsletter agent

        :param newsletter_id: ID of the newsletter
        :type newsletter_id: int
        :returns: Dict of data
        :rtype: dict
        """
        return 'get_newsletter_config', {'newsletter_id': newsletter_id}

    @raw_json
    def get_newsletter_log(self, order_column: str = None, order_direction: str = None, start: int = 0,
                           length: int = 25, search: str = None) -> dict:
        """
        Get the data on the Tautulli newsletter logs table

        :param order_column: Column to order rows by (i.e. 'timestamp', 'newsletter_id', 'start_date')
        :type order_column: str, optional
        :param order_direction: Direction to order rows ('desc' or 'asc')
        :type order_direction: str, optional
        :param start: Row number to start from (default: 0)
        :type start: int, optional
        :param length: Number of items to return (default: 25)
        :type length: int, optional
        :param search: String to search for
        :type search: str, optional
        :returns: Dict of data
        :rtype: dict
        """
        if _is_invalid_choice(value=order_column, variable_name='order_column',
                              choices=static.newsletter_order_column):
            return False, None
        if _is_invalid_choice(value=order_direction, variable_name='order_direction',
                              choices=static.order_direction):
            return False, None
        params = build_optional_params(order_column=order_column, order_dir=order_direction, start=start, length=length,
                                       search=search)
        return 'get_newsletter_log', params

    @property
    @raw_json
    def newsletters(self) -> List[dict]:
        """
        Get a list of configured newsletters

        :returns: List of data
        :rtype: List[dict]
        """
        return 'get_newsletters', None

    @raw_json
    def get_notification_log(self, order_column: str = None, order_direction: str = None, start: int = 0,
                             length: int = 25, search: str = None) -> dict:
        """
        Get the data on the Tautulli notification logs table

        :param order_column: Column to order rows by (i.e. 'timestamp', 'agent_name', 'notifier_id')
        :type order_column: str, optional
        :param order_direction: Direction to order rows ('desc' or 'asc')
        :type order_direction: str, optional
        :param start: Row number to start from (default: 0)
        :type start: int, optional
        :param length: Number of items to return (default: 25)
        :type length: int, optional
        :param search: String to search for
        :type search: str, optional
        :returns: Dict of data
        :rtype: dict
        """
        if _is_invalid_choice(value=order_column, variable_name='order_column',
                              choices=static.notifications_order_column):
            return False, None
        if _is_invalid_choice(value=order_direction, variable_name='order_direction',
                              choices=static.order_direction):
            return False, None
        params = build_optional_params(order_column=order_column, order_dir=order_direction, start=start, length=length,
                                       search=search)
        return 'get_notification_log', params

    @raw_json
    def get_notifier_config(self, notifier_id: int) -> dict:
        """
        Get the configuration for an existing notification agent

        :param notifier_id: ID of the notifier
        :type notifier_id: int
        :returns: Dict of data
        :rtype: dict
        """
        return 'get_notifier_config', {'notifier_id': notifier_id}

    @property
    @raw_json
    def notifier_parameters(self) -> List[dict]:
        """
        Get a list of available notification parameters

        :returns: List of data
        :rtype: List[dict]
        """
        return 'get_notifier_parameters', None

    @raw_json
    def get_notifiers(self, notify_action: str = None) -> List[dict]:
        """
        Get a list of configured notifiers

        :param notify_action: The notification action to filter out
        :type notify_action: str, optional
        :returns: List of data
        :rtype: List[dict]
        """
        params = build_optional_params(notify_action=notify_action)
        return 'get_notifiers', params

    @raw_json
    def get_old_rating_keys(self, rating_key: str, media_type: str) -> dict:
        """
        Get a list of old rating keys from the Tautulli database for all the item's parent/children

        :param rating_key: Rating key of item
        :type rating_key: str
        :param media_type: Type of media (i.e. 'movie', 'show', 'episode', 'album', 'track')
        :type media_type: str
        :returns: Dict of data
        :rtype: dict
        """
        if _is_invalid_choice(value=media_type, variable_name='media_type',
                              choices=static.all_media_types):
            return False, None
        params = {'rating_key': rating_key, 'media_type': media_type}
        return 'get_old_rating_keys', params

    @raw_json
    def get_playlists_table(self, section_id: str = None, user_id: str = None) -> dict:
        """
        Get the data on the Tautulli playlists tables

        :param section_id: Section ID of the Plex library
        :type section_id: str, optional
        :param user_id: User ID of the Plex user
        :type user_id: str, optional
        :returns: Dict of data
        :rtype: dict
        """
        if not _one_needed(section_id=section_id, user_id=user_id):
            return False, None
        params = {}
        name, value = _which_used(section_id=section_id, user_id=user_id)
        if name:
            params[name] = value
        return 'get_playlists_table', params

    def get_plays_by_date(self, time_range: int = None, y_axis: str = None, user_ids: List[str] = None,
                          grouping: bool = False) -> dict:
        """
        Get graph data by date

        :param time_range: Number of days of data to return
        :type time_range: int, optional
        :param y_axis: Stat type ('plays' or 'duration')
        :type y_axis: str, optional
        :param user_ids: List of user IDs to filter data
        :type user_ids: List[str], optional
        :param grouping: Whether to group the results (default: False)
        :type grouping: bool, optional
        :returns: Dict of data
        :rtype: dict
        """
        return self._get_x_by(endpoint='get_plays_by_date', time_range=time_range, y_axis=y_axis, user_ids=user_ids,
                              grouping=grouping)

    def get_plays_by_day_of_week(self, time_range: int = None, y_axis: str = None, user_ids: List[str] = None,
                                 grouping: bool = False) -> dict:
        """
        Get graph data by day of the week

        :param time_range: Number of days of data to return
        :type time_range: int, optional
        :param y_axis: Stat type ('plays' or 'duration')
        :type y_axis: str, optional
        :param user_ids: List of user IDs to filter data
        :type user_ids: List[str], optional
        :param grouping: Whether to group the results (default: False)
        :type grouping: bool, optional
        :returns: Dict of data
        :rtype: dict
        """
        return self._get_x_by(endpoint='get_plays_by_dayofweek', time_range=time_range, y_axis=y_axis,
                              user_ids=user_ids,
                              grouping=grouping)

    def get_plays_by_hour_of_day(self, time_range: int = None, y_axis: str = None, user_ids: List[str] = None,
                                 grouping: bool = False) -> dict:
        """
        Get graph data by hour of the day

        :param time_range: Number of days of data to return
        :type time_range: int, optional
        :param y_axis: Stat type ('plays' or 'duration')
        :type y_axis: str, optional
        :param user_ids: List of user IDs to filter data
        :type user_ids: List[str], optional
        :param grouping: Whether to group the results (default: False)
        :type grouping: bool, optional
        :returns: Dict of data
        :rtype: dict
        """
        # noinspection SpellCheckingInspection
        return self._get_x_by(endpoint='get_plays_by_hourofday', time_range=time_range, y_axis=y_axis,
                              user_ids=user_ids,
                              grouping=grouping)

    def get_plays_by_source_resolution(self, time_range: int = None, y_axis: str = None, user_ids: List[str] = None,
                                       grouping: bool = False) -> dict:
        """
        Get graph data by source resolution

        :param time_range: Number of days of data to return
        :type time_range: int, optional
        :param y_axis: Stat type ('plays' or 'duration')
        :type y_axis: str, optional
        :param user_ids: List of user IDs to filter data
        :type user_ids: List[str], optional
        :param grouping: Whether to group the results (default: False)
        :type grouping: bool, optional
        :returns: Dict of data
        :rtype: dict
        """
        return self._get_x_by(endpoint='get_plays_by_source_resolution', time_range=time_range, y_axis=y_axis,
                              user_ids=user_ids, grouping=grouping)

    def get_plays_by_stream_resolution(self, time_range: int = None, y_axis: str = None, user_ids: List[str] = None,
                                       grouping: bool = False) -> dict:
        """
        Get graph data by stream resolution

        :param time_range: Number of days of data to return
        :type time_range: int, optional
        :param y_axis: Stat type ('plays' or 'duration')
        :type y_axis: str, optional
        :param user_ids: List of user IDs to filter data
        :type user_ids: List[str], optional
        :param grouping: Whether to group the results (default: False)
        :type grouping: bool, optional
        :returns: Dict of data
        :rtype: dict
        """
        return self._get_x_by(endpoint='get_plays_by_stream_resolution', time_range=time_range, y_axis=y_axis,
                              user_ids=user_ids, grouping=grouping)

    def get_plays_by_stream_type(self, time_range: int = None, y_axis: str = None, user_ids: List[str] = None,
                                 grouping: bool = False) -> dict:
        """
        Get graph data by stream type

        :param time_range: Number of days of data to return
        :type time_range: int, optional
        :param y_axis: Stat type ('plays' or 'duration')
        :type y_axis: str, optional
        :param user_ids: List of user IDs to filter data
        :type user_ids: List[str], optional
        :param grouping: Whether to group the results (default: False)
        :type grouping: bool, optional
        :returns: Dict of data
        :rtype: dict
        """
        return self._get_x_by(endpoint='get_plays_by_stream_type', time_range=time_range, y_axis=y_axis,
                              user_ids=user_ids, grouping=grouping)

    def get_plays_by_top_10_platforms(self, time_range: int = None, y_axis: str = None, user_ids: List[str] = None,
                                      grouping: bool = False) -> dict:
        """
        Get graph data by top 10 platforms

        :param time_range: Number of days of data to return
        :type time_range: int, optional
        :param y_axis: Stat type ('plays' or 'duration')
        :type y_axis: str, optional
        :param user_ids: List of user IDs to filter data
        :type user_ids: List[str], optional
        :param grouping: Whether to group the results (default: False)
        :type grouping: bool, optional
        :returns: Dict of data
        :rtype: dict
        """
        return self._get_x_by(endpoint='get_plays_by_top_10_platforms', time_range=time_range, y_axis=y_axis,
                              user_ids=user_ids, grouping=grouping)

    def get_plays_by_top_10_users(self, time_range: int = None, y_axis: str = None, user_ids: List[str] = None,
                                  grouping: bool = False) -> dict:
        """
        Get graph data by top 10 users

        :param time_range: Number of days of data to return
        :type time_range: int, optional
        :param y_axis: Stat type ('plays' or 'duration')
        :type y_axis: str, optional
        :param user_ids: List of user IDs to filter data
        :type user_ids: List[str], optional
        :param grouping: Whether to group the results (default: False)
        :type grouping: bool, optional
        :returns: Dict of data
        :rtype: dict
        """
        return self._get_x_by(endpoint='get_plays_by_top_10_users', time_range=time_range, y_axis=y_axis,
                              user_ids=user_ids, grouping=grouping)

    def get_plays_per_month(self, time_range: int = None, y_axis: str = None, user_ids: List[str] = None,
                            grouping: bool = False) -> dict:
        """
        Get graph data by month

        :param time_range: Number of days of data to return
        :type time_range: int, optional
        :param y_axis: Stat type ('plays' or 'duration')
        :type y_axis: str, optional
        :param user_ids: List of user IDs to filter data
        :type user_ids: List[str], optional
        :param grouping: Whether to group the results (default: False)
        :type grouping: bool, optional
        :returns: Dict of data
        :rtype: dict
        """
        return self._get_x_by(endpoint='get_plays_per_month', time_range=time_range, y_axis=y_axis, user_ids=user_ids,
                              grouping=grouping)

    @raw_json
    def get_plex_log(self, window: int = None, logfile: str = None) -> dict:
        """
        Get the Plex Media Server logs

        :param window: Number of tail lines to return
        :type window: int, optional
        :param logfile: Log file to download
        :type logfile: str, optional
        :returns: Dict of data
        :rtype: dict
        """
        if _is_invalid_choice(value=logfile, variable_name='logfile',
                              choices=static.plex_logfile_types):
            return False, None
        params = build_optional_params(window=window, logfile=logfile)
        return 'get_plex_log', params

    @property
    @raw_json
    def pms_update(self) -> dict:
        """
        Check for updates to the Plex Media Server

        :returns: Dict of data
        :rtype: dict
        """
        return 'get_pms_update', None

    @raw_json
    def get_recently_added(self, count: int, start: int = 0, media_type: str = None, section_id: str = None) -> dict:
        """
        Get all items that were recently added to Plex

        :param count: Number of item to return
        :type count: int
        :param start: Item number to start from
        :type start: int, optional
        :param media_type: Media type (i.e. 'movie', 'show', 'artist')
        :type media_type: str, optional
        :param section_id: ID of the Plex library section
        :type section_id: str, optional
        :returns: Dict of data
        :rtype: dict
        """
        if _is_invalid_choice(value=media_type, variable_name='media_type',
                              choices=static.recently_added_media_types):
            return False, None
        params = build_optional_params(start=start, media_type=media_type, section_id=section_id)
        params['count'] = count
        return 'get_recently_added', params

    @property
    def server_friendly_name(self) -> str:
        """
        Get the name of the Plex Media Server

        :returns: Name of the Plex Media Server
        :rtype: str
        """
        json_data = self._get_json(command='get_server_friendly_name')
        if _success_result(json_data=json_data):
            return _get_response_data(json_data=json_data)
        return static.empty_string

    @raw_json
    def get_server_id(self, hostname: str, port: int, ssl: bool = False, remote: bool = False) -> dict:
        """
        Get the Plex Media Server identifier

        :param hostname: IP address of the Plex Media Server
        :type hostname: str
        :param port: Port of the Plex Media Server
        :type port: int
        :param ssl: Whether to use SSL (default: False)
        :type ssl: bool, optional
        :param remote: Whether the Plex Media Server is remote (default: False)
        :type remote: bool, optional
        :returns: Dict of data
        :rtype: dict
        """
        ssl = bool_to_int(boolean=ssl)
        remote = bool_to_int(boolean=remote)
        params = build_optional_params(ssl=ssl, remote=remote)
        params['hostname'] = hostname
        params['port'] = port
        return 'get_server_id', params

    @property
    @raw_json
    def server_identity(self) -> dict:
        """
        Get info about the local server

        :returns: Dict of data
        :rtype: dict
        """
        return 'get_server_identity', None

    @property
    @raw_json
    def server_info(self) -> dict:
        """
        Get the Plex Media Server information

        :returns: Dict of data
        :rtype: dict
        """
        return 'get_server_info', None

    @property
    @raw_json
    def server_list(self) -> List[dict]:
        """
        Get all your servers that are published to Plex.tv

        :returns: List of data
        :rtype: List[dict]
        """
        return 'get_server_list', None

    def get_server_pref(self, pref: str) -> str:
        """
        Get a specified Plex Media Server preference

        :param pref: Name of preference
        :type pref: str
        :returns: Value of preference
        :rtype: str
        """
        json_data = self._get_json(command='get_server_pref', params={'pref': pref})
        if _success_result(json_data=json_data):
            return _get_response_data(json_data=json_data)
        return static.empty_string

    @property
    @raw_json
    def servers_info(self) -> List[dict]:
        """
        Get info about the Plex Media Server

        :returns: List of data
        :rtype: List[dict]
        """
        return 'get_servers_info', None

    @raw_json
    def get_settings(self, key: str = None) -> dict:
        """
        Get all settings from the config file

        :param key: Name of a config section to return
        :type key: str, optional
        :returns: Dict of data
        :rtype: dict
        """
        params = build_optional_params(key=key)
        return 'get_settings', params

    @raw_json
    def get_stream_data(self, row_id: int = None, session_key: int = None) -> dict:
        """
        Get the details of a stream from history or current stream

        :param row_id: Row ID number for a history item
        :type row_id: int, optional
        :param session_key: Session key for the current stream
        :type session_key: int, optional
        :returns: Dict of data
        :rtype: dict
        """
        if not _one_needed(row_id=row_id, session_key=session_key):
            return False, None
        params = {}
        name, value = _which_used(row_id=row_id, session_key=session_key)
        if name:
            params[name] = value
        return 'get_stream_data', params

    def get_stream_type_by_top_10_platforms(self, time_range: int = None, y_axis: str = None,
                                            user_ids: List[str] = None,
                                            grouping: bool = False) -> dict:
        """
        Get graph data by stream type by the top 10 platforms

        :param time_range: Number of days of data to return
        :type time_range: int, optional
        :param y_axis: Stat type ('plays' or 'duration')
        :type y_axis: str, optional
        :param user_ids: List of user IDs to filter data
        :type user_ids: List[str], optional
        :param grouping: Whether to group the results (default: False)
        :type grouping: bool, optional
        :returns: Dict of data
        :rtype: dict
        """
        return self._get_x_by(endpoint='get_stream_type_by_top_10_platforms', time_range=time_range, y_axis=y_axis,
                              user_ids=user_ids, grouping=grouping)

    def get_stream_type_by_top_10_users(self, time_range: int = None, y_axis: str = None, user_ids: List[str] = None,
                                        grouping: bool = False) -> dict:
        """
        Get graph data by stream type by the top 10 users

        :param time_range: Number of days of data to return
        :type time_range: int, optional
        :param y_axis: Stat type ('plays' or 'duration')
        :type y_axis: str, optional
        :param user_ids: List of user IDs to filter data
        :type user_ids: List[str], optional
        :param grouping: Whether to group the results (default: False)
        :type grouping: bool, optional
        :returns: Dict of data
        :rtype: dict
        """
        return self._get_x_by(endpoint='get_stream_type_by_top_10_users', time_range=time_range, y_axis=y_axis,
                              user_ids=user_ids, grouping=grouping)

    @raw_json
    def get_synced_items(self, machine_id: str = None, user_id: str = None) -> dict:
        """
        Get a list of synced items on the Plex Media Server

        :param machine_id: Plex Media Server identifier
        :type machine_id: str, optional
        :param user_id: ID of the Plex user
        :type user_id: str, optional
        :returns: Dict of data
        :rtype: dict
        """
        params = build_optional_params(machine_id=machine_id, user_id=user_id)
        return 'get_synced_items', params

    @property
    @raw_json
    def tautulli_info(self) -> dict:
        """
        Get the Tautulli server information

        :returns: Dict of data
        :rtype: dict
        """
        return 'get_tautulli_info', None

    @raw_json
    def get_user(self, user_id: str, include_last_seen: bool = False) -> dict:
        """
        Get a user's details

        :param user_id: ID of the Plex user
        :type user_id: str
        :param include_last_seen: Whether to include the last_seen value for the user (default: False)
        :type include_last_seen: bool, optional
        :returns: Dict of data
        :rtype: dict
        """
        params = build_optional_params(user_id=user_id, include_last_seen=include_last_seen)
        return 'get_user', params

    @raw_json
    def get_user_ips(self, user_id: str, order_column: str = None, order_direction: str = None, start: int = 0,
                     length: int = 25, search: str = None) -> dict:
        """
        Get the data on Tautulli's users IP table

        :param user_id: ID of the Plex user
        :type user_id: str
        :param order_column: Column to order rows by (i.e. 'last_seen', 'ip_address', 'player')
        :type order_column: str, optional
        :param order_direction: Direction to order rows ('desc' or 'asc')
        :type order_direction: str, optional
        :param start: Row number to start from (default: 0)
        :type start: int, optional
        :param length: Number of items to return (default: 25)
        :type length: int, optional
        :param search: String to search for (e.g. "xxx.xxx.xxx.xxx")
        :type search: str, optional
        :returns: Dict of data
        :rtype: dict
        """
        if _is_invalid_choice(value=order_column, variable_name='order_column',
                              choices=static.user_ips_order_columns):
            return False, None
        if _is_invalid_choice(value=order_direction, variable_name='order_direction',
                              choices=static.order_direction):
            return False, None
        params = build_optional_params(order_column=order_column, order_dir=order_direction, start=start, length=length,
                                       search=search)
        params['user_id'] = user_id
        return 'get_user_ips', params

    @raw_json
    def get_user_logins(self, user_id: str, order_column: str = None, order_direction: str = None, start: int = 0,
                        length: int = 25, search: str = None) -> dict:
        """
        Get the data on Tautulli's user login table

        :param user_id: ID of the Plex user
        :type user_id: str
        :param order_column: Column to order rows by (i.e. 'date', 'time', 'ip_address')
        :type order_column: str, optional
        :param order_direction: Direction to order rows ('desc' or 'asc')
        :type order_direction: str, optional
        :param start: Row number to start from (default: 0)
        :type start: int, optional
        :param length: Number of items to return (default: 25)
        :type length: int, optional
        :param search: String to search for (e.g. "xxx.xxx.xxx.xxx")
        :type search: str, optional
        :returns: Dict of data
        :rtype: dict
        """
        if _is_invalid_choice(value=order_column, variable_name='order_column',
                              choices=static.user_logins_order_columns):
            return False, None
        if _is_invalid_choice(value=order_direction, variable_name='order_direction',
                              choices=static.order_direction):
            return False, None
        params = build_optional_params(order_column=order_column, order_dir=order_direction, start=start, length=length,
                                       search=search)
        params['user_id'] = user_id
        return 'get_user_logins', params

    @property
    @raw_json
    def user_names(self) -> List[dict]:
        """
        Get a list of all usernames and user ids

        :returns: List of data
        :rtype: List[dict]
        """
        return 'get_user_names', None

    @raw_json
    def get_user_player_stats(self, user_id: str, grouping: bool = False) -> dict:
        """
        Get a user's player statistics

        :param user_id: ID of the Plex user
        :type user_id: str
        :param grouping: Whether to group results (default: False)
        :type grouping: bool, optional
        :returns: Dict of data
        :rtype: dict
        """
        grouping = bool_to_int(boolean=grouping)
        params = build_optional_params(grouping=grouping)
        params['user_id'] = user_id
        return 'get_user_player_stats', params

    @raw_json
    def get_user_watch_time_stats(self, user_id: str, grouping: bool = False, query_days: List[int] = None) -> dict:
        """
        Get a user's watch time statistics

        :param user_id: ID of the Plex user
        :type user_id: str
        :param grouping: Whether to group results (default: False)
        :type grouping: bool, optional
        :param query_days: List of days to get results for (e.g. [0, 1, 14, 30])
        :type query_days: list[int], optional
        :returns: Dict of data
        :rtype: dict
        """
        grouping = bool_to_int(boolean=grouping)
        params = build_optional_params(grouping=grouping)
        if query_days:
            params['query_days'] = int_list_to_string(int_list=query_days)
        params['user_id'] = user_id
        return 'get_user_watch_time_stats', params

    @property
    @raw_json
    def users(self) -> List[dict]:
        """
        Get a list of all users that have access to your server

        :returns: List of data
        :rtype: List[dict]
        """
        return 'get_users', None

    @raw_json
    def get_users_table(self, grouping: bool = False, order_column: str = None, order_direction: str = None,
                        start: int = 0, length: int = 25, search: str = None) -> dict:
        """
        Get the data on Tautulli's users table

        :param grouping: Whether to group results (default: False)
        :type grouping: bool, optional
        :param order_column: Column to order rows by ('friendly_name', 'ip_address', 'player')
        :type order_column: str, optional
        :param order_direction: Direction to order rows ('desc' or 'asc')
        :type order_direction: str, optional
        :param start: Row number to start from (default: 0)
        :type start: int, optional
        :param length: Number of items to return (default: 25)
        :type length: int, optional
        :param search: String to search for
        :type search: str, optional
        :returns: Dict of data
        :rtype: dict
        """
        grouping = bool_to_int(boolean=grouping)
        if _is_invalid_choice(value=order_column, variable_name='order_column',
                              choices=static.user_logins_order_columns):
            return False, None
        if _is_invalid_choice(value=order_direction, variable_name='order_direction',
                              choices=static.order_direction):
            return False, None
        params = build_optional_params(grouping=grouping, order_column=order_column, order_dir=order_direction,
                                       start=start, length=length, search=search)
        return 'get_users_table', params

    @raw_json
    def get_whois_lookup(self, ip_address: str) -> dict:
        """
        Get the connection info for an IP address

        :param ip_address: IP address
        :type ip_address: str
        :returns: Dict of data
        :rtype: dict
        """
        return 'get_whois_lookup', {'ip_address': ip_address}

    @set_and_forget
    def import_config(self, config_file_path: str, backup: bool = True) -> bool:
        """
        Import a Tautulli config file

        :param config_file_path: Full path to the config file to import
        :type config_file_path: str
        :param backup: Whether to back up the current config before importing (default: True)
        :type backup: bool, optional
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return 'import_config', {'config_path': config_file_path, 'backup': backup}

    @set_and_forget
    def import_database(self, app: str, database_file_path: str, method: str = None, table_name: str = None,
                        backup: bool = True, import_ignore_interval: int = None) -> bool:
        """
        Import a Tautulli, PlexWatch or Plexivity database into Tautulli

        :param app: Type of app the database is from ('tautulli', 'plexwatch' or 'plexivity')
        :type app: str
        :param database_file_path: Full path to the database file to import
        :type database_file_path: str
        :param method: Only if app is 'tautulli', method to import database ('merge' or 'overwrite')
        :type method: str, optional
        :param table_name: Only if app is 'plexwatch' or 'plexivity', table name to import ('processed' or 'grouped')
        :type table_name: str, optional
        :param backup: Whether to back up the current database before importing (default: True)
        :type backup: bool, optional
        :param import_ignore_interval: Only if app is 'plexwatch' or 'plexivity', the minimum number of seconds for a stream to import
        :type import_ignore_interval: int, optional
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        if _is_invalid_choice(value=app, variable_name='app',
                              choices=static.database_app_types):
            return False, None
        if app == 'tautulli':
            if _is_invalid_choice(value=method, variable_name='method',
                                  choices=static.tautulli_database_import_methods):
                return False, None
        if app in ['plexivity', 'plexwatch']:
            if _is_invalid_choice(value=table_name, variable_name='table_name',
                                  choices=static.plexivity_table_names):
                return False, None
        params = build_optional_params(method=method, table_name=table_name, backup=backup,
                                       import_ignore_interval=import_ignore_interval)
        params['app'] = app
        params['database_path'] = database_file_path
        return 'import_database', params

    @set_and_forget
    def logout_user_session(self, row_ids: List[int]) -> bool:
        """
        Logout Tautulli user sessions

        :param row_ids: List of row IDS to sign out
        :type row_ids: list[int], optional
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return 'logout_user_session', {'row_ids': int_list_to_string(int_list=row_ids)}

    @raw_json
    def notify(self, notifier_id: int, subject: str, body: str, headers: str = None, script_args: str = None) -> dict:
        """
        Send a notification using Tautulli

        :param notifier_id: ID of the notification agent
        :type notifier_id: int
        :param subject: Subject of the message
        :type subject: str
        :param body: Body of the message
        :type body: str
        :param headers: JSON headers for webhook notifications
        :type headers: str, optional
        :param script_args: Arguments for script notifications
        :type script_args: str, optional
        :returns: Dict of data
        :rtype: dict
        """
        params = build_optional_params(headers=headers, script_args=script_args)
        params['notifier_id'] = notifier_id
        params['subject'] = subject
        params['body'] = body
        return 'notify', params

    @raw_json
    def notify_newsletter(self, newsletter_id: int, subject: str = None, body: str = None, message: str = None) -> dict:
        """
        Send a newsletter using Tautulli

        :param newsletter_id: ID of the newsletter agent
        :type newsletter_id: int
        :param subject: Subject of the newsletter
        :type subject: str, optional
        :param body: Body of the newsletter
        :type body: str, optional
        :param message: Message of the newsletter
        :type message: str, optional
        :returns: Dict of data
        :rtype: dict
        """
        params = build_optional_params(subject=subject, body=body, message=message)
        params['newsletter_id'] = newsletter_id
        return 'notify_newsletter', params

    @set_and_forget
    def notify_recently_added(self, rating_key: int, notifier_id: int = None) -> bool:
        """
        Send a recently added notification using Tautulli

        :param rating_key: Rating key for the media item
        :type rating_key: int
        :param notifier_id: ID of the notification agent. Notification will be sent to all enabled notification agents if notifier_id is not provided.
        :type notifier_id: int, optional
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        params = build_optional_params(notifier_id=notifier_id)
        params['rating_key'] = rating_key
        return 'notify_recently_added', params

    def pms_image_proxy(self, img: str = None, rating_key: str = None, width: int = None, height: int = None,
                        opacity: int = None, background_hex: str = None, blur: int = None, img_format: str = 'png',
                        fallback: str = None, refresh: bool = False) -> bytes:
        """
        Gets an image from the Plex Media Server and saves it to the image cache directory

        :param img: Path of image (e.g. "/library/metadata/153037/thumb/1462175060")
        :type img: str, optional
        :param rating_key: Rating key of image
        :type rating_key: str, optional
        :param width: Width of image
        :type width: int, optional
        :param height: Height of image
        :type height: int, optional
        :param opacity: Opacity of image
        :type opacity: int, optional
        :param background_hex: Background hex color
        :type background_hex: str, optional
        :param blur: Blur level of image
        :type blur: int, optional
        :param img_format: Format of image (i.e. 'png')
        :type img_format: str, optional
        :param fallback: Fallback of image (i.e. 'poster', 'cover', 'art', 'poster-live', 'art-live', 'art-live-full')
        :type fallback: str, optional
        :param refresh: Whether or refresh the image cache (default: False)
        :type refresh: bool, optional
        :returns: Bytes of image
        :rtype: bytearray
        """
        if not _one_needed(img=img, rating_key=rating_key):
            return False, None
        if _is_invalid_choice(value=fallback, variable_name='fallback',
                              choices=static.image_fallback_types):
            return False, None
        params = build_optional_params(width=width, height=height, opacity=opacity, background=background_hex,
                                       blur=blur,
                                       img_format=img_format, fallback=fallback, refresh=refresh)
        name, value = _which_used(img=img, rating_key=rating_key)
        if name:
            params[name] = value

        response = self._get(command='pms_image_proxy', params=params)
        if response:
            return response.content

        return static.empty_bytes

    @set_and_forget
    def refresh_libraries_list(self) -> bool:
        """
        Refresh the Tautulli libraries list

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return 'refresh_libraries_list', None

    @set_and_forget
    def refresh_users_list(self) -> bool:
        """
        Refresh the Tautulli users list

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return 'refresh_users_list', None

    @raw_json
    def register_device(self, device_id: str, device_name: str, platform: str = None, version: str = None,
                        friendly_name: str = None, onesignal_id: str = None, min_version: str = None) -> dict:
        """
        Register the Tautulli Android App for notifications

        :param device_id: Unique device identifier for the mobile device
        :type device_id: str
        :param device_name: Device name of the mobile device
        :type device_name: str
        :param platform: The platform of the mobile devices
        :type platform: str, optional
        :param version: The version of the app
        :type version: str, optional
        :param friendly_name: Friendly name to identity the mobile device
        :type friendly_name: str, optional
        :param onesignal_id: The OneSignal ID of the mobile device
        :type onesignal_id: str, optional
        :param min_version: The minimum Tautulli version supported by the mobile device (e.g. "v2.5.6")
        :type min_version: str, optional
        :returns: Dict of data
        :rtype: dict
        """
        params = build_optional_params(platform=platform, version=version, friendly_name=friendly_name,
                                       onesignal_id=onesignal_id, min_version=min_version)
        params['device_id'] = device_id
        params['device_name'] = device_name
        return 'register_device', params

    @set_and_forget
    def regroup_history(self) -> bool:
        """
        Regroup play history in the database

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return 'regroup_history', None

    @set_and_forget
    def restart(self) -> bool:
        """
        Restart Tautulli

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return 'restart', None

    @raw_json
    def search(self, query: str, limit: int = None) -> dict:
        """
        Get search results from the Plex Media Server

        :param query: String to search for
        :type query: str
        :param limit: Maximum number of items to return per media type
        :type limit: int, optional
        :returns: Dict of data
        :rtype: dict
        """
        params = build_optional_params(limit=limit)
        params['query'] = query
        return 'search', params

    @property
    @raw_json
    def server_status(self) -> dict:
        """
        Get the current status of Tautulli's connection to the Plex server

        :returns: Dict of data
        :rtype: dict
        """
        return 'server_status', None

    @set_and_forget
    def set_mobile_device_config(self, mobile_device_id: int, friendly_name: str = None) -> bool:
        """
        Configure an existing notification agent

        :param mobile_device_id: ID of the mobile device config to update
        :type mobile_device_id: int
        :param friendly_name: Friendly name to identify the mobile device
        :type friendly_name: str, optional
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        params = build_optional_params(friendly_name=friendly_name)
        params['mobile_device_id'] = mobile_device_id
        return 'set_mobile_device_config', params

    @set_and_forget
    def set_newsletter_config(self, newsletter_id: int, agent_id: int, **kwargs) -> bool:
        """
        Configure an existing newsletter agent

        :param newsletter_id: ID of the newsletter config to update
        :type newsletter_id: int
        :param agent_id: Type of the newsletter to update
        :type agent_id: int
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        params = {}
        for k, v in kwargs.items():
            params[f"newsletter_config_{k}"] = v
            params[f"newsletter_email_{k}"] = v  # TODO: Confirm this is correct
        params['newsletter_id'] = newsletter_id
        params['agent_id'] = agent_id
        return 'set_newsletter_config', params

    @set_and_forget
    def set_notifier_config(self, agent: str, notifier_id: int, agent_id: int, **kwargs) -> bool:
        """
        Configure an existing notification agent

        :param agent: Type of the notification agent to update
        :type agent: str
        :param notifier_id: ID of the notifier config to update
        :type notifier_id: int
        :param agent_id: Agent of the notifier to update
        :type agent_id: int
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        params = {}
        for k, v in kwargs.items():
            params[f"{agent}_{k}"] = v
            # TODO: If I know the valid agents, we can do validation on this (look up name by ID)
        params['notifier_id'] = notifier_id
        params['agent_id'] = agent_id
        return 'set_notifier_config', params

    @raw_json
    def sql(self, query: str) -> dict:
        """
        Query the Tautulli database with raw SQL.

        Automatically makes a backup of the database if the latest backup is older than 24 hours.

        `api_sql` must be manually enabled in the config file while Tautulli is shut down.

        :param query: SQL query
        :type query: str
        :returns: Dict of data
        :rtype: dict
        """
        return 'sql', {'query': query}

    @raw_json
    def status(self, check: str = None) -> dict:
        """
        Get the current status of Tautulli

        :param check: What to check (i.e. 'database')
        :type check: str, optional
        :returns: Dict of data
        :rtype: dict
        """
        params = build_optional_params(check=check)
        return 'status', params

    @set_and_forget
    def terminate_session(self, session_key: int = None, session_id: str = None, message: str = None) -> bool:
        """
        Stop a streaming session

        :param session_key: Session key of the session to terminate
        :type session_key: int, optional
        :param session_id: Session ID of the session to terminate
        :type session_id: str, optional
        :param message: Custom message to send to the client
        :type message: str, optional
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        if not _one_needed(session_key=session_key, session_id=session_id):
            return False, None
        params = build_optional_params(message=message)
        name, value = _which_used(session_key=session_key, session_id=session_id)
        if name:
            params[name] = value
        return 'terminate_session', params

    @set_and_forget
    def undelete_library(self, section_id: str, section_name: str) -> bool:
        """
        Restore a deleted library section to Tautulli

        :param section_id: ID of the Plex library section
        :type section_id: str
        :param section_name: Name of the Plex library section
        :type section_name: str, optional
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return 'undelete_library', {'section_id': section_id, 'section_name': section_name}

    @set_and_forget
    def undelete_user(self, user_id: str, username: str) -> bool:
        """
        Restore a deleted user to Tautulli

        :param user_id: ID of the Plex user
        :type user_id: str
        :param username: Username of the Plex user
        :type username: str
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return 'undelete_user', {'user_id': user_id, 'username': username}

    @set_and_forget
    def update(self) -> bool:
        """
        Update Tautulli

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return 'update', None

    @property
    @raw_json
    def update_check(self) -> dict:
        """
        Check for Tautulli updates

        :returns: Dict of data
        :rtype: dict
        """
        return 'update_check', None

    @set_and_forget
    def update_metadata_details(self, old_rating_key: str, new_rating_key: str, media_type: str) -> bool:
        """
        Update the metadata in the Tautulli database by matching rating keys.

        Also updates all parents or children of the media item if it is a show/season/episode or artist/album/track.

        :param old_rating_key: Old rating key for item
        :type old_rating_key: str
        :param new_rating_key: New rating key for item
        :type new_rating_key: str
        :param media_type: Type of media (i.e. 'movie', 'show', 'episode', 'album', 'track')
        :type media_type: str
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        if _is_invalid_choice(value=media_type, variable_name='media_type',
                              choices=static.all_media_types):
            return False, None
        params = {'old_rating_key': old_rating_key, 'new_rating_key': new_rating_key, 'media_type': media_type}
        return 'update_metadata_details', params
