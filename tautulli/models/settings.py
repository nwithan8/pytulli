# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:23:37+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class IFTTTModel(BaseModel):
    ifttt_on_stop: Optional[bool] = None
    ifttt_on_pause: Optional[bool] = None
    ifttt_key: Optional[str] = None
    ifttt_on_concurrent: Optional[bool] = None
    ifttt_on_created: Optional[bool] = None
    ifttt_on_buffer: Optional[bool] = None
    ifttt_enabled: Optional[bool] = None
    ifttt_on_pmsupdate: Optional[bool] = None
    ifttt_on_newdevice: Optional[bool] = None
    ifttt_on_intdown: Optional[bool] = None
    ifttt_on_extup: Optional[bool] = None
    ifttt_on_intup: Optional[bool] = None
    ifttt_on_resume: Optional[bool] = None
    ifttt_on_watched: Optional[bool] = None
    ifttt_event: Optional[str] = None
    ifttt_on_extdown: Optional[bool] = None
    ifttt_on_play: Optional[bool] = None


class GrowlModel(BaseModel):
    growl_enabled: Optional[bool] = None
    growl_on_play: Optional[bool] = None
    growl_on_stop: Optional[bool] = None
    growl_on_buffer: Optional[bool] = None
    growl_on_pause: Optional[bool] = None
    growl_on_intdown: Optional[bool] = None
    growl_host: Optional[str] = None
    growl_on_extup: Optional[bool] = None
    growl_on_newdevice: Optional[bool] = None
    growl_on_pmsupdate: Optional[bool] = None
    growl_password: Optional[str] = None
    growl_on_resume: Optional[bool] = None
    growl_on_created: Optional[bool] = None
    growl_on_concurrent: Optional[bool] = None
    growl_on_watched: Optional[bool] = None
    growl_on_intup: Optional[bool] = None
    growl_on_extdown: Optional[bool] = None


class PMSModel(BaseModel):
    pms_use_bif: Optional[bool] = None
    pms_uuid: Optional[str] = None
    pms_url: Optional[str] = None
    pms_update_channel: Optional[str] = None
    pms_update_distro: Optional[str] = None
    pms_name: Optional[str] = None
    pms_logs_folder: Optional[str] = None
    pms_plexpass: Optional[int] = None
    pms_token: Optional[str] = None
    pms_port: Optional[int] = None
    pms_is_remote: Optional[int] = None
    pms_identifier: Optional[str] = None
    pms_ssl: Optional[int] = None
    pms_version: Optional[str] = None
    pms_update_distro_build: Optional[str] = None
    pms_ip: Optional[str] = None
    pms_logs_line_cap: Optional[int] = None
    pms_platform: Optional[str] = None
    pms_url_manual: Optional[int] = None
    pms_web_url: Optional[str] = None
    pms_is_cloud: Optional[int] = None
    pms_url_override: Optional[str] = None


