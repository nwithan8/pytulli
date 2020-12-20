import logging
from typing import Union, List
from urllib.parse import urlencode
import requests
from datetime import datetime

from tautulli.classes import HomeStats, HomeStatsCategory, User, WatchTimeStats, WatchTimeStat
from tautulli import static
from tautulli.utils import build_optional_params, _get_response_data, _success_result, int_list_to_string, _one_needed, _which_used, bool_to_int, _is_invalid_choice, datetime_to_string
from tautulli.decorators import raw_json, set_and_forget
import tautulli._info as package_info

def _stat_category_to_number(stat_category: str) -> Union[int, None]:
    translations = {
        'movies': 0,
        'shows': 1,
        'artists': 2,
        'users': 7
    }
    return translations.get(stat_category, None)


class API:
    def __init__(self, base_url: str, api_key: str, verbose: bool = False):
        if base_url.endswith("/"):
            base_url = base_url[:-1]
        self._url = f"{base_url}/api/v2?apikey={api_key}"
        self._session = requests.Session()
        logging.basicConfig(format='%(levelname)s:%(message)s', level=(logging.DEBUG if verbose else logging.ERROR))
        self._logger = logging.getLogger(package_info.__title__)

    def _create_url(self, command: str, params: dict = None) -> str:
        url = f"{self._url}&cmd={command}"
        if params:
            url += f"&{urlencode(params)}"
        return url

    def _get(self, command: str, params: dict = None) -> requests.Response:
        url = self._create_url(command=command, params=params)
        return self._session.get(url=url)

    def _get_json(self, command: str, params: dict = None) -> dict:
        response = self._get(command=command, params=params)
        if response:
            return response.json()
        return static.empty_dict

    @set_and_forget
    def ping(self) -> bool:
        return "get_server_friendly_name", None

    @property
    def arnold(self) -> str:
        json_data = self._get_json(command='arnold')
        if json_data:
            return _get_response_data(json_data=json_data)
        return static.empty_string

    @set_and_forget
    def add_newsletter_config(self, agent_id: int):
        return "add_newsletter_config", {'agent_id': agent_id}

    @set_and_forget
    def add_notifier_config(self, agent_id: int) -> bool:
        return "add_notifier_config", {'agent_id': agent_id}

    @set_and_forget
    def backup_config(self) -> bool:
        return "backup_config", None

    @set_and_forget
    def backup_database(self) -> bool:
        return "backup_db", None

    @set_and_forget
    def delete_all_library_history(self, server_id: str, section_id: str, row_ids: List[int] = None) -> bool:
        params = {'server_id': server_id, 'section_id': section_id}
        if row_ids:
            params['row_ids'] = int_list_to_string(int_list=row_ids)
        return "delete_all_library_history", params

    @set_and_forget
    def delete_all_user_history(self, user_id: str, row_ids: List[int] = None) -> bool:
        params = {'user_id': user_id}
        if row_ids:
            params['row_ids'] = int_list_to_string(int_list=row_ids)
        return "delete_all_user_history", params

    @set_and_forget
    def delete_cache(self) -> bool:
        return "delete_cache", None

    @set_and_forget
    def delete_export(self, export_id: int, delete_all: bool = False) -> bool:
        return "delete_export", {'export_id': export_id, 'delete_all': delete_all}

    @set_and_forget
    def delete_history(self, row_ids: List[int]) -> bool:
        params = {'row_ids': int_list_to_string(int_list=row_ids)}
        return 'delete_history', params

    @set_and_forget
    def delete_hosted_images(self, rating_key: int = None, service: str = None, delete_all: bool = False) -> bool:
        if _is_invalid_choice(value=service, variable_name="service",
                              choices=static.cloud_image_hosts):
            return False, None
        params = build_optional_params(rating_key=rating_key, service=service, delete_all=delete_all)
        return 'delete_hosted_images', params

    @set_and_forget
    def delete_image_cache(self) -> bool:
        return 'delete_image_cache', None

    @set_and_forget
    def delete_library(self, server_id: str, section_id: str, row_ids: List[int] = None) -> bool:
        params = {'server_id': server_id, 'section_id': section_id}
        if row_ids:
            params['row_ids'] = int_list_to_string(int_list=row_ids)
        return 'delete_library', params

    @set_and_forget
    def delete_login_log(self) -> bool:
        return 'delete_login_log', None

    @set_and_forget
    def delete_loopup_info(self, rating_key: int = None, service: str = None, delete_all: bool = False) -> bool:
        if _is_invalid_choice(value=service, variable_name="service",
                              choices=static.cloud_lookup_hosts):
            return False, None
        params = build_optional_params(rating_key=rating_key, service=service, delete_all=delete_all)
        return 'delete_hosted_images', params

    @set_and_forget
    def delete_media_info_cache(self, section_id: str) -> bool:
        return 'delete_media_info_cache', {'section_id': section_id}

    @set_and_forget
    def delete_mobile_device(self, mobile_device_id: int = None, device_id: str = None) -> bool:
        if not _one_needed(mobile_device_id=mobile_device_id, device_id=device_id):
            return False, None
        return 'delete_mobile_device', {'mobile_device_id': mobile_device_id, 'device_id': device_id}

    @set_and_forget
    def delete_newsletter(self, newsletter_id: int) -> bool:
        return 'delete_newsletter', {'newsletter_id': newsletter_id}

    @set_and_forget
    def delete_newsletter_log(self) -> bool:
        return 'delete_newsletter_log', None

    @set_and_forget
    def delete_notification_log(self) -> bool:
        return 'delete_notification_log', None

    @set_and_forget
    def delete_notifier(self, notifier_id: int) -> bool:
        return 'delete_notifier', {'notifier_id': notifier_id}

    @set_and_forget
    def delete_recently_added(self) -> bool:
        return 'delete_recently_added', None

    @set_and_forget
    def delete_synced_item(self, client_id: str, sync_id: str) -> bool:
        return 'delete_synced_item', {'client_id': client_id, 'sync_id': sync_id}

    @set_and_forget
    def delete_temp_sessions(self) -> bool:
        return 'delete_temp_sessions', None

    @set_and_forget
    def delete_user(self, user_id: str, row_ids: List[int] = None) -> bool:
        params = {'user_id': user_id}
        if row_ids:
            params['row_ids'] = int_list_to_string(int_list=row_ids)
        return 'delete_user', params

    @property
    def docs(self) -> dict:
        return self._get_json(command='docs')

    @property
    def docs_md(self) -> str:
        response = self._get(command='docs_md')
        if response:
            return response.text
        return static.empty_string

    def download_config(self) -> str:
        response = self._get(command='download_config')
        if response:
            return response.text
        return static.empty_string

    def download_database(self) -> bytes:
        response = self._get(command='download_database')
        if response:
            return response.content
        return static.empty_bytes

    """
    @property
    def metadata(self) -> :
    """

    def download_log(self) -> bytes:
        response = self._get(command='download_log')
        if response:
            return response.content
        return static.empty_bytes

    def download_plex_log(self) -> bytes:
        response = self._get(command='download_plex_log')
        if response:
            return response.content
        return static.empty_bytes

    @set_and_forget
    def edit_library(self, section_id: str, custom_thumb: str = None, custom_art: str = None, keep_history: bool = True) -> bool:
        keep_history = bool_to_int(boolean=keep_history)
        params = build_optional_params(custom_thumb=custom_thumb, custom_art=custom_art, keep_history=keep_history)
        params['section_id'] = section_id
        return 'edit_library', params

    @set_and_forget
    def edit_user(self, user_id: str, friendly_name: str = None, custom_thumb: str = None, keep_history: bool = True, allow_guest: bool = False) -> bool:
        keep_history = bool_to_int(boolean=keep_history)
        allow_guest = bool_to_int(boolean=allow_guest)
        params = build_optional_params(friendly_name=friendly_name, custom_thumb=custom_thumb, keep_history=keep_history, allow_guest=allow_guest)
        params['user_id'] = user_id
        return 'edit_user', params

    @set_and_forget
    def export_metadata(self, section_id: int = None, user_id: int = None, rating_key: int = None, file_format: str = 'csv', metadata_level: int = 1, media_info_level: int = 1, thumb_level: int = 0, art_level: int = 0, custom_fields: List[str] = None, export_type: str = None, individual_files: bool = False) -> bool:
        if not _one_needed(section_id=section_id, user_id=user_id, rating_key=rating_key):
            return False, None
        if _is_invalid_choice(value=file_format, variable_name="file_format",
                              choices=static.export_file_formats):
            return False, None
        if _is_invalid_choice(value=export_type, variable_name="export_type",
                              choices=static.export_media_types):
            return False, None
        if custom_fields:
            custom_fields = ','.join(custom_fields)
        params = build_optional_params(file_format=file_format, metadata_level=metadata_level, media_info_level=media_info_level, thumb_level=thumb_level, art_level=art_level, custom_fields=custom_fields, export_type=export_type, individual_files=individual_files)
        name, value = _which_used(section_id=section_id, user_id=user_id, rating_key=rating_key)
        if name:
            params[name] = value
        return 'export_metadata', params

    @property
    @raw_json
    def activity(self, session_key: int = None, session_id: str = None) -> dict:
        params = build_optional_params(session_key=session_key, session_id=session_id)
        return self._get_json(command='get_activity', params=params)

    def get_apikey(self, username: str = None, password: str = None) -> str:
        params = build_optional_params(username=username, password=password)
        json_data = self._get_json(command='get_apikey', params=params)
        if _success_result(json_data=json_data):
            return _get_response_data(json_data=json_data)
        return static.empty_string

    @raw_json
    def get_collections_table(self, section_id: str) -> dict:
        return 'get_collections_table', {'section_id': section_id}

    @property
    @raw_json
    def date_formats(self) -> dict:
        return 'get_date_formats', None

    @raw_json
    def get_export_fields(self, media_type: str, sub_media_type: str = None) -> dict:
        if _is_invalid_choice(value=media_type, variable_name="media_type", choices=static.export_media_types):
            return False, None
        if sub_media_type:
            if media_type == 'collection':
                if _is_invalid_choice(value=sub_media_type, variable_name="sub_media_type", choices=static.collections_sub_media_types):
                    return False, None
            elif media_type == 'playlist':
                if _is_invalid_choice(value=sub_media_type, variable_name="sub_media_type",
                                      choices=static.playlist_sub_media_types):
                    return False, None
        params = build_optional_params(sub_media_type=sub_media_type)
        params['media_type'] = media_type
        return 'get_export_fields', params

    @raw_json
    def get_exports_table(self, section_id: str = None, user_id: str = None, rating_key: str = None, order_column: str = None, order_direction: str = None, start: int = 0, length: int = 25, search: str = None) -> dict:
        if not _one_needed(section_id=section_id, user_id=user_id, rating_key=rating_key):
            return False, None
        if _is_invalid_choice(value=order_column, variable_name="order_column",
                              choices=static.exports_order_columns):
            return False, None
        if _is_invalid_choice(value=order_direction, variable_name="order_direction",
                              choices=static.order_direction):
            return False, None
        params = build_optional_params(order_column=order_column, order_dir=order_direction, start=start, length=length, search=search)
        name, value = _which_used(section_id=section_id, user_id=user_id, rating_key=rating_key)
        if name:
            params[name] = value
        return 'get_exports_table', params

    @raw_json
    def get_geoip_lookup(self, ip_address: str) -> dict:
        return 'get_geoip_lookup', {'ip_address': ip_address}

    @raw_json
    def get_history(self, grouping: bool = False, include_activity: bool = False, user: str = None, user_id: int = None, rating_key: int = None, parent_rating_key: int = None, grandparent_rating_key: int = None, start_date: datetime = None, section_id: int = None, media_type: str = None, transcode_decision: str = None, guid: str = None, order_column: str = None, order_direction: str = None, start: int = 0, length: int = 25, search: str = None) -> dict:
        grouping = bool_to_int(boolean=grouping)
        include_activity = bool_to_int(boolean=include_activity)
        start_date = datetime_to_string(datetime_object=start_date)
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
        params = build_optional_params(grouping=grouping, include_activity=include_activity, user=user, user_id=user_id, rating_key=rating_key, parent_rating_key=parent_rating_key, grandparent_rating_key=grandparent_rating_key, start_date=start_date, section_id=section_id, media_type=media_type, transcode_decision=transcode_decision, guid=guid, order_column=order_column, order_dir=order_direction, start=start,length=length, search=search)
        return 'get_history', params

    @raw_json
    def get_home_stats(self, grouping: bool = False, time_range: int = 30, stats_type: str = 'plays', start: int = 0, count = 5, stat_id: str = None):
        grouping = bool_to_int(boolean=grouping)
        if _is_invalid_choice(value=stats_type, variable_name="stats_type",
                              choices=static.stats_type):
            return False, None
        if _is_invalid_choice(value=stat_id, variable_name='stat_id',
                              choices=static.stats_category):
            return False, None
        params = build_optional_params(grouping=grouping, time_range=time_range, stats_type=stats_type, start=start, count=count, stat_id=stat_id)
        return 'get_home_stats', params

    @raw_json
    def libraries(self) -> dict:
        return 'get_libraries', None

    @raw_json
    def get_libraries_table(self, grouping: bool = False, order_column: str = None, order_direction: str = None, start: int = 0, length: int = 25, search: str = None) -> dict:
        grouping = bool_to_int(boolean=grouping)
        if _is_invalid_choice(value=order_column, variable_name="order_column",
                              choices=static.libraries_order_columns):
            return False, None
        if _is_invalid_choice(value=order_direction, variable_name='order_direction',
                              choices=static.order_direction):
            return False, None
        params = build_optional_params(grouping=grouping, order_column=order_column, order_dir=order_direction, start=start, length=length, search=search)
        return 'get_libraries_table', params

    @raw_json
    def get_library(self, section_id: str) -> dict:
        return 'get_library', {'section_id': section_id}
    
    @raw_json
    def get_library_media_info(self, section_id: str, rating_key: str, section_type: str = None, order_column: str = None, order_direction: str = None, start: int = 0, length: int = 25, search: str = None, refresh: bool = False) -> dict:
        if not _one_needed(section_id=section_id, rating_key=rating_key):
            return False, None
        if _is_invalid_choice(value=order_column, variable_name="order_column",
                              choices=static.library_order_columns):
            return False, None
        if _is_invalid_choice(value=order_direction, variable_name='order_direction',
                              choices=static.order_direction):
            return False, None
        params = build_optional_params(section_id=section_id, order_column=order_column, order_dir=order_direction, start=start, length=length, search=search, refresh=refresh)
        name, value = _which_used(section_id=section_id, rating_key=rating_key)
        if name:
            params[name] = value
        return 'get_library_media_info', params

    @property
    @raw_json
    def library_names(self) -> dict:
        return 'get_library_names', None

    @raw_json
    def get_library_user_stats(self, section_id: str, grouping: bool = False) -> dict:
        grouping = bool_to_int(boolean=grouping)
        params = build_optional_params(grouping=grouping)
        params['section_id'] = section_id
        return 'get_library_user_stats', params

    @raw_json
    def get_library_watch_time_stats(self, section_id: str, grouping: bool = False, query_days: List[int] = None) -> dict:
        grouping = bool_to_int(boolean=grouping)
        params = build_optional_params(grouping=grouping)
        params['section_id'] = section_id
        if query_days:
            params['query_days'] = int_list_to_string(int_list=query_days)
        return 'get_library_watch_time_stats', params

    @raw_json
    def get_logs(self, sort: str = None, search: str = None, order_direction: str = None, regex: str = None, start: int = None, end: int = None) -> dict:
        if _is_invalid_choice(value=sort, variable_name='sort',
                              choices=static.log_sorting):
            return False, None
        if _is_invalid_choice(value=order_direction, variable_name='order_direction',
                              choices=static.order_direction):
            return False, None
        params = build_optional_params(sort=sort, search=search, order=order_direction, regex=regex, start=start, end=end)
        return 'get_logs', params

    @raw_json
    def get_metadata(self, rating_key: str = None, sync_id: str = None) -> dict:
        if not _one_needed(sync_id=sync_id, rating_key=rating_key):
            return False, None
        params = {}
        name, value = _which_used(sync_id=sync_id, rating_key=rating_key)
        if name:
            params[name] = value
        return 'get_metadata', params

    @raw_json
    def get_new_rating_keys(self, rating_key: str, media_type: str) -> dict:
        if _is_invalid_choice(value=media_type, variable_name='media_type',
                              choices=static.all_media_types):
            return False, None
        params = {'rating_key': rating_key, 'media_type': media_type}
        return 'get_new_rating_keys', params

    @raw_json
    def get_newsletter_config(self, newsletter_id: int) -> dict:
        return 'get_newsletter_config', {'newsletter_id': newsletter_id}

    @raw_json
    def get_newsletter_log(self, order_column: str = None, order_direction: str = None, start: int = 0, length: int = 25, search: str = None) -> dict:
        if _is_invalid_choice(value=order_column, variable_name='order_column',
                              choices=static.newsletter_order_column):
            return False, None
        if _is_invalid_choice(value=order_direction, variable_name='order_direction',
                              choices=static.order_direction):
            return False, None
        params = build_optional_params(order_column=order_column, order_dir=order_direction, start=start, length=length, search=search)
        return 'get_newsletter_log', params

    @property
    @raw_json
    def newsletters(self) -> dict:
        return 'get_newsletters', None

    @raw_json
    def get_notification_log(self, order_column: str = None, order_direction: str = None, start: int = 0, length: int = 25, search: str = None) -> dict:
        if _is_invalid_choice(value=order_column, variable_name='order_column',
                              choices=static.notifications_order_column):
            return False, None
        if _is_invalid_choice(value=order_direction, variable_name='order_direction',
                              choices=static.order_direction):
            return False, None
        params = build_optional_params(order_column=order_column, order_dir=order_direction, start=start, length=length, search=search)
        return 'get_notification_log', params

    @raw_json
    def get_notifier_config(self, notifier_id: int) -> dict:
        return 'get_notifier_config', {'notifier_id': notifier_id}

    @property
    @raw_json
    def notifier_parameters(self) -> dict:
        return 'get_notifier_parameters', None

    @raw_json
    def get_notifiers(self, notify_action: str = None) -> dict:
        params = build_optional_params(notify_action=notify_action)
        return 'get_notifiers', params

    @raw_json
    def get_old_rating_keys(self, rating_key: str, media_type: str) -> dict:
        if _is_invalid_choice(value=media_type, variable_name='media_type',
                              choices=static.all_media_types):
            return False, None
        params = {'rating_key': rating_key, 'media_type': media_type}
        return 'get_old_rating_keys', params

    @raw_json
    def get_playlists_table(self, section_id: str = None, user_id: str = None) -> dict:
        if not _one_needed(section_id=section_id, user_id=user_id):
            return False, None
        params = {}
        name, value = _which_used(section_id=section_id, user_id=user_id)
        if name:
            params[name] = value
        return 'get_playlists_table', params

    @raw_json
    def _get_X_by(self, endpoint: str, time_range: int = None, y_axis: str = None, user_id: str = None, grouping: bool = False) -> dict:
        grouping = bool_to_int(boolean=grouping)
        if _is_invalid_choice(value=y_axis, variable_name='y_axis',
                              choices=static.stats_type):
            return False, None
        params = build_optional_params(time_range=time_range, y_axis=y_axis, user_id=user_id, grouping=grouping)
        return endpoint, params


    def get_plays_by_date(self, time_range: int = None, y_axis: str = None, user_id: str = None, grouping: bool = False) -> dict:
        return self._get_X_by(endpoint='get_plays_by_date', time_range=time_range, y_axis=y_axis, user_id=user_id, grouping=grouping)

    def get_plays_by_day_of_week(self, time_range: int = None, y_axis: str = None, user_id: str = None, grouping: bool = False) -> dict:
        return self._get_X_by(endpoint='get_plays_by_dayofweek', time_range=time_range, y_axis=y_axis, user_id=user_id, grouping=grouping)

    def get_plays_by_hour_of_day(self, time_range: int = None, y_axis: str = None, user_id: str = None, grouping: bool = False) -> dict:
        return self._get_X_by(endpoint='get_plays_by_hourofday', time_range=time_range, y_axis=y_axis, user_id=user_id, grouping=grouping)

    def get_plays_by_source_resolution(self, time_range: int = None, y_axis: str = None, user_id: str = None, grouping: bool = False) -> dict:
        return self._get_X_by(endpoint='get_plays_by_source_resolution', time_range=time_range, y_axis=y_axis, user_id=user_id, grouping=grouping)

    def get_plays_by_stream_resolution(self, time_range: int = None, y_axis: str = None, user_id: str = None, grouping: bool = False) -> dict:
        return self._get_X_by(endpoint='get_plays_by_stream_resolution', time_range=time_range, y_axis=y_axis, user_id=user_id, grouping=grouping)

    def get_plays_by_stream_type(self, time_range: int = None, y_axis: str = None, user_id: str = None, grouping: bool = False) -> dict:
        return self._get_X_by(endpoint='get_plays_by_stream_type', time_range=time_range, y_axis=y_axis, user_id=user_id, grouping=grouping)

    def get_plays_by_top_10_platforms(self, time_range: int = None, y_axis: str = None, user_id: str = None, grouping: bool = False) -> dict:
        return self._get_X_by(endpoint='get_plays_by_top_10_platforms', time_range=time_range, y_axis=y_axis, user_id=user_id, grouping=grouping)

    def get_plays_by_top_10_users(self, time_range: int = None, y_axis: str = None, user_id: str = None, grouping: bool = False) -> dict:
        return self._get_X_by(endpoint='get_plays_by_top_10_users', time_range=time_range, y_axis=y_axis, user_id=user_id, grouping=grouping)

    def get_plays_per_month(self, time_range: int = None, y_axis: str = None, user_id: str = None, grouping: bool = False) -> dict:
        return self._get_X_by(endpoint='get_plays_per_month', time_range=time_range, y_axis=y_axis, user_id=user_id, grouping=grouping)

    @raw_json
    def get_plex_log(self, window: int = None, log_type: str = None) -> dict:
        if _is_invalid_choice(value=log_type, variable_name='log_type',
                              choices=static.plex_log_types):
            return False, None
        params = build_optional_params(window=window, log_type=log_type)
        return 'get_plex_log', params

    def get_pms_token(self, username: str, password: str) -> str:
        params = {'username': username, 'password': password}
        json_data = self._get_json(command='get_pms_token', params=params)
        if _success_result(json_data=json_data):
            return _get_response_data(json_data=json_data)
        return static.empty_string

    @property
    @raw_json
    def pms_update(self) -> dict:
        return 'get_pms_update', None

    @raw_json
    def get_recently_added(self, count: int, start: int = 0, media_type: str = None, section_id: str = None) -> dict:
        if _is_invalid_choice(value=media_type, variable_name='media_type',
                              choices=static.recently_added_media_types):
            return False, None
        params = build_optional_params(start=start, media_type=media_type, section_id=section_id)
        params['count'] = count
        return 'get_recently_added', params

    @property
    def server_friendly_name(self) -> str:
        json_data = self._get_json(command='get_server_friendly_name')
        if _success_result(json_data=json_data):
            return _get_response_data(json_data=json_data)
        return static.empty_string

    @raw_json
    def get_server_id(self, hostname: str, port: int, ssl: bool = False, remote: bool = False) -> dict:
        ssl = bool_to_int(boolean=ssl)
        remote = bool_to_int(boolean=remote)
        params = build_optional_params(ssl=ssl, remote=remote)
        params['hostname'] = hostname
        params['port'] = port
        return 'get_server_id', params

    @property
    @raw_json
    def server_identity(self) -> dict:
        return 'get_server_identity', None

    @property
    @raw_json
    def server_info(self) -> dict:
        return 'get_server_info', None

    @property
    @raw_json
    def server_list(self) -> dict:
        return 'get_server_list', None

    def get_server_pref(self, pref: str) -> str:
        json_data = self._get_json(command='get_server_pref', params={'pref': pref})
        if _success_result(json_data=json_data):
            return _get_response_data(json_data=json_data)
        return static.empty_string

    @property
    @raw_json
    def servers_info(self) -> dict:
        return 'get_servers_info', None

    @raw_json
    def get_settings(self, key: str = None) -> dict:
        params = build_optional_params(key=key)
        return 'get_settings', params

    @raw_json
    def get_stream_data(self, row_id: int = None, session_key: int = None) -> dict:
        if not _one_needed(row_id=row_id, session_key=session_key):
            return False, None
        params = {}
        name, value = _which_used(row_id=row_id, session_key=session_key)
        if name:
            params[name] = value
        return 'get_stream_data', params

    def get_stream_type_by_top_10_platforms(self, time_range: int = None, y_axis: str = None, user_id: str = None, grouping: bool = False) -> dict:
        return self._get_X_by(endpoint='get_stream_type_by_top_10_platforms', time_range=time_range, y_axis=y_axis, user_id=user_id, grouping=grouping)

    def get_stream_type_by_top_10_users(self, time_range: int = None, y_axis: str = None, user_id: str = None, grouping: bool = False) -> dict:
        return self._get_X_by(endpoint='get_stream_type_by_top_10_users', time_range=time_range, y_axis=y_axis, user_id=user_id, grouping=grouping)

    @raw_json
    def get_synced_items(self, machine_id: str, user_id: str = None) -> dict:
        params = build_optional_params(user_id=user_id)
        params['machine_id'] = machine_id
        return 'get_synced_items', params

    @raw_json
    def get_user(self, user_id: str) -> dict:
        return 'get_user', {'user_id': user_id}

    @raw_json
    def get_user_ips(self, user_id: str, order_column: str = None, order_direction: str = None, start: int = 0, length: int = 25, search: str = None) -> dict:
        if _is_invalid_choice(value=order_column, variable_name='order_column',
                              choices=static.user_ips_order_columns):
            return False, None
        if _is_invalid_choice(value=order_direction, variable_name='order_direction',
                              choices=static.order_direction):
            return False, None
        params = build_optional_params(order_column=order_column, order_dir=order_direction, start=start, length=length, search=search)
        params['user_id'] = user_id
        return 'get_user_ips', params

    @raw_json
    def get_user_logins(self, user_id: str, order_column: str = None, order_direction: str = None, start: int = 0, length: int = 25, search: str = None) -> dict:
        if _is_invalid_choice(value=order_column, variable_name='order_column',
                              choices=static.user_logins_order_columns):
            return False, None
        if _is_invalid_choice(value=order_direction, variable_name='order_direction',
                              choices=static.order_direction):
            return False, None
        params = build_optional_params(order_column=order_column, order_dir=order_direction, start=start, length=length, search=search)
        params['user_id'] = user_id
        return 'get_user_logins', params

    @property
    @raw_json
    def user_names(self) -> dict:
        return 'get_user_names', None

    @raw_json
    def get_user_player_stats(self, user_id: str, grouping: bool = False) -> dict:
        grouping = bool_to_int(boolean=grouping)
        params = build_optional_params(grouping=grouping)
        params['user_id'] = user_id
        return 'get_user_player_stats', params

    @raw_json
    def get_user_watch_time_stats(self, user_id: str, grouping: bool = False, query_days: List[int] = None) -> dict:
        grouping = bool_to_int(boolean=grouping)
        params = build_optional_params(grouping=grouping)
        if query_days:
            params['query_days'] = int_list_to_string(int_list=query_days)
        params['user_id'] = user_id
        return 'get_user_watch_time_stats', params

    @property
    @raw_json
    def users(self) -> dict:
        return 'get_users', None

    @raw_json
    def get_users_table(self, grouping: bool = False, order_column: str = None, order_direction: str = None, start: int = 0, length: int = 25, search: str = None) -> dict:
        grouping = bool_to_int(boolean=grouping)
        if _is_invalid_choice(value=order_column, variable_name='order_column',
                              choices=static.user_logins_order_columns):
            return False, None
        if _is_invalid_choice(value=order_direction, variable_name='order_direction',
                              choices=static.order_direction):
            return False, None
        params = build_optional_params(grouping=grouping, order_column=order_column, order_dir=order_direction, start=start, length=length, search=search)
        return 'get_users_table', params

    @raw_json
    def get_whois_lookup(self, ip_address: str) -> dict:
        return 'get_whois_lookup', {'ip_address': ip_address}

    @set_and_forget
    def import_config(self, config_file_path: str, backup: bool = True) -> bool:
        return 'import_config', {'config_path': config_file_path, 'backup': backup}

    @set_and_forget
    def import_database(self, app: str, database_file_path: str, method: str = None, table_name: str = None, backup: bool = True) -> bool:
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
        params = build_optional_params(method=method, table_name=table_name, backup=backup)
        params['app'] = app
        params['database_path'] = database_file_path
        return 'import_database', params

    @set_and_forget
    def notify(self, notifier_id: int, subject: str, body: str, headers: str = None, script_args: str = None) -> bool:
        params = build_optional_params(headers=headers, script_args=script_args)
        params['notifier_id'] = notifier_id
        params['subject'] = subject
        params['body'] = body
        return 'notify', params
























    def get_user_watch_time_stats(self, user_id: str, days: List[int] = None) -> Union[
        WatchTimeStats, None]:
        params = {'user_id': user_id}
        if days:
            params['query_days'] = ','.join(map(str, days))
        json_data = self._get_json(command="get_user_watch_time_stats", params=params)
        if json_data:
            return WatchTimeStats(data=json_data['response']['data'])
        return None

    def get_user_ips(self, user_id: str) -> dict:
        json_data = self._get_json(command='get_user_ips', params={'user_id': user_id, 'order_column': 'last_seen'})
        if json_data:
            return json_data['response']['data']
        return {}

    def get_last_time_user_seen(self, user_id: str) -> int:
        user_ips = self.get_user_ips(user_id=user_id)
        if not user_ips:
            return 0
        return user_ips[0]['last_seen']

    def refresh_users(self) -> bool:
        if self._get(command='refresh_users_list'):
            return True
        return False

    def delete_user(self, plex_username: str) -> bool:
        if self._get(command='delete_user', params={'user_id': plex_username}):
            return True
        return False

    # ACTIVITY

    def home_stats(self, time_range: int = 30, stat_category: str = 'user', stat_type: str = 'duration',
                   stat_count: int = 5) -> Union[HomeStats, None]:
        category_number = _stat_category_to_number(stat_category=stat_category)
        if not category_number:
            return None
        params = {'time_range': time_range,
                  'stats_type': stat_type,
                  'stats_count': stat_count}
        json_data = self._get_json(command='get_home_stats', params=params)
        if json_data:
            return HomeStats(data=json_data['response']['data'])
        return None

    @property
    def current_activity(self) -> dict:
        json_data = self._get_json(command="get_activity")
        if json_data:
            return json_data['response']['data']
        return {}

    # MEDIA

    @property
    def libraries(self) -> dict:
        json_data = self._get_json(command="get_libraries")
        if json_data:
            return json_data['response']['data']
        return {}

    def get_library_media_info(self, section_id: str) -> dict:
        json_data = self._get_json(command='get_library_media_info', params={'section_id': section_id})
        if json_data:
            return json_data['response']['data']
        return {}

    def recently_added(self, count: int = 5) -> dict:
        json_data = self._get_json(command='get_recently_added', params={'count': count})
        if json_data:
            return json_data['response']['data']
        return {}

    def image_thumb_url(self, thumb: str) -> str:
        return f'{self.url}&cmd=pms_image_proxy&img={thumb}'

    def delete_image_cache(self) -> bool:
        if self._get(command='delete_image_cache'):
            return True
        return False

    def search(self, keyword: str) -> dict:
        json_data = self._get_json(command='search', params={'query': keyword})
        if json_data:
            return json_data['response']['data']
        return {}

    # SESSIONS

    def terminate_session(self, session_id, message: str = None) -> bool:
        params = {'session_id': session_id}
        if message:
            params['message'] = message
        if self._get(command='terminate_session', params=params):
            return True
        return False