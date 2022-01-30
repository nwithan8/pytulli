from tests.setup import raw_client


def test_get_api_key():
    no_key_client = raw_client(no_key=True)
    key = no_key_client.get_api_key()
    assert key is not None
    assert key != ''


def test_ping():
    client = raw_client()
    res = client.ping()
    assert res is not None
    assert type(res) == bool
    assert res is True