class MonitoringModel(BaseModel):
    notify_upload_posters: Optional[int] = None
    movie_notify_enable: Optional[bool] = None
    notify_on_resume_body_text: Optional[str] = None
    notify_on_pmsupdate_body_text: Optional[str] = None
    refresh_libraries_on_startup: Optional[bool] = None
    session_db_write_attempts: Optional[int] = None
    notify_on_created_body_text: Optional[str] = None
    buffer_wait: Optional[int] = None
    notify_on_intup_subject_text: Optional[str] = None
    notify_recently_added_grandparent: Optional[bool] = None
    notify_on_newdevice_subject_text: Optional[str] = None
    notify_on_extup_subject_text: Optional[str] = None
    notify_on_watched_subject_text: Optional[str] = None
    notify_on_pause_subject_text: Optional[str] = None
    notify_on_extup_body_text: Optional[str] = None
    notify_on_watched_body_text: Optional[str] = None
    music_notify_on_pause: Optional[bool] = None
    notify_on_start_body_text: Optional[str] = None
    notify_on_pause_body_text: Optional[str] = None
    notify_on_buffer_body_text: Optional[str] = None
    music_notify_on_stop: Optional[bool] = None
    tv_notify_on_stop: Optional[bool] = None
    notify_on_stop_body_text: Optional[str] = None
    notify_on_created_subject_text: Optional[str] = None
    notify_on_extdown_body_text: Optional[str] = None
    notify_scripts_args_text: Optional[str] = None
    music_logging_enable: Optional[bool] = None
    movie_notify_on_stop: Optional[bool] = None
    notify_watched_percent: Optional[int] = None
    notify_on_concurrent_subject_text: Optional[str] = None
    notify_on_concurrent_body_text: Optional[str] = None
    tv_logging_enable: Optional[bool] = None
    tv_notify_enable: Optional[bool] = None
    notify_recently_added_delay: Optional[int] = None
    notify_on_intdown_body_text: Optional[str] = None
    logging_ignore_interval: Optional[int] = None
    notify_on_newdevice_body_text: Optional[str] = None
    refresh_users_interval: Optional[int] = None
    monitoring_use_websocket: Optional[bool] = None
    monitor_pms_updates: Optional[bool] = None
    notify_on_start_subject_text: Optional[str] = None
    notify_recently_added: Optional[bool] = None
    notify_on_pmsupdate_subject_text: Optional[str] = None
    music_notify_enable: Optional[bool] = None
    movie_notify_on_start: Optional[bool] = None
    notify_concurrent_by_ip: Optional[bool] = None
    refresh_users_on_startup: Optional[bool] = None
    buffer_threshold: Optional[int] = None
    notify_on_extdown_subject_text: Optional[str] = None
    refresh_libraries_interval: Optional[int] = None
    tv_notify_on_start: Optional[bool] = None
    video_logging_enable: Optional[bool] = None
    notify_on_resume_subject_text: Optional[str] = None
    notify_concurrent_threshold: Optional[int] = None
    notify_on_stop_subject_text: Optional[str] = None
    movie_notify_on_pause: Optional[bool] = None
    notify_consecutive: Optional[bool] = None
    movie_logging_enable: Optional[bool] = None
    notify_on_intup_body_text: Optional[str] = None
    notify_on_intdown_subject_text: Optional[str] = None
    music_notify_on_start: Optional[bool] = None
    tv_notify_on_pause: Optional[bool] = None
    monitor_remote_access: Optional[bool] = None
    imgur_client_id: Optional[str] = None
    monitoring_interval: Optional[int] = None
    notify_on_buffer_subject_text: Optional[str] = None
    tv_watched_percent: Optional[int] = None
    notify_group_recently_added_grandparent: Optional[bool] = None
    notify_recently_added_upgrade: Optional[bool] = None
    notify_group_recently_added: Optional[bool] = None
    notify_group_recently_added_parent: Optional[bool] = None
    movie_watched_percent: Optional[int] = None
    music_watched_percent: Optional[int] = None
    notify_continued_session_threshold: Optional[int] = None
    notify_remote_access_threshold: Optional[int] = None
    notify_new_device_initial_only: Optional[bool] = None


class GetFileSizesHoldModel(BaseModel):
    section_ids: Optional[List] = None
    rating_keys: Optional[List] = None


