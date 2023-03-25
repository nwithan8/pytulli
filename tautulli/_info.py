import json
import os
from typing import List


def __supported_api_versions__() -> List[str]:
    with open(os.path.join(os.path.dirname(__file__), "API_VERSIONS.json")) as f:
        versions = f.read()
        return json.loads(versions)

def __min_api_version__() -> str:
    return __supported_api_versions__()[0]
