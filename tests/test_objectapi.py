from tests.setup import object_client


def test_tautulli_info():
    client = object_client()

    tautulli_info = client.tautulli_info
    assert tautulli_info is not None
