from functools import wraps

from tautulli.utils import _success_result, _get_response_data

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
        # print(json_data)
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
        # print(json_data)
        return _get_response_data(json_data=json_data)
    return wrapper