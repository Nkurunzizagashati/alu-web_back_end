#!/usr/bin/env python3

"""
    This module contains a function which takes in a mixed list
    of integers and floats and returns their sum as a float
"""

from typing import List
from typing import Union
"""
    Imported List, and Union from typing to help us specify that
    it should be a list of objects, and also a combination of
    different data types respectively
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        This function takes in a list of integers and floats and
        returns a sum of them which is a float type
    """

    prev_sum: float = 0.00
    for item in mxd_lst:
        prev_sum += item

    return prev_sum
