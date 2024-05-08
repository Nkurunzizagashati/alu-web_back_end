#!/usr/bin/env python3

"""
    This module contains a function that will take a list
    of floats as an argument and returns the sum of the list
"""


type input_list = list[float]

def sum_list(input_list) -> float:
    """
        This function takes in a list of floats(input_list)
        and returns its sum which should be of float type
    """

    prev_sum: float = 0.00

    for item in input_list:
        prev_sum += item

    return prev_sum