class GeneralModel(BaseModel):
    week_start_monday: Optional[bool] = None
    git_token: Optional[str] = None
    home_stats_cards: Optional[List[str]] = None
    backup_interval: Optional[int] = None
    graph_days: Optional[int] = None
    graph_type: Optional[str] = None
    get_file_sizes: Optional[bool] = None
    http_basic_auth: Optional[bool] = None
    api_sql: Optional[bool] = None
    http_root: Optional[str] = None
    http_proxy: Optional[bool] = None
    freeze_db: Optional[bool] = None
    ip_logging_enable: Optional[bool] = None
    launch_browser: Optional[bool] = None
    http_username: Optional[str] = None
    https_create_cert: Optional[bool] = None
    do_not_override_git_branch: Optional[bool] = None
    home_stats_length: Optional[str] = None
    http_host: Optional[str] = None
    first_run_complete: Optional[bool] = None
    enable_https: Optional[bool] = None
    check_github: Optional[bool] = None
    api_enabled: Optional[bool] = None
    git_path: Optional[str] = None
    update_labels: Optional[bool] = None
    config_version: Optional[str] = None
    check_github_interval: Optional[int] = None
    https_ip: Optional[str] = None
    group_history_tables: Optional[bool] = None
    https_domain: Optional[str] = None
    graph_tab: Optional[str] = None
    geoip_db: Optional[str] = None
    http_password: Optional[str] = None
    home_stats_count: Optional[str] = None
    backup_dir: Optional[str] = None
    git_user: Optional[str] = None
    interface: Optional[str] = None
    cache_images: Optional[bool] = None
    log_blacklist: Optional[bool] = None
    graph_months: Optional[str] = None
    cleanup_files: Optional[bool] = None
    check_github_on_startup: Optional[bool] = None
    http_port: Optional[int] = None
    log_dir: Optional[str] = None
    update_db_interval: Optional[int] = None
    allow_guest_access: Optional[bool] = None
    time_format: Optional[str] = None
    cache_dir: Optional[str] = None
    home_sections: Optional[List[str]] = None
    backup_days: Optional[int] = None
    https_cert: Optional[str] = None
    api_key: Optional[str] = None
    update_section_ids: Optional[bool] = None
    date_format: Optional[str] = None
    home_stats_type: Optional[bool] = None
    http_environment: Optional[str] = None
    history_table_activity: Optional[bool] = None
    https_key: Optional[str] = None
    http_hash_password: Optional[bool] = None
    home_library_cards: Optional[List[str]] = None
    http_hashed_password: Optional[bool] = None
    git_branch: Optional[str] = None
    anon_redirect: Optional[str] = None
    http_plex_admin: Optional[bool] = None
    update_show_changelog: Optional[int] = None
    show_advanced_settings: Optional[bool] = None
    git_remote: Optional[str] = None
    https_cert_chain: Optional[str] = None
    git_repo: Optional[str] = None
    home_stats_recently_added_count: Optional[str] = None
    themoviedb_apikey: Optional[str] = None
    tvmaze_lookup: Optional[bool] = None
    update_notifiers_db: Optional[bool] = None
    themoviedb_lookup: Optional[bool] = None
    plexpy_auto_update: Optional[bool] = None
    update_libraries_db_notify: Optional[bool] = None
    home_refresh_interval: Optional[int] = None
    http_base_url: Optional[str] = None
    win_sys_tray: Optional[bool] = None
    musicbrainz_lookup: Optional[bool] = None
    geoip_db_update_days: Optional[int] = None
    maxmind_license_key: Optional[str] = None
    geoip_db_installed: Optional[bool] = None
    launch_startup: Optional[bool] = None
    sys_tray_icon: Optional[bool] = None
    export_dir: Optional[str] = None
    http_rate_limit_attempts: Optional[int] = None
    http_rate_limit_attempts_interval: Optional[int] = None
    http_rate_limit_lockout_time: Optional[int] = None
    get_file_sizes_hold: Optional[GetFileSizesHoldModel] = None
    interface_list: Optional[List[str]] = None


class SlackModel(BaseModel):
    slack_on_stop: Optional[bool] = None
    slack_icon_emoji: Optional[str] = None
    slack_on_watched: Optional[bool] = None
    slack_on_extup: Optional[bool] = None
    slack_on_resume: Optional[bool] = None
    slack_hook: Optional[str] = None
    slack_incl_subject: Optional[bool] = None
    slack_on_pmsupdate: Optional[bool] = None
    slack_channel: Optional[str] = None
    slack_on_buffer: Optional[bool] = None
    slack_on_extdown: Optional[bool] = None
    slack_username: Optional[str] = None
    slack_incl_pmslink: Optional[bool] = None
    slack_enabled: Optional[bool] = None
    slack_incl_poster: Optional[bool] = None
    slack_on_pause: Optional[bool] = None
    slack_on_concurrent: Optional[bool] = None
    slack_on_intup: Optional[bool] = None
    slack_on_intdown: Optional[bool] = None
    slack_on_play: Optional[bool] = None
    slack_on_created: Optional[bool] = None
    slack_on_newdevice: Optional[bool] = None


