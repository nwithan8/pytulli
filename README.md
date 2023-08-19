# A Python client for Tautulli's API

[![PyPi](https://img.shields.io/pypi/dm/tautulli?label=Downloads&logo=pypi)](https://pypi.org/project/tautulli)
[![License](https://img.shields.io/pypi/l/tautulli?color=orange&style=flat-square)](https://github.com/nwithan8/pytulli/blob/master/LICENSE)

[![Open Issues](https://img.shields.io/github/issues-raw/nwithan8/pytulli?color=gold&style=flat-square)](https://github.com/nwithan8/pytulli/issues?q=is%3Aopen+is%3Aissue)
[![Closed Issues](https://img.shields.io/github/issues-closed-raw/nwithan8/pytulli?color=black&style=flat-square)](https://github.com/nwithan8/pytulli/issues?q=is%3Aissue+is%3Aclosed)
[![Latest Release](https://img.shields.io/github/v/release/nwithan8/pytulli?color=red&label=latest%20release&logo=github&style=flat-square)](https://github.com/nwithan8/pytulli/releases)

[![Discord](https://img.shields.io/discord/472537215457689601?color=blue&logo=discord&style=flat-square)](https://discord.gg/7jGbCJQ)
[![Twitter](https://img.shields.io/twitter/follow/nwithan8?label=%40nwithan8&logo=twitter&style=flat-square)](https://twitter.com/nwithan8)

Interact with Tautulli's API in Python

# Installation

- From PyPi (recommended): ``python -m pip install tautulli``
- From GitHub ``python -m pip install git+https://github.com/nwithan8/pytulli.git``
  - This is not recommended, as the version will always default to 0.0.0


# Usage

This client covers nearly 100% of all Tautulli's available API calls, including type checks and enforcing required variables.

More details about Tautulli's API can be found on the [Tautulli's GitHub wiki page](https://github.com/Tautulli/Tautulli/wiki/Tautulli-API-Reference).

Most API call functions that return data return raw JSON data. Some return strings or file contents (in the case of downloads).

API calls functions that do not return data return `True`/`False` booleans to confirm that the API call was successful.

Import the ``tautulli`` package as initialize the API
Example:
```python
from tautulli import RawAPI

api = RawAPI(base_url="http://myipaddress:port", api_key="thisisanapikey")
```

You can optionally pass ``verbose=True`` into the API declaration to produce verbose debugging logs and error messages.

Additional utilities and shortcuts can be accessed via the `tautulli.tools` module.

# Documentation

Documentation available on [ReadTheDocs](https://pytulli.readthedocs.io/en/latest/documentation.html)
