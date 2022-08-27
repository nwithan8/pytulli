import pytest

from tautulli import models
from tests.setup import object_client


@pytest.mark.skip(reason="Can't test add.")
def test_add_newsletter_config():
    client = object_client()


@pytest.mark.skip(reason="Can't test add.")
def test_add_notifier_config():
    client = object_client()


def test_arnold():
    client = object_client()
    arnold_quote = client.arnold
    assert arnold_quote is not None
    assert type(arnold_quote) == str


@pytest.mark.skip(reason="Can't test backup.")
def test_backup_config():
    client = object_client()


@pytest.mark.skip(reason="Can't test backup.")
def test_backup_database():
    client = object_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_all_library_history():
    client = object_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_all_user_history():
    client = object_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_cache():
    client = object_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_export():
    client = object_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_history():
    client = object_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_hosted_images():
    client = object_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_image_cache():
    client = object_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_library():
    client = object_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_login_log():
    client = object_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_lookup_info():
    client = object_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_media_info_cache():
    client = object_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_mobile_device():
    client = object_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_newsletter():
    client = object_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_newsletter_log():
    client = object_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_notification_log():
    client = object_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_notifier():
    client = object_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_recently_added():
    client = object_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_synced_item():
    client = object_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_temp_sessions():
    client = object_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_user():
    client = object_client()


def test_docs():
    client = object_client()
    docs = client.docs
    assert docs is not None
    assert type(docs) == models.Docs


def test_docs_md():
    client = object_client()
    docs = client.docs_md
    assert docs is not None
    assert type(docs) == str


@pytest.mark.skip(reason="Can't test download.")
def test_download_config():
    client = object_client()


@pytest.mark.skip(reason="Can't test download.")
def test_download_database():
    client = object_client()


@pytest.mark.skip(reason="Can't test download.")
def test_download_export():
    client = object_client()


@pytest.mark.skip(reason="Can't test download.")
def test_download_log():
    client = object_client()


@pytest.mark.skip(reason="Can't test download.")
def test_download_plex_log():
    client = object_client()


@pytest.mark.skip(reason="Can't test edit.")
def test_edit_library():
    client = object_client()


@pytest.mark.skip(reason="Can't test edit.")
def test_edit_user():
    client = object_client()


@pytest.mark.skip(reason="Can't test export.")
def test_export_metadata():
    client = object_client()


def test_activity():
    client = object_client()
    activity = client.activity()
    assert activity is not None
    assert type(activity) == models.Activity


def test_get_api_key():
    no_key_client = object_client(no_key=True)
    key = no_key_client.get_api_key()
    assert key is not None


@pytest.mark.skip(reason="Requires parameters.")
def test_get_children_metadata():
    client = object_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_get_collections_table():
    client = object_client()


def test_date_formats():
    client = object_client()
    date_formats = client.date_formats
    assert date_formats is not None
    assert type(date_formats) == models.DateFormats


def test_get_export_fields():
    client = object_client()
    export_fields = client.get_export_fields(media_type="movie")
    assert export_fields is not None
    assert type(export_fields) == models.ExportFields


def test_get_exports_table():
    client = object_client()
    exports = client.get_exports_table()
    assert exports is not None
    assert type(exports) == models.ExportsTable


def test_get_geoip_lookup():
    client = object_client()
    geoip_lookup = client.get_geoip_lookup("100.100.1.10")
    assert geoip_lookup is not None
    assert type(geoip_lookup) == models.GeoIPLookup


def test_get_history():
    client = object_client()
    history = client.get_history()
    assert history is not None
    assert type(history) == models.History


def test_get_home_stats():
    client = object_client()
    home_stats = client.get_home_stats()
    assert home_stats is not None
    assert type(home_stats) == list
    for stat in home_stats:
        assert type(stat) == models.HomeStat


@pytest.mark.skip(reason="Requires parameters.")
def test_get_item_user_stats():
    client = object_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_get_item_watch_time_stats():
    client = object_client()


def test_libraries():
    client = object_client()
    libraries = client.libraries
    assert libraries is not None
    assert type(libraries) == list
    for library in libraries:
        assert type(library) == models.LibrariesEntry


def test_get_libraries_table():
    client = object_client()
    libraries = client.get_libraries_table()
    assert libraries is not None
    assert type(libraries) == models.LibrariesTable


@pytest.mark.skip(reason="Requires parameters.")
def test_get_library():
    client = object_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_get_library_media_info():
    client = object_client()


def test_library_names():
    client = object_client()
    library_names = client.library_names
    assert library_names is not None
    assert type(library_names) == list
    for library_name in library_names:
        assert type(library_name) == models.LibraryName


@pytest.mark.skip(reason="Requires parameters.")
def test_get_library_user_stats():
    client = object_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_get_library_watch_time_stats():
    client = object_client()


def test_get_logs():
    client = object_client()
    logs = client.get_logs()
    assert logs is not None
    assert type(logs) == list
    for log in logs:
        assert type(log) == models.LogEntry