class BoxcarModel(BaseModel):
    boxcar_sound: Optional[str] = None
    boxcar_on_newdevice: Optional[bool] = None
    boxcar_on_watched: Optional[bool] = None
    boxcar_on_buffer: Optional[bool] = None
    boxcar_on_stop: Optional[bool] = None
    boxcar_on_extdown: Optional[bool] = None
    boxcar_on_pmsupdate: Optional[bool] = None
    boxcar_on_intdown: Optional[bool] = None
    boxcar_on_pause: Optional[bool] = None
    boxcar_on_play: Optional[bool] = None
    boxcar_on_created: Optional[bool] = None
    boxcar_on_intup: Optional[bool] = None
    boxcar_on_resume: Optional[bool] = None
    boxcar_on_concurrent: Optional[bool] = None
    boxcar_enabled: Optional[bool] = None
    boxcar_on_extup: Optional[bool] = None
    boxcar_token: Optional[str] = None


class PushBulletModel(BaseModel):
    pushbullet_on_play: Optional[bool] = None
    pushbullet_channel_tag: Optional[str] = None
    pushbullet_on_buffer: Optional[bool] = None
    pushbullet_apikey: Optional[str] = None
    pushbullet_on_resume: Optional[bool] = None
    pushbullet_on_concurrent: Optional[bool] = None
    pushbullet_on_created: Optional[bool] = None
    pushbullet_on_pause: Optional[bool] = None
    pushbullet_on_extdown: Optional[bool] = None
    pushbullet_on_stop: Optional[bool] = None
    pushbullet_on_extup: Optional[bool] = None
    pushbullet_on_pmsupdate: Optional[bool] = None
    pushbullet_enabled: Optional[bool] = None
    pushbullet_on_watched: Optional[bool] = None
    pushbullet_on_intdown: Optional[bool] = None
    pushbullet_deviceid: Optional[str] = None
    pushbullet_on_intup: Optional[bool] = None
    pushbullet_on_newdevice: Optional[bool] = None


class ScriptsModel(BaseModel):
    scripts_on_newdevice: Optional[bool] = None
    scripts_on_stop: Optional[bool] = None
    scripts_on_intdown_script: Optional[str] = None
    scripts_on_newdevice_script: Optional[str] = None
    scripts_folder: Optional[str] = None
    scripts_on_pmsupdate: Optional[bool] = None
    scripts_on_buffer: Optional[bool] = None
    scripts_on_concurrent: Optional[bool] = None
    scripts_on_intup_script: Optional[str] = None
    scripts_on_intdown: Optional[bool] = None
    scripts_on_resume: Optional[bool] = None
    scripts_on_extdown_script: Optional[str] = None
    scripts_on_extup: Optional[bool] = None
    scripts_on_play_script: Optional[str] = None
    scripts_on_created_script: Optional[str] = None
    scripts_on_pmsupdate_script: Optional[str] = None
    scripts_on_resume_script: Optional[str] = None
    scripts_on_stop_script: Optional[str] = None
    scripts_on_watched_script: Optional[str] = None
    scripts_enabled: Optional[bool] = None
    scripts_on_extup_script: Optional[str] = None
    scripts_on_extdown: Optional[bool] = None
    scripts_on_created: Optional[bool] = None
    scripts_on_concurrent_script: Optional[str] = None
    scripts_on_pause_script: Optional[str] = None
    scripts_on_pause: Optional[bool] = None
    scripts_on_intup: Optional[bool] = None
    scripts_timeout: Optional[int] = None
    scripts_on_watched: Optional[bool] = None
    scripts_on_buffer_script: Optional[str] = None
    scripts_on_play: Optional[bool] = None


class NMAModel(BaseModel):
    nma_on_pmsupdate: Optional[bool] = None
    nma_priority: Optional[bool] = None
    nma_on_intdown: Optional[bool] = None
    nma_on_buffer: Optional[bool] = None
    nma_on_play: Optional[bool] = None
    nma_on_newdevice: Optional[bool] = None
    nma_on_resume: Optional[bool] = None
    nma_on_concurrent: Optional[bool] = None
    nma_on_watched: Optional[bool] = None
    nma_apikey: Optional[str] = None
    nma_on_intup: Optional[bool] = None
    nma_on_stop: Optional[bool] = None
    nma_on_created: Optional[bool] = None
    nma_on_pause: Optional[bool] = None
    nma_enabled: Optional[bool] = None
    nma_on_extdown: Optional[bool] = None
    nma_on_extup: Optional[bool] = None


