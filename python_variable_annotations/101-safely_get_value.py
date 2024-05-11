#!/usr/bin/env python3

"""
    I am addin the correct type annotation
    to the function's params
"""

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: T = None) -> Union[T, None]:
    """
        Added the correct type annotation to this function
    """
    if key in dct:
        return dct[key]
    else:
        return default
