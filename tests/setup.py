import os

from dotenv import load_dotenv

import tautulli


def raw_client(no_key: bool = False) -> tautulli.RawAPI:
    load_dotenv()
    url = os.getenv("T_URL")
    if not url:
        raise ValueError("T_URL is not set")
    if no_key:
        return tautulli.RawAPI(base_url=url, api_key="placeholder")
    else:
        key = os.getenv("T_KEY")
        if not key:
            temp_client = tautulli.RawAPI(base_url=url, api_key="placeholder")
            key = temp_client.get_api_key()
        if not key:
            raise ValueError("T_KEY is not set and could not be retrieved from server")
        return tautulli.RawAPI(base_url=url, api_key=key, verbose=True)