class HipchatModel(BaseModel):
    hipchat_emoticon: Optional[str] = None
    hipchat_incl_subject: Optional[bool] = None
    hipchat_on_extdown: Optional[bool] = None
    hipchat_on_intup: Optional[bool] = None
    hipchat_enabled: Optional[bool] = None
    hipchat_on_created: Optional[bool] = None
    hipchat_on_newdevice: Optional[bool] = None
    hipchat_on_play: Optional[bool] = None
    hipchat_on_resume: Optional[bool] = None
    hipchat_on_buffer: Optional[bool] = None
    hipchat_incl_poster: Optional[bool] = None
    hipchat_on_watched: Optional[bool] = None
    hipchat_color: Optional[str] = None
    hipchat_on_concurrent: Optional[bool] = None
    hipchat_url: Optional[str] = None
    hipchat_on_pmsupdate: Optional[bool] = None
    hipchat_on_extup: Optional[bool] = None
    hipchat_incl_pmslink: Optional[bool] = None
    hipchat_on_pause: Optional[bool] = None
    hipchat_on_intdown: Optional[bool] = None
    hipchat_on_stop: Optional[bool] = None


class PushalotModel(BaseModel):
    pushalot_apikey: Optional[str] = None
    pushalot_on_pmsupdate: Optional[bool] = None
    pushalot_enabled: Optional[bool] = None
    pushalot_on_extdown: Optional[bool] = None
    pushalot_on_created: Optional[bool] = None
    pushalot_on_pause: Optional[bool] = None
    pushalot_on_stop: Optional[bool] = None
    pushalot_on_buffer: Optional[bool] = None
    pushalot_on_intup: Optional[bool] = None
    pushalot_on_newdevice: Optional[bool] = None
    pushalot_on_concurrent: Optional[bool] = None
    pushalot_on_watched: Optional[bool] = None
    pushalot_on_play: Optional[bool] = None
    pushalot_on_extup: Optional[bool] = None
    pushalot_on_intdown: Optional[bool] = None
    pushalot_on_resume: Optional[bool] = None


class ProwlModel(BaseModel):
    prowl_on_created: Optional[bool] = None
    prowl_on_play: Optional[bool] = None
    prowl_on_extdown: Optional[bool] = None
    prowl_on_pause: Optional[bool] = None
    prowl_on_intdown: Optional[bool] = None
    prowl_on_intup: Optional[bool] = None
    prowl_enabled: Optional[bool] = None
    prowl_priority: Optional[bool] = None
    prowl_on_pmsupdate: Optional[bool] = None
    prowl_on_newdevice: Optional[bool] = None
    prowl_on_extup: Optional[bool] = None
    prowl_on_watched: Optional[bool] = None
    prowl_on_buffer: Optional[bool] = None
    prowl_on_resume: Optional[bool] = None
    prowl_on_stop: Optional[bool] = None
    prowl_on_concurrent: Optional[bool] = None
    prowl_keys: Optional[str] = None


class AdvancedModel(BaseModel):
    verify_ssl_cert: Optional[bool] = None
    journal_mode: Optional[str] = None
    pms_timeout: Optional[int] = None
    cache_sizemb: Optional[int] = None
    session_db_write_attempts: Optional[int] = None
    system_analytics: Optional[bool] = None
    notification_threads: Optional[int] = None
    remote_access_ping_threshold: Optional[int] = None
    websocket_connection_timeout: Optional[int] = None
    config_version: Optional[int] = None
    metadata_cache_seconds: Optional[int] = None
    websocket_connection_attempts: Optional[int] = None
    jwt_secret: Optional[str] = None
    websocket_monitor_ping_pong: Optional[bool] = None
    synchronous_mode: Optional[str] = None
    pms_update_check_interval: Optional[int] = None
    jwt_update_secret: Optional[bool] = None
    verbose_logs: Optional[bool] = None
    add_live_tv_library: Optional[bool] = None
    remote_access_ping_interval: Optional[int] = None
    check_github_cache_seconds: Optional[int] = None
    export_threads: Optional[int] = None


