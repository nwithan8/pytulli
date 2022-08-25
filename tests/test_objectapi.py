from typing import List

import pytest

from tautulli import models
from tests.setup import object_client


# TODO: troubleshoot this test
def test_get_api_key():
    no_key_client = object_client(no_key=True)
    key = no_key_client.get_api_key()
    assert key is not None


def test_ping():
    client = object_client()
    res = client.ping()
    assert res is not None
    assert type(res) == bool
    assert res is True


def test_tautulli_info():
    client = object_client()
    tautulli_info = client.tautulli_info
    assert tautulli_info is not None
    assert type(tautulli_info) == models.TautulliInfo


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


def test_arnold():
    client = object_client()
    arnold_quote = client.arnold
    assert arnold_quote is not None
    assert type(arnold_quote) == str


def test_activity():
    client = object_client()
    activity = client.activity()
    assert activity is not None
    assert type(activity) == models.Activity


@pytest.mark.skip(reason="Cannot test as properties won't exist on a fake Tautilli instance")
def test_activity_summary():
    client = object_client()
    activity = client.activity_summary
    assert activity is not None
    assert type(activity) == models.ActivitySummary


@pytest.mark.skip(reason="Cannot test as properties won't exist on a fake Tautilli instance")
def test_activity_summary_message():
    client = object_client()
    activity = client.activity_summary_message
    assert activity is not None
    assert type(activity) == str


def test_date_formats():
    client = object_client()
    date_formats = client.date_formats
    assert date_formats is not None
    assert type(date_formats) == models.DateFormats


@pytest.mark.skip("This test is failing due to server-side issues")
def test_get_export_fields():
    client = object_client()
    export_fields = client.get_export_fields(media_type="movie")
    assert export_fields is not None
    assert type(export_fields) == models.ExportFields


@pytest.mark.skip("Not implemented.")
def test_get_exports_table():
    client = object_client()


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
        assert type(stat) == models.HomeStats


def test_libraries():
    client = object_client()
    libraries = client.libraries
    assert libraries is not None
    assert type(libraries) == models.Libraries


def test_get_libraries_table():
    client = object_client()
    libraries = client.get_libraries_table()
    assert libraries is not None
    assert type(libraries) == models.LibrariesTable


def test_library_names():
    client = object_client()
    library_names = client.library_names
    assert library_names is not None
    assert type(library_names) == List[models.LibraryName]


def test_get_logs():
    client = object_client()
    logs = client.get_logs()
    assert logs is not None
    assert type(logs) == list
    for log in logs:
        assert type(log) == models.Logs


def test_get_newsletter_log():
    client = object_client()
    newsletter_log = client.get_newsletter_log()
    assert newsletter_log is not None
    assert type(newsletter_log) == models.NewsletterLog


def test_newsletters():
    client = object_client()
    newsletters = client.newsletters
    assert newsletters is not None
    assert type(newsletters) == models.Newsletters


def test_get_notification_log():
    client = object_client()
    notification_log = client.get_notification_log()
    assert notification_log is not None
    assert type(notification_log) == models.NotificationLog


def test_notifier_parameters():
    client = object_client()
    notifier_parameters = client.notifier_parameters
    assert notifier_parameters is not None
    assert type(notifier_parameters) == list
    for parameter in notifier_parameters:
        assert type(parameter) == models.NotifierParameters


def test_get_notifiers():
    client = object_client()
    notifiers = client.get_notifiers()
    assert notifiers is not None
    assert type(notifiers) == models.Notifiers


def test_get_playlists_table():
    client = object_client()
    playlists = client.get_playlists_table()
    assert playlists is not None
    assert type(playlists) == models.PlaylistsTable


@pytest.mark.skip("Not implemented.")
def test_get_plays_by_date():
    client = object_client()


@pytest.mark.skip("Not implemented.")
def test_get_plays_by_day_of_week():
    client = object_client()


@pytest.mark.skip("Not implemented.")
def test_get_plays_by_hour_of_day():
    client = object_client()


@pytest.mark.skip("Not implemented.")
def test_get_plays_by_source_resolution():
    client = object_client()


@pytest.mark.skip("Not implemented.")
def test_get_plays_by_stream_resolution():
    client = object_client()


@pytest.mark.skip("Not implemented.")
def test_get_plays_by_stream_type():
    client = object_client()


@pytest.mark.skip("Not implemented.")
def test_get_plays_by_top_10_platforms():
    client = object_client()


@pytest.mark.skip("Not implemented.")
def test_get_plays_by_top_10_users():
    client = object_client()


@pytest.mark.skip("Not implemented.")
def test_get_plays_per_month():
    client = object_client()


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


def test_servers_info():
    client = object_client()
    servers_info = client.servers_info
    assert servers_info is not None
    assert type(servers_info) == models.ServersInfo


def test_get_settings():
    client = object_client()
    settings = client.get_settings()
    assert settings is not None
    assert type(settings) == models.Settings


@pytest.mark.skip("Not implemented.")
def test_get_stream_type_by_top_10_platforms():
    client = object_client()


@pytest.mark.skip("Not implemented.")
def test_get_stream_type_by_top_10_users():
    client = object_client()


def test_user_names():
    client = object_client()
    user_names = client.user_names
    assert user_names is not None
    assert type(user_names) == list
    for user_name in user_names:
        assert type(user_name) == models.UserNames


def test_users():
    client = object_client()
    users = client.users
    assert users is not None
    assert type(users) == list
    for user in users:
        assert type(user) == models.Users


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


@pytest.mark.skip("Not implemented.")
def test_status():
    client = object_client()


def test_update_check():
    client = object_client()
    update_check = client.update_check
    assert update_check is not None
    assert type(update_check) == models.UpdateCheck
