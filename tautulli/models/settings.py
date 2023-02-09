# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:23:37+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class IFTTT(BaseModel):
    ifttt_on_stop: Optional[bool]
    ifttt_on_pause: Optional[bool]
    ifttt_key: Optional[str]
    ifttt_on_concurrent: Optional[bool]
    ifttt_on_created: Optional[bool]
    ifttt_on_buffer: Optional[bool]
    ifttt_enabled: Optional[bool]
    ifttt_on_pmsupdate: Optional[bool]
    ifttt_on_newdevice: Optional[bool]
    ifttt_on_intdown: Optional[bool]
    ifttt_on_extup: Optional[bool]
    ifttt_on_intup: Optional[bool]
    ifttt_on_resume: Optional[bool]
    ifttt_on_watched: Optional[bool]
    ifttt_event: Optional[str]
    ifttt_on_extdown: Optional[bool]
    ifttt_on_play: Optional[bool]


class Growl(BaseModel):
    growl_enabled: Optional[bool]
    growl_on_play: Optional[bool]
    growl_on_stop: Optional[bool]
    growl_on_buffer: Optional[bool]
    growl_on_pause: Optional[bool]
    growl_on_intdown: Optional[bool]
    growl_host: Optional[str]
    growl_on_extup: Optional[bool]
    growl_on_newdevice: Optional[bool]
    growl_on_pmsupdate: Optional[bool]
    growl_password: Optional[str]
    growl_on_resume: Optional[bool]
    growl_on_created: Optional[bool]
    growl_on_concurrent: Optional[bool]
    growl_on_watched: Optional[bool]
    growl_on_intup: Optional[bool]
    growl_on_extdown: Optional[bool]


class PMS(BaseModel):
    pms_use_bif: Optional[bool]
    pms_uuid: Optional[str]
    pms_url: Optional[str]
    pms_update_channel: Optional[str]
    pms_update_distro: Optional[str]
    pms_name: Optional[str]
    pms_logs_folder: Optional[str]
    pms_plexpass: Optional[int]
    pms_token: Optional[str] = None
    pms_port: Optional[int]
    pms_is_remote: Optional[int]
    pms_identifier: Optional[str]
    pms_ssl: Optional[int]
    pms_version: Optional[str]
    pms_update_distro_build: Optional[str]
    pms_ip: Optional[str]
    pms_logs_line_cap: Optional[str]
    pms_platform: Optional[str]
    pms_url_manual: Optional[int]
    pms_web_url: Optional[str]
    pms_is_cloud: Optional[int]
    pms_url_override: Optional[str]


