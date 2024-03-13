from urllib.parse import quote_plus


def _human_bitrate(number, denominator: int = 1, letter: str = "", d: int = 1):
    if d <= 0:
        return f'{int(number / denominator):d} {letter}bps'
    else:
        return f'{float(number / denominator):.{d}f} {letter}bps'


# noinspection PyPep8Naming
def to_human_bitrate(kilobytes, d: int = 1) -> str:
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


def redact(full_string: str, to_redact: str, redaction: str = "[REDACTED]") -> str:
    """
    Redact a string from a full string

    :param full_string: Full string to redact from
    :type full_string: str
    :param to_redact: String to redact
    :type to_redact: str
    :param redaction: String to replace the redacted string with
    :type redaction: str
    :returns: Redacted string
    :rtype: str
    """
    return full_string.replace(to_redact, redaction)


def url_encode(string: str) -> str:
    """
    URL encode a string

    :param string: String to encode
    :type string: str
    :returns: URL encoded string
    :rtype: str
    """
    return quote_plus(string)
