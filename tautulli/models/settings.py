# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:23:37+00:00

from __future__ import annotations

from typing import Any, List

from pydantic import BaseModel


class IFTTT(BaseModel):
    ifttt_on_stop: bool
    ifttt_on_pause: bool
    ifttt_key: str
    ifttt_on_concurrent: bool
    ifttt_on_created: bool
    ifttt_on_buffer: bool
    ifttt_enabled: bool
    ifttt_on_pmsupdate: bool
    ifttt_on_newdevice: bool
    ifttt_on_intdown: bool
    ifttt_on_extup: bool
    ifttt_on_intup: bool
    ifttt_on_resume: bool
    ifttt_on_watched: bool
    ifttt_event: str
    ifttt_on_extdown: bool
    ifttt_on_play: bool


class Growl(BaseModel):
    growl_enabled: bool
    growl_on_play: bool
    growl_on_stop: bool
    growl_on_buffer: bool
    growl_on_pause: bool
    growl_on_intdown: bool
    growl_host: str
    growl_on_extup: bool
    growl_on_newdevice: bool
    growl_on_pmsupdate: bool
    growl_password: str
    growl_on_resume: bool
    growl_on_created: bool
    growl_on_concurrent: bool
    growl_on_watched: bool
    growl_on_intup: bool
    growl_on_extdown: bool


class PMS(BaseModel):
    pms_use_bif: bool
    pms_uuid: str
    pms_url: str
    pms_update_channel: str
    pms_update_distro: str
    pms_name: str
    pms_logs_folder: str
    pms_plexpass: int
    pms_token: str
    pms_port: int
    pms_is_remote: int
    pms_identifier: str
    pms_ssl: int
    pms_version: str
    pms_update_distro_build: str
    pms_ip: str
    pms_logs_line_cap: str
    pms_platform: str
    pms_url_manual: int
    pms_web_url: str
    pms_is_cloud: int
    pms_url_override: str


class Monitoring(BaseModel):
    notify_upload_posters: str
    movie_notify_enable: bool
    notify_on_resume_body_text: str
    notify_on_pmsupdate_body_text: str
    refresh_libraries_on_startup: bool
    session_db_write_attempts: str
    notify_on_created_body_text: str
    buffer_wait: str
    notify_on_intup_subject_text: str
    notify_recently_added_grandparent: bool
    notify_on_newdevice_subject_text: str
    notify_on_extup_subject_text: str
    notify_on_watched_subject_text: str
    notify_on_pause_subject_text: str
    notify_on_extup_body_text: str
    notify_on_watched_body_text: str
    music_notify_on_pause: bool
    notify_on_start_body_text: str
    notify_on_pause_body_text: str
    notify_on_buffer_body_text: str
    music_notify_on_stop: bool
    tv_notify_on_stop: bool
    notify_on_stop_body_text: str
    notify_on_created_subject_text: str
    notify_on_extdown_body_text: str
    notify_scripts_args_text: str
    music_logging_enable: bool
    movie_notify_on_stop: bool
    notify_watched_percent: str
    notify_on_concurrent_subject_text: str
    notify_on_concurrent_body_text: str
    tv_logging_enable: bool
    tv_notify_enable: bool
    notify_recently_added_delay: str
    notify_on_intdown_body_text: str
    logging_ignore_interval: str
    notify_on_newdevice_body_text: str
    refresh_users_interval: str
    monitoring_use_websocket: bool
    monitor_pms_updates: bool
    notify_on_start_subject_text: str
    notify_recently_added: bool
    notify_on_pmsupdate_subject_text: str
    music_notify_enable: bool
    movie_notify_on_start: bool
    notify_concurrent_by_ip: bool
    refresh_users_on_startup: bool
    buffer_threshold: str
    notify_on_extdown_subject_text: str
    refresh_libraries_interval: str
    tv_notify_on_start: bool
    video_logging_enable: bool
    notify_on_resume_subject_text: str
    notify_concurrent_threshold: str
    notify_on_stop_subject_text: str
    movie_notify_on_pause: bool
    notify_consecutive: bool
    movie_logging_enable: bool
    notify_on_intup_body_text: str
    notify_on_intdown_subject_text: str
    music_notify_on_start: bool
    tv_notify_on_pause: bool
    monitor_remote_access: bool
    imgur_client_id: str
    monitoring_interval: str
    notify_on_buffer_subject_text: str
    tv_watched_percent: str
    notify_group_recently_added_grandparent: bool
    notify_recently_added_upgrade: bool
    notify_group_recently_added: bool
    notify_group_recently_added_parent: bool
    movie_watched_percent: str
    music_watched_percent: str
    notify_continued_session_threshold: str
    notify_remote_access_threshold: str
    notify_new_device_initial_only: bool