class Monitoring(BaseModel):
    notify_upload_posters: Optional[str]
    movie_notify_enable: Optional[bool]
    notify_on_resume_body_text: Optional[str]
    notify_on_pmsupdate_body_text: Optional[str]
    refresh_libraries_on_startup: Optional[bool]
    session_db_write_attempts: Optional[str]
    notify_on_created_body_text: Optional[str]
    buffer_wait: Optional[str]
    notify_on_intup_subject_text: Optional[str]
    notify_recently_added_grandparent: Optional[bool]
    notify_on_newdevice_subject_text: Optional[str]
    notify_on_extup_subject_text: Optional[str]
    notify_on_watched_subject_text: Optional[str]
    notify_on_pause_subject_text: Optional[str]
    notify_on_extup_body_text: Optional[str]
    notify_on_watched_body_text: Optional[str]
    music_notify_on_pause: Optional[bool]
    notify_on_start_body_text: Optional[str]
    notify_on_pause_body_text: Optional[str]
    notify_on_buffer_body_text: Optional[str]
    music_notify_on_stop: Optional[bool]
    tv_notify_on_stop: Optional[bool]
    notify_on_stop_body_text: Optional[str]
    notify_on_created_subject_text: Optional[str]
    notify_on_extdown_body_text: Optional[str]
    notify_scripts_args_text: Optional[str]
    music_logging_enable: Optional[bool]
    movie_notify_on_stop: Optional[bool]
    notify_watched_percent: Optional[str]
    notify_on_concurrent_subject_text: Optional[str]
    notify_on_concurrent_body_text: Optional[str]
    tv_logging_enable: Optional[bool]
    tv_notify_enable: Optional[bool]
    notify_recently_added_delay: Optional[str]
    notify_on_intdown_body_text: Optional[str]
    logging_ignore_interval: Optional[str]
    notify_on_newdevice_body_text: Optional[str]
    refresh_users_interval: Optional[str]
    monitoring_use_websocket: Optional[bool]
    monitor_pms_updates: Optional[bool]
    notify_on_start_subject_text: Optional[str]
    notify_recently_added: Optional[bool]
    notify_on_pmsupdate_subject_text: Optional[str]
    music_notify_enable: Optional[bool]
    movie_notify_on_start: Optional[bool]
    notify_concurrent_by_ip: Optional[bool]
    refresh_users_on_startup: Optional[bool]
    buffer_threshold: Optional[str]
    notify_on_extdown_subject_text: Optional[str]
    refresh_libraries_interval: Optional[str]
    tv_notify_on_start: Optional[bool]
    video_logging_enable: Optional[bool]
    notify_on_resume_subject_text: Optional[str]
    notify_concurrent_threshold: Optional[str]
    notify_on_stop_subject_text: Optional[str]
    movie_notify_on_pause: Optional[bool]
    notify_consecutive: Optional[bool]
    movie_logging_enable: Optional[bool]
    notify_on_intup_body_text: Optional[str]
    notify_on_intdown_subject_text: Optional[str]
    music_notify_on_start: Optional[bool]
    tv_notify_on_pause: Optional[bool]
    monitor_remote_access: Optional[bool]
    imgur_client_id: Optional[str]
    monitoring_interval: Optional[str]
    notify_on_buffer_subject_text: Optional[str]
    tv_watched_percent: Optional[str]
    notify_group_recently_added_grandparent: Optional[bool]
    notify_recently_added_upgrade: Optional[bool]
    notify_group_recently_added: Optional[bool]
    notify_group_recently_added_parent: Optional[bool]
    movie_watched_percent: Optional[str]
    music_watched_percent: Optional[str]
    notify_continued_session_threshold: Optional[str]
    notify_remote_access_threshold: Optional[str]
    notify_new_device_initial_only: Optional[bool]


class GetFileSizesHold(BaseModel):
    section_ids: Optional[List]
    rating_keys: Optional[List]


class General(BaseModel):
    week_start_monday: Optional[bool]
    git_token: Optional[str]
    home_stats_cards: Optional[List[str]]
    backup_interval: Optional[str]
    graph_days: Optional[str]
    graph_type: Optional[str]
    get_file_sizes: Optional[bool]
    http_basic_auth: Optional[bool]
    api_sql: Optional[bool]
    http_root: Optional[str]
    http_proxy: Optional[bool]
    freeze_db: Optional[bool]
    ip_logging_enable: Optional[bool]
    launch_browser: Optional[bool]
    http_username: Optional[str]
    https_create_cert: Optional[bool]
    do_not_override_git_branch: Optional[bool]
    home_stats_length: Optional[str]
    http_host: Optional[str]
    first_run_complete: Optional[bool]
    enable_https: Optional[bool]
    check_github: Optional[bool]
    api_enabled: Optional[bool]
    git_path: Optional[str]
    update_labels: Optional[bool]
    config_version: Optional[str]
    check_github_interval: Optional[str]
    https_ip: Optional[str]
    group_history_tables: Optional[bool]
    https_domain: Optional[str]
    graph_tab: Optional[str]
    geoip_db: Optional[str]
    http_password: Optional[str]
    home_stats_count: Optional[str]
    backup_dir: Optional[str]
    git_user: Optional[str]
    interface: Optional[str]
    cache_images: Optional[bool]
    log_blacklist: Optional[bool]
    graph_months: Optional[str]
    cleanup_files: Optional[bool]
    check_github_on_startup: Optional[bool]
    http_port: Optional[str]
    log_dir: Optional[str]
    update_db_interval: Optional[str]
    allow_guest_access: Optional[bool]
    time_format: Optional[str]
    cache_dir: Optional[str]
    home_sections: Optional[List[str]]
    backup_days: Optional[str]
    https_cert: Optional[str]
    api_key: Optional[str]
    update_section_ids: Optional[bool]
    date_format: Optional[str]
    home_stats_type: Optional[bool]
    http_environment: Optional[str]
    history_table_activity: Optional[bool]
    https_key: Optional[str]
    http_hash_password: Optional[bool]
    home_library_cards: Optional[List[str]]
    http_hashed_password: Optional[bool]
    git_branch: Optional[str]
    anon_redirect: Optional[str]
    http_plex_admin: Optional[bool]
    update_show_changelog: Optional[int]
    show_advanced_settings: Optional[bool]
    git_remote: Optional[str]
    https_cert_chain: Optional[str]
    git_repo: Optional[str]
    home_stats_recently_added_count: Optional[str]
    themoviedb_apikey: Optional[str]
    tvmaze_lookup: Optional[bool]
    update_notifiers_db: Optional[bool]
    themoviedb_lookup: Optional[bool]
    plexpy_auto_update: Optional[bool]
    update_libraries_db_notify: Optional[bool]
    home_refresh_interval: Optional[str]
    http_base_url: Optional[str]
    win_sys_tray: Optional[bool]
    musicbrainz_lookup: Optional[bool]
    geoip_db_update_days: Optional[str]
    maxmind_license_key: Optional[str]
    geoip_db_installed: Optional[bool]
    launch_startup: Optional[bool]
    sys_tray_icon: Optional[bool]
    export_dir: Optional[str]
    http_rate_limit_attempts: Optional[str]
    http_rate_limit_attempts_interval: Optional[str]
    http_rate_limit_lockout_time: Optional[str]
    get_file_sizes_hold: Optional[GetFileSizesHold]
    interface_list: Optional[List[str]]