class FacebookModel(BaseModel):
    facebook_app_secret: Optional[str] = None
    facebook_on_stop: Optional[bool] = None
    facebook_token: Optional[str] = None
    facebook_on_buffer: Optional[bool] = None
    facebook_on_play: Optional[bool] = None
    facebook_enabled: Optional[bool] = None
    facebook_on_intup: Optional[bool] = None
    facebook_incl_poster: Optional[bool] = None
    facebook_on_pmsupdate: Optional[bool] = None
    facebook_on_intdown: Optional[bool] = None
    facebook_on_extup: Optional[bool] = None
    facebook_on_resume: Optional[bool] = None
    facebook_on_concurrent: Optional[bool] = None
    facebook_on_extdown: Optional[bool] = None
    facebook_group: Optional[str] = None
    facebook_on_pause: Optional[bool] = None
    facebook_app_id: Optional[str] = None
    facebook_incl_pmslink: Optional[bool] = None
    facebook_on_newdevice: Optional[bool] = None
    facebook_on_watched: Optional[bool] = None
    facebook_redirect_uri: Optional[str] = None
    facebook_incl_subject: Optional[bool] = None
    facebook_on_created: Optional[bool] = None


class EmailModel(BaseModel):
    email_from_name: Optional[str] = None
    email_bcc: Optional[str] = None
    email_on_pause: Optional[bool] = None
    email_smtp_password: Optional[str] = None
    email_tls: Optional[bool] = None
    email_smtp_port: Optional[str] = None
    email_on_watched: Optional[bool] = None
    email_smtp_server: Optional[str] = None
    email_on_intdown: Optional[bool] = None
    email_on_concurrent: Optional[bool] = None
    email_on_intup: Optional[bool] = None
    email_enabled: Optional[bool] = None
    email_on_buffer: Optional[bool] = None
    email_on_resume: Optional[bool] = None
    email_smtp_user: Optional[str] = None
    email_cc: Optional[str] = None
    email_on_newdevice: Optional[bool] = None
    email_on_stop: Optional[bool] = None
    email_on_extdown: Optional[bool] = None
    email_html_support: Optional[bool] = None
    email_on_extup: Optional[bool] = None
    email_on_created: Optional[bool] = None
    email_on_pmsupdate: Optional[bool] = None
    email_to: Optional[str] = None
    email_from: Optional[str] = None
    email_on_play: Optional[bool] = None


class OSXNotifyModel(BaseModel):
    osx_notify_on_intdown: Optional[bool] = None
    osx_notify_on_buffer: Optional[bool] = None
    osx_notify_app: Optional[str] = None
    osx_notify_on_created: Optional[bool] = None
    osx_notify_on_pmsupdate: Optional[bool] = None
    osx_notify_on_stop: Optional[bool] = None
    osx_notify_enabled: Optional[bool] = None
    osx_notify_on_intup: Optional[bool] = None
    osx_notify_on_watched: Optional[bool] = None
    osx_notify_on_pause: Optional[bool] = None
    osx_notify_on_concurrent: Optional[bool] = None
    osx_notify_on_newdevice: Optional[bool] = None
    osx_notify_on_play: Optional[bool] = None
    osx_notify_on_extdown: Optional[bool] = None
    osx_notify_on_extup: Optional[bool] = None
    osx_notify_on_resume: Optional[bool] = None


class PlexWatchModel(BaseModel):
    grouping_user_history: Optional[bool] = None
    plexwatch_database: Optional[str] = None
    grouping_global_history: Optional[bool] = None
    grouping_charts: Optional[bool] = None


class PushoverModel(BaseModel):
    pushover_enabled: Optional[bool] = None
    pushover_on_extup: Optional[bool] = None
    pushover_on_intup: Optional[bool] = None
    pushover_on_buffer: Optional[bool] = None
    pushover_html_support: Optional[bool] = None
    pushover_keys: Optional[str] = None
    pushover_incl_url: Optional[bool] = None
    pushover_on_pause: Optional[bool] = None
    pushover_on_play: Optional[bool] = None
    pushover_on_stop: Optional[bool] = None
    pushover_apitoken: Optional[str] = None
    pushover_incl_pmslink: Optional[bool] = None
    pushover_on_pmsupdate: Optional[bool] = None
    pushover_on_extdown: Optional[bool] = None
    pushover_priority: Optional[bool] = None
    pushover_on_intdown: Optional[bool] = None
    pushover_on_newdevice: Optional[bool] = None
    pushover_sound: Optional[str] = None
    pushover_on_created: Optional[bool] = None
    pushover_on_resume: Optional[bool] = None
    pushover_on_concurrent: Optional[bool] = None
    pushover_on_watched: Optional[bool] = None


