# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T01:28:24+00:00

from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel


class Docs(BaseModel):
    add_newsletter_config: Optional[str]
    add_notifier_config: Optional[str]
    arnold: Optional[str]
    backup_config: Optional[str]
    backup_db: Optional[str]
    delete_all_library_history: Optional[str]
    delete_all_user_history: Optional[str]
    delete_cache: Optional[str]
    delete_export: Optional[str]
    delete_history: Optional[str]
    delete_hosted_images: Optional[str]
    delete_image_cache: Optional[str]
    delete_library: Optional[str]
    delete_login_log: Optional[str]
    delete_lookup_info: Optional[str]
    delete_media_info_cache: Optional[str]
    delete_mobile_device: Optional[str]
    delete_newsletter: Optional[str]
    delete_newsletter_log: Optional[str]
    delete_notification_log: Optional[str]
    delete_notifier: Optional[str]
    delete_recently_added: Optional[str]
    delete_synced_item: Optional[str]
    delete_temp_sessions: Optional[str]
    delete_user: Optional[str]
    docs: Optional[str]
    docs_md: Optional[str]
    download_config: Optional[str]
    download_database: Optional[str]
    download_export: Optional[str]
    download_log: Optional[str]
    download_plex_log: Optional[str]
    edit_library: Optional[str]
    edit_user: Optional[str]
    export_metadata: Optional[str]
    get_activity: Optional[str]
    get_apikey: Optional[str]
    get_collections_table: Optional[str]
    get_date_formats: Optional[str]
    get_export_fields: Optional[str]
    get_exports_table: Optional[str]
    get_geoip_lookup: Optional[str]
    get_history: Optional[str]
    get_home_stats: Optional[str]
    get_libraries: Optional[str]
    get_libraries_table: Optional[str]
    get_library: Optional[str]
    get_library_media_info: Optional[str]
    get_library_names: Optional[str]
    get_library_user_stats: Optional[str]
    get_library_watch_time_stats: Optional[str]
    get_logs: Optional[str]
    get_metadata: Optional[str]
    get_new_rating_keys: Optional[str]
    get_newsletter_config: Optional[str]
    get_newsletter_log: Optional[str]
    get_newsletters: Optional[str]
    get_notification_log: Optional[str]
    get_notifier_config: Optional[str]
    get_notifier_parameters: Optional[str]
    get_notifiers: Optional[str]
    get_old_rating_keys: Optional[str]
    get_playlists_table: Optional[str]
    get_plays_by_date: Optional[str]
    get_plays_by_dayofweek: Optional[str]
    get_plays_by_hourofday: Optional[str]
    get_plays_by_source_resolution: Optional[str]
    get_plays_by_stream_resolution: Optional[str]
    get_plays_by_stream_type: Optional[str]
    get_plays_by_top_10_platforms: Optional[str]
    get_plays_by_top_10_users: Optional[str]
    get_plays_per_month: Optional[str]
    get_plex_log: Optional[str]
    get_pms_update: Optional[str]
    get_recently_added: Optional[str]
    get_server_friendly_name: Optional[str]
    get_server_id: Optional[str]
    get_server_identity: Optional[str]
    get_server_info: Optional[str]
    get_server_list: Optional[str]
    get_server_pref: Optional[str]
    get_servers_info: Optional[str]
    get_settings: Optional[str]
    get_stream_data: Optional[str]
    get_stream_type_by_top_10_platforms: Optional[str]
    get_stream_type_by_top_10_users: Optional[str]
    get_synced_items: Optional[str]
    get_user: Optional[str]
    get_user_ips: Optional[str]
    get_user_logins: Optional[str]
    get_user_names: Optional[str]
    get_user_player_stats: Optional[str]
    get_user_watch_time_stats: Optional[str]
    get_users: Optional[str]
    get_users_table: Optional[str]
    get_whois_lookup: Optional[str]
    import_config: Optional[str]
    import_database: Optional[str]
    logout_user_session: Optional[str]
    notify: Optional[str]
    notify_newsletter: Optional[str]
    notify_recently_added: Optional[str]
    pms_image_proxy: Optional[str]
    refresh_libraries_list: Optional[str]
    refresh_users_list: Optional[str]
    register_device: Optional[str]
    restart: Optional[str]
    search: Optional[str]
    server_status: Optional[str]
    set_mobile_device_config: Optional[str]
    set_newsletter_config: Optional[str]
    set_notifier_config: Optional[str]
    sql: Optional[str]
    status: Optional[str]
    terminate_session: Optional[str]
    undelete_library: Optional[str]
    undelete_user: Optional[str]
    update: Optional[str]
    update_check: Optional[str]
    update_metadata_details: Optional[str]


class Response(BaseModel):
    result: Optional[str]
    message: Any
    data: Docs


class Model(BaseModel):
    response: Response
