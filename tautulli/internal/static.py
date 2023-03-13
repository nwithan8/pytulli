empty_string = ""
empty_bytes = b''
empty_dict = {}
empty_list = []

cloud_image_hosts = ['imgur', 'cloudinary']
cloud_lookup_hosts = ['themoviedb', 'tvmaze', 'musicbrainz']
export_file_formats = ['csv', 'json', 'xml', 'm3u']
export_media_types = ['collection', 'playlist']
collections_sub_media_types = ['movie', 'show', 'artist', 'album', 'photoalbum']
playlist_sub_media_types = ['video', 'audio', 'photo']
order_direction = ['desc', 'asc']
exports_order_columns = ["added_at", "sort_title", "container", "bitrate", "video_codec", "video_resolution", "video_framerate", "audio_codec", "audio_channels", "file_size", "last_played", "play_count"]
history_order_columns = ["date", "friendly_name", "ip_address", "platform", "player", "full_title", "started", "paused_counter", "stopped", "duration"]
history_media_types = ["movie", "episode", "track", "live", "collection", "playlist"]
transcode_decisions = ['direct play', 'copy', 'transcode']
stats_type = ['plays', 'duration']
stats_category = ['top_movies', 'popular_movies', 'top_tv', 'popular_tv', 'top_music', 'popular_music', 'top_libraries', 'top_users', 'top_platforms', 'last_watched', 'most_concurrent']
libraries_order_columns = ["library_thumb", "section_name", "section_type", "count", "parent_count", "child_count", "last_accessed", "last_played", "plays", "duration"]
library_order_columns = ["added_at", "sort_title", "container", "bitrate", "video_codec", "video_resolution", "video_framerate", "audio_codec", "audio_channels", "file_size", "last_played", "play_count"]
log_sorting = ["time", "thread", "msg", "loglevel"]
all_media_types = ["movie", "show", "season", "episode", "artist", "album", "track"]
newsletter_order_column = ["timestamp", "newsletter_id", "agent_name", "notify_action", "subject_text", "start_date", "end_date", "uuid"]
notifications_order_column = ["timestamp", "notifier_id", "agent_name", "notify_action", "subject_text", "body_text"]
plex_log_types = ['server', 'scanner']
recently_added_media_types = ['movie', 'show', 'artist']
user_ips_order_columns = ["last_seen", "first_seen", "ip_address", "platform", "player", "last_played", "play_count"]
user_logins_order_columns = ["date", "time", "ip_address", "host", "os", "browser"]
user_tables_order_columns = ["user_thumb", "friendly_name", "last_seen", "ip_address", "platform", "player", "last_played", "plays", "duration"]
database_app_types = ['tautulli', 'plexwatch', 'plexivity']
tautulli_database_import_methods = ['merge', 'overwrite']
plexivity_table_names = ['processed', 'grouped']
image_fallback_types = ["poster", "cover", "art", "poster-live", "art-live", "art-live-full"]
library_media_info_types = ['movie', 'show', 'artist', 'photo']
logfile_types = ["tautulli", "tautulli_api", "plex_websocket"]
plex_logfile_types = ["Plex Media Server", "Plex Media Scanner"]

switcher = {
    "playing": "▶️",
    "paused": "⏸",
    "stopped": "⏹",
    "buffering": "⏳",
    "error": "⚠️"
}

media_type_icons = {
    'episode': '📺',
    'track': '🎧',
    'movie': '🎞',
    'clip': '🎬',
    'photo': '🖼',
    'live': '📡'
}

sessions_message = """{stream_count} {word}"""
transcodes_message = """{transcode_count} {word}"""
bandwidth_message = """🌐 {bandwidth}"""
lan_bandwidth_message = """(🏠 {bandwidth})"""

session_title_message = """{icon} {media_type_icon} {username}: *{title}*"""
session_player_message = """__Player__: {product} ({player})"""
session_details_message = """__Quality__: {quality_profile} ({bandwidth}){transcoding}"""
session_progress_message = """__Progress__: {progress} (ETA: {eta})"""

