#!/usr/bin/env python3

"""
    This module contains a function that takes in
    a string and an int or a float and returns a tuple
"""

from typing import Union
from typing import Tuple
"""
    Imported Union from typing for defining hte possibility
    of two different data types
"""


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """
        This function takes in a string and an int or a
        float and return a tuple with the first element
        which is that string and the second which is the
        square of that int or float depending on the one
        used
    """

    return Tuple[k, v * v]