class GetFileSizesHold(BaseModel):
    section_ids: List
    rating_keys: List


class General(BaseModel):
    week_start_monday: bool
    git_token: str
    home_stats_cards: List[str]
    backup_interval: str
    graph_days: str
    graph_type: str
    get_file_sizes: bool
    http_basic_auth: bool
    api_sql: bool
    http_root: str
    http_proxy: bool
    freeze_db: bool
    ip_logging_enable: bool
    launch_browser: bool
    http_username: str
    https_create_cert: bool
    do_not_override_git_branch: bool
    home_stats_length: str
    http_host: str
    first_run_complete: bool
    enable_https: bool
    check_github: bool
    api_enabled: bool
    git_path: str
    update_labels: bool
    config_version: str
    check_github_interval: str
    https_ip: str
    group_history_tables: bool
    https_domain: str
    graph_tab: str
    geoip_db: str
    http_password: str
    home_stats_count: str
    backup_dir: str
    git_user: str
    interface: str
    cache_images: bool
    log_blacklist: bool
    graph_months: str
    cleanup_files: bool
    check_github_on_startup: bool
    http_port: str
    log_dir: str
    update_db_interval: str
    allow_guest_access: bool
    time_format: str
    cache_dir: str
    home_sections: List[str]
    backup_days: str
    https_cert: str
    api_key: str
    update_section_ids: bool
    date_format: str
    home_stats_type: bool
    http_environment: str
    history_table_activity: bool
    https_key: str
    http_hash_password: bool
    home_library_cards: List[str]
    http_hashed_password: bool
    git_branch: str
    anon_redirect: str
    http_plex_admin: bool
    update_show_changelog: int
    show_advanced_settings: bool
    git_remote: str
    https_cert_chain: str
    git_repo: str
    home_stats_recently_added_count: str
    themoviedb_apikey: str
    tvmaze_lookup: bool
    update_notifiers_db: bool
    themoviedb_lookup: bool
    plexpy_auto_update: bool
    update_libraries_db_notify: bool
    home_refresh_interval: str
    http_base_url: str
    win_sys_tray: bool
    musicbrainz_lookup: bool
    geoip_db_update_days: str
    maxmind_license_key: str
    geoip_db_installed: bool
    launch_startup: bool
    sys_tray_icon: bool
    export_dir: str
    http_rate_limit_attempts: str
    http_rate_limit_attempts_interval: str
    http_rate_limit_lockout_time: str
    get_file_sizes_hold: GetFileSizesHold
    interface_list: List[str]


class Slack(BaseModel):
    slack_on_stop: bool
    slack_icon_emoji: str
    slack_on_watched: bool
    slack_on_extup: bool
    slack_on_resume: bool
    slack_hook: str
    slack_incl_subject: bool
    slack_on_pmsupdate: bool
    slack_channel: str
    slack_on_buffer: bool
    slack_on_extdown: bool
    slack_username: str
    slack_incl_pmslink: bool
    slack_enabled: bool
    slack_incl_poster: bool
    slack_on_pause: bool
    slack_on_concurrent: bool
    slack_on_intup: bool
    slack_on_intdown: bool
    slack_on_play: bool
    slack_on_created: bool
    slack_on_newdevice: bool


class Boxcar(BaseModel):
    boxcar_sound: str
    boxcar_on_newdevice: bool
    boxcar_on_watched: bool
    boxcar_on_buffer: bool
    boxcar_on_stop: bool
    boxcar_on_extdown: bool
    boxcar_on_pmsupdate: bool
    boxcar_on_intdown: bool
    boxcar_on_pause: bool
    boxcar_on_play: bool
    boxcar_on_created: bool
    boxcar_on_intup: bool
    boxcar_on_resume: bool
    boxcar_on_concurrent: bool
    boxcar_enabled: bool
    boxcar_on_extup: bool
    boxcar_token: str