class Slack(BaseModel):
    slack_on_stop: Optional[bool]
    slack_icon_emoji: Optional[str]
    slack_on_watched: Optional[bool]
    slack_on_extup: Optional[bool]
    slack_on_resume: Optional[bool]
    slack_hook: Optional[str]
    slack_incl_subject: Optional[bool]
    slack_on_pmsupdate: Optional[bool]
    slack_channel: Optional[str]
    slack_on_buffer: Optional[bool]
    slack_on_extdown: Optional[bool]
    slack_username: Optional[str]
    slack_incl_pmslink: Optional[bool]
    slack_enabled: Optional[bool]
    slack_incl_poster: Optional[bool]
    slack_on_pause: Optional[bool]
    slack_on_concurrent: Optional[bool]
    slack_on_intup: Optional[bool]
    slack_on_intdown: Optional[bool]
    slack_on_play: Optional[bool]
    slack_on_created: Optional[bool]
    slack_on_newdevice: Optional[bool]


class Boxcar(BaseModel):
    boxcar_sound: Optional[str]
    boxcar_on_newdevice: Optional[bool]
    boxcar_on_watched: Optional[bool]
    boxcar_on_buffer: Optional[bool]
    boxcar_on_stop: Optional[bool]
    boxcar_on_extdown: Optional[bool]
    boxcar_on_pmsupdate: Optional[bool]
    boxcar_on_intdown: Optional[bool]
    boxcar_on_pause: Optional[bool]
    boxcar_on_play: Optional[bool]
    boxcar_on_created: Optional[bool]
    boxcar_on_intup: Optional[bool]
    boxcar_on_resume: Optional[bool]
    boxcar_on_concurrent: Optional[bool]
    boxcar_enabled: Optional[bool]
    boxcar_on_extup: Optional[bool]
    boxcar_token: Optional[str]


class PushBullet(BaseModel):
    pushbullet_on_play: Optional[bool]
    pushbullet_channel_tag: Optional[str]
    pushbullet_on_buffer: Optional[bool]
    pushbullet_apikey: Optional[str]
    pushbullet_on_resume: Optional[bool]
    pushbullet_on_concurrent: Optional[bool]
    pushbullet_on_created: Optional[bool]
    pushbullet_on_pause: Optional[bool]
    pushbullet_on_extdown: Optional[bool]
    pushbullet_on_stop: Optional[bool]
    pushbullet_on_extup: Optional[bool]
    pushbullet_on_pmsupdate: Optional[bool]
    pushbullet_enabled: Optional[bool]
    pushbullet_on_watched: Optional[bool]
    pushbullet_on_intdown: Optional[bool]
    pushbullet_deviceid: Optional[str]
    pushbullet_on_intup: Optional[bool]
    pushbullet_on_newdevice: Optional[bool]


