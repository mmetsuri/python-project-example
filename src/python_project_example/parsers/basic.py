
"""
String parsing functions.
"""
from typing import Union
from ..util.helper import StringHelper


def parse_str(data: str, lower_case=False) -> Union[str, None]:
    """
    Split string to a list, use whitespace.
    """
    if lower_case:
        data = StringHelper.to_lower(data)
        
    if StringHelper.has_spaces(data):
        return data.split(' ')

    return None
