import pytest

from tautulli._info import __min_api_version__
from tautulli.exceptions import HttpException
from tests.setup import raw_client, invalid_raw_client, no_ssl_client


@pytest.mark.skip(reason="Doesn't play well in CI.")
def test_invalid_api_key():
    client = invalid_raw_client()
    with pytest.raises(HttpException) as e:
        _ = client.tautulli_info
    assert type(e.value) == HttpException
    assert "Invalid apikey" in str(e)


def test_ssl():
    client = raw_client()
    assert client._ssl_verify is True
    client = no_ssl_client()
    assert client._ssl_verify is False
    arnold_quote = client.arnold  # attempt to use the client
    assert arnold_quote is not None
    assert type(arnold_quote) == str


@pytest.mark.skip(reason="Can't test add.")
def test_add_newsletter_config():
    client = raw_client()


@pytest.mark.skip(reason="Can't test add.")
def test_add_notifier_config():
    client = raw_client()


def test_arnold():
    client = raw_client()
    arnold_quote = client.arnold
    assert arnold_quote is not None
    assert type(arnold_quote) == str


@pytest.mark.skip(reason="Can't test backup.")
def test_backup_config():
    client = raw_client()


@pytest.mark.skip(reason="Can't test backup.")
def test_backup_database():
    client = raw_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_all_library_history():
    client = raw_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_all_user_history():
    client = raw_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_cache():
    client = raw_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_export():
    client = raw_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_history():
    client = raw_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_hosted_images():
    client = raw_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_image_cache():
    client = raw_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_library():
    client = raw_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_login_log():
    client = raw_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_lookup_info():
    client = raw_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_media_info_cache():
    client = raw_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_mobile_device():
    client = raw_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_newsletter():
    client = raw_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_newsletter_log():
    client = raw_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_notification_log():
    client = raw_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_notifier():
    client = raw_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_recently_added():
    client = raw_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_synced_item():
    client = raw_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_temp_sessions():
    client = raw_client()


@pytest.mark.skip(reason="Can't test delete.")
def test_delete_user():
    client = raw_client()


def test_docs():
    client = raw_client()
    docs = client.docs
    assert docs is not None
    assert type(docs) == dict


def test_docs_md():
    client = raw_client()
    docs = client.docs_md
    assert docs is not None
    assert type(docs) == str


@pytest.mark.skip(reason="Can't test download.")
def test_download_config():
    client = raw_client()


@pytest.mark.skip(reason="Can't test download.")
def test_download_database():
    client = raw_client()


@pytest.mark.skip(reason="Can't test download.")
def test_download_export():
    client = raw_client()


@pytest.mark.skip(reason="Can't test download.")
def test_download_log():
    client = raw_client()


@pytest.mark.skip(reason="Can't test download.")
def test_download_plex_log():
    client = raw_client()


@pytest.mark.skip(reason="Can't test edit.")
def test_edit_library():
    client = raw_client()


@pytest.mark.skip(reason="Can't test edit.")
def test_edit_user():
    client = raw_client()


@pytest.mark.skip(reason="Can't test export.")
def test_export_metadata():
    client = raw_client()


def test_activity():
    client = raw_client()
    activity = client.activity()
    assert activity is not None
    assert type(activity) == dict


def test_get_api_key():
    no_key_client = raw_client(no_key=True)
    key = no_key_client.get_api_key()
    assert key is not None


@pytest.mark.skip(reason="Requires parameters.")
def test_get_children_metadata():
    client = raw_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_get_collections_table():
    client = raw_client()


def test_date_formats():
    client = raw_client()
    date_formats = client.date_formats
    assert date_formats is not None
    assert type(date_formats) == dict


def test_get_export_fields():
    client = raw_client()
    export_fields = client.get_export_fields(media_type="movie")
    assert export_fields is not None
    assert type(export_fields) == dict


def test_get_exports_table():
    client = raw_client()
    exports = client.get_exports_table()
    assert exports is not None
    assert type(exports) == dict


def test_get_geoip_lookup():
    client = raw_client()
    geoip_lookup = client.get_geoip_lookup("100.100.1.10")
    assert geoip_lookup is not None
    assert type(geoip_lookup) == dict


def test_get_history():
    client = raw_client()
    history = client.get_history()
    assert history is not None
    assert type(history) == dict


def test_get_home_stats():
    client = raw_client()
    home_stats = client.get_home_stats()
    assert home_stats is not None
    assert type(home_stats) == list


@pytest.mark.skip(reason="Requires parameters.")
def test_get_item_user_stats():
    client = raw_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_get_item_watch_time_stats():
    client = raw_client()


def test_libraries():
    client = raw_client()
    libraries = client.libraries
    assert libraries is not None
    assert type(libraries) == list


def test_get_libraries_table():
    client = raw_client()
    libraries = client.get_libraries_table()
    assert libraries is not None
    assert type(libraries) == dict


