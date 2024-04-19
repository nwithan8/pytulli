import warnings
from datetime import datetime
from typing import Union, List

from tautulli.api.json_api import RawAPI
from tautulli.internal.decorators import raw_api_bool, make_object, make_property_object
from tautulli.models import *
from tautulli.tools.api_helper import APIShortcuts


# noinspection PyTypeChecker,PyUnusedLocal
class ObjectAPI:
    def __init__(self, base_url: str, api_key: str, verbose: bool = False, verify: bool = True,
                 ssl_verify: bool = True):
        self._raw_api = RawAPI(base_url=base_url, api_key=api_key, verbose=verbose, verify=verify,
                               ssl_verify=ssl_verify)

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

    def __str__(self):
        return f"ObjectAPI(url={self._raw_api._redacted_url})"

    @property
    def shortcuts(self) -> APIShortcuts:
        """
        Shortcuts for common API actions

        :returns: Access to API shortcuts
        :rtype: APIShortcuts
        """
        return self._raw_api.shortcuts

    @raw_api_bool
    def add_newsletter_config(self, agent_id: int) -> bool:
        """
        Add a new newsletter notification agent

        :param agent_id: Newsletter type to add
        :type agent_id: int
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return False

    @raw_api_bool
    def add_notifier_config(self, agent_id: int) -> bool:
        """
        Add a new notifier notification agent

        :param agent_id: Notification agent to add
        :type: int
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return False

    @property
    def arnold(self) -> str:
        """
        Get to the chopper!

        :returns: Random Arnold Schwarzenegger quote
        :rtype: str
        """
        return self._raw_api.arnold

    @raw_api_bool
    def backup_config(self) -> bool:
        """
        Backup the config.ini file

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return False

    @raw_api_bool
    def backup_database(self) -> bool:
        """
        Backup the plexpy.db database

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return False

    @raw_api_bool
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
        return False

    @raw_api_bool
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
        return False

    @raw_api_bool
    def delete_cache(self) -> bool:
        """
        Delete the cache directory

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return False

    @raw_api_bool
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
        return False

    @raw_api_bool
    def delete_history(self, row_ids: List[int]) -> bool:
        """
        Delete history rows from Tautulli

        :param row_ids: List of row IDs to delete
        :type row_ids: list[int]
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return False

    @raw_api_bool
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
        return False

    @raw_api_bool
    def delete_image_cache(self) -> bool:
        """
        Delete image cache directory

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return False

    @raw_api_bool
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
        return False

    @raw_api_bool
    def delete_login_log(self) -> bool:
        """
        Delete the Tautulli login logs

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return False

    @raw_api_bool
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
        return False

    @raw_api_bool
    def delete_media_info_cache(self, section_id: str) -> bool:
        """
        Delete media info table cache for a specific library

        :param section_id: ID of the Plex library section
        :type section_id: str
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return False

    @raw_api_bool
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
        return False

    @raw_api_bool
    def delete_newsletter(self, newsletter_id: int) -> bool:
        """
        Remove a newsletter from the database

        :param newsletter_id: ID of the newsletter to delete
        :type newsletter_id: int
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return False

    @raw_api_bool
    def delete_newsletter_log(self) -> bool:
        """
        Delete the Tautulli newsletter logs

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return False

    @raw_api_bool
    def delete_notification_log(self) -> bool:
        """
        Delete the Tautulli notification logs

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return False

    @raw_api_bool
    def delete_notifier(self, notifier_id: int) -> bool:
        """
        Remove a notifier from the database

        :param notifier_id: ID of the notifier to delete
        :type notifier_id: int
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return False

    @raw_api_bool
    def delete_recently_added(self) -> bool:
        """
        Flush all the recently added items in the database

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return False

    @raw_api_bool
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
        return False

    @raw_api_bool
    def delete_temp_sessions(self) -> bool:
        """
        Flush all temporary sessions in the database

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return False

    @raw_api_bool
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
        return False

    @property
    def docs_md(self) -> str:
        """
        Get the Tautulli API docs formatted with markdown

        :returns: API docs str
        :rtype: str
        """
        return self._raw_api.docs_md

    @property
    @make_property_object
    def docs(self) -> Docs:
        """
        Get the Tautulli API docs

        :returns: Docs object
        """
        return 'Docs'

    def download_config(self) -> str:
        """
        Download the Tautulli configuration file

        :returns: Config file string
        :rtype: str
        """
        return self._raw_api.download_config()

    def download_database(self) -> bytes:
        """
        Download the Tautulli database file

        :returns: Database file bytearray
        :rtype: bytearray
        """
        return self._raw_api.download_database()

    def download_export(self, export_id: int) -> bytes:
        """
        Download an exported metadata file

        :returns: Metadata file byte array
        :rtype: bytes
        """
        return self._raw_api.download_export(export_id=export_id)

    def download_log(self) -> bytes:
        """
        Download the Tautulli log file

        :returns: Log file bytearray
        :rtype: bytearray
        """
        return self._raw_api.download_log()

    def download_plex_log(self) -> bytes:
        """
        Download the Plex log file

        :returns: Log file bytearray
        :rtype: bytearray
        """
        return self._raw_api.download_plex_log()

    @raw_api_bool
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
        return False

    @raw_api_bool
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
        return False

    @raw_api_bool
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
        return False

    @make_object
    def activity(self, session_key: int = None, session_id: str = None) -> Activity:
        """
        Get the current activity on the Plex Media Server

        :param session_key: Session key for the session info to return
        :type session_key: int, optional
        :param session_id: Session ID of the session info to return
        :type session_id: str, optional
        :returns: Activity object
        """
        return 'Activity'

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
        return self._raw_api.get_api_key(username=username, password=password)

    @make_object
    def get_children_metadata(self, rating_key: str, media_type: str) -> ChildrenMetadata:
        """
        Get the metadata for the children of a media item.

        :param rating_key: The rating key of the media item
        :type rating_key: str
        :param media_type: The type of media item (movie, show, season, episode)
        :type media_type: str
        :returns: ChildrenMetadata object
        :rtype: ChildrenMetadata
        """
        return 'ChildrenMetadata'

    @make_object
    def get_collections_table(self, section_id: str) -> CollectionsTable:
        """
        Get the data on the Tautulli collections tables

        :param section_id: ID of the Plex library section
        :type section_id: str
        :returns: CollectionsTable object
        """
        return 'CollectionsTable'

    @property
    @make_property_object
    def date_formats(self) -> DateFormats:
        """
        Get the data and time formats used by Tautulli

        :returns: DateFormats object
        """
        return "DateFormats"

    @make_object
    def get_export_fields(self, media_type: str, sub_media_type: str = None) -> ExportFields:
        """
        Get a list of available custom export fields

        :param media_type: Media type of the fields to return
        :type media_type: str, optional
        :param sub_media_type: Child media type for collections (i.e. 'movie', 'show', 'video', 'audio', 'photo')
        :type sub_media_type: str, optional
        :returns: ExportFields
        """
        return 'ExportFields'

    @make_object
    def get_exports_table(self, section_id: str = None, user_id: str = None, rating_key: str = None,
                          order_column: str = None, order_direction: str = None, start: int = 0, length: int = 25,
                          search: str = None) -> ExportsTable:
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
        :returns: ExportsTable object
        :rtype: ExportsTable
        """
        return 'ExportsTable'

    @make_object
    def get_geoip_lookup(self, ip_address: str) -> GeoIPLookup:
        """
        Get the Geolocation info for an IP address

        :param ip_address: IP address to look up
        :type ip_address: str
        :returns: GeoIPLookup
        """
        return 'GeoIPLookup'

    @make_object
    def get_history(self, grouping: bool = False, include_activity: bool = False, user: str = None, user_id: int = None,
                    rating_key: int = None, parent_rating_key: int = None, grandparent_rating_key: int = None,
                    start_date: datetime = None, section_id: int = None, media_type: str = None,
                    transcode_decision: str = None, guid: str = None, order_column: str = None,
                    order_direction: str = None, start: int = 0, length: int = 25, search: str = None) -> History:
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
        :param start_date: Date to start results from
        :type start_date: datetime, optional
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
        :returns: History object
        """
        return 'History'

    @make_object
    def get_home_stats(self, grouping: bool = False, time_range: int = 30, stats_type: str = 'plays', start: int = 0,
                       count: int = 5, stat_id: str = None, user_id: int = None, section_id: int = None,
                       before: datetime = None, after: datetime = None) -> List[HomeStat]:
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
        :returns: List of HomeStat object
        """
        return 'HomeStat'

    @make_object
    def get_item_user_stats(self, rating_key: str, grouping: bool = False, media_type: str = None) \
            -> List[ItemUserStat]:
        """
        Get the user statistics for the media item

        :param rating_key: Rating key of the media item
        :type rating_key: str
        :param grouping: Whether to group results (default: False)
        :type grouping: bool, optional
        :param media_type: Media type of the item (only required for a collection)
        :type media_type: str, optional
        :returns: List of ItemUserStat objects
        :rtype: List[ItemUserStat]
        """
        return 'ItemUserStat'

    @make_object
    def get_item_watch_time_stats(self, rating_key: str, grouping: bool = False, query_days: List[int] = None,
                                  media_type: str = None) \
            -> List[ItemWatchTimeStat]:
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
        :returns: List of ItemWatchTimeStat objects
        :rtype: List[ItemWatchTimeStat]
        """
        return 'ItemWatchTimeStat'

    @property
    @make_property_object
    def libraries(self) -> List[LibrariesEntry]:
        """
        Get a list of all libraries on your server

        :returns: List of LibrariesEntry objects

        """
        return 'LibrariesEntry'

    @make_object
    def get_libraries_table(self, grouping: bool = False, order_column: str = None, order_direction: str = None,
                            start: int = 0, length: int = 25, search: str = None) -> LibrariesTable:
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
        :returns: LibrariesTable object

        """
        return 'LibrariesTable'

    @make_object
    def get_library(self, section_id: str) -> Library:
        """
        Get a library's details

        :param section_id: ID of the Plex library section
        :type section_id: str
        :returns: Library object

        """
        return 'Library'

    @make_object
    def get_library_media_info(self, section_id: str, rating_key: str, section_type: str = None,
                               order_column: str = None, order_direction: str = None, start: int = 0, length: int = 25,
                               search: str = None, refresh: bool = False) -> LibraryMediaInfo:
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
        :returns: LibraryMediaInfo object

        """
        return 'LibraryMediaInfo'

    @property
    @make_property_object
    def library_names(self) -> List[LibraryName]:
        """
        Get list of library names and IDs on the Plex Media Server

        :returns: List of LibraryName objects
        """
        return 'LibraryName'

    @make_object
    def get_library_user_stats(self, section_id: str, grouping: bool = False) -> LibraryUserStats:
        """
        Get a library's user statistics

        :param section_id: ID of the Plex library section
        :type section_id: str
        :param grouping: Whether to group results (default: False)
        :type grouping: bool, optional
        :returns: LibraryUserStats objects

        """
        return 'LibraryUserStats'

    @make_object
    def get_library_watch_time_stats(self, section_id: str, grouping: bool = False,
                                     query_days: List[int] = None) -> LibraryWatchTimeStats:
        """
        Get a library's watch time statistics

        :param section_id: ID of the Plex library section
        :type section_id: str
        :param grouping: Whether to group results (default: False)
        :type grouping: bool, optional
        :param query_days: List of days to get results for (i.e. [0, 1, 14, 30])
        :type query_days: list[int], optional
        :returns: LibraryWatchTimeStats object

        """
        return 'LibraryWatchTimeStats'

    @make_object
    def get_logs(self, sort: str = None, search: str = None, order_direction: str = None, regex: str = None,
                 start: int = None, end: int = None) -> List[LogEntry]:
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
        :returns: List of LogEntry objects

        """
        return 'LogEntry'

    @make_object
    def get_metadata(self, rating_key: str = None, sync_id: str = None) -> Metadata:
        """
        Get the metadata for a media item

        :param rating_key: Rating key of the media item
        :type rating_key: str, optional
        :param sync_id: Sync ID of a synced item
        :type sync_id: str, optional
        :returns: Metadata object

        """
        return 'Metadata'

    @make_object
    def get_new_rating_keys(self, rating_key: str, media_type: str) -> NewRatingKeys:
        """
        Get a list of new rating keys for the Plex Media Server of all the item's parent/children

        :param rating_key: Rating key of item
        :type rating_key: str
        :param media_type: Type of media (i.e. 'movie', 'show', 'episode', 'album', 'track')
        :type media_type: str
        :returns: NewRatingKeys object

        """
        return 'NewRatingKeys'

    @make_object
    def get_newsletter_config(self, newsletter_id: int) -> NewsletterConfig:
        """
        Get the configuration for an existing newsletter agent

        :param newsletter_id: ID of the newsletter
        :type newsletter_id: int
        :returns: NewsletterConfig object

        """
        return 'NewsletterConfig'

    @make_object
    def get_newsletter_log(self, order_column: str = None, order_direction: str = None, start: int = 0,
                           length: int = 25, search: str = None) -> NewsletterLog:
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
        :returns: NewsletterLog object

        """
        return 'NewsletterLog'

    @property
    @make_property_object
    def newsletters(self) -> List[Newsletter]:
        """
        Get a list of configured newsletters

        :returns: List of Newsletter objects
        """
        return 'Newsletter'

    @make_object
    def get_notification_log(self, order_column: str = None, order_direction: str = None, start: int = 0,
                             length: int = 25, search: str = None) -> NotificationLog:
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
        :returns: NotificationLog object

        """
        return 'NotificationLog'

    @make_object
    def get_notifier_config(self, notifier_id: int) -> NotifierConfig:
        """
        Get the configuration for an existing notification agent

        :param notifier_id: ID of the notifier
        :type notifier_id: int
        :returns: NotifierConfig object

        """
        return 'NotifierConfig'

    @property
    @make_property_object
    def notifier_parameters(self) -> List[NotifierParameter]:
        """
        Get a list of available notification parameters

        :returns: List of NotifierParameter objects
        """
        return 'NotifierParameter'

    @make_object
    def get_notifiers(self, notify_action: str = None) -> List[Notifier]:
        """
        Get a list of configured notifiers

        :param notify_action: The notification action to filter out
        :type notify_action: str, optional
        :returns: List of Notifier objects

        """
        return 'Notifier'

    @make_object
    def get_old_rating_keys(self, rating_key: str, media_type: str) -> OldRatingKeys:
        """
        Get a list of old rating keys from the Tautulli database for all the item's parent/children

        :param rating_key: Rating key of item
        :type rating_key: str
        :param media_type: Type of media (i.e. 'movie', 'show', 'episode', 'album', 'track')
        :type media_type: str
        :returns: OldRatingKeys object
        """
        return 'OldRatingKeys'

    @make_object
    def get_playlists_table(self, section_id: str = None, user_id: str = None) -> PlaylistsTable:
        """
        Get the data on the Tautulli playlists tables

        :param section_id: Section ID of the Plex library
        :type section_id: str, optional
        :param user_id: User ID of the Plex user
        :type user_id: str, optional
        :returns: PlaylistsTable object

        """
        return 'PlaylistsTable'

    @make_object
    def get_plays_by_date(self, time_range: int = None, y_axis: str = None, user_ids: List[str] = None,
                          grouping: bool = False) -> PlaysOrStreamTypesBy:
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
        :returns: PlaysOrStreamTypesBy object
        :rtype: PlaysOrStreamTypesBy
        """
        return 'PlaysOrStreamTypesBy'

    @make_object
    def get_plays_by_day_of_week(self, time_range: int = None, y_axis: str = None, user_ids: List[str] = None,
                                 grouping: bool = False) -> PlaysOrStreamTypesBy:
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
        :returns: PlaysOrStreamTypesBy object
        :rtype: PlaysOrStreamTypesBy
        """
        return 'PlaysOrStreamTypesBy'

    @make_object
    def get_plays_by_hour_of_day(self, time_range: int = None, y_axis: str = None, user_ids: List[str] = None,
                                 grouping: bool = False) -> PlaysOrStreamTypesBy:
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
        :returns: PlaysOrStreamTypesBy object
        :rtype: PlaysOrStreamTypesBy
        """
        return 'PlaysOrStreamTypesBy'

    @make_object
    def get_plays_by_source_resolution(self, time_range: int = None, y_axis: str = None, user_ids: List[str] = None,
                                       grouping: bool = False) -> PlaysOrStreamTypesBy:
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
        :returns: PlaysOrStreamTypesBy object
        :rtype: PlaysOrStreamTypesBy
        """
        return 'PlaysOrStreamTypesBy'

    @make_object
    def get_plays_by_stream_resolution(self, time_range: int = None, y_axis: str = None, user_ids: List[str] = None,
                                       grouping: bool = False) -> PlaysOrStreamTypesBy:
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
        :returns: PlaysOrStreamTypesBy object
        :rtype: PlaysOrStreamTypesBy
        """
        return 'PlaysOrStreamTypesBy'

    @make_object
    def get_plays_by_stream_type(self, time_range: int = None, y_axis: str = None, user_ids: List[str] = None,
                                 grouping: bool = False) -> PlaysOrStreamTypesBy:
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
        :returns: PlaysOrStreamTypesBy object
        :rtype: PlaysOrStreamTypesBy
        """
        return 'PlaysOrStreamTypesBy'

    @make_object
    def get_plays_by_top_10_platforms(self, time_range: int = None, y_axis: str = None, user_ids: List[str] = None,
                                      grouping: bool = False) -> PlaysOrStreamTypesBy:
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
        :returns: PlaysOrStreamTypesBy object
        :rtype: PlaysOrStreamTypesBy
        """
        return 'PlaysOrStreamTypesBy'

    @make_object
    def get_plays_by_top_10_users(self, time_range: int = None, y_axis: str = None, user_ids: List[str] = None,
                                  grouping: bool = False) -> PlaysOrStreamTypesBy:
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
        :returns: PlaysOrStreamTypesBy object
        :rtype: PlaysOrStreamTypesBy
        """
        return 'PlaysOrStreamTypesBy'

    @make_object
    def get_plays_per_month(self, time_range: int = None, y_axis: str = None, user_ids: List[str] = None,
                            grouping: bool = False) -> PlaysOrStreamTypesBy:
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
        :returns: PlaysOrStreamTypesBy object
        :rtype: PlaysOrStreamTypesBy
        """
        return 'PlaysOrStreamTypesBy'

    @make_object
    def get_plex_log(self, window: int = None, log_type: str = None) -> PlexLog:
        """
        Get the Plex Media Server logs

        :param window: Number of tail lines to return
        :type window: int, optional
        :param log_type: Log type ('server' or 'scanner')
        :type log_type: str, optional
        :returns: PlexLog object

        """
        return 'PlexLog'

    @property
    @make_property_object
    def pms_update(self) -> PMSUpdate:
        """
        Check for updates to the Plex Media Server

        :returns: PMSUpdate object
        """
        return 'PMSUpdate'

    @make_object
    def get_recently_added(self, count: int, start: int = 0, media_type: str = None,
                           section_id: str = None) -> RecentlyAdded:
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
        :returns: RecentlyAdded object
        """
        return 'RecentlyAdded'

    @property
    def server_friendly_name(self) -> str:
        """
        Get the name of the Plex Media Server

        :returns: Name of the Plex Media Server
        :rtype: str
        """
        return self._raw_api.server_friendly_name

    @make_object
    def get_server_id(self, hostname: str, port: int, ssl: bool = False, remote: bool = False) -> ServerID:
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
        :returns: ServerID object

        """
        return 'ServerID'

    @property
    @make_property_object
    def server_identity(self) -> ServerIdentity:
        """
        Get info about the local server

        :returns: ServerIdentity object
        """
        return 'ServerIdentity'

    @property
    @make_property_object
    def server_info(self) -> ServerInfo:
        """
        Get the Plex Media Server information

        :returns: ServerInfo object
        """
        return 'ServerInfo'

    @property
    @make_property_object
    def server_list(self) -> List[ServerListEntry]:
        """
        Get all your servers that are published to Plex.tv

        :returns: List of ServerListEntry objects

        """
        return 'ServerListEntry'

    def get_server_pref(self, pref: str) -> str:
        """
        Get a specified Plex Media Server preference

        :param pref: Name of preference
        :type pref: str
        :returns: Value of preference
        :rtype: str
        """
        return self._raw_api.get_server_pref(pref=pref)

    @property
    @make_property_object
    def servers_info(self) -> List[ServersInfoEntry]:
        """
        Get info about the Plex Media Server

        :returns: List of ServersInfoEntry objects

        """
        return 'ServersInfoEntry'

    @make_object
    def get_settings(self, key: str = None) -> Settings:
        """
        Get all settings from the config file

        :param key: Name of a config section to return
        :type key: str, optional
        :returns: Settings object

        """
        return 'Settings'

    @make_object
    def get_stream_data(self, row_id: int = None, session_key: int = None) -> StreamData:
        """
        Get the details of a stream from history or current stream

        :param row_id: Row ID number for a history item
        :type row_id: int, optional
        :param session_key: Session key for the current stream
        :type session_key: int, optional
        :returns: StreamData object

        """
        return 'StreamData'

    @make_object
    def get_stream_type_by_top_10_platforms(self, time_range: int = None, y_axis: str = None,
                                            user_ids: List[str] = None,
                                            grouping: bool = False) -> PlaysOrStreamTypesBy:
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
        :returns: PlaysOrStreamTypesBy object
        :rtype: PlaysOrStreamTypesBy
        """
        return 'PlaysOrStreamTypesBy'

    @make_object
    def get_stream_type_by_top_10_users(self, time_range: int = None, y_axis: str = None, user_ids: List[str] = None,
                                        grouping: bool = False) -> PlaysOrStreamTypesBy:
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
        :returns: PlaysOrStreamTypesBy object
        :rtype: PlaysOrStreamTypesBy
        """
        return 'PlaysOrStreamTypesBy'

    @make_object
    def get_synced_items(self, machine_id: str, user_id: str = None) -> SyncedItems:
        """
        Get a list of synced items on the Plex Media Server

        :param machine_id: Plex Media Server identifier
        :type machine_id: str
        :param user_id: ID of the Plex user
        :type user_id: str, optional
        :returns: SyncedItems object

        """
        return 'SyncedItems'

    @property
    @make_property_object
    def tautulli_info(self) -> TautulliInfo:
        """
        Get the Tautulli server information

        :returns: Dict of data
        :rtype: dict
        """
        return 'TautulliInfo'

    @make_object
    def get_user(self, user_id: str) -> User:
        """
        Get a user's details

        :param user_id: ID of the Plex user
        :type user_id: str
        :returns: User object

        """
        return 'User'

    @make_object
    def get_user_ips(self, user_id: str, order_column: str = None, order_direction: str = None, start: int = 0,
                     length: int = 25, search: str = None) -> UserIPs:
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
        :returns: UserIPs object

        """
        return 'UserIPs'

    @make_object
    def get_user_logins(self, user_id: str, order_column: str = None, order_direction: str = None, start: int = 0,
                        length: int = 25, search: str = None) -> UserLogins:
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
        :returns: UserLogins object

        """
        return 'UserLogins'

    @property
    @make_property_object
    def user_names(self) -> List[UserName]:
        """
        Get a list of all usernames and user ids

        :returns: List of UserName objects

        """
        return 'UserName'

    @make_object
    def get_user_player_stats(self, user_id: str, grouping: bool = False) -> UserPlayerStats:
        """
        Get a user's player statistics

        :param user_id: ID of the Plex user
        :type user_id: str
        :param grouping: Whether to group results (default: False)
        :type grouping: bool, optional
        :returns: UserPlayerStats object

        """
        return 'UserPlayerStats'

    @make_object
    def get_user_watch_time_stats(self, user_id: str, grouping: bool = False,
                                  query_days: List[int] = None) -> UserWatchTimeStats:
        """
        Get a user's watch time statistics

        :param user_id: ID of the Plex user
        :type user_id: str
        :param grouping: Whether to group results (default: False)
        :type grouping: bool, optional
        :param query_days: List of days to get results for (e.g. [0, 1, 14, 30])
        :type query_days: list[int], optional
        :returns: UserWatchTimeStats object

        """
        return 'UserWatchTimeStats'

    @property
    @make_property_object
    def users(self) -> List[User]:
        """
        Get a list of all users that have access to your server

        :returns: List of User objects

        """
        return 'User'

    @make_object
    def get_users_table(self, grouping: bool = False, order_column: str = None, order_direction: str = None,
                        start: int = 0, length: int = 25, search: str = None) -> UsersTable:
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
        :returns: UsersTable object

        """
        return 'UsersTable'

    @make_object
    def get_whois_lookup(self, ip_address: str) -> WHOISLookup:
        """
        Get the connection info for an IP address

        :param ip_address: IP address
        :type ip_address: str
        :returns: WHOISLookup object

        """
        return 'WHOISLookup'

    @raw_api_bool
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
        return False

    @raw_api_bool
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
        return False

    @raw_api_bool
    def logout_user_session(self, row_ids: List[int]) -> bool:
        """
        Logout Tautulli user sessions

        :param row_ids: List of row IDS to sign out
        :type row_ids: list[int], optional
        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return False

    @make_object
    def notify(self, notifier_id: int, subject: str, body: str, headers: str = None,
               script_args: str = None) -> Notification:
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
        :returns: Notification object

        """
        return 'Notification'

    @make_object
    def notify_newsletter(self, newsletter_id: int, subject: str = None, body: str = None,
                          message: str = None) -> NewsletterNotification:
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
        :returns: NewsletterNotification object

        """
        return 'NewsletterNotification'

    @raw_api_bool
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
        return False

    def pms_image_proxy(self, img: str = None, rating_key: str = None, width: int = None, height: int = None,
                        opacity: int = None, background_hex: str = None, blur: int = None, img_format: str = 'png',
                        fallback: str = None, refresh: bool = False) -> bool:
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
        return self._raw_api.pms_image_proxy(img=img, rating_key=rating_key, width=width, height=height,
                                             opacity=opacity,
                                             background_hex=background_hex, blur=blur, img_format=img_format,
                                             fallback=fallback, refresh=refresh)

    @raw_api_bool
    def refresh_libraries_list(self) -> bool:
        """
        Refresh the Tautulli libraries list

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return False

    @raw_api_bool
    def refresh_users_list(self) -> bool:
        """
        Refresh the Tautulli users list

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return False

    @make_object
    def register_device(self, device_id: str, device_name: str, friendly_name: str = None, onesignal_id: str = None,
                        min_version: str = None) -> RegisteredDevice:
        """
        Register the Tautulli Android App for notifications

        :param device_id: Unique device identifier for the mobile device
        :type device_id: str
        :param device_name: Device name of the mobil device
        :type device_name: str
        :param friendly_name: Friendly name to identity the mobile device
        :type friendly_name: str, optional
        :param onesignal_id: The OneSignal ID of the mobile device
        :type onesignal_id: str, optional
        :param min_version: The minimum Tautulli version supported by the mobile device (e.g. "v2.5.6")
        :type min_version: str, optional
        :returns: RegisteredDevice object

        """
        return 'RegisteredDevice'

    @raw_api_bool
    def regroup_history(self) -> bool:
        """
        Regroup play history in the database

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return False

    @raw_api_bool
    def restart(self) -> bool:
        """
        Restart Tautulli

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return False

    @make_object
    def search(self, query: str, limit: int = None) -> SearchResults:
        """
        Get search results from the Plex Media Server

        :param query: String to search for
        :type query: str
        :param limit: Maximum number of items to return per media type
        :type limit: int, optional
        :returns: SearchResults object

        """
        return 'SearchResults'

    @property
    @make_property_object
    def server_status(self) -> ServerStatus:
        """
        Get the current status of Tautulli's connection to the Plex server

        :returns: ServerStatus object
        :rtype: ServerStatus
        """
        return 'ServerStatus'

    @raw_api_bool
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
        return False

    @raw_api_bool
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
        return False

    @raw_api_bool
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
        return False

    # TODO: Test to see what this returns, no schema on API docs
    @make_object
    def sql(self, query: str) -> None:
        """
        Query the Tautulli database with raw SQL.

        Automatically makes a backup of the database if the latest backup is older than 24 hours.

        `api_sql` must be manually enabled in the config file while Tautulli is shut down.

        :param query: SQL query
        :type query: str
        :returns: SQLResults object

        """
        warnings.warn("Deprecated", DeprecationWarning)
        return None
        # return 'SQLResults'

    @make_object
    def status(self, check: str = None) -> Status:
        """
        Get the current status of Tautulli

        :param check: What to check (i.e. 'database')
        :type check: str, optional
        :returns: Status object
        :rtype: Status
        """
        return 'Status'

    @raw_api_bool
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
        return False

    @raw_api_bool
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
        return False

    @raw_api_bool
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
        return False

    @raw_api_bool
    def update(self) -> bool:
        """
        Update Tautulli

        :returns: `True` if successful, `False` if unsuccessful
        :rtype: bool
        """
        return False

    @property
    @make_property_object
    def update_check(self) -> UpdateCheck:
        """
        Check for Tautulli updates

        :returns: UpdateCheck object

        """
        return 'UpdateCheck'

    @raw_api_bool
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
        return False