@pytest.mark.skip(reason="Requires parameters.")
def test_get_metadata():
    client = object_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_get_new_rating_keys():
    client = object_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_get_newsletter_config():
    client = object_client()


def test_get_newsletter_log():
    client = object_client()
    newsletter_log = client.get_newsletter_log()
    assert newsletter_log is not None
    assert type(newsletter_log) == models.NewsletterLog


def test_newsletters():
    client = object_client()
    newsletters = client.newsletters
    assert newsletters is not None
    assert type(newsletters) == list
    for newsletter in newsletters:
        assert type(newsletter) == models.Newsletter


def test_get_notification_log():
    client = object_client()
    notification_log = client.get_notification_log()
    assert notification_log is not None
    assert type(notification_log) == models.NotificationLog


@pytest.mark.skip(reason="Requires parameters.")
def test_get_notifier_config():
    client = object_client()


def test_notifier_parameters():
    client = object_client()
    notifier_parameters = client.notifier_parameters
    assert notifier_parameters is not None
    assert type(notifier_parameters) == list
    for parameter in notifier_parameters:
        assert type(parameter) == models.NotifierParameter


def test_get_notifiers():
    client = object_client()
    notifiers = client.get_notifiers()
    assert notifiers is not None
    assert type(notifiers) == list
    for notifier in notifiers:
        assert type(notifier) == models.Notifier


@pytest.mark.skip(reason="Requires parameters.")
def test_get_old_rating_keys():
    client = object_client()


def test_get_playlists_table():
    client = object_client()
    playlists = client.get_playlists_table()
    assert playlists is not None
    assert type(playlists) == models.PlaylistsTable


def test_get_plays_by_date():
    client = object_client()
    plays_by_date = client.get_plays_by_date()
    assert plays_by_date is not None
    assert type(plays_by_date) == models.PlaysOrStreamTypesBy


def test_get_plays_by_day_of_week():
    client = object_client()
    plays_by_day_of_week = client.get_plays_by_day_of_week()
    assert plays_by_day_of_week is not None
    assert type(plays_by_day_of_week) == models.PlaysOrStreamTypesBy


def test_get_plays_by_hour_of_day():
    client = object_client()
    plays_by_hour_of_day = client.get_plays_by_hour_of_day()
    assert plays_by_hour_of_day is not None
    assert type(plays_by_hour_of_day) == models.PlaysOrStreamTypesBy


def test_get_plays_by_source_resolution():
    client = object_client()
    plays_by_source_resolution = client.get_plays_by_source_resolution()
    assert plays_by_source_resolution is not None
    assert type(plays_by_source_resolution) == models.PlaysOrStreamTypesBy


def test_get_plays_by_stream_resolution():
    client = object_client()
    plays_by_stream_resolution = client.get_plays_by_stream_resolution()
    assert plays_by_stream_resolution is not None
    assert type(plays_by_stream_resolution) == models.PlaysOrStreamTypesBy


def test_get_plays_by_stream_type():
    client = object_client()
    plays_by_stream_type = client.get_plays_by_stream_type()
    assert plays_by_stream_type is not None
    assert type(plays_by_stream_type) == models.PlaysOrStreamTypesBy


def test_get_plays_by_top_10_platforms():
    client = object_client()
    plays_by_top_10_platforms = client.get_plays_by_top_10_platforms()
    assert plays_by_top_10_platforms is not None
    assert type(plays_by_top_10_platforms) == models.PlaysOrStreamTypesBy


def test_get_plays_by_top_10_users():
    client = object_client()
    plays_by_top_10_users = client.get_plays_by_top_10_users()
    assert plays_by_top_10_users is not None
    assert type(plays_by_top_10_users) == models.PlaysOrStreamTypesBy


def test_get_plays_per_month():
    client = object_client()
    plays_per_month = client.get_plays_per_month()
    assert plays_per_month is not None
    assert type(plays_per_month) == models.PlaysOrStreamTypesBy


def test_get_plex_log():
    client = object_client()
    plex_log = client.get_plex_log()
    assert plex_log is not None
    assert type(plex_log) == models.PlexLog


def test_pms_update():
    client = object_client()
    pms_update = client.pms_update
    assert pms_update is not None
    assert type(pms_update) == models.PMSUpdate


def test_get_recently_added():
    client = object_client()
    recently_added = client.get_recently_added(count=10, media_type='movie')
    assert recently_added is not None
    assert type(recently_added) == models.RecentlyAdded


def test_server_friendly_name():
    client = object_client()
    server_friendly_name = client.server_friendly_name
    assert server_friendly_name is not None
    assert type(server_friendly_name) == str


@pytest.mark.skip(reason="Requires parameters.")
def test_get_server_id():
    client = object_client()


def test_server_identity():
    client = object_client()
    server_identity = client.server_identity
    assert server_identity is not None
    assert type(server_identity) == models.ServerIdentity


