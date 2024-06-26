#!/usr/bin/env python3

"""
    I am addin the correct type annotation
    to the function's params
"""

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
        I am addin the correct type annotation
        to the function's params
    """
    if key in dct:
        return dct[key]
    else:
        return default
