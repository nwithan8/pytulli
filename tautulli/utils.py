from typing import Union, List
import logging
from datetime import datetime

import tautulli._info as package_info


def datetime_to_string(datetime_object: datetime, string_format: str = "%Y-%m-%d"):
    return datetime_object.strftime(fmt=string_format)

def build_optional_params(**kwargs):
    params = {}
    for k, v in kwargs.items():
        if v:
            params[k] = v
    return params

def bool_to_int(boolean: bool) -> int:
    if boolean:
        return 1
    return 0

def int_list_to_string(int_list: List[int]):
    int_list = list(map(str, int_list))
    return ','.join(int_list)

def _one_needed(**kwargs):
    one_used = False
    for k, v in kwargs.items():
        if v:
            one_used = True
    if not one_used:
        logger = logging.getLogger(package_info.__title__)
        logger.error(f"Please provide one of the following: {', '.join(kwargs.keys())}")
    return one_used

def _which_used(**kwargs):
    for k, v in kwargs.items():
        if v:
            return k, v
    return None, None

def _is_invalid_choice(value, variable_name: str, choices: List):
    if value and value not in choices:
        logger = logging.getLogger(package_info.__title__)
        logger.error(f"Invalid '{variable_name}'. Please use one of the following: {', '.join(choices)}")
        return True
    return False

def _get_response_data(json_data: dict) -> Union[str, int, List, dict]:
    return json_data.get('response', {}).get('data', {})

def _success_result(json_data: dict) -> bool:
    if json_data.get('response', {}).get('result', "") == "success":
        return True
    logger = logging.getLogger(package_info.__title__)
    logger.debug(json_data.get('response', {}).get('message', "No error message in API response"))
    return False