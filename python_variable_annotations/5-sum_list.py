#!/usr/bin/env python3

"""
    This module contains a function that takes in
    a list of floats and returns the sum of them
"""

from typing import List
"""
    Imported List from typing and its the one that will
    help us to mention that it should be a list of floats
"""


def sum_list(input_list: List[float]) -> float:
    """
        This function takes in a list of floats(input_list)
        and returns its sum which should be of float type
    """

    prev_sum: float = 0.00

    for item in input_list:
        prev_sum += item

    return prev_sum
