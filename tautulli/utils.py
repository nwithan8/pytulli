from typing import Union, List
import logging
from datetime import datetime

from tautulli import __title__


def datetime_to_string(datetime_object: datetime, string_format: str = "%Y-%m-%d"):
    """
    Convert a datetime.datetime object to a string
    :param datetime_object: Datetime.datetime object to convert
    :type datetime_object: datetime
    :param string_format: Date format to use
    :type string_format: str
    :return: Date in string format
    :rtype: str
    """
    if not datetime_object:
        return None
    return datetime_object.strftime(fmt=string_format)


def build_optional_params(**kwargs):
    """
    Build a dict with only kwargs elements that are not None
    :param kwargs: All possible parameters to include in final dict
    :type kwargs: dict
    :return: Dict of non-None parameters
    :rtype: dict
    """
    params = {}
    for k, v in kwargs.items():
        if v:
            params[k] = v
    return params


def bool_to_int(boolean: bool) -> int:
    """
    Convert a boolean to a 0/1 equivalent
    :param boolean: Boolean to convert
    :type boolean: bool
    :return: 0 if False, 1 if True
    :rtype: int
    """
    if boolean:
        return 1
    return 0


def int_list_to_string(int_list: List[int]):
    """
    Convert a list of ints to a comma-separated string
    e.g. [0, 1, 4] -> "0,1,4"
    :param int_list: List of ints to convert
    :type int_list: list
    :return: Comma-separated string of ints
    :rtype: str
    """
    int_list = list(map(str, int_list))
    return ','.join(int_list)


def _one_needed(**kwargs):
    """
    Check if at least one of the kwargs is not None
    Logs error message if not.
    :param kwargs: Dict of keyword arguments
    :type kwargs: dict
    :return: Whether at least on kwarg is not None
    :rtype: bool
    """
    one_used = False
    for k, v in kwargs.items():
        if v:
            one_used = True
    if not one_used:
        logger = logging.getLogger(__title__)
        logger.error(f"Please provide one of the following: {', '.join(kwargs.keys())}")
    return one_used


def _which_used(**kwargs):
    """
    Get which (first) of kwargs is not None
    :param kwargs: Dict of keyword arguments
    :type kwargs: dict
    :return: First (keyword, value) that is not None
    :rtype: tuple
    """
    for k, v in kwargs.items():
        if v:
            return k, v
    return None, None


def _is_invalid_choice(value, variable_name: str, choices: List):
    """
    Check if value is one of the possible choices
    Logs error message if not.
    :param value: Value to evaluate
    :type value: object
    :param variable_name: Name of variable (for logging purposes)
    :type variable_name: str
    :param choices: Options for value
    :type choices: list
    :return: If value is in choices
    :rtype: bool
    """
    if value and value not in choices:
        logger = logging.getLogger(package_info.__title__)
        logger.error(f"Invalid '{variable_name}'. Please use one of the following: {', '.join(choices)}")
        return True
    return False


def _get_response_data(json_data: dict) -> Union[str, int, List, dict]:
    """
    Return ['response']['data'] from JSON data
    :param json_data: JSON data to parse
    :type json_data: dict
    :return: json_data['response']['data']
    :rtype: dict
    """
    return json_data.get('response', {}).get('data', {})


def _success_result(json_data: dict) -> bool:
    """
    Return if ['response']['result'] from JSON data is 'success'
    Logs debug message if not.
    :param json_data: JSON data to parse
    :type json_data: dict
    :return: json_data['response']['result'] == 'success'
    :rtype: bool
    """
    if json_data.get('response', {}).get('result', "") == "success":
        return True
    logger = logging.getLogger(package_info.__title__)
    logger.debug(json_data.get('response', {}).get('message', "No error message in API response"))
    return False
