import logging
from datetime import datetime, timedelta
from typing import Union, List, Iterable

from pytz import timezone

from tautulli._info import __title__

switcher = {
    "playing": "▶️",
    "paused": "⏸",
    "stopped": "⏹",
    "buffering": "⏳",
    "error": "⚠️"
}

media_type_icons = {
    'episode': '📺',
    'track': '🎧',
    'movie': '🎞',
    'clip': '🎬',
    'photo': '🖼',
    'live': '📡'
}

sessions_message = """{stream_count} {word}"""
transcodes_message = """{transcode_count} {word}"""
bandwidth_message = """🌐 {bandwidth}"""
lan_bandwidth_message = """(🏠 {bandwidth})"""

session_title_message = """{icon} {media_type_icon} {username}: *{title}*"""
session_player_message = """__Player__: {product} ({player})"""
session_details_message = """__Quality__: {quality_profile} ({bandwidth}){transcoding}"""
session_progress_message = """__Progress__: {progress} (ETA: {eta})"""


def datetime_to_string(datetime_object: datetime, string_format: str = "%Y-%m-%d") -> str:
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


def build_optional_params(**kwargs) -> dict:
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


def int_list_to_string(int_list: List[int]) -> str:
    """
    Convert a list of ints to a comma-separated string
    e.g. [0, 1, 4] -> "0,1,4"

    :param int_list: List of ints to convert
    :type int_list: list
    :return: Comma-separated string of ints
    :rtype: str
    """
    int_list = list(map(str, int_list))
    return comma_delimit(int_list)


def _human_bitrate(number, denominator: int = 1, letter: str = "", d: int = 1):
    if d <= 0:
        return f'{int(number / denominator):d} {letter}bps'
    else:
        return f'{float(number / denominator):.{d}f} {letter}bps'


def human_bitrate(kilobytes, d: int = 1) -> str:
    # Return the given kilobytes as a human friendly bps, Kbps, Mbps, Gbps, or Tbps string

    KB = float(1024)
    MB = float(KB ** 2)  # 1,048,576
    GB = float(KB ** 3)  # 1,073,741,824
    TB = float(KB ** 4)  # 1,099,511,627,776

    denominator = 1
    letter = ""
    if kilobytes < KB:
        pass
    elif KB <= kilobytes < MB:
        denominator = KB
        letter = "k"
    elif MB <= kilobytes < GB:
        denominator = MB
        letter = "M"
    elif GB <= kilobytes < TB:
        denominator = GB
        letter = "G"
    else:
        denominator = TB
        letter = "T"

    return _human_bitrate(kilobytes, denominator=denominator, letter=letter, d=d)


def comma_delimit(items: Iterable) -> str:
    return ','.join(items)


def make_plural(word, count: int, suffix_override: str = 's') -> str:
    if count > 1:
        return f"{word}{suffix_override}"
    return word


def _one_needed(**kwargs) -> bool:
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
        logger.error(f"Please provide one of the following: {comma_delimit(kwargs.keys())}")
    return one_used


def _which_used(**kwargs) -> tuple:
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


def _is_invalid_choice(value, variable_name: str, choices: List) -> bool:
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
        logger = logging.getLogger(__title__)
        logger.error(f"Invalid '{variable_name}'. Please use one of the following: {comma_delimit(choices)}")
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
    logger = logging.getLogger(__title__)
    logger.debug(json_data.get('response', {}).get('message', "No error message in API response"))
    return False


def milliseconds_to_minutes_seconds(milliseconds: int) -> str:
    seconds = int(milliseconds / 1000)
    minutes = int(seconds / 60)
    if minutes < 10:
        minutes = f"0{minutes}"
    seconds = int(seconds % 60)
    if seconds < 10:
        seconds = f"0{seconds}"
    return f"{minutes}:{seconds}"


def now_plus_milliseconds(milliseconds: int, timezone_code: str = None) -> datetime:
    if timezone_code:
        now = datetime.now(timezone(timezone_code))  # will raise exception if invalid timezone_code
    else:
        now = datetime.now()
    return now + timedelta(milliseconds=milliseconds)