class Scripts(BaseModel):
    scripts_on_newdevice: Optional[bool]
    scripts_on_stop: Optional[bool]
    scripts_on_intdown_script: Optional[str]
    scripts_on_newdevice_script: Optional[str]
    scripts_folder: Optional[str]
    scripts_on_pmsupdate: Optional[bool]
    scripts_on_buffer: Optional[bool]
    scripts_on_concurrent: Optional[bool]
    scripts_on_intup_script: Optional[str]
    scripts_on_intdown: Optional[bool]
    scripts_on_resume: Optional[bool]
    scripts_on_extdown_script: Optional[str]
    scripts_on_extup: Optional[bool]
    scripts_on_play_script: Optional[str]
    scripts_on_created_script: Optional[str]
    scripts_on_pmsupdate_script: Optional[str]
    scripts_on_resume_script: Optional[str]
    scripts_on_stop_script: Optional[str]
    scripts_on_watched_script: Optional[str]
    scripts_enabled: Optional[bool]
    scripts_on_extup_script: Optional[str]
    scripts_on_extdown: Optional[bool]
    scripts_on_created: Optional[bool]
    scripts_on_concurrent_script: Optional[str]
    scripts_on_pause_script: Optional[str]
    scripts_on_pause: Optional[bool]
    scripts_on_intup: Optional[bool]
    scripts_timeout: Optional[str]
    scripts_on_watched: Optional[bool]
    scripts_on_buffer_script: Optional[str]
    scripts_on_play: Optional[bool]


class NMA(BaseModel):
    nma_on_pmsupdate: Optional[bool]
    nma_priority: Optional[bool]
    nma_on_intdown: Optional[bool]
    nma_on_buffer: Optional[bool]
    nma_on_play: Optional[bool]
    nma_on_newdevice: Optional[bool]
    nma_on_resume: Optional[bool]
    nma_on_concurrent: Optional[bool]
    nma_on_watched: Optional[bool]
    nma_apikey: Optional[str]
    nma_on_intup: Optional[bool]
    nma_on_stop: Optional[bool]
    nma_on_created: Optional[bool]
    nma_on_pause: Optional[bool]
    nma_enabled: Optional[bool]
    nma_on_extdown: Optional[bool]
    nma_on_extup: Optional[bool]


class Hipchat(BaseModel):
    hipchat_emoticon: Optional[str]
    hipchat_incl_subject: Optional[bool]
    hipchat_on_extdown: Optional[bool]
    hipchat_on_intup: Optional[bool]
    hipchat_enabled: Optional[bool]
    hipchat_on_created: Optional[bool]
    hipchat_on_newdevice: Optional[bool]
    hipchat_on_play: Optional[bool]
    hipchat_on_resume: Optional[bool]
    hipchat_on_buffer: Optional[bool]
    hipchat_incl_poster: Optional[bool]
    hipchat_on_watched: Optional[bool]
    hipchat_color: Optional[str]
    hipchat_on_concurrent: Optional[bool]
    hipchat_url: Optional[str]
    hipchat_on_pmsupdate: Optional[bool]
    hipchat_on_extup: Optional[bool]
    hipchat_incl_pmslink: Optional[bool]
    hipchat_on_pause: Optional[bool]
    hipchat_on_intdown: Optional[bool]
    hipchat_on_stop: Optional[bool]


class Pushalot(BaseModel):
    pushalot_apikey: Optional[str]
    pushalot_on_pmsupdate: Optional[bool]
    pushalot_enabled: Optional[bool]
    pushalot_on_extdown: Optional[bool]
    pushalot_on_created: Optional[bool]
    pushalot_on_pause: Optional[bool]
    pushalot_on_stop: Optional[bool]
    pushalot_on_buffer: Optional[bool]
    pushalot_on_intup: Optional[bool]
    pushalot_on_newdevice: Optional[bool]
    pushalot_on_concurrent: Optional[bool]
    pushalot_on_watched: Optional[bool]
    pushalot_on_play: Optional[bool]
    pushalot_on_extup: Optional[bool]
    pushalot_on_intdown: Optional[bool]
    pushalot_on_resume: Optional[bool]