@pytest.mark.skip(reason="Requires parameters.")
def test_get_library():
    client = raw_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_get_library_media_info():
    client = raw_client()


def test_library_names():
    client = raw_client()
    library_names = client.library_names
    assert library_names is not None
    assert type(library_names) == list


@pytest.mark.skip(reason="Requires parameters.")
def test_get_library_user_stats():
    client = raw_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_get_library_watch_time_stats():
    client = raw_client()


def test_get_logs():
    client = raw_client()
    logs = client.get_logs()
    assert logs is not None
    assert type(logs) == list


@pytest.mark.skip(reason="Requires parameters.")
def test_get_metadata():
    client = raw_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_get_new_rating_keys():
    client = raw_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_get_newsletter_config():
    client = raw_client()


def test_get_newsletter_log():
    client = raw_client()
    newsletter_log = client.get_newsletter_log()
    assert newsletter_log is not None
    assert type(newsletter_log) == dict


def test_newsletters():
    client = raw_client()
    newsletters = client.newsletters
    assert newsletters is not None
    assert type(newsletters) == list


def test_get_notification_log():
    client = raw_client()
    notification_log = client.get_notification_log()
    assert notification_log is not None
    assert type(notification_log) == dict


@pytest.mark.skip(reason="Requires parameters.")
def test_get_notifier_config():
    client = raw_client()


def test_notifier_parameters():
    client = raw_client()
    notifier_parameters = client.notifier_parameters
    assert notifier_parameters is not None
    assert type(notifier_parameters) == list


def test_get_notifiers():
    client = raw_client()
    notifiers = client.get_notifiers()
    assert notifiers is not None
    assert type(notifiers) == list


@pytest.mark.skip(reason="Requires parameters.")
def test_get_old_rating_keys():
    client = raw_client()


def test_get_playlists_table():
    client = raw_client()
    playlists = client.get_playlists_table()
    assert playlists is not None
    assert type(playlists) == dict


def test_get_plays_by_date():
    client = raw_client()
    plays_by_date = client.get_plays_by_date()
    assert plays_by_date is not None
    assert type(plays_by_date) == dict


def test_get_plays_by_day_of_week():
    client = raw_client()
    plays_by_day_of_week = client.get_plays_by_day_of_week()
    assert plays_by_day_of_week is not None
    assert type(plays_by_day_of_week) == dict


def test_get_plays_by_hour_of_day():
    client = raw_client()
    plays_by_hour_of_day = client.get_plays_by_hour_of_day()
    assert plays_by_hour_of_day is not None
    assert type(plays_by_hour_of_day) == dict


def test_get_plays_by_source_resolution():
    client = raw_client()
    plays_by_source_resolution = client.get_plays_by_source_resolution()
    assert plays_by_source_resolution is not None
    assert type(plays_by_source_resolution) == dict


def test_get_plays_by_stream_resolution():
    client = raw_client()
    plays_by_stream_resolution = client.get_plays_by_stream_resolution()
    assert plays_by_stream_resolution is not None
    assert type(plays_by_stream_resolution) == dict


def test_get_plays_by_stream_type():
    client = raw_client()
    plays_by_stream_type = client.get_plays_by_stream_type()
    assert plays_by_stream_type is not None
    assert type(plays_by_stream_type) == dict


def test_get_plays_by_top_10_platforms():
    client = raw_client()
    plays_by_top_10_platforms = client.get_plays_by_top_10_platforms()
    assert plays_by_top_10_platforms is not None
    assert type(plays_by_top_10_platforms) == dict


def test_get_plays_by_top_10_users():
    client = raw_client()
    plays_by_top_10_users = client.get_plays_by_top_10_users()
    assert plays_by_top_10_users is not None
    assert type(plays_by_top_10_users) == dict


def test_get_plays_per_month():
    client = raw_client()
    plays_per_month = client.get_plays_per_month()
    assert plays_per_month is not None
    assert type(plays_per_month) == dict


def test_get_plex_log():
    client = raw_client()
    plex_log = client.get_plex_log()
    assert plex_log is not None
    assert type(plex_log) == dict


def test_pms_update():
    client = raw_client()
    pms_update = client.pms_update
    assert pms_update is not None
    assert type(pms_update) == dict


def test_get_recently_added():
    client = raw_client()
    recently_added = client.get_recently_added(count=10, media_type='movie')
    assert recently_added is not None
    assert type(recently_added) == dict


def test_server_friendly_name():
    client = raw_client()
    server_friendly_name = client.server_friendly_name
    assert server_friendly_name is not None
    assert type(server_friendly_name) == str


@pytest.mark.skip(reason="Requires parameters.")
def test_get_server_id():
    client = raw_client()


def test_server_identity():
    client = raw_client()
    server_identity = client.server_identity
    assert server_identity is not None
    assert type(server_identity) == dict


