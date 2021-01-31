import sys
from functools import wraps

from tautulli.utils import _success_result, _get_response_data
from tautulli.models import *


def raw_api_bool(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs) -> bool:
        try:
            method = getattr(self._raw_api, func.__name__)
            return method(*args, **kwargs)
        except AttributeError:
            return False

    return wrapper


def make_property_object(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs) -> object:
        try:
            data = getattr(self._raw_api, func.__name__)
            if not data:
                return None
            class_name = globals()[func(self)]
            if class_name.__name__ == "Datum":
                return [class_name(**item) for item in data]
            else:
                return class_name(**data)
        except AttributeError:
            return None

    return wrapper


def make_object(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs) -> object:
        try:
            method = getattr(self._raw_api, func.__name__)
            data = method(*args, **kwargs)
            if not data:
                return None
            class_name = getattr(sys.modules[__name__], func())
            return class_name(data=data)
        except AttributeError:
            return None

    return wrapper


def set_and_forget(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs) -> bool:
        """
        Return if the ['response']['result'] part of the JSON response == 'success'
        :rtype: bool
        """
        command, params = func(self, *args, **kwargs)
        if not command:
            return False
        json_data = self._get_json(command=command, params=params)
        return _success_result(json_data=json_data)

    return wrapper


def raw_json(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs) -> dict:
        """
        Return the ['response']['data'] part of the JSON response
        :rtype: dict
        """
        command, params = func(self, *args, **kwargs)
        if not command:
            return {}
        json_data = self._get_json(command=command, params=params)
        return _get_response_data(json_data=json_data)

    return wrapper