class TelegramModel(BaseModel):
    telegram_on_buffer: Optional[bool] = None
    telegram_bot_token: Optional[str] = None
    telegram_incl_poster: Optional[bool] = None
    telegram_on_resume: Optional[bool] = None
    telegram_on_pmsupdate: Optional[bool] = None
    telegram_html_support: Optional[bool] = None
    telegram_on_created: Optional[bool] = None
    telegram_incl_subject: Optional[bool] = None
    telegram_disable_web_preview: Optional[bool] = None
    telegram_enabled: Optional[bool] = None
    telegram_on_concurrent: Optional[bool] = None
    telegram_on_intdown: Optional[bool] = None
    telegram_on_extdown: Optional[bool] = None
    telegram_on_pause: Optional[bool] = None
    telegram_on_newdevice: Optional[bool] = None
    telegram_on_watched: Optional[bool] = None
    telegram_on_stop: Optional[bool] = None
    telegram_on_play: Optional[bool] = None
    telegram_on_extup: Optional[bool] = None
    telegram_chat_id: Optional[str] = None
    telegram_on_intup: Optional[bool] = None


class TwitterModel(BaseModel):
    twitter_on_resume: Optional[bool] = None
    twitter_on_pmsupdate: Optional[bool] = None
    twitter_on_buffer: Optional[bool] = None
    twitter_on_concurrent: Optional[bool] = None
    twitter_enabled: Optional[bool] = None
    twitter_on_watched: Optional[bool] = None
    twitter_consumer_secret: Optional[str] = None
    twitter_on_extup: Optional[bool] = None
    twitter_on_intdown: Optional[bool] = None
    twitter_on_intup: Optional[bool] = None
    twitter_access_token_secret: Optional[str] = None
    twitter_on_newdevice: Optional[bool] = None
    twitter_on_stop: Optional[bool] = None
    twitter_consumer_key: Optional[str] = None
    twitter_access_token: Optional[str] = None
    twitter_incl_subject: Optional[bool] = None
    twitter_on_extdown: Optional[bool] = None
    twitter_on_pause: Optional[bool] = None
    twitter_on_play: Optional[bool] = None
    twitter_incl_poster: Optional[bool] = None
    twitter_on_created: Optional[bool] = None


class PlexModel(BaseModel):
    plex_on_created: Optional[bool] = None
    plex_on_concurrent: Optional[bool] = None
    plex_client_host: Optional[str] = None
    plex_on_stop: Optional[bool] = None
    plex_on_resume: Optional[bool] = None
    plex_on_watched: Optional[bool] = None
    plex_on_play: Optional[bool] = None
    plex_on_extdown: Optional[bool] = None
    plex_on_intdown: Optional[bool] = None
    plex_on_newdevice: Optional[bool] = None
    plex_enabled: Optional[bool] = None
    plex_on_buffer: Optional[bool] = None
    plex_on_intup: Optional[bool] = None
    plex_on_pmsupdate: Optional[bool] = None
    plex_username: Optional[str] = None
    plex_on_pause: Optional[bool] = None
    plex_password: Optional[str] = None
    plex_on_extup: Optional[bool] = None


class JoinModel(BaseModel):
    join_on_concurrent: Optional[bool] = None
    join_on_newdevice: Optional[bool] = None
    join_deviceid: Optional[str] = None
    join_on_play: Optional[bool] = None
    join_on_watched: Optional[bool] = None
    join_on_resume: Optional[bool] = None
    join_on_created: Optional[bool] = None
    join_on_extdown: Optional[bool] = None
    join_on_intup: Optional[bool] = None
    join_on_buffer: Optional[bool] = None
    join_incl_subject: Optional[bool] = None
    join_enabled: Optional[bool] = None
    join_on_pause: Optional[bool] = None
    join_apikey: Optional[str] = None
    join_on_pmsupdate: Optional[bool] = None
    join_on_intdown: Optional[bool] = None
    join_on_extup: Optional[bool] = None
    join_on_stop: Optional[bool] = None


