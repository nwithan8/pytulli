import pytest

from tautulli.tools import APIShortcuts
from tests.setup import raw_client, object_client


def test_shortcuts_from_raw_client():
    client = raw_client(no_key=True)
    shortcuts = client.shortcuts
    assert shortcuts is not None
    assert type(shortcuts) == APIShortcuts


def test_shortcuts_from_object_client():
    client = object_client(no_key=True)
    shortcuts = client.shortcuts
    assert shortcuts is not None
    assert type(shortcuts) == APIShortcuts


@pytest.mark.skip(reason="Ping will return false because no Plex Media Server exists")
def test_ping():
    client = raw_client()
    res = client.shortcuts.ping()
    assert res is not None
    assert type(res) == bool
    assert res is True

def test_api_version():
    client = raw_client()
    version = client.shortcuts.api_version
    assert version is not None
    assert type(version) == str


def test_activity_summary():
    client = raw_client()
    activity = client.shortcuts.activity_summary
    assert activity is not None
    assert type(activity) == dict


def test_activity_summary_message():
    client = raw_client()
    activity = client.shortcuts.activity_summary_message
    assert activity is not None
    assert type(activity) == str
