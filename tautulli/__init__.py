import os
from typing import List

from tautulli.api import ObjectAPI
from tautulli.api import RawAPI

__version__ = 'VERSIONADDEDBYGITHUB'

__title__ = "tautulli"
__author__ = 'Nate Harris'
__author_email__ = 'n8gr8gbln@gmail.com'
__github_username__ = "nwithan8"
__github_repo__ = "pytulli"
__copyright__ = "Copyright © YEARADDEDBYGITHUB - Nate Harris"
__license__ = 'GNU General Public License v3 (GPLv3)'
__description__ = "A complete Python client for Tautulli's API"
__keywords__ = ["Tautulli", "API", "client", "Plex", "PMS", "Plex Media Server", "media", "server", "JSON"]


def __supported_api_versions__() -> List[str]:
    with open(os.path.join(os.path.dirname(__file__), "API_VERSIONS")) as f:
        return f.read().splitlines()


def __min_api_version__() -> str:
    return __supported_api_versions__()[0]
