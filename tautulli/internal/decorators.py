import sys
from functools import wraps

from tautulli.internal.utils import _success_result, _get_response_data


def raw_api_bool(func):
    """
    Execute the Raw API equivalent of an Object API function.

    :returns: Result of the Raw API equivalent, or `False` if an error occurs.
    :rtype: bool
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs) -> bool:
        try:
            method = getattr(self._raw_api, func.__name__)
            return method(*args, **kwargs)
        except AttributeError:
            return False

    return wrapper


def make_property_object(func):
    """
    Execute the Raw API equivalent of on Object API function.

    Parse the response JSON into an object.

    :returns: An instance of the class (determined by the first value in the tuple returned from the Object API function)
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs) -> object:
        try:
            data = getattr(self._raw_api, func.__name__)
            class_name = func(self)
            clazz = getattr(sys.modules["tautulli.models"], class_name)
            if type(data) == list:
                return [clazz(**item) for item in data]
            else:
                return clazz(**data)
        except AttributeError:
            return None

    return wrapper


def make_object(func):
    """
    Execute the Raw API equivalent of on Object API function.

    Parse the response JSON into an object.

    :returns: An instance of the class (determined by the first value in the tuple returned from the Object API function)
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs) -> object:
        try:
            method = getattr(self._raw_api, func.__name__)
            data = method(*args, **kwargs)
            class_name = func(self, *args, **kwargs)
            clazz = getattr(sys.modules["tautulli.models"], class_name)
            if type(data) == list:
                return [clazz(**item) for item in data]
            else:
                return clazz(**data)
        except AttributeError:
            return None

    return wrapper


def set_and_forget(func):
    """
    Execute an API call that does not return valuable data.

    :returns: `True` if the server replied with success, `False` otherwise.
    """
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
    """
    Execute an API call that returns valuable data.

    :returns: A JSON dictionary of the data returned by the API call.
    """
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