class PushBullet(BaseModel):
    pushbullet_on_play: bool
    pushbullet_channel_tag: str
    pushbullet_on_buffer: bool
    pushbullet_apikey: str
    pushbullet_on_resume: bool
    pushbullet_on_concurrent: bool
    pushbullet_on_created: bool
    pushbullet_on_pause: bool
    pushbullet_on_extdown: bool
    pushbullet_on_stop: bool
    pushbullet_on_extup: bool
    pushbullet_on_pmsupdate: bool
    pushbullet_enabled: bool
    pushbullet_on_watched: bool
    pushbullet_on_intdown: bool
    pushbullet_deviceid: str
    pushbullet_on_intup: bool
    pushbullet_on_newdevice: bool


class Scripts(BaseModel):
    scripts_on_newdevice: bool
    scripts_on_stop: bool
    scripts_on_intdown_script: str
    scripts_on_newdevice_script: str
    scripts_folder: str
    scripts_on_pmsupdate: bool
    scripts_on_buffer: bool
    scripts_on_concurrent: bool
    scripts_on_intup_script: str
    scripts_on_intdown: bool
    scripts_on_resume: bool
    scripts_on_extdown_script: str
    scripts_on_extup: bool
    scripts_on_play_script: str
    scripts_on_created_script: str
    scripts_on_pmsupdate_script: str
    scripts_on_resume_script: str
    scripts_on_stop_script: str
    scripts_on_watched_script: str
    scripts_enabled: bool
    scripts_on_extup_script: str
    scripts_on_extdown: bool
    scripts_on_created: bool
    scripts_on_concurrent_script: str
    scripts_on_pause_script: str
    scripts_on_pause: bool
    scripts_on_intup: bool
    scripts_timeout: str
    scripts_on_watched: bool
    scripts_on_buffer_script: str
    scripts_on_play: bool


class NMA(BaseModel):
    nma_on_pmsupdate: bool
    nma_priority: bool
    nma_on_intdown: bool
    nma_on_buffer: bool
    nma_on_play: bool
    nma_on_newdevice: bool
    nma_on_resume: bool
    nma_on_concurrent: bool
    nma_on_watched: bool
    nma_apikey: str
    nma_on_intup: bool
    nma_on_stop: bool
    nma_on_created: bool
    nma_on_pause: bool
    nma_enabled: bool
    nma_on_extdown: bool
    nma_on_extup: bool


class Hipchat(BaseModel):
    hipchat_emoticon: str
    hipchat_incl_subject: bool
    hipchat_on_extdown: bool
    hipchat_on_intup: bool
    hipchat_enabled: bool
    hipchat_on_created: bool
    hipchat_on_newdevice: bool
    hipchat_on_play: bool
    hipchat_on_resume: bool
    hipchat_on_buffer: bool
    hipchat_incl_poster: bool
    hipchat_on_watched: bool
    hipchat_color: str
    hipchat_on_concurrent: bool
    hipchat_url: str
    hipchat_on_pmsupdate: bool
    hipchat_on_extup: bool
    hipchat_incl_pmslink: bool
    hipchat_on_pause: bool
    hipchat_on_intdown: bool
    hipchat_on_stop: bool


class Pushalot(BaseModel):
    pushalot_apikey: str
    pushalot_on_pmsupdate: bool
    pushalot_enabled: bool
    pushalot_on_extdown: bool
    pushalot_on_created: bool
    pushalot_on_pause: bool
    pushalot_on_stop: bool
    pushalot_on_buffer: bool
    pushalot_on_intup: bool
    pushalot_on_newdevice: bool
    pushalot_on_concurrent: bool
    pushalot_on_watched: bool
    pushalot_on_play: bool
    pushalot_on_extup: bool
    pushalot_on_intdown: bool
    pushalot_on_resume: bool


class Prowl(BaseModel):
    prowl_on_created: bool
    prowl_on_play: bool
    prowl_on_extdown: bool
    prowl_on_pause: bool
    prowl_on_intdown: bool
    prowl_on_intup: bool
    prowl_enabled: bool
    prowl_priority: bool
    prowl_on_pmsupdate: bool
    prowl_on_newdevice: bool
    prowl_on_extup: bool
    prowl_on_watched: bool
    prowl_on_buffer: bool
    prowl_on_resume: bool
    prowl_on_stop: bool
    prowl_on_concurrent: bool
    prowl_keys: str