class Prowl(BaseModel):
    prowl_on_created: Optional[bool]
    prowl_on_play: Optional[bool]
    prowl_on_extdown: Optional[bool]
    prowl_on_pause: Optional[bool]
    prowl_on_intdown: Optional[bool]
    prowl_on_intup: Optional[bool]
    prowl_enabled: Optional[bool]
    prowl_priority: Optional[bool]
    prowl_on_pmsupdate: Optional[bool]
    prowl_on_newdevice: Optional[bool]
    prowl_on_extup: Optional[bool]
    prowl_on_watched: Optional[bool]
    prowl_on_buffer: Optional[bool]
    prowl_on_resume: Optional[bool]
    prowl_on_stop: Optional[bool]
    prowl_on_concurrent: Optional[bool]
    prowl_keys: Optional[str]


class Advanced(BaseModel):
    verify_ssl_cert: Optional[bool]
    journal_mode: Optional[str]
    pms_timeout: Optional[str]
    cache_sizemb: Optional[str]
    session_db_write_attempts: Optional[str]
    system_analytics: Optional[bool]
    notification_threads: Optional[str]
    remote_access_ping_threshold: Optional[str]
    websocket_connection_timeout: Optional[str]
    config_version: Optional[str]
    metadata_cache_seconds: Optional[str]
    websocket_connection_attempts: Optional[str]
    jwt_secret: Optional[str]
    websocket_monitor_ping_pong: Optional[bool]
    synchronous_mode: Optional[str]
    pms_update_check_interval: Optional[str]
    jwt_update_secret: Optional[bool]
    verbose_logs: Optional[bool]
    add_live_tv_library: Optional[bool]
    remote_access_ping_interval: Optional[str]
    check_github_cache_seconds: Optional[str]
    export_threads: Optional[str]


class Facebook(BaseModel):
    facebook_app_secret: Optional[str]
    facebook_on_stop: Optional[bool]
    facebook_token: Optional[str]
    facebook_on_buffer: Optional[bool]
    facebook_on_play: Optional[bool]
    facebook_enabled: Optional[bool]
    facebook_on_intup: Optional[bool]
    facebook_incl_poster: Optional[bool]
    facebook_on_pmsupdate: Optional[bool]
    facebook_on_intdown: Optional[bool]
    facebook_on_extup: Optional[bool]
    facebook_on_resume: Optional[bool]
    facebook_on_concurrent: Optional[bool]
    facebook_on_extdown: Optional[bool]
    facebook_group: Optional[str]
    facebook_on_pause: Optional[bool]
    facebook_app_id: Optional[str]
    facebook_incl_pmslink: Optional[bool]
    facebook_on_newdevice: Optional[bool]
    facebook_on_watched: Optional[bool]
    facebook_redirect_uri: Optional[str]
    facebook_incl_subject: Optional[bool]
    facebook_on_created: Optional[bool]


class Email(BaseModel):
    email_from_name: Optional[str]
    email_bcc: Optional[str]
    email_on_pause: Optional[bool]
    email_smtp_password: Optional[str]
    email_tls: Optional[bool]
    email_smtp_port: Optional[str]
    email_on_watched: Optional[bool]
    email_smtp_server: Optional[str]
    email_on_intdown: Optional[bool]
    email_on_concurrent: Optional[bool]
    email_on_intup: Optional[bool]
    email_enabled: Optional[bool]
    email_on_buffer: Optional[bool]
    email_on_resume: Optional[bool]
    email_smtp_user: Optional[str]
    email_cc: Optional[str]
    email_on_newdevice: Optional[bool]
    email_on_stop: Optional[bool]
    email_on_extdown: Optional[bool]
    email_html_support: Optional[bool]
    email_on_extup: Optional[bool]
    email_on_created: Optional[bool]
    email_on_pmsupdate: Optional[bool]
    email_to: Optional[str]
    email_from: Optional[str]
    email_on_play: Optional[bool]


class OSXNotify(BaseModel):
    osx_notify_on_intdown: Optional[bool]
    osx_notify_on_buffer: Optional[bool]
    osx_notify_app: Optional[str]
    osx_notify_on_created: Optional[bool]
    osx_notify_on_pmsupdate: Optional[bool]
    osx_notify_on_stop: Optional[bool]
    osx_notify_enabled: Optional[bool]
    osx_notify_on_intup: Optional[bool]
    osx_notify_on_watched: Optional[bool]
    osx_notify_on_pause: Optional[bool]
    osx_notify_on_concurrent: Optional[bool]
    osx_notify_on_newdevice: Optional[bool]
    osx_notify_on_play: Optional[bool]
    osx_notify_on_extdown: Optional[bool]
    osx_notify_on_extup: Optional[bool]
    osx_notify_on_resume: Optional[bool]


