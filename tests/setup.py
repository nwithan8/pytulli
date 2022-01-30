import os

from dotenv import load_dotenv

import tautulli


def raw_client(bypass_key: bool = False) -> tautulli.RawAPI:
    load_dotenv()
    url = os.getenv("T_URL")
    if not url:
        raise ValueError("T_URL is not set")
    key = os.getenv("T_KEY")
    if not key:
        if bypass_key:
            key = ""
        else:
            raise ValueError("T_KEY is not set")
    return tautulli.RawAPI(base_url=url, api_key=key, verbose=True)