class Advanced(BaseModel):
    verify_ssl_cert: bool
    journal_mode: str
    pms_timeout: str
    cache_sizemb: str
    session_db_write_attempts: str
    system_analytics: bool
    notification_threads: str
    remote_access_ping_threshold: str
    websocket_connection_timeout: str
    config_version: str
    metadata_cache_seconds: str
    websocket_connection_attempts: str
    jwt_secret: str
    websocket_monitor_ping_pong: bool
    synchronous_mode: str
    pms_update_check_interval: str
    jwt_update_secret: bool
    verbose_logs: bool
    add_live_tv_library: bool
    remote_access_ping_interval: str
    check_github_cache_seconds: str
    export_threads: str


class Facebook(BaseModel):
    facebook_app_secret: str
    facebook_on_stop: bool
    facebook_token: str
    facebook_on_buffer: bool
    facebook_on_play: bool
    facebook_enabled: bool
    facebook_on_intup: bool
    facebook_incl_poster: bool
    facebook_on_pmsupdate: bool
    facebook_on_intdown: bool
    facebook_on_extup: bool
    facebook_on_resume: bool
    facebook_on_concurrent: bool
    facebook_on_extdown: bool
    facebook_group: str
    facebook_on_pause: bool
    facebook_app_id: str
    facebook_incl_pmslink: bool
    facebook_on_newdevice: bool
    facebook_on_watched: bool
    facebook_redirect_uri: str
    facebook_incl_subject: bool
    facebook_on_created: bool


class Email(BaseModel):
    email_from_name: str
    email_bcc: str
    email_on_pause: bool
    email_smtp_password: str
    email_tls: bool
    email_smtp_port: str
    email_on_watched: bool
    email_smtp_server: str
    email_on_intdown: bool
    email_on_concurrent: bool
    email_on_intup: bool
    email_enabled: bool
    email_on_buffer: bool
    email_on_resume: bool
    email_smtp_user: str
    email_cc: str
    email_on_newdevice: bool
    email_on_stop: bool
    email_on_extdown: bool
    email_html_support: bool
    email_on_extup: bool
    email_on_created: bool
    email_on_pmsupdate: bool
    email_to: str
    email_from: str
    email_on_play: bool


class OSXNotify(BaseModel):
    osx_notify_on_intdown: bool
    osx_notify_on_buffer: bool
    osx_notify_app: str
    osx_notify_on_created: bool
    osx_notify_on_pmsupdate: bool
    osx_notify_on_stop: bool
    osx_notify_enabled: bool
    osx_notify_on_intup: bool
    osx_notify_on_watched: bool
    osx_notify_on_pause: bool
    osx_notify_on_concurrent: bool
    osx_notify_on_newdevice: bool
    osx_notify_on_play: bool
    osx_notify_on_extdown: bool
    osx_notify_on_extup: bool
    osx_notify_on_resume: bool


class PlexWatch(BaseModel):
    grouping_user_history: bool
    plexwatch_database: str
    grouping_global_history: bool
    grouping_charts: bool


class Pushover(BaseModel):
    pushover_enabled: bool
    pushover_on_extup: bool
    pushover_on_intup: bool
    pushover_on_buffer: bool
    pushover_html_support: bool
    pushover_keys: str
    pushover_incl_url: bool
    pushover_on_pause: bool
    pushover_on_play: bool
    pushover_on_stop: bool
    pushover_apitoken: str
    pushover_incl_pmslink: bool
    pushover_on_pmsupdate: bool
    pushover_on_extdown: bool
    pushover_priority: bool
    pushover_on_intdown: bool
    pushover_on_newdevice: bool
    pushover_sound: str
    pushover_on_created: bool
    pushover_on_resume: bool
    pushover_on_concurrent: bool
    pushover_on_watched: bool


class Telegram(BaseModel):
    telegram_on_buffer: bool
    telegram_bot_token: str
    telegram_incl_poster: bool
    telegram_on_resume: bool
    telegram_on_pmsupdate: bool
    telegram_html_support: bool
    telegram_on_created: bool
    telegram_incl_subject: bool
    telegram_disable_web_preview: bool
    telegram_enabled: bool
    telegram_on_concurrent: bool
    telegram_on_intdown: bool
    telegram_on_extdown: bool
    telegram_on_pause: bool
    telegram_on_newdevice: bool
    telegram_on_watched: bool
    telegram_on_stop: bool
    telegram_on_play: bool
    telegram_on_extup: bool
    telegram_chat_id: str
    telegram_on_intup: bool


