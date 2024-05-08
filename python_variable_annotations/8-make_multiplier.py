#!/usr/bin/env python3

"""
    This module contains a function that takes in a float multiplier
    and returns a function that multiplies a float by a multiplier
"""

from typing import Callable
"""
    Imported Collable from typing which will help me
    to return a function
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a float multiplier as an argument and returns
    a function
    that multiplies a float by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        This inner function multiplies a float value by the multiplier.
        """
        return value * multiplier

    return multiplier_function