class PlexWatch(BaseModel):
    grouping_user_history: Optional[bool]
    plexwatch_database: Optional[str]
    grouping_global_history: Optional[bool]
    grouping_charts: Optional[bool]


class Pushover(BaseModel):
    pushover_enabled: Optional[bool]
    pushover_on_extup: Optional[bool]
    pushover_on_intup: Optional[bool]
    pushover_on_buffer: Optional[bool]
    pushover_html_support: Optional[bool]
    pushover_keys: Optional[str]
    pushover_incl_url: Optional[bool]
    pushover_on_pause: Optional[bool]
    pushover_on_play: Optional[bool]
    pushover_on_stop: Optional[bool]
    pushover_apitoken: Optional[str]
    pushover_incl_pmslink: Optional[bool]
    pushover_on_pmsupdate: Optional[bool]
    pushover_on_extdown: Optional[bool]
    pushover_priority: Optional[bool]
    pushover_on_intdown: Optional[bool]
    pushover_on_newdevice: Optional[bool]
    pushover_sound: Optional[str]
    pushover_on_created: Optional[bool]
    pushover_on_resume: Optional[bool]
    pushover_on_concurrent: Optional[bool]
    pushover_on_watched: Optional[bool]


class Telegram(BaseModel):
    telegram_on_buffer: Optional[bool]
    telegram_bot_token: Optional[str]
    telegram_incl_poster: Optional[bool]
    telegram_on_resume: Optional[bool]
    telegram_on_pmsupdate: Optional[bool]
    telegram_html_support: Optional[bool]
    telegram_on_created: Optional[bool]
    telegram_incl_subject: Optional[bool]
    telegram_disable_web_preview: Optional[bool]
    telegram_enabled: Optional[bool]
    telegram_on_concurrent: Optional[bool]
    telegram_on_intdown: Optional[bool]
    telegram_on_extdown: Optional[bool]
    telegram_on_pause: Optional[bool]
    telegram_on_newdevice: Optional[bool]
    telegram_on_watched: Optional[bool]
    telegram_on_stop: Optional[bool]
    telegram_on_play: Optional[bool]
    telegram_on_extup: Optional[bool]
    telegram_chat_id: Optional[str]
    telegram_on_intup: Optional[bool]


class Twitter(BaseModel):
    twitter_on_resume: Optional[bool]
    twitter_on_pmsupdate: Optional[bool]
    twitter_on_buffer: Optional[bool]
    twitter_on_concurrent: Optional[bool]
    twitter_enabled: Optional[bool]
    twitter_on_watched: Optional[bool]
    twitter_consumer_secret: Optional[str]
    twitter_on_extup: Optional[bool]
    twitter_on_intdown: Optional[bool]
    twitter_on_intup: Optional[bool]
    twitter_access_token_secret: Optional[str]
    twitter_on_newdevice: Optional[bool]
    twitter_on_stop: Optional[bool]
    twitter_consumer_key: Optional[str]
    twitter_access_token: Optional[str]
    twitter_incl_subject: Optional[bool]
    twitter_on_extdown: Optional[bool]
    twitter_on_pause: Optional[bool]
    twitter_on_play: Optional[bool]
    twitter_incl_poster: Optional[bool]
    twitter_on_created: Optional[bool]


class Plex(BaseModel):
    plex_on_created: Optional[bool]
    plex_on_concurrent: Optional[bool]
    plex_client_host: Optional[str]
    plex_on_stop: Optional[bool]
    plex_on_resume: Optional[bool]
    plex_on_watched: Optional[bool]
    plex_on_play: Optional[bool]
    plex_on_extdown: Optional[bool]
    plex_on_intdown: Optional[bool]
    plex_on_newdevice: Optional[bool]
    plex_enabled: Optional[bool]
    plex_on_buffer: Optional[bool]
    plex_on_intup: Optional[bool]
    plex_on_pmsupdate: Optional[bool]
    plex_username: Optional[str]
    plex_on_pause: Optional[bool]
    plex_password: Optional[str]
    plex_on_extup: Optional[bool]