class Twitter(BaseModel):
    twitter_on_resume: bool
    twitter_on_pmsupdate: bool
    twitter_on_buffer: bool
    twitter_on_concurrent: bool
    twitter_enabled: bool
    twitter_on_watched: bool
    twitter_consumer_secret: str
    twitter_on_extup: bool
    twitter_on_intdown: bool
    twitter_on_intup: bool
    twitter_access_token_secret: str
    twitter_on_newdevice: bool
    twitter_on_stop: bool
    twitter_consumer_key: str
    twitter_access_token: str
    twitter_incl_subject: bool
    twitter_on_extdown: bool
    twitter_on_pause: bool
    twitter_on_play: bool
    twitter_incl_poster: bool
    twitter_on_created: bool


class Plex(BaseModel):
    plex_on_created: bool
    plex_on_concurrent: bool
    plex_client_host: str
    plex_on_stop: bool
    plex_on_resume: bool
    plex_on_watched: bool
    plex_on_play: bool
    plex_on_extdown: bool
    plex_on_intdown: bool
    plex_on_newdevice: bool
    plex_enabled: bool
    plex_on_buffer: bool
    plex_on_intup: bool
    plex_on_pmsupdate: bool
    plex_username: str
    plex_on_pause: bool
    plex_password: str
    plex_on_extup: bool


class Join(BaseModel):
    join_on_concurrent: bool
    join_on_newdevice: bool
    join_deviceid: str
    join_on_play: bool
    join_on_watched: bool
    join_on_resume: bool
    join_on_created: bool
    join_on_extdown: bool
    join_on_intup: bool
    join_on_buffer: bool
    join_incl_subject: bool
    join_enabled: bool
    join_on_pause: bool
    join_apikey: str
    join_on_pmsupdate: bool
    join_on_intdown: bool
    join_on_extup: bool
    join_on_stop: bool


class XBMC(BaseModel):
    xbmc_password: str
    xbmc_on_play: bool
    xbmc_on_pause: bool
    xbmc_username: str
    xbmc_on_extup: bool
    xbmc_on_watched: bool
    xbmc_on_buffer: bool
    xbmc_enabled: bool
    xbmc_host: str
    xbmc_on_created: bool
    xbmc_on_intup: bool
    xbmc_on_extdown: bool
    xbmc_on_pmsupdate: bool
    xbmc_on_stop: bool
    xbmc_on_newdevice: bool
    xbmc_on_resume: bool
    xbmc_on_intdown: bool
    xbmc_on_concurrent: bool


class Browser(BaseModel):
    browser_on_intdown: bool
    browser_on_newdevice: bool
    browser_on_pmsupdate: bool
    browser_on_intup: bool
    browser_on_buffer: bool
    browser_auto_hide_delay: str
    browser_on_created: bool
    browser_on_pause: bool
    browser_on_stop: bool
    browser_on_play: bool
    browser_on_watched: bool
    browser_on_extdown: bool
    browser_on_extup: bool
    browser_on_resume: bool
    browser_on_concurrent: bool
    browser_enabled: bool


class Newsletter(BaseModel):
    newsletter_dir: str
    newsletter_templates: str
    newsletter_self_hosted: bool
    newsletter_static_url: bool
    newsletter_inline_styles: bool
    newsletter_password: str
    newsletter_custom_dir: str
    newsletter_auth: bool


class Cloudinary(BaseModel):
    cloudinary_api_key: str
    cloudinary_cloud_name: str
    cloudinary_api_secret: str


class Data(BaseModel):
    IFTTT: IFTTT
    Growl: Growl
    PMS: PMS
    Monitoring: Monitoring
    General: General
    Slack: Slack
    Boxcar: Boxcar
    PushBullet: PushBullet
    Scripts: Scripts
    NMA: NMA
    Hipchat: Hipchat
    Pushalot: Pushalot
    Prowl: Prowl
    Advanced: Advanced
    Facebook: Facebook
    Email: Email
    OSX_Notify: OSXNotify
    PlexWatch: PlexWatch
    Pushover: Pushover
    Telegram: Telegram
    Twitter: Twitter
    Plex: Plex
    Join: Join
    XBMC: XBMC
    Browser: Browser
    Newsletter: Newsletter
    Cloudinary: Cloudinary


class Response(BaseModel):
    result: str
    message: Any
    data: Data


class Model(BaseModel):
    response: Response
