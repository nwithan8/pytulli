# Python client for Tautulli API
Interact with Tautulli's API in Python

# Installation
From PyPi: ``python -m pip install tautulli``

From GitHub ``python -m pip install git+https://github.com/nwithan8/pytulli.git``

# Usage
This client covers nearly 100% of all Tautulli's available API calls, including type checks and enforcing required variables.

More details about Tautulli's API can be found on the [Tautulli's GitHub wiki page](https://github.com/Tautulli/Tautulli-Wiki/wiki/Tautulli-API-Reference).

Most API call functions that return data return raw JSON data. Some return strings or file contents (in the case of downloads).

API calls functions that do not return data return `True`/`False` booleans to confirm that the API call was successful.

Import the ``tautulli`` package as initialize the API
Example:
```python
from tautulli import tautulli

api = tautulli.API(base_url="http://myipaddress:port", api_key="thisisanapikey")
```

You can optionally pass ``verbose=True`` into the API declaration to produce verbose debugging logs and error messages.

# Documentation

Documentation available on [ReadTheDocs](https://pytulli.readthedocs.io/en/latest/documentation.html)