class Join(BaseModel):
    join_on_concurrent: Optional[bool]
    join_on_newdevice: Optional[bool]
    join_deviceid: Optional[str]
    join_on_play: Optional[bool]
    join_on_watched: Optional[bool]
    join_on_resume: Optional[bool]
    join_on_created: Optional[bool]
    join_on_extdown: Optional[bool]
    join_on_intup: Optional[bool]
    join_on_buffer: Optional[bool]
    join_incl_subject: Optional[bool]
    join_enabled: Optional[bool]
    join_on_pause: Optional[bool]
    join_apikey: Optional[str]
    join_on_pmsupdate: Optional[bool]
    join_on_intdown: Optional[bool]
    join_on_extup: Optional[bool]
    join_on_stop: Optional[bool]


class XBMC(BaseModel):
    xbmc_password: Optional[str]
    xbmc_on_play: Optional[bool]
    xbmc_on_pause: Optional[bool]
    xbmc_username: Optional[str]
    xbmc_on_extup: Optional[bool]
    xbmc_on_watched: Optional[bool]
    xbmc_on_buffer: Optional[bool]
    xbmc_enabled: Optional[bool]
    xbmc_host: Optional[str]
    xbmc_on_created: Optional[bool]
    xbmc_on_intup: Optional[bool]
    xbmc_on_extdown: Optional[bool]
    xbmc_on_pmsupdate: Optional[bool]
    xbmc_on_stop: Optional[bool]
    xbmc_on_newdevice: Optional[bool]
    xbmc_on_resume: Optional[bool]
    xbmc_on_intdown: Optional[bool]
    xbmc_on_concurrent: Optional[bool]


class Browser(BaseModel):
    browser_on_intdown: Optional[bool]
    browser_on_newdevice: Optional[bool]
    browser_on_pmsupdate: Optional[bool]
    browser_on_intup: Optional[bool]
    browser_on_buffer: Optional[bool]
    browser_auto_hide_delay: Optional[str]
    browser_on_created: Optional[bool]
    browser_on_pause: Optional[bool]
    browser_on_stop: Optional[bool]
    browser_on_play: Optional[bool]
    browser_on_watched: Optional[bool]
    browser_on_extdown: Optional[bool]
    browser_on_extup: Optional[bool]
    browser_on_resume: Optional[bool]
    browser_on_concurrent: Optional[bool]
    browser_enabled: Optional[bool]


class Newsletter(BaseModel):
    newsletter_dir: Optional[str]
    newsletter_templates: Optional[str]
    newsletter_self_hosted: Optional[bool]
    newsletter_static_url: Optional[bool]
    newsletter_inline_styles: Optional[bool]
    newsletter_password: Optional[str]
    newsletter_custom_dir: Optional[str]
    newsletter_auth: Optional[bool]


class Cloudinary(BaseModel):
    cloudinary_api_key: Optional[str]
    cloudinary_cloud_name: Optional[str]
    cloudinary_api_secret: Optional[str]


class Settings(BaseModel):
    IFTTT: Optional[IFTTT]
    Growl: Optional[Growl]
    PMS: Optional[PMS]
    Monitoring: Optional[Monitoring]
    General: Optional[General]
    Slack: Optional[Slack]
    Boxcar: Optional[Boxcar]
    PushBullet: Optional[PushBullet]
    Scripts: Optional[Scripts]
    NMA: Optional[NMA]
    Hipchat: Optional[Hipchat]
    Pushalot: Optional[Pushalot]
    Prowl: Optional[Prowl]
    Advanced: Optional[Advanced]
    Facebook: Optional[Facebook]
    Email: Optional[Email]
    OSX_Notify: Optional[OSXNotify]
    PlexWatch: Optional[PlexWatch]
    Pushover: Optional[Pushover]
    Telegram: Optional[Telegram]
    Twitter: Optional[Twitter]
    Plex: Optional[Plex]
    Join: Optional[Join]
    XBMC: Optional[XBMC]
    Browser: Optional[Browser]
    Newsletter: Optional[Newsletter]
    Cloudinary: Optional[Cloudinary]


class Response(BaseModel):
    result: Optional[str]
    message: Any
    data: Settings


class Model(BaseModel):
    response: Response
