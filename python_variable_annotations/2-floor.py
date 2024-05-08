#!/usr/bin/env python3

"""
    This module contains functions related to mathematical operations.
"""

import math
"""
    Imported the math module and it's the one that will
    give us access to the floor method
"""


def floor(n: float) -> int:
    """
        Return the floor of a floating-point number.

        Parameters:
            n (float): The floating-point number.

        Returns:
            int: The floor of the floating-point number.
    """
    return math.floor(n)
