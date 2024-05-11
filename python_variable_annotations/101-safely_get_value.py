#!/usr/bin/env python3

"""
    I am addin the correct type annotation
    to the function's params
"""

from typing import TypeVar, Mapping, Any, Union, None

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
        Added the correct type annotation to this function
    """
    if key in dct:
        return dct[key]
    else:
        return default
