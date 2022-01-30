from tests.setup import raw_client


def test_get_api_key():
    no_auth_client = raw_client(bypass_key=True)
    key = no_auth_client.get_api_key()
    assert key is not None
    assert key != ''
