from typing import Union, Optional, Any

from pydantic import BaseModel, BeforeValidator, Field
from typing_extensions import Annotated


# ref: https://docs.pydantic.dev/latest/concepts/validators/#using-the-annotated-pattern
def empty_string_to_none(value: Any) -> Union[str, None]:
    """
    Handle coercing empty strings to None.
    :param value: The value to be converted.
    :return: None if the value is an empty string, otherwise the original value.
    """
    return value if value != "" else None


EmptyStringNullableInt: Union[int, None] = Annotated[Optional[int], BeforeValidator(empty_string_to_none)]

EmptyStringNullableFloat: Union[float, None] = Annotated[Optional[float], BeforeValidator(empty_string_to_none)]


class _Base(BaseModel):
    pass
