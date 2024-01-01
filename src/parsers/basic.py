
from ..util.helper import StringHelper
from typing import Union


def parse_str(data: str, lower_case=False) -> Union[str, None]:

    if lower_case:
        data = StringHelper.to_lower(data)
        
    if StringHelper.has_spaces(data):
        return data.split(' ')

    return None