def test_server_info():
    client = raw_client()
    server_info = client.server_info
    assert server_info is not None
    assert type(server_info) == dict


@pytest.mark.skip(reason="Will fail if no Plex Media Servers are configured.")
def test_get_server_list():
    client = raw_client()
    server_list = client.server_list
    assert server_list is not None
    assert type(server_list) == list
    for server in server_list:
        assert type(server) == dict


@pytest.mark.skip(reason="Requires parameters.")
def test_get_server_pref():
    client = raw_client()


def test_servers_info():
    client = raw_client()
    servers_info = client.servers_info
    assert servers_info is not None
    assert type(servers_info) == list


def test_get_settings():
    client = raw_client()
    settings = client.get_settings()
    assert settings is not None
    assert type(settings) == dict


@pytest.mark.skip(reason="Requires parameters.")
def test_get_stream_data():
    client = raw_client()


def test_get_stream_type_by_top_10_platforms():
    client = raw_client()
    stream_type_by_top_10_platforms = client.get_stream_type_by_top_10_platforms()
    assert stream_type_by_top_10_platforms is not None
    assert type(stream_type_by_top_10_platforms) == dict


def test_get_stream_type_by_top_10_users():
    client = raw_client()
    stream_type_by_top_10_users = client.get_stream_type_by_top_10_users()
    assert stream_type_by_top_10_users is not None
    assert type(stream_type_by_top_10_users) == dict


@pytest.mark.skip(reason="Requires parameters.")
def test_get_synced_items():
    client = raw_client()


def test_tautulli_info():
    client = raw_client()
    tautulli_info = client.tautulli_info
    assert tautulli_info is not None
    assert type(tautulli_info) == dict


@pytest.mark.skip(reason="Requires parameters.")
def test_get_user():
    client = raw_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_get_user_ips():
    client = raw_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_get_user_logins():
    client = raw_client()


def test_user_names():
    client = raw_client()
    user_names = client.user_names
    assert user_names is not None
    assert type(user_names) == list


@pytest.mark.skip(reason="Requires parameters.")
def test_get_user_player_stats():
    client = raw_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_get_user_watch_time_stats():
    client = raw_client()


def test_users():
    client = raw_client()
    users = client.users
    assert users is not None
    assert type(users) == list


def test_get_users_table():
    client = raw_client()
    users_table = client.get_users_table()
    assert users_table is not None
    assert type(users_table) == dict


def test_get_whois_lookup():
    client = raw_client()
    whois_lookup = client.get_whois_lookup('google.com')
    assert whois_lookup is not None
    assert type(whois_lookup) == dict


@pytest.mark.skip(reason="Can't test import")
def test_import_config():
    client = raw_client()


@pytest.mark.skip(reason="Can't test import")
def test_import_database():
    client = raw_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_logout_user_session():
    client = raw_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_notify():
    client = raw_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_notify_newsletter():
    client = raw_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_notify_recently_added():
    client = raw_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_pms_image_proxy():
    client = raw_client()


@pytest.mark.skip(reason="Can't test update.")
def test_refresh_libraries():
    client = raw_client()


@pytest.mark.skip(reason="Can't test update.")
def test_refresh_users_list():
    client = raw_client()


@pytest.mark.skip(reason="Can't test update.")
def test_register_device():
    client = raw_client()


@pytest.mark.skip(reason="Can't test update.")
def test_restart():
    client = raw_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_search():
    client = raw_client()


def test_server_status():
    client = raw_client()
    status = client.server_status
    assert status is not None
    assert type(status) == dict


@pytest.mark.skip(reason="Can't test update.")
def test_set_mobile_device_config():
    client = raw_client()


@pytest.mark.skip(reason="Can't test update.")
def test_set_newsletter_config():
    client = raw_client()


@pytest.mark.skip(reason="Can't test update.")
def test_set_notifier_config():
    client = raw_client()


@pytest.mark.skip(reason="Requires parameters.")
def test_sql():
    client = raw_client()


def test_status():
    client = raw_client()
    status = client.status()
    assert status is not None
    assert type(status) == dict


@pytest.mark.skip(reason="Can't test update.")
def test_terminate_session():
    client = raw_client()


@pytest.mark.skip(reason="Can't test update.")
def test_undelete_library():
    client = raw_client()


@pytest.mark.skip(reason="Can't test update.")
def test_undelete_user():
    client = raw_client()


@pytest.mark.skip(reason="Can't test update.")
def test_update():
    client = raw_client()


def test_update_check():
    client = raw_client()
    update_check = client.update_check
    assert update_check is not None
    assert type(update_check) == dict


@pytest.mark.skip(reason="Can't test update.")
def test_update_metadata_details():
    client = raw_client()


def test__verify_compatibility():
    client = raw_client()
    min_api_version = __min_api_version__()
    passes = client._verify_compatibility(min_version=min_api_version)
    assert passes is True