class XBMCModel(BaseModel):
    xbmc_password: Optional[str] = None
    xbmc_on_play: Optional[bool] = None
    xbmc_on_pause: Optional[bool] = None
    xbmc_username: Optional[str] = None
    xbmc_on_extup: Optional[bool] = None
    xbmc_on_watched: Optional[bool] = None
    xbmc_on_buffer: Optional[bool] = None
    xbmc_enabled: Optional[bool] = None
    xbmc_host: Optional[str] = None
    xbmc_on_created: Optional[bool] = None
    xbmc_on_intup: Optional[bool] = None
    xbmc_on_extdown: Optional[bool] = None
    xbmc_on_pmsupdate: Optional[bool] = None
    xbmc_on_stop: Optional[bool] = None
    xbmc_on_newdevice: Optional[bool] = None
    xbmc_on_resume: Optional[bool] = None
    xbmc_on_intdown: Optional[bool] = None
    xbmc_on_concurrent: Optional[bool] = None


class BrowserModel(BaseModel):
    browser_on_intdown: Optional[bool] = None
    browser_on_newdevice: Optional[bool] = None
    browser_on_pmsupdate: Optional[bool] = None
    browser_on_intup: Optional[bool] = None
    browser_on_buffer: Optional[bool] = None
    browser_auto_hide_delay: Optional[int] = None
    browser_on_created: Optional[bool] = None
    browser_on_pause: Optional[bool] = None
    browser_on_stop: Optional[bool] = None
    browser_on_play: Optional[bool] = None
    browser_on_watched: Optional[bool] = None
    browser_on_extdown: Optional[bool] = None
    browser_on_extup: Optional[bool] = None
    browser_on_resume: Optional[bool] = None
    browser_on_concurrent: Optional[bool] = None
    browser_enabled: Optional[bool] = None


class NewsletterModel(BaseModel):
    newsletter_dir: Optional[str] = None
    newsletter_templates: Optional[str] = None
    newsletter_self_hosted: Optional[bool] = None
    newsletter_static_url: Optional[bool] = None
    newsletter_inline_styles: Optional[bool] = None
    newsletter_password: Optional[str] = None
    newsletter_custom_dir: Optional[str] = None
    newsletter_auth: Optional[bool] = None


class CloudinaryModel(BaseModel):
    cloudinary_api_key: Optional[str] = None
    cloudinary_cloud_name: Optional[str] = None
    cloudinary_api_secret: Optional[str] = None


class SettingsModel(BaseModel):
    IFTTT: Optional[IFTTTModel] = None
    Growl: Optional[GrowlModel] = None
    PMS: Optional[PMSModel] = None
    Monitoring: Optional[MonitoringModel] = None
    General: Optional[GeneralModel] = None
    Slack: Optional[SlackModel] = None
    Boxcar: Optional[BoxcarModel] = None
    PushBullet: Optional[PushBulletModel] = None
    Scripts: Optional[ScriptsModel] = None
    NMA: Optional[NMAModel] = None
    Hipchat: Optional[HipchatModel] = None
    Pushalot: Optional[PushalotModel] = None
    Prowl: Optional[ProwlModel] = None
    Advanced: Optional[AdvancedModel] = None
    Facebook: Optional[FacebookModel] = None
    Email: Optional[EmailModel] = None
    OSX_Notify: Optional[OSXNotifyModel] = None
    PlexWatch: Optional[PlexWatchModel] = None
    Pushover: Optional[PushoverModel] = None
    Telegram: Optional[TelegramModel] = None
    Twitter: Optional[TwitterModel] = None
    Plex: Optional[PlexModel] = None
    Join: Optional[JoinModel] = None
    XBMC: Optional[XBMCModel] = None
    Browser: Optional[BrowserModel] = None
    Newsletter: Optional[NewsletterModel] = None
    Cloudinary: Optional[CloudinaryModel] = None