def test_server_info():
    client = object_client()
    server_info = client.server_info
    assert server_info is not None
    assert type(server_info) == models.ServerInfo


@pytest.mark.skip(reason="Will fail if no Plex Media Servers are configured.")
def test_get_server_list():
    client = object_client()
    server_list = client.server_list
    assert server_list is not None
    assert type(server_list) == list
    for server in server_list:
        assert type(server) == models.ServerListEntry


@pytest.mark.skip(reason="Requires parameters.")
def test_get_server_pref():
    client = object_client()


def test_servers_info():
    client = object_client()
    servers_info = client.servers_info
    assert servers_info is not None
    assert type(servers_info) == list
    for server in servers_info:
        assert type(server) == models.ServersInfoEntry


def test_get_settings():
    client = object_client()
    settings = client.get_settings()
    assert settings is not None
    assert type(settings) == models.Settings


@pytest.mark.skip(reason="Requires parameters.")
def test_get_stream_data():
    client = object_client()


def test_get_stream_type_by_top_10_platforms():
    client = object_client()
    stream_type_by_top_10_platforms = client.get_stream_type_by_top_10_platforms()
    assert stream_type_by_top_10_platforms is not None
    assert type(stream_type_by_top_10_platforms) == models.PlaysOrStreamTypesBy


def test_get_stream_type_by_top_10_users():
    client = object_client()
    stream_type_by_top_10_users = client.get_stream_type_by_top_10_users()
    assert stream_type_by_top_10_users is not None
    assert type(stream_type_by_top_10_users) == models.PlaysOrStreamTypesBy


@pytest.mark.skip(reason="Requires parameters.")
def test_get_synced_items():
    client = object_client()


def test_tautulli_info():
    client = object_client()
    tautulli_info = client.tautulli_info
    assert tautulli_info is not None
    assert type(tautulli_info) == models.TautulliInfo


@pytest.mark.skip(reason="Requires parameters.")
def test_get_user():
    client = object_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_get_user_ips():
    client = object_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_get_user_logins():
    client = object_client()


def test_user_names():
    client = object_client()
    user_names = client.user_names
    assert user_names is not None
    assert type(user_names) == list
    for user_name in user_names:
        assert type(user_name) == models.UserName


@pytest.mark.skip(reason="Requires parameters.")
def test_get_user_player_stats():
    client = object_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_get_user_watch_time_stats():
    client = object_client()


def test_users():
    client = object_client()
    users = client.users
    assert users is not None
    assert type(users) == list
    for user in users:
        assert type(user) == models.User


def test_get_users_table():
    client = object_client()
    users_table = client.get_users_table()
    assert users_table is not None
    assert type(users_table) == models.UsersTable


def test_get_whois_lookup():
    client = object_client()
    whois_lookup = client.get_whois_lookup('google.com')
    assert whois_lookup is not None
    assert type(whois_lookup) == models.WHOISLookup


@pytest.mark.skip(reason="Can't test import")
def test_import_config():
    client = object_client()


@pytest.mark.skip(reason="Can't test import")
def test_import_database():
    client = object_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_logout_user_session():
    client = object_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_notify():
    client = object_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_notify_newsletter():
    client = object_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_notify_recently_added():
    client = object_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_pms_image_proxy():
    client = object_client()


@pytest.mark.skip(reason="Can't test update.")
def test_refresh_libraries():
    client = object_client()


@pytest.mark.skip(reason="Can't test update.")
def test_refresh_users_list():
    client = object_client()


@pytest.mark.skip(reason="Can't test update.")
def test_register_device():
    client = object_client()


@pytest.mark.skip(reason="Can't test update.")
def test_restart():
    client = object_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_search():
    client = object_client()


def test_server_status():
    client = object_client()
    status = client.server_status
    assert status is not None
    assert type(status) == models.ServerStatus


@pytest.mark.skip(reason="Can't test update.")
def test_set_mobile_device_config():
    client = object_client()


@pytest.mark.skip(reason="Can't test update.")
def test_set_newsletter_config():
    client = object_client()


@pytest.mark.skip(reason="Can't test update.")
def test_set_notifier_config():
    client = object_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_sql():
    client = object_client()


def test_status():
    client = object_client()
    status = client.status()
    assert status is not None
    assert type(status) == models.Status


@pytest.mark.skip(reason="Can't test update.")
def test_terminate_session():
    client = object_client()


@pytest.mark.skip(reason="Can't test update.")
def test_undelete_library():
    client = object_client()


@pytest.mark.skip(reason="Can't test update.")
def test_undelete_user():
    client = object_client()


@pytest.mark.skip(reason="Can't test update.")
def test_update():
    client = object_client()


def test_update_check():
    client = object_client()
    update_check = client.update_check
    assert update_check is not None
    assert type(update_check) == models.UpdateCheck


@pytest.mark.skip(reason="Can't test update.")
def test_update_metadata_details():
    client = object_client